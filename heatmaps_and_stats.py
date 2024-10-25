import argparse
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns

def main():

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate trait heatmaps from family data")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_percent_traits_file", help="Output for percent traits scored heatmap")
    # parser.add_argument("output_traits_counts_file", help="Output for total traits count heatmap")
    
    # parse arguments
    args = parser.parse_args()

    # Read the .csv file
    families = pd.read_csv(args.input_file)

    # Group by family and show
    family_group = families.groupby('family').size()
    family_group_sorted = family_group.sort_values(ascending=False)
    print(family_group_sorted)


    # Create a table to show how many times each trait scored within each family
    trait_columns = families.drop(columns=['family', 'GBIF_occurrence_ID', 'catalogNumber', 'image_url'])
    traits_scored_by_family = families.groupby('family')[trait_columns.columns].sum()

    # Heatmap with % traits scored
    family_counts = families['family'].value_counts()
    traits_percentage = traits_scored_by_family.div(family_counts, axis=0) * 100
    plt.figure(figsize=(12, 2))
    sns.heatmap(traits_percentage, cmap='coolwarm', annot=False, linewidths=0.5)
    plt.title('Percentage of Traits Scored per Family')
    plt.xlabel('Traits')
    plt.ylabel('Family')
    plt.yticks(rotation=360)
    plt.savefig(args.output_percent_traits_file)

    # Total number of traits scored regardless of family df
    # traits_scored = families[trait_columns.columns].sum()
    # traits_scored_df = pd.DataFrame([traits_scored], index=['Count'])

    # Save this as a heatmap
    # plt.figure(figsize=(12, 2))
    # sns.heatmap(traits_scored_df, cmap='coolwarm', annot=False, linewidths=0.5)
    # plt.title('Number of Times Each Trait is Scored')
    # plt.xlabel('Traits')
    # plt.yticks([])
    # plt.savefig(args.output_traits_counts_file)

if __name__ == "__main__":
        main()