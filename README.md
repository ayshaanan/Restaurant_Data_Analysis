# 🍽️ Restaurant Data Analysis & Machine Learning

A comprehensive **Machine Learning and Data Analysis project** completed as part of the **Cognifyz Technologies internship**, using restaurant data to perform predictive modeling, recommendation, classification, and geographical analysis.

The project consists of four independent tasks, covering the complete workflow from **data preprocessing and exploratory analysis to machine learning and location-based insights**.

---

## 📌 Project Overview

The objective of this project is to extract meaningful insights from restaurant data and apply machine learning techniques to solve practical problems in the restaurant domain.

The project focuses on:

* Predicting restaurant ratings
* Building a restaurant recommendation system
* Classifying restaurants based on cuisine
* Performing geographical analysis of restaurants

The project demonstrates practical experience with **Python, Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn**.

---

## 🎯 Objectives

* Understand and preprocess real-world restaurant data.
* Handle missing values and categorical variables.
* Perform exploratory data analysis and visualization.
* Build and evaluate machine learning models.
* Develop a content-based restaurant recommendation system.
* Classify restaurants according to their cuisines.
* Analyze geographical patterns using restaurant location data.
* Extract meaningful insights from restaurant ratings, cuisines, pricing, and locations.

---

## 📂 Project Structure

```text
Restaurant_Data_Analysis/
│
├── restaurant.csv
├── .gitignore
│
├── Task_1/
│   ├── Task_1.py
│   ├── restaurant.csv
│   ├── Task1 Report.pdf
│   └── Output Screenshots
│
├── Task_2/
│   ├── Task_2.py
│   ├── restaurant.csv
│   ├── Task_2 Report.pdf
│   └── Output Screenshots
│
├── Task_3/
│   ├── Task_3.py
│   ├── restaurant.csv
│   ├── Task_3 Report.pdf
│   └── Output Screenshots
│
└── task_4/
    ├── Task_4.py
    ├── restaurant.csv
    ├── Task_4 Report.pdf
    ├── Graph 1.png
    ├── Graph 2.png
    └── Output Screenshots
```

---

# 🧩 Tasks Completed

## 🔹 Task 1 — Restaurant Rating Prediction

### Objective

Build a **Machine Learning regression model** capable of predicting the aggregate rating of a restaurant based on other available features.

### Key Steps

1. Load and explore the restaurant dataset.
2. Handle missing values and perform data preprocessing.
3. Encode relevant categorical variables.
4. Prepare the input features and target variable.
5. Split the dataset into training and testing sets.
6. Train regression models.
7. Evaluate the model using appropriate regression metrics.
8. Analyze the factors influencing restaurant ratings.

### Machine Learning Concepts

* Data preprocessing
* Feature selection
* Categorical encoding
* Train-test splitting
* Regression
* Model evaluation

---

## 🔹 Task 2 — Restaurant Recommendation System

### Objective

Develop a **restaurant recommendation system** that recommends restaurants according to user preferences.

### Key Steps

1. Preprocess the restaurant dataset.
2. Identify relevant restaurant attributes.
3. Consider user preferences such as:

   * Cuisine
   * Price range
   * Restaurant characteristics
4. Implement a **content-based filtering approach**.
5. Compare restaurant attributes to user preferences.
6. Generate suitable restaurant recommendations.
7. Test the recommendation system with sample preferences.

### Machine Learning Concepts

* Recommendation systems
* Content-based filtering
* Feature representation
* Similarity-based recommendations
* Data preprocessing

---

## 🔹 Task 3 — Cuisine Classification

### Objective

Develop a **Machine Learning classification model** to classify restaurants according to their cuisine categories.

### Key Steps

1. Load and preprocess the restaurant dataset.
2. Handle missing values.
3. Encode categorical features.
4. Prepare the classification dataset.
5. Split the data into training and testing sets.
6. Train a classification model.
7. Evaluate the classification performance.
8. Analyze the model's performance across different cuisine categories.

### Machine Learning Concepts

* Classification
* Feature preprocessing
* Categorical encoding
* Train-test splitting
* Model evaluation
* Accuracy and classification metrics

---

## 🔹 Task 4 — Geographical Analysis of Restaurants

### Objective

Perform a **geographical analysis** of restaurants using their latitude and longitude information to identify location-based patterns.

### Key Steps

1. Analyze the latitude and longitude coordinates of restaurants.
2. Visualize restaurant locations.
3. Group restaurants according to city or locality.
4. Analyze restaurant concentration across different locations.
5. Compare location-based characteristics such as:

   * Restaurant ratings
   * Cuisines
   * Price ranges
6. Identify geographical trends and patterns in the dataset.

### Analysis Concepts

* Geographical data analysis
* Location-based grouping
* Data visualization
* City/locality analysis
* Pattern identification

---

# 🛠️ Technologies & Libraries

### Programming Language

* **Python**

### Libraries

* **Pandas** — Data manipulation and analysis
* **NumPy** — Numerical computations
* **Matplotlib** — Data visualization
* **Seaborn** — Statistical visualization
* **Scikit-learn** — Machine Learning algorithms and evaluation

### Tools

* **Visual Studio Code**
* **Git**
* **GitHub**

---

# 📊 Dataset

The project uses a restaurant dataset containing information related to restaurants, including attributes such as:

* Restaurant ID
* Restaurant Name
* Country
* City
* Address
* Locality
* Longitude
* Latitude
* Cuisines
* Average Cost for Two
* Table Booking
* Online Delivery
* Price Range
* Aggregate Rating
* Rating Color
* Rating Text
* Votes

The dataset is used across the four tasks to perform analysis, prediction, recommendation, classification, and geographical exploration.

---

# ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/ayshaanan/Restaurant_Data_Analysis.git
```

### 2. Navigate to the project directory

```bash
cd Restaurant_Data_Analysis
```

### 3. Install the required libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 4. Run an individual task

For example:

```bash
python Task_1/Task_1.py
```

Similarly, the other tasks can be executed using:

```bash
python Task_2/Task_2.py
python Task_3/Task_3.py
python task_4/Task_4.py
```

---

# 📈 Project Workflow

```text
                Restaurant Dataset
                        │
                        ▼
              Data Preprocessing
                        │
                        ▼
             Exploratory Analysis
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
      Regression   Recommendation  Classification
          │             │             │
          ▼             ▼             ▼
    Rating         Restaurant      Cuisine
   Prediction     Suggestions    Classification
          │             │             │
          └─────────────┼─────────────┘
                        ▼
              Geographical Analysis
                        │
                        ▼
                 Insights & Results
```

---

# 📁 Results & Documentation

Each task folder contains its corresponding:

* Python implementation
* Task report
* Output screenshots
* Graphs/visualizations where applicable
* Dataset used for the task

The reports and visual outputs provide additional documentation of the analysis and results obtained during the project.

---

# 💡 Skills Demonstrated

Through this project, the following skills were developed and applied:

* Python programming
* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Data visualization
* Feature engineering
* Regression
* Classification
* Recommendation systems
* Geographical data analysis
* Machine Learning model evaluation
* Git and GitHub
* Project organization and documentation

---

# 🎓 Internship

**Machine Learning / Data Science Internship — Cognifyz Technologies**

This project was completed as part of the internship tasks provided by **Cognifyz Technologies**, with the goal of gaining practical experience in data analysis and machine learning using a real-world restaurant dataset.

---

# 👩‍💻 Author

**Aysha Anan**

Computer Science Engineering Student

GitHub: [@ayshaanan](https://github.com/ayshaanan)

---

## ⭐ Acknowledgements

* Cognifyz Technologies — Internship project and task specifications
* Restaurant dataset used for analysis and machine learning
* Python open-source data science ecosystem

---

## 📌 Repository

**Restaurant Data Analysis**

[View the project on GitHub](https://github.com/ayshaanan/Restaurant_Data_Analysis)
