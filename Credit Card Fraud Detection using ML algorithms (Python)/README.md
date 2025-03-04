### Credit Card Fraud Detection

#### Introduction

In this project, we address the challenge of detecting fraudulent credit card transactions using a combination of NumPy, scikit-learn, and other Python libraries. Our approach involves developing a binary classifier to identify fraudulent activities. We experiment with several machine learning techniques, including Decision Trees, Random Forests, and Gradient Boosting, to determine which model performs best in accurately detecting fraud.

#### Dataset

This dataset encompasses transactions recorded over a two-day period, featuring a total of 284,807 transactions, of which 492 are identified as fraudulent. The dataset exhibits a significant class imbalance, with the positive class (frauds) constituting merely 0.172% of all transactions. Additionally, it comprises only numerical input variables that have been derived from a Principal Component Analysis (PCA) transformation.

- Time: transaction sequence
- V1 - V28: 28 numerical features transformed via PCA
- Amount: Dollar amount
- Class: 0 - genuine, 1 - fraud

Data can be accessed via the following link: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud.