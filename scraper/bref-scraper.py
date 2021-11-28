# -*- coding: utf-8 -*-
"""
@author: aaronpetry.io
"""

#Import requests, csv, and BeautifulSoup
import requests
import csv
import os
from bs4 import BeautifulSoup
from pathlib import Path

#Create list of the year to pull from 
years = ['2022']

#Create an empty list to store the data
nba_adv_stats = []

#Create the header row with labels from the table 
url = "https://www.basketball-reference.com/leagues/NBA_" + years[0] + ".html#misc::none"

#Get the URL from basketball-refernece
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Find the advanced stats header row (skip the top header row and ignore rank)
adv_stats_table = soup.find('table', attrs={'id':'advanced-team'})
adv_stats_headers = adv_stats_table.find('thead')
headers = adv_stats_headers.find_all('th')
headers = [ele.text.strip() for ele in headers[6:]]

#Manually add the 'Year' header
year_header = ['Year']
combined_headers = year_header + headers

#Append the headers to the beginning of the nba_adv_stats list
nba_adv_stats.append([ele for ele in combined_headers])

#Find the advanced stats body 
adv_stats_body = adv_stats_table.find('tbody')
adv_stats_rows = adv_stats_body.find_all('tr')

#For each year in the years list, add the advanced stats data
for year in years:
    #For each row in the advanced stats table, add the team data to the nba_adv_stats list
    for row in adv_stats_rows:
        #Populate the Year column (will need to update once this is a loop)
        year_column = [year]

        #Find the rest of the data columns
        data_columns = row.find_all('td')
        data_columns = [ele.text.strip() for ele in data_columns]

        #Combine columns
        combined_columns = year_column + data_columns
        
        #Combine the columns and add them to the nba_adv_list list
        nba_adv_stats.append([ele for ele in combined_columns])

#Create a dynamic CSV file name based on the year scraped
csv_path = os.path.join(os.getcwd(), "data/")
csv_file = csv_path + "nba_adv_stats_" + years[0] + ".csv"

#Write the nba_adv_stats list to a CSV
with open(csv_file, "w", encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for data in nba_adv_stats:
        writer.writerow(data)