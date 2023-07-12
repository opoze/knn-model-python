### KNN Model Python
Machine Learning supervised KNN algorithm to vital signs classification

This repository is intended to be used as a part of the work done in 2023/1 semester in the Programming Techs class of Unisinos University.
Is a part of master degree.

The README is reduced because of the pre shared presentation slides and Latex article.

### What is KNN
KNN is a non-parametric, lazy learning algorithm. It stores all instances correspond to training data points in n-dimensional space. To label a new point, it looks at the labeled points closest to that new point also known as its nearest neighbors.
It is based on the idea that the observations closest to a given data point are the most "similar" observations in a data set, and we can therefore classify unforeseen points based on the values of the closest existing points

### What about the Vital Signal format

**Data model inside of application**
```json
{
    heart_rate: 82,
    temperature: 36.5
    spo2: 95
    label: 0
}
```


**Labelling threshold:**
Labelling: label **1** for unhealty and **0** for healthy
Healthy (0) classification. In according with literature review and medical accepted for healthy range.

- Body Temperature: 36.5 to 37.3
- Heart Rate: 60 to 100
- SpO2: 95 or higher

### How to run
python3 main.py

### Project Dependencies
pip3 install  -r requirements.txt

### Database
SQL script for the project base materialized view is under the resources folder.

Used with - MIMICIII - https://physionet.org/content/mimiciii/1.4/


### Results

**Scatter Plot**

**Confusion Matrix**

