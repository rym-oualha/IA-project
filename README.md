# IA-project

## Introduction
Welcome to the Intelligent Plant Pot System project! This system is designed to analyze images of plants to determine their nature and recommend optimal care strategies using the VGG-16 model for computer vision. It also features an easy-to-use interface built with the Streamlit library.

## Project Description
This project was developed in 2021 as a solution for plant enthusiasts to enhance their gardening experience. It leverages computer vision and machine learning techniques to identify plant species from images and provide personalized care recommendations.

## Key Features
Utilizes the VGG-16 model to achieve an overall accuracy of 85% in plant species recognition.
Provides an intuitive and user-friendly interface built with Streamlit for easy interaction.
Recommends optimal care strategies based on the recognized plant species.

## Requirements
* Python 3.8
* Dependencies listed in requirements.txt

## Usage
To create a virtual env :
```

pipenv --python 3.8

```
To activate the Pipenv shell:
```

pipenv shell

```
To run the code :  
<ins>(after adding your model and own path for images)</ins>
```

pipenv install -r requirements.txt
streamlit run test.py

```

Hope it helped you :fairy_woman:
