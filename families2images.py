import argparse
import pandas as pd
import os
import zipfile
import requests

def convert_families_to_local_image_store(inputfile, outputfile):
    
    df = pd.read_csv(inputfile)
    
    image_files = []
    os.mkdir('images')
    for i, row in df.iterrows():
        image_url = row['image_url']

        print('downloading image for {} from {}'.format(row['catalogNumber'], image_url))
        # Send a GET request to the image URL
        response = requests.get(image_url)
        # Open a local file in binary-write mode and save the image
        image_file = 'images/{catalog_number}.jpg'.format(catalog_number=row['catalogNumber'])
        with open(image_file, 'wb') as file:
            file.write(response.content)
        image_files.append(image_file)
    
    with zipfile.ZipFile(outputfile, 'w') as zipf:
        for image_file in image_files:
            print('zipping', image_file)
            zipf.write(image_file)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process an CSV file of GBIF-mediated specimen occurrences to request a GBIF download.")
    parser.add_argument('input_file', help="Path to the input CSV file")
    parser.add_argument('output_file', help="Path to the output image zip file")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Process CSV file and download associated images for each occurrence
    convert_families_to_local_image_store(args.input_file, args.output_file)

if __name__ == "__main__":
    main()