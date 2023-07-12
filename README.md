### KNN Model Python
Machine Learning supervised KNN algorithm to vital signs classification

This repository is intended to be used as a part of the work done in 2023/1 semester in the Programming Techs class of Unisinos University.
Is a part of master degree.

The README is reduced because of the pre shared presentation slides and Latex article.

### What is KNN
KNN is a non-parametric, lazy learning algorithm. It stores all instances correspond to training data points in n-dimensional space. To label a new point, it looks at the labeled points closest to that new point also known as its nearest neighbors.
It is based on the idea that the observations closest to a given data point are the most "similar" observations in a data set, and we can therefore classify unforeseen points based on the values of the closest existing points

### Data

**Data model inside of application**
```json
{
    heart_rate: 82,
    temperature: 36.5
    spo2: 95
    label: 0
}
```

**Data Labelling and threshold:**
Labelling: label **1** for unhealty and **0** for healthy
Healthy (0) classification. In according with literature review and medical accepted for healthy range.

- Body Temperature: 36.5 to 37.3
- Heart Rate: 60 to 100
- SpO2: 95 or higher

**Database:**
[SQL](https://github.com/opoze/knn-model-python/blob/main/resources/vital_signs_materialized_view_create.sql) script for the project base materialized view is under the resources folder. 

Used with - MIMICIII - https://physionet.org/content/mimiciii/1.4/

![Materialized View  Head](https://raw.githubusercontent.com/opoze/knn-model-python/main/resources/vital_sign_sample.png)


### Application

**How to run**
```
python3 main.py
```

**Project Dependencies**
```
pip3 install  -r requirements.txt
```

**Application Flowchart**

![Application Flowchart](https://raw.githubusercontent.com/opoze/knn-model-python/main/resources/application_flow_chart.png)

**Application Class Diagram**
Application class diagram [XML](https://github.com/opoze/knn-model-python/blob/main/resources/class_diagrams.drawio) in resource folder.

![Application Class Diagram](https://raw.githubusercontent.com/opoze/knn-model-python/main/resources/class_diagram.png)

### Results

**Scatter Plot**

![Scatter Plot](https://raw.githubusercontent.com/opoze/knn-model-python/main/resources/scatter_plot_sample.png)

**Confusion Matrix**

![Confusion Matrix](https://raw.githubusercontent.com/opoze/knn-model-python/main/resources/confusion_matriz_sample.png)