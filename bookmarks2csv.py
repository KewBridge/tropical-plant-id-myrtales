import argparse
import csv
from bs4 import BeautifulSoup
import re
import pandas as pd
from pygbif import occurrences as occ

def getCatalogNumberByOccurrence(gbif_occurrence_id):
    gbif_occ = occ.get(key = gbif_occurrence_id)
    return gbif_occ['catalogNumber']


def url2ImageUrl(url):
    image_url = 'https:' + url.split('src=')[1]
    return image_url


def parse_bookmarks_to_csv(input_file, output_file):
    # Open and read the HTML file
    with open(input_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Make a list where we can save the fmaily data
    family_data = []
    # Find all families used as content headers in the HTML file
    for family in soup.findAll('h3', string = re.compile('[A-Z][a-z]+aceae')):
        # Now we look for the links wheihc were bookmarked under this family 
        # folder using the find_next_sibling method
        for tagged_link in family.find_next_sibling().find_all('a'):
            # We are only interested in links which have been tagged
            if 'tags' in tagged_link.attrs.keys():
                # The href attribute holds the URL (link) to the GBIF data portal record
                gbif_url = tagged_link['href']
                # Split the GBF data portal URL into elements
                gbif_url_elems = gbif_url.split('/')
                # The occurrence ID will be shown after the "occurrence" element
                gbif_occurrence_id = gbif_url_elems[gbif_url_elems.index('occurrence')+1]
                # Split the tags by comma
                tags = tagged_link['tags'].split(',')
                # Get image URL from bookmarked data portal URL
                image_url = url2ImageUrl(gbif_url)
                # Get catalog number
                catalogNumber = getCatalogNumberByOccurrence(gbif_occurrence_id)
                # Assemble a dictionary holding all the data and save to our list
                family_data.append({'family':family.text, 'GBIF_occurrence_ID':gbif_occurrence_id, 'catalogNumber':catalogNumber, 'image_url':image_url, 'tags':tags})
        
    # Convert the family data list to a pandas dataframe
    df = pd.DataFrame(family_data)

    # Expand the 'tags' column into multiple boolean columns
    tags_dummies = df['tags'].str.join('|').str.get_dummies()

    # Concatenate the boolean columns back to the original DataFrame
    df = pd.concat([df, tags_dummies], axis=1)
    # Discard the "tags" column as is no longer needed
    df.drop(columns=['tags'], inplace=True)

    # Save the dataframe as a tab separated file
    df.to_csv(output_file, sep='\t', encoding='utf8', index=False)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process an HTML bookmarks file and output tagged data to a CSV file.")
    parser.add_argument('input_file', help="Path to the input HTML file")
    parser.add_argument('output_file', help="Path to the output CSV file")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Process HTML file and output to CSV
    parse_bookmarks_to_csv(args.input_file, args.output_file)

if __name__ == "__main__":
    main()