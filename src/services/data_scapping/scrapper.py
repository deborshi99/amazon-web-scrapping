from bs4 import BeautifulSoup
import requests
import traceback, sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
import json
import os 
import warnings
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import datetime
warnings.filterwarnings('ignore')
import time

# // build veryfy if the user input is a string or url

class scrappy:
    def __init__(self, start_url):
        try:
            self.chrome_options = Options()
            self.chrome_options.add_argument("--headless")
            # self.chrome_options.add_argument(f'--proxy-server=164.38.155.97:-80')
            # self.chrome_options.add_argument('--log-level=3')

            self.start_url = start_url    
            self.response = requests.get(self.start_url)
            if self.response.status_code != 200:
                print(f'Connection Failed, return status = {self.response.status_code}')
            else:
                print('Connection Successful')
        except ValueError:
            print(f'Entered URL should not be empty')
        except TypeError:
            print(f'Entered URL should be a text')
        except Exception:
            print('Exception occured!!!')
            traceback.print_exc(file=sys.stdout)
    
    def connect_item(self, url, product):
        ## connecting to chrome driver 
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=self.chrome_options) # For not showing the chrome dialog box
        browser.get(url)
        html_body = browser.page_source
        soup = BeautifulSoup(html_body) # initializing bs4 for scrapping data 
        
        ## Getting the details of the product        
        productname = soup.find('span', id='productTitle').text
        productdiscount = float(soup.find('span', class_='a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage').text.replace('-','').replace('%', ''))
        productprice = float(soup.find('span', class_='a-price-whole').text.replace(',',''))
        totalproductratings = int(soup.find('span', id='acrCustomerReviewText').text.split(' ')[0].replace(',', ''))
        # print(url)
        # fivestarreviews, fourstarreviews, threestarreviews, twostarreviews, onestarreviews =
        # a= [
        #     i.text.replace('%','') for i in soup.find_all('a', class_='a-size-base a-link-normal') if i.text != ' Details ' and i.text != '' and i.text != '5 star' and i.text != '4 star' and i.text != '3 star' and i.text != '2 star' and i.text != '1 star' 
        # ]
        fivestarreviews = int(browser.find_element(By.XPATH, '//*[@id="histogramTable"]/tbody/tr[1]/td[3]/a').text.replace('%', ''))
        fourstarreviews = int(browser.find_element(By.XPATH, '//*[@id="histogramTable"]/tbody/tr[2]/td[3]/a').text.replace('%', ''))
        threestarreviews = int(browser.find_element(By.XPATH, '//*[@id="histogramTable"]/tbody/tr[3]/td[3]/a').text.replace('%', ''))
        twostarreviews = int(browser.find_element(By.XPATH, '//*[@id="histogramTable"]/tbody/tr[4]/td[3]/a').text.replace('%', ''))
        onestarreviews = int(browser.find_element(By.XPATH, '//*[@id="histogramTable"]/tbody/tr[5]/td[3]/a').text.replace('%', ''))
        
        countryoforigin = browser.find_element(By.XPATH, '//*[@id="detailBullets_feature_div"]/ul/li[6]/span/span[2]').text
        manufacturer = browser.find_element(By.XPATH, '//*[@id="detailBullets_feature_div"]/ul/li[3]/span/span[2]').text
        # Creating the dictionary 
        browser.quit()
        result_dict = {
            'Product': product,
            'ProductName': productname,
            'URL': url,
            'ProductDiscount': productdiscount,
            'ProductPrice': productprice,
            'TotalUserratings': totalproductratings,
            'CountryOfOrigin': countryoforigin,
            'Manufacturer': manufacturer,
            '5 stars': fivestarreviews,
            '4 stars': fourstarreviews,
            '3 stars': threestarreviews,
            '2 stars': twostarreviews,
            '1 stars': onestarreviews,
            'FetchedTimeStamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        print(result_dict)
        return result_dict
        
        
    def direct_to_items(self, item):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.chrome_options)
        browser.get(self.start_url)
        ## Enter the item
        browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys(item)
        ## Click the search icon
        browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()
        counter = 0
        while True:
            try:
                counter = counter + 1
                html_body = browser.page_source
                soup = BeautifulSoup(html_body)
                links = [f"https://www.amazon.in{x['href']}" for x in soup.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal', href=True)]
                os.makedirs('./links', exist_ok=True)
                with open(f'./links/{item}_{counter}.json', 'w') as file:
                    json.dump(links, file)
                next_page = soup.find('a', class_="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator", href=True)
                if type(next_page) != type(None):
                    # raise Exception('no pages left')
                    next_page_url = f"https://www.amazon.in{next_page['href']}"
                    browser.get(next_page_url)
                else:
                    break
            except (TimeoutException, WebDriverException) as e:
                print("Last page reached")
                break
        browser.quit()