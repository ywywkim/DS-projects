## Quality Inspection (Defect Detection) of Printed Circuit Board using Deep Neural Network Model

### Introduction

Quality inspection of products is a critical process in manufacturing and is typically relied on human operators to evaluate items for acceptance or rejection, sometimes resulting in an unsatisfactory outcome. 
This manual process is not only costly but also time-consuming. To enhance efficiency, we engage in leveraging computer vision (CV), deep learning algorithm to automate parts of the inspection process. 
This project focuses on developing a Convolutional Neural Network (CNN) model using the TensorFlow library in Python to address the challenges of automated inspection. 
We will evaluate the model's performance primarily using the recall metric to assess its effectiveness in classifying defective parts.

### Dataset
- This data set is a subset of the VisA dataset, which contains subsets of object images. Within the dataset, we will utilize PCB1 data, which contain image data of printed circuit board parts.
In the data, there are a total of 1,104 images, where 1,004 images are normal samples and 100 are anomaly samples.

The data can be accessed here : https://github.com/amazon-science/spot-diff?tab=readme-ov-file.
