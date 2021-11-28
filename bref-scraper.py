# -*- coding: utf-8 -*-
"""
@author: aaronpetry.io
"""

#Import requests, csv, and BeautifulSoup
import requests
import csv
from bs4 import BeautifulSoup

#Create list of the year to pull from 
years = ['2022']

#Create an empty list to store the data
nba_adv_stats = []

#Create the header row with labels from the table 
url = "https://www.basketball-reference.com/leagues/NBA_" + years[0] + ".html#misc::none"

#Get the URL from basketball-refernece
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Find the advanced stats header row
adv_stats_table = soup.find('table', attrs={'id':'advanced-team'})
adv_stats_headers = adv_stats_table.find('thead')
headers = adv_stats_headers.find_all('th')
headers = [ele.text.strip() for ele in headers]

#Append the headers to the beginning of the nba_adV_stats list
nba_adv_stats.append([ele for ele in headers])

#Find the advanced stats body 
adv_stats_body = adv_stats_table.find('tbody')
adv_stats_rows = adv_stats_body.find_all('tr')

#For each row in the advanced stats table, add the team data to the nba_adv_stats list
for row in adv_stats_rows:

    #Find the rest of the data columns
    data_columns = row.find_all('td')
    data_columns = [ele.text.strip() for ele in data_columns]
    
    #Combine the columns and add them to the nba_adv_list list
    nba_adv_stats.append([ele for ele in data_columns])

#Create a dynamic CSV file name based on the year scraped
csv_file = "nba_adv_stats_" + years[0] + ".csv"

#Write the nba_adv_stats list to a CSV
with open(csv_file, "w", encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for data in nba_adv_stats:
        writer.writerow(data)