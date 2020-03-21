# Data Analysis Methods final project
This project members are: Xichao Wang, Jia Xie, and Shuang Zhou.

Project proposal: https://docs.google.com/document/d/1tCGZvaMA7WnUxMxE96vIPj5145Aw8W71AkT_e6bcEkE/edit?usp=sharing

## Overview
In this project, we use machine learning models to build a sentence classifier to identify sentence topics with given pre-trained labels.

Working environment: Jupyter Lab

Programming Language: Python

Dependencies: 

**sklearn** (scikit-learn: free machine learning library)

**tenserflow** (tenserflow: Google machine learning library)

## Phase 1 & 2: Data Collection and Data Cleaning
We used three different methods to gather the data: data crawling, download directly, and Twitter API.

Crawling: https://projects.propublica.org/api-docs/congress-api/statements/

Download: https://www.dcinbox.com/

API: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets

To build a sentence classifier, we would ues sentences as input and topics as output. We need some labled data such as search by quary on DC inbox. Therefore, we download 12 topics which is about 12,000 articles, 40,000 sentences for training purpose.

Sample data:
![data view](https://github.com/CS-UCR/cs105-prj-phase3-api/blob/master/github_pics/Screen%20Shot%202020-03-20%20at%206.13.32%20PM.png)

More information about cleaning DC inbox data, please check: api_proj_phase3_dc.ipynb

## Phase 3: Data Analysis Phase

Since the data we have is natural language, we decided to use two different ways to training the models.

**Universal Sentence Encoder (USE)**

Using USE to transform sentences to numerical matrics and feed to machine learning models. More detail, please check: EncodeDCinbox.ipynb

Pure USE methods (feed 512-dimension data): tweetModelTrain.ipynb

**Language Model with Term Frequency–Inverse Document Frequency (TF-IDF)**

Using TF-IDF information to feed the machine learning models.

Pure TF-IDF methods (feed 32,000-dimension data): api_proj_phase3_tfidf.ipynb

**Dimension Reduction**

Using sklearn's decomposition to reduce the dimension to 50, then using T-SNE to reduce the dimension from 50 to 2 and feed 2D data to machine learning models.

USE with 2D data: trainDatatfidf.ipynb
TF-IDF with 2D data: trainDataUSE.ipynb

## Contributions:

Jia Xie: Gathering data from API, crawing, and download. Cleaning data. Applied dimension reduction method for model training and plot the 2D diagrams.

Xichao Wang: Gathering data from API, crawing, and download. Cleaning data. Applied pure tf-idf method for model training.

Shuang Zhou: Gathering data from API, crawing, and download. Cleaning data. Applied pure USE method for model training.
