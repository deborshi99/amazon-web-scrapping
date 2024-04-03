<h1>Amazon Web Scrapping </h1>

Hello everyone, in a nutshell, this project will give you the details of a product from all the pages available.

Below is the flow diagram

<img src="/flow_diagram.png" alt="Employee data" title="Employee Data title">

<h2> Start the amazon scrappy </h2>

1. install the required libraries using the command: ```pip install -r src/requirements.txt```
2. Change the 'item' value in src/config.json to any product you like(shirt, pants, shoes, etc..).
3. Run ```main.py```.
4. The CSV file will be available inside ```src/output_csv/output.csv```

<h2>Libraries and its usage</h2>

1. ```selenium``` -> this python library is used to automate the process of getting all the ```URLS``` from all *Pages*
2. ```BeautifulSoup``` -> this library is used to scrap the required data from each ```URL``` fetched from ```selenium```,
3. ```pandas``` -> this library is used to write the data from ```BeautifulSoup``` to the Folder(```src/output_csv/output.csv```)

<h2>What kind of data is getting fetched?</h2>

1. ```Product``` -> The item you seached for.
2. ```ProductName``` -> Name of the product
3. ```URL``` -> URL of the product.
4. ```ProductDiscount``` -> Discount available for the product.
5. ```ProductPrice``` -> Price of the product.
6. ```TotalUserratings``` -> Total number of users rated for the product.
7. ```CountryOfOrigin``` -> Country of Origin.
8. ```Manufacturer``` -> Brand/manufacturer name.
9. ```FetchedTimeStamp``` -> Timestamp at which the record has been fetched.
10. '5 stars', '4 stars', '3 stars', '2 stars', '1 stars' --> this are the ratings(out of 5) for the product given my the users

<h2>Future Developement</h2>

1. A ```flask``` api can be developed and be hosted on the web for better usage.
