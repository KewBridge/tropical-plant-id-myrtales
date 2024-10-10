import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process an HTML bookmarks file and output tagged data to a CSV file.")
    parser.add_argument('input_file', help="Path to the input HTML file")
    parser.add_argument('output_file', help="Path to the output CSV file")
    
    # Parse arguments
    args = parser.parse_args()

    with open(args.output_file, 'w', encoding='utf-8') as file_out:
        with open(args.input_file, 'r', encoding='utf-8') as file_in:
            for line in file_in.readlines():
                cleanline = line.replace('<DT>','')
                cleanline = cleanline.replace('<p>','')
                file_out.write(cleanline)

if __name__ == "__main__":
    main()
