import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the .csv file
families = pd.read_csv('families.csv')

# Group by family and show
family_group = families.groupby('family').size()

family_group_sorted = family_group.sort_values(ascending=False)

print(family_group_sorted)


# Create a table to find out how many times each trait scored within each family
trait_columns = families.drop(columns=['family', 'GBIF_occurrence_ID', 'catalogNumber', 'image_url'])

traits_scored_by_family = families.groupby('family')[trait_columns.columns].sum()

print(traits_scored_by_family)


# Total number of traits scored regardless of family
traits_scored = families[trait_columns.columns].sum()

traits_scored_df = pd.DataFrame([traits_scored], index=['Count'])

print(traits_scored)

plt.figure(figsize=(12, 2))
sns.heatmap(traits_scored_df, cmap='coolwarm', annot=False, linewidths=0.5)
plt.title('Number of Times Each Trait is Scored')
plt.xlabel('Traits')
plt.yticks([])

plt.show()


# Heatmap with % traits scored
family_counts = families['family'].value_counts()

traits_percentage = traits_scored_by_family.div(family_counts, axis=0) * 100

plt.figure(figsize=(12, 2))
sns.heatmap(traits_percentage, cmap='coolwarm', annot=False, linewidths=0.5)
plt.title('Percentage of Traits Scored per Family')
plt.xlabel('Traits')
plt.ylabel('Family')
plt.yticks(rotation=360)

plt.show()
