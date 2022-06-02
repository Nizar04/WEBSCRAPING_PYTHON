


#Importing Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import concurrent.futures
from csv import reader


#Data Storage
urls = []
PRICES = []

#Number of thread that will be used for the parrallel process
Num_of_threads =  1500


#Code below is used for getting the URLS from the CSV_FILES
with open('links.csv', 'r') as f:
        csv_reader = reader(f)
        for row in csv_reader:
            urls.append(row[0])


#Function used to do the scrapping
def go_scrappy(url):
    #Gets the request with the url and passes to BeautifulSoup
    request =  requests.get(str(url))
    #Gets the HTML CODE/DATA FROM THE WEB PAGE
    codeH   =  BeautifulSoup(request.content, 'html.parser')
    # fetches the data from codeH to get the data we want
    price   =  codeH.find('p').text
    #passes the fetched data to the DATA_FRAME "PRICES"
    PRICES.append(price)
    #Prints the data within the console
    print(price)
    return


#Reponsible for the parrallelisation of the code
with concurrent.futures.ThreadPoolExecutor(Num_of_threads) as executor:
    #Executes in the functions
    executor.map(go_scrappy, urls)

#prints the number of the fetched data
print(len(PRICES))
#Making a data frame to save our data of console
DataFrame = pd.DataFrame(PRICES)
#Converts data frame to a csv File
DataFrame.to_csv('parralle_prices.csv', index=False)

#Prints the Message once everything is done
print('Done')

