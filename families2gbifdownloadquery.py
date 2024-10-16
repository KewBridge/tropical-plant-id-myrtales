import argparse
import csv
import pandas as pd
import json

def convert_families_to_gbif_download_query(inputfile, outputfile, creator, notification_address):
    df = pd.read_csv(inputfile)
    download_request = dict()
    predicate = dict()
    predicates = dict()
    download_request['creator'] = creator
    download_request['notification_address'] = [notification_address]
    download_request['sendNotification'] = True
    download_request['format'] = 'SIMPLE_CSV'
    
    download_request['predicate'] = predicate
    predicate['type'] = 'and'
    predicate['predicates'] = [predicates]
    predicates['type'] = 'in'
    predicates['key'] = 'GBIF_ID'
    predicates['values'] = df.GBIF_occurrence_ID.to_list()
    with open(outputfile, 'w') as json_file:
        json.dump(download_request, json_file, indent=4)  

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process an CSV file of GBIF-mediated specimen occurrences to request a GBIF download.")
    parser.add_argument('input_file', help="Path to the input CSV file")
    parser.add_argument('--gbif_user_name', required=False, help="GBIF user name")
    parser.add_argument('--gbif_email_address', required=False, help="GBIF notification email address")
    parser.add_argument('output_file', help="Path to the output JSON file")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Process HTML file and output to CSV
    convert_families_to_gbif_download_query(args.input_file, args.output_file, args.gbif_user_name, args.gbif_email_address)

if __name__ == "__main__":
    main()