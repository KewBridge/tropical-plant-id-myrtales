# tropical-plant-id-myrtales

## Background

The Tropical Plant Families ID Handbook consists of a two page spread per family, with key characteristics listed. We've been planning to use this as a source of descriptive data which can be applied to herbarium specimens so that they can be scored by character.

This repository manages a short pilot project where we have scored herbarium specimens in the *Myrtales*, ie these families:

- Combretaceae
- Lythraceae
- Vochysiaceae
- Myrtaceae 
- Melastomataceae

## Process

1. We extracted the identification page data for the families listed above
2. For each family, Tzu Li ran a search on GBIF for occurrence records from the Kew herbarium in the family, and opened the records in gallery view. Links to run these GBIF data portal queries are given below:
    - [Combretaceae](https://www.gbif.org/occurrence/gallery?dataset_key=cd6e21c8-9e8a-493a-8a76-fbf7862069e5&taxon_key=2431&advanced=1)
    - [Lythraceae](https://www.gbif.org/occurrence/gallery?dataset_key=cd6e21c8-9e8a-493a-8a76-fbf7862069e5&taxon_key=6684&advanced=1)
    - [Vochysiaceae](https://www.gbif.org/occurrence/gallery?dataset_key=cd6e21c8-9e8a-493a-8a76-fbf7862069e5&taxon_key=3231623&advanced=1)
    - [Myrtaceae](https://www.gbif.org/occurrence/gallery?dataset_key=cd6e21c8-9e8a-493a-8a76-fbf7862069e5&taxon_key=5014&advanced=1) 
    - [Melastomataceae](https://www.gbif.org/occurrence/gallery?dataset_key=cd6e21c8-9e8a-493a-8a76-fbf7862069e5&taxon_key=6683&advanced=1)
3. Consulting the gallery view alongside the identification page data, he selected specimen images which displayed the characteristics, recording these by creating a bookmark in his web browser, with tags for the characters. Characters were organised into three categories - (i) those from the general key characters list, (ii) those from the more detailed descriptive paragraph, and (iii) those indicating habit, taken from the specimen label.
4. The bookmark data was exported from the web browser, and is saved in this repository as [resources/bookmarks.html](resources/bookmarks.html)
5. The HTML format bookmark data was cleaned and reformatted to a tabular datafile.

## How to run the scripts

This assumes that you have cloned the repository to a machine where you have: (a) a local installation of Python, (b) the build tool `make` and (c) a command line terminal program to run the following commands:

1. Set up a virtual environment: `python -m venv env` and activate it: `source env/Scripts/activate`
2. Install the libraries: `pip install -r requirements.txt`
3. Run the conversion process: `make csv`

## References
```bibtex
@book{utteridgeKewTropicalPlant2015,
  title = {The {{Kew}} Tropical Plant Families Identification Handbook},
  editor = {Utteridge, Timothy M. A. and Bramley, Gemma},
  year = {2015},
  edition = {Second Edition},
  publisher = {Kew Publishing, Royal Botanic Gardens},
  address = {Kew},
  isbn = {978-1-84246-602-5},
  langid = {english}
```

## Who's involved

- [Nicky Nicolson](https://github.com/nickynicolson), Digital collections
- [Amy Fiddes](https://github.com/amyfiddes), science intern from the University of Sheffield, Digital collections
- [Eve Lucas](https://github.com/el12kg), Accelerated taxonomy
- [Tzu Li Yang](TzuLiYang), summer intern from the National Taiwan University (NTU), Accelerated taxonomy

## How to contribute

You can submit issues [here](https://github.com/KewBridge/tropical-plant-id-myrtales/issues)
