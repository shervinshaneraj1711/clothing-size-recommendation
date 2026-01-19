# Clothing Size Recommendation Using Body Measurements

## Project Overview
This project predicts the appropriate clothing size (S, M, L, XL) based on body measurements such as height, weight, chest, waist, and hip using a machine learning classification model.

## Problem Statement
Choosing the correct clothing size is challenging for customers and often leads to size mismatch issues. This project aims to solve this problem using basic machine learning techniques.

## Dataset
A synthetic dataset was generated using realistic clothing size measurement ranges to simulate real-world data.

Features used:
- Height (cm)
- Weight (kg)
- Chest (cm)
- Waist (cm)
- Hip (cm)

Target:
- Clothing Size (S, M, L, XL)

## Machine Learning Model
- Algorithm: Logistic Regression
- Type: Multi-class Classification
- Libraries: scikit-learn, pandas, numpy

## How to Run the Project
1. Install required libraries: pip install pandas numpy scikit-learn
2. Generate dataset: python generate_dataset.py
3. Open and run the notebook: jupyter notebook
4. Run all cells in `size_classification.ipynb`

## Output
The model predicts the most suitable clothing size for a given set of body measurements.

## Author
Shervin Shane Raj Louis Raj
