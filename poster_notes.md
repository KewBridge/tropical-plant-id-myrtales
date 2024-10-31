# Poster Notes

### Objectives
- 

---
### Background Info
- 

---

### Methods

*summarised from README.md*

The Kew Tropical Plant Identification Handbook provided a source of descriptive data. This data was applied to GBIF specimen images from Kew herbarium to be scored by character. This short pilot project focused on the order Myrtales; specimen images from the families Combretaceae, Lythraceae, Vochysiaceae, Myrtaceae, and Melastomataceae were used for trait scoring.

For each family, a GBIF search for occurrence records from Kew herbarium was carried out. The search was filtered according to this [protocol](https://github.com/KewBridge/tropical-plant-id-myrtales/blob/main/mobilising-traits-protocol/Protocol.md). Additional country level filters were needed for Lythraceae, as this family is also found in temperate regions, to ensure only tropical material was selected. After navigating to the gallery view, images were selected that displayed characters on the identification page of the handbook. Characters were organised into 3 categories: (i) those from the general key and spot characters lists, (ii) those from the more detailed descriptive paragraph, and (iii) those indicating habitat, taken from the specimen label. These characteristics were recorded by creating bookmarks in the web browser, with tags for the characters. The bookmark data was exported and saved in HTML format. This data was cleaned and reformatted to a tabular datafile. A citable GBIF download is available for the selected records, as is a [hugging face dataset](https://huggingface.co/datasets/nickynicolson/tropical_plant_id_myrtales) for images and labels. 

--- 

### Potential Figures?
- Example page from handbook with sections used for tagging circled / highlighted?
- Same for tagging data from herbarium specimen