<h1>Amazon Web Scrapping </h1>

Hello everyone, in a nutshell, this project will give you the details of a product from all the pages available.

Below is the flow diagram

<h2> Start the amazon scrappy </h2>

1. install the required libraries using the command: ```pip install -r src/requirements.txt```
2. Change the 'item' value in src/config.json to any product you like(shirt, pants, shoes, etc..).
3. Run ```main.py```.
4. The CSV file will be available inside src/output_csv/output.csv

<h2>Libraries and its usage</h2>
1. ```selenium``` -> this python library is used to automate the process of getting all the ```URLS``` from all *Pages*
