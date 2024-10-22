import argparse
from pygbif import occurrences as occ
import json
import requests

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process a GBIF download ID to get a bibtex format citation")
    parser.add_argument('input_file', help="Path to the input GBIF download ID file")
    parser.add_argument('output_file', help="Path to the output bibtex file")
    
    # Parse arguments
    args = parser.parse_args()

    with open(args.output_file, 'w', encoding='utf-8') as file_out:
        with open(args.input_file, 'r', encoding='utf-8') as file_in:
            gbif_download_id = file_in.read()
            dl_meta = occ.download_meta(key = gbif_download_id)
            doi = dl_meta['doi']
            url = "https://data.crosscite.org/application/x-bibtex/{doi}".format(doi=doi)
            response = requests.get(url)
            file_out.write(response.text)

if __name__ == "__main__":
    main()
