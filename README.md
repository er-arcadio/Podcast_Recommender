# "This American Life" Podcast Recommender

### Project 5 at Metis - ["This Repo"](https://github.com/er-arcadio/Podcast_Recommender)

**Objective: "How can we get more people to get into podcast listening?"**

The goal of this NLP project is to attempt to use data science techniques to make it easier on users to start listening to podcasts, and use machine learning to generate personalized recommendations so that they can continue once they've started. The transcripts of each podcast will be carefully scraped from thisamericanlife.org, explored and visualized via Jupyter Notebook, modeled via a flask app, and summarized in [this Youtube video](https://youtu.be/d5uRXDlIP3g).

**Note: The following files are not available because they are too large for GitHub "uncleaned_podcasts.csv" and "w2v.pkl"**

## Scraping and Cleaning the Podcast Transcriptions

- Scrape the podcast transcriptions from "This American Life"
- Clean the data and prepreocess the transcriptions for ease of use later on

**Files Refferenced**

[Scraping Podcasts Notebook](https://github.com/er-arcadio/Podcast_Recommender/blob/master/Notebooks_and_CSVs/Scraping_Podcasts.ipynb)

[Cleaning & Preprocessing Notebook](https://github.com/er-arcadio/Podcast_Recommender/blob/master/Notebooks_and_CSVs/Clean_WordEmbed_Recommend.ipynb)


## Providing a Starting Point & Generating Recommendations

- Upload Google's pretrained word embedding neural network to vectorize all the podcasts
- Develop techniques to put podcast vecotors, user vectors, and search query vectors in the same word embedding space
- Use cosine similarity to generate recommendations and search results
- Topic Model on the corups using TF-IDF and NMF
- Create a word cloud for presentation 

**Files Refferenced**

[Word Embedding & Recommendation Notebook](https://github.com/er-arcadio/Podcast_Recommender/blob/master/Notebooks_and_CSVs/Clean_WordEmbed_Recommend.ipynb)

[Topic Modeling & Word Cloud Notebook](https://github.com/er-arcadio/Podcast_Recommender/blob/master/Notebooks_and_CSVs/TopicModeling_Podcasts.ipynb)


## Flask App Search & Recommender, and Presentation

- Create an app using Flask that will allow the user to search, and store a user's likes to then make recommendations based on all their likes. 
- Prepare a presentation and record it on YouTube

**Files Refferenced**

[Flask App Files](https://github.com/er-arcadio/Podcast_Recommender/tree/master/Flask_App)

[Presentation (pdf)](https://github.com/er-arcadio/Podcast_Recommender/blob/master/PodcastRecommender.pdf)

See a [YouTube video](https://youtu.be/d5uRXDlIP3g) of me summarizing it all.

