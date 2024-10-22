import argparse
import csv
import pandas as pd
import json
from pygbif import occurrences as occ
import os

def convert_families_to_gbif_download_query(inputfile, outputfile, creator, notification_address):
    
    df = pd.read_csv(inputfile)
    
    download_request_predicate = dict()
    download_request_predicate['type'] = 'and'

    predicates = dict()    
    download_request_predicate['predicates'] = [predicates]
    predicates['type'] = 'in'
    predicates['key'] = 'GBIF_ID'
    predicates['values'] = df.GBIF_occurrence_ID.to_list()

    occ_sample = occ.get(key=df.GBIF_occurrence_ID.to_list()[0])
    print(json.dumps(occ_sample, indent=4))

    # Use pygbif to download
    gbif_password = os.getenv('GBIF_PASSWORD')

    dl = occ.download(download_request_predicate, user=creator, pwd=gbif_password, email=notification_address)
    download_id = dl[0]

    with open(outputfile, 'w') as dl_id_file:
         dl_id_file.write(download_id)

    # It is also possible to make a JSON format download and send it to the 
    # GBIF endpoint using CURL.
    # This download_request_wrapper object adds the necessary information 
    # around the predicate that we defined above 
    
    # download_request_wrapper = dict()
    # download_request_wrapper['creator'] = creator
    # download_request_wrapper['notification_address'] = [notification_address]
    # download_request_wrapper['sendNotification'] = True
    # download_request_wrapper['format'] = 'SIMPLE_CSV'
    # download_request_wrapper['predicate'] = download_request_predicate

    # with open(outputfile, 'w') as json_file:
    #     json.dump(download_request_wrapper, json_file, indent=4)  

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process an CSV file of GBIF-mediated specimen occurrences to request a GBIF download.")
    parser.add_argument('input_file', help="Path to the input CSV file")
    parser.add_argument('--gbif_user_name', required=False, help="GBIF user name")
    parser.add_argument('--gbif_email_address', required=False, help="GBIF notification email address")
    parser.add_argument('output_file', help="Path to the output download ID file")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Process HTML file and output to CSV
    convert_families_to_gbif_download_query(args.input_file, args.output_file, args.gbif_user_name, args.gbif_email_address)

if __name__ == "__main__":
    main()