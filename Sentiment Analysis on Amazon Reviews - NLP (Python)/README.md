### Sentiment Analysis on Amazon Product Reviews - Natural Language Processing in Python

#### Introduction

In the age of digital commerce, understanding customer sentiment is crucial for businesses to enhance their products and services. This project aims to develop a robust sentiment analysis classifier that evaluates Amazon customer reviews, leveraging two powerful tools: NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) and Huggingface's Roberta Transformers. VADER is particularly effective for analyzing sentiments expressed in social media and short texts, making it well-suited for customer reviews. In contrast, Roberta, a transformer-based model, harnesses the power of deep learning to capture nuanced sentiments in longer and more complex reviews. By integrating these methodologies, this project seeks to provide a comprehensive understanding of customer feedback, enabling businesses to make informed decisions based on sentiment trends.


#### Dataset

- This dataset consists of reviews of fine foods from amazon. The data span a period of more than 10 years, including all ~500,000 reviews up to October 2012. Reviews include product and user information, ratings, and a plain text review. It also includes reviews from all other Amazon categories.
- Data includes:
 - Reviews from Oct 1999 - Oct 2012
 - 568,454 reviews
 - 256,059 users
 - 74,258 products
 - 260 users with > 50 reviews