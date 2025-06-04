# Fake News Detection Project (Old-Version Branch)

## Overview
This project uses an older version of the fake news detection implementation, as the main version is not available for download. It focuses on analyzing and detecting fake news using datasets from BuzzFeed and PolitiFact, with machine learning models implemented in Jupyter notebooks.

## About the IPython Notebooks
- **bert.ipynb**: This Jupyter notebook implements a BERT-based model for fake news detection. It includes code for loading the BuzzFeed and PolitiFact datasets, preprocessing text data, training the BERT model, and evaluating its performance in classifying news articles as real or fake.
- **Roberta.ipynb**: This Jupyter notebook implements a RoBERTa-based model for fake news detection. Similar to `bert.ipynb`, it contains steps for data loading, preprocessing, training, and evaluation, leveraging the RoBERTa architecture for potentially improved performance over BERT.

## Project Structure
```
├── bert.ipynb                     # Jupyter notebook for BERT-based model
├── buzzfeed_news_with_filenames.csv # BuzzFeed news data with filenames
├── politifact_news_with_filenames.csv # PolitiFact news data with filenames

├── prepare_dataset.py                 # Python script for preprocessing datasets
├── README.md                         # This file
└── Roberta.ipynb                     # Jupyter notebook for RoBERTa-based model
```


## Preprocessing
The `prepare_dataset.py` script preprocesses the datasets by extracting the **title** and **text** from the JSON files in the `FakeNewsContent/` and `RealNewsContent/` directories. This processed data is used for training and evaluating the BERT and RoBERTa models in the respective notebooks.

