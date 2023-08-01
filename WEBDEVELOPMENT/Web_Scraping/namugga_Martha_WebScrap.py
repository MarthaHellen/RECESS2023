# Introduction to Web Scraping with BeautifulSoup

""" 
Extraction of information from a website by using BeautifulSoup
and parsing the HTML and XML code of the webpages

#Install Beautiful soup
pip install BeautifulSoup4

#import libraries
from bs4 import BeautifulSoup # import BeautifulSoup library
import requests #featches the HTML content
https://xeno-canto.org
"""

import json
import csv
from bs4 import BeautifulSoup
import requests


# Get title of website
url = "https://xeno-canto.org"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# title = soup.find('title')
# print(title)

# Today's assignments A12
# Extract all birds species from this website  url = https://xeno-canto.org
# and generate a csv or JASON file format file for the bird species, family and more
# Extract all bird songs from this website url = https://xeno-canto.org
# Use this API to get data The endpoint for the webservice is at https://xeno-canto.org/api/2/recordings

# Extrct all bird spiecies


def bird_species_extraction(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        bird_species_table = soup.find('table', class_="results")
        bird_species = []

        if bird_species_table:
            birds = bird_species_table.find_all('tr')
            for row in birds:
                bird_name = row.find_all('td')
                other_bird_info = []
                birdlink = None
                common_name = None
                scientific_name = None

                for specific_bird in bird_name:
                    # Check if the current td contains an anchor link (href)
                    if specific_bird.find('a'):
                        birdlink = specific_bird
                    else:
                        other_bird_info.append(specific_bird.text.strip())

                if birdlink and len(other_bird_info) > 0:
                    common_name = birdlink.text.strip()
                    scientific_name = other_bird_info[0]
                    bird_species.append({'Common Name': common_name, 'Scientific Name': scientific_name})

        return bird_species
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return []
    


#Extracting bird songs
def bird_song_extraction(api_url):
        # Make a request to the API and check if its successful
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        
        # Loop through the data and extract bird songs
        bird_songs = []
        if 'recordings' in data:
            for recording in data['recordings']:
             bird_songs.append(recording['en'])

        return bird_songs
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        # return []



if __name__ == "__main__":

    # #Extracting the birds
    # url = "https://xeno-canto.org/collection/species/all"
    # bird_species_data = bird_species_extraction(url)

    # data = {'bird_species': bird_species_data}
    # with open('bird_species.json', 'w', encoding='utf-8') as jsonfile:
    #     json.dump(data, jsonfile)
    # print("Data has been successfully scraped and saved to bird_species.csv and bird_species.json.")

    # if bird_species_data:
    # # Save to CSV
    # with open('bird_species.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #     fieldnames = ['species']  # Add more fieldnames as needed
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writeheader()
    #     writer.writerows(bird_species_data)

    #Extracting the songs
    api_url = "https://xeno-canto.org/api/2/recordings?query=type:song"
    songs = bird_song_extraction(api_url)

    recordings ={"Bird songs" : songs}
    with open('bird_songs.json', 'w', encoding='utf-8') as jsonfile2:
        json.dump(songs, jsonfile2)
    print("Data has been successfully scraped and saved to bird_songs.json.")


