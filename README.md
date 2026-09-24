Video link here:  https://drive.google.com/file/d/11NWC0NSfY-75pIih-iWrulbrwitji_mH/view?usp=sharing

# 🚢 Titanic Dataset — Exploratory Data Analysis

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on the Titanic passenger dataset to understand the factors associated with passenger survival.

The analysis focuses on examining passenger demographics, passenger class, fare, family-related information, and embarkation points. The project also includes data cleaning, correlation analysis, statistical summaries, and multiple visualizations to identify meaningful patterns in the dataset.

---

## 🎯 Objectives

* Understand the structure and characteristics of the Titanic dataset.
* Identify missing values and handle them appropriately.
* Check for duplicate records.
* Explore relationships between passenger attributes and survival.
* Analyze survival patterns across gender and passenger class.
* Examine the relationship between age, fare, family size, and survival.
* Visualize important patterns using different statistical plots.
* Generate insights from the data through group-based analysis.

---

## 📂 Dataset

The project uses the **Titanic training dataset (`train.csv`)**.

The dataset contains **891 passenger records and 12 columns**. The main features include:

| Column        | Description                       |
| ------------- | --------------------------------- |
| `PassengerId` | Unique passenger identifier       |
| `Survived`    | Survival status (0 = No, 1 = Yes) |
| `Pclass`      | Passenger class                   |
| `Name`        | Passenger name                    |
| `Sex`         | Passenger gender                  |
| `Age`         | Passenger age                     |
| `SibSp`       | Number of siblings/spouses aboard |
| `Parch`       | Number of parents/children aboard |
| `Ticket`      | Ticket number                     |
| `Fare`        | Passenger fare                    |
| `Cabin`       | Cabin information                 |
| `Embarked`    | Port of embarkation               |

The notebook confirms that `Age`, `Cabin`, and `Embarked` contain missing values, which are handled during the data-cleaning stage.

---

## 🛠️ Technologies & Libraries

* **Python**
* **NumPy** — Numerical operations
* **Pandas** — Data manipulation and analysis
* **Matplotlib** — Data visualization
* **Seaborn** — Statistical visualization
* **Jupyter Notebook**

---

## 🔍 Analysis Performed

### 1. Data Understanding

The dataset was explored using:

* `head()`
* `tail()`
* `info()`
* `shape`
* `columns`
* `describe()`

The dataset contains **891 rows and 12 columns**.

### 2. Data Quality Checks

The following checks were performed:

* Duplicate record detection
* Missing-value analysis
* Unique-value inspection
* Data type and structure inspection

### 3. Missing Value Handling

Missing values were handled using:

* **Median imputation** for the `Age` column.
* `"Unknown"` replacement for missing `Cabin` values.
* `"Unknown"` replacement for missing `Embarked` values.

This preserves the available records while making the dataset more suitable for further analysis.

### 4. Correlation Analysis

A correlation matrix was created using the numerical columns, followed by a **Seaborn heatmap** to visually examine relationships between numerical variables.

The analysis shows, among other relationships, a negative correlation between `Pclass` and `Survived`, while `Fare` has a positive correlation with `Survived`.

### 5. Group-Based Analysis

Survival was analyzed across different passenger characteristics using Pandas `groupby()` operations, including:

* Gender-wise survival
* Passenger-class-wise survival rate
* Gender-wise survival rate
* Family-related variables (`SibSp` and `Parch`)
* Embarkation-wise survival
* Overall survival distribution

---

## 📊 Visualizations

Several visualization techniques were used to understand the data:

<img width="482" height="377" alt="image" src="https://github.com/user-attachments/assets/845caf99-1157-421c-84ac-91d6851682b9" />

<img width="400" height="410" alt="image" src="https://github.com/user-attachments/assets/c36f1780-3d8e-4552-a5d2-463aee973b4f" />

<img width="487" height="395" alt="image" src="https://github.com/user-attachments/assets/3f8dfaa2-be62-48d3-a7b4-f1e8c61780e0" /> 

<img width="504" height="369" alt="image" src="https://github.com/user-attachments/assets/729e52e1-1dc2-49b6-bdd3-3ee15fd63759" />

<img width="513" height="377" alt="image" src="https://github.com/user-attachments/assets/c3de0cb2-1b4e-4b99-94c2-159d66f45868" />

<img width="504" height="379" alt="image" src="https://github.com/user-attachments/assets/cd03704e-a679-49de-bb30-ad841f91e729" />



---

## 💡 Key Observations

The analysis highlights several important patterns:

* **Gender has a strong relationship with survival**, with survival rates differing considerably between male and female passengers.
* **Passenger class is associated with survival**, with survival rates varying across the three classes.
* `Pclass` and `Fare` show noticeable relationships with the survival variable.
* Passenger age and fare distributions vary across passenger classes and survival groups.
* The port of embarkation also shows differences in survival rates.
* Family-related variables such as `SibSp` and `Parch` provide additional information about passenger groups and their survival patterns.

These observations demonstrate how EDA can be used to discover patterns and relationships before applying further statistical or machine-learning techniques.

---

## 📁 Project Structure

```text
Titanic-EDA/
│
├── titanic.ipynb
├── train.csv
└── README.md
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-link>
```

### 2. Install the required libraries

```bash
pip install numpy pandas matplotlib seaborn jupyter
```

### 3. Open the notebook

```bash
jupyter notebook titanic.ipynb
```

Make sure `train.csv` is available in the same directory as the notebook.

---

## 📌 Conclusion

This project demonstrates a complete **Exploratory Data Analysis workflow** using Python.

Starting from understanding the dataset and checking data quality, the analysis proceeds through missing-value handling, correlation analysis, group-based analysis, and visualization. The results provide a clearer understanding of the factors associated with Titanic passenger survival.
