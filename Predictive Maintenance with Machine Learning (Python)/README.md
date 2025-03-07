## Predictive Maintenance with Machine Learning

### Introduction

This work focuses on Data Science applications in predictive maintenance, addressing the critical need for determining machine failure risks and their nature in Industry 4.0. The rationale is clear: the costs associated with repairing or replacing a faulty machine often exceed those for replacing individual components. Consequently, implementing sensors to monitor machine conditions and collect relevant data can yield significant cost savings for industries.

Utilizing the AI4I Predictive Maintenance Dataset from the UCI Repository, this analysis aims to meet the outlined needs. The study follows a structured Machine Learning framework, beginning with an exploratory analysis of the dataset to gain insights into the underlying patterns. Subsequently, data preprocessing techniques are applied to prepare the dataset for predictive algorithms. The focus is on predicting potential machine failures. Finally, we evaluate model performance using appropriate metrics and assess interpretability to identify the most effective model.

### Dataset
The dataset consists of 10 000 data points stored as rows with 14 features in columns:
- UID: unique identifier ranging from 1 to 10000;
- Product ID: consisting of a letter L, M, or H for low (60% of all products), medium (30%) and high (10%) as product quality variants and a variant-specific serial number;
- Air temperature [K]: generated using a random walk process later normalized to a standard deviation of 2 K around 300 K;
- Process temperature [K]: generated using a random walk process normalized to a standard deviation of 1 K, added to the air temperature plus 10 K;
- Rotational speed [rpm]: calculated from a power of 2860 W, overlaid with a normally distributed noise;
- Torque [Nm]: torque values are normally distributed around 40 Nm with a standard deviation of 10 Nm and no negative values;
- Tool wear [min]: The quality variants H/M/L add 5/3/2 minutes of tool wear to the used tool in the process;
- Machine failure: label that indicates, whether the machine has failed in this particular data point for any of the following failure modes are true. The machine failure consists of five independent failure modes:
- tool wear failure (TWF): the tool will be replaced of fail at a randomly selected tool wear time between 200 - 240 mins;
- heat dissipation failure (HDF): heat dissipation causes a process failure, if the difference between air- and process temperature is below 8.6 K and the tools rotational speed is below 1380 rpm;
- power failure (PWF):the product of torque and rotational speed (in rad/s) equals the power required for the process. If this power is below 3500 W or above 9000 W, the process fails;
- overstrain failure (OSF): if the product of tool wear and torque exceeds 11,000 minNm for the L product variant (12,000 M, 13,000 H), the process fails due to overstrain;
- random failures (RNF): each process has a chance of 0,1 % to fail regardless of its process parameters. If at least one of the above failure modes is true, the process fails and the 'machine failure' label is set to 1. It is therefore not transparent to the machine learning method, which of the failure modes has caused the process to fail.

The access to the full data and other details can be found here : https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification.
