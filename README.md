# Loan Approval Prediction Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Project-Completed-success)
![Accuracy](https://img.shields.io/badge/Accuracy-96.16%25-brightgreen)
![F1 Score](https://img.shields.io/badge/F1--Score-0.975-brightgreen)

## 📌 Project Overview

This project focuses on building an end-to-end **Machine Learning classification system** to predict whether a loan application will be **Approved or Rejected** based on applicant financial and personal information.

The objective is to develop a predictive model that can assist financial institutions in making faster and data-driven loan approval decisions.

The complete ML pipeline includes data preprocessing, exploratory data analysis, feature engineering, model training, hyperparameter optimization, and evaluation.

| | |
|---|---|
| **Task** | Binary classification — Approved vs Rejected |
| **Dataset size** | 6,120 loan applications, 23 raw columns |
| **Final model** | Random Forest (tuned) |
| **Final performance** | **96.16% accuracy · 0.975 F1** |

---

# 📂 Dataset

The dataset contains applicant information related to:

* Personal details
* Employment information
* Financial status
* Credit history
* Assets
* Loan details

The target variable:

* **Loan Status**

  * Approved → 1
  * Rejected → 0

The raw dataset was intentionally messy — inconsistent text casing (`M`/`Male`/`male`/`MALE`), a whitespace-corrupted numeric column (`credit_score` stored as `' 764.0'`, forcing it to string dtype), a fully empty column, a duplicate index column, and a junk free-text column — all handled in the preprocessing stage below.

---

# 🔍 Exploratory Data Analysis (EDA)

Performed detailed analysis to understand relationships between applicant features and loan approval.

EDA includes:

* Target variable distribution
* Feature distributions
* Approval rate analysis
* Credit score analysis
* Income and loan amount comparison
* Correlation analysis using heatmaps
* Categorical feature analysis

**Key finding:** Demographic features (gender, marital status, education, self-employment, property area) showed almost no effect on approval — approval rates stayed within 1–3 points of the 76.8% baseline across every category. Credit score, however, showed a strong effect:

| Credit Band | Approval Rate |
|---|---|
| Poor | 64.8% |
| Fair | 73.7% |
| Good | 90.8% |
| Excellent | 91.7% |

This pointed clearly toward financial-capacity features — not demographics — as the real drivers of approval.

---

# ⚙️ Data Preprocessing

The following preprocessing steps were performed:

* Data cleaning
* Handling missing and inconsistent values
* Removing unnecessary columns
* Encoding categorical variables
* Converting target labels into numerical format
* Train-test splitting (80/20, stratified to preserve the 77/23 class balance)

### Encoding Techniques Used:

**Ordinal Encoding**

Used for education because categories have a natural order:
Not Graduate → 0
Graduate → 1
Post Graduate → 2

**One-Hot Encoding**

Used for nominal categorical features:

* Gender
* Marital Status
* Employment Status
* Loan Purpose
* Property Area
* Credit Score Band

---

# 🛠️ Feature Engineering

Created additional features to improve model performance:

### 1. Debt-to-Income Ratio

Measures loan amount compared to annual income.

Formula:
Loan Amount / Annual Income

---

### 2. Total Assets

Calculated total financial assets:
Residential Assets +
Commercial Assets +
Bank Balance

---

### 3. Asset-to-Loan Ratio

Measures financial strength:
Total Assets / Loan Amount

---

### 4. Expense Ratio

Measures monthly spending compared to income:
Monthly Expenses / Monthly Income

---

### 5. Credit Score Categories

Converted credit scores into groups:

* Poor
* Fair
* Good
* Excellent

**Payoff:** Three of these engineered features — `debt_to_income`, `monthly_income`, and `expense_ratio` — ended up in the **top 6 most important features** of the final model, ranking above several raw columns.

---

# 🤖 Machine Learning Models

Three classification algorithms were trained and compared:

## 1. Logistic Regression

A statistical classification algorithm used as a baseline model.

## 2. Decision Tree Classifier

A tree-based model that learns decision rules from data.

## 3. Random Forest Classifier

An ensemble learning algorithm that combines multiple decision trees to improve accuracy and reduce overfitting.

All models were trained with `class_weight='balanced'` to account for the 77/23 class imbalance in the dataset.

---

# 📊 Model Evaluation

Models were evaluated using:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Classification Report

These metrics helped compare model performance, especially because loan approval datasets may contain class imbalance.

### Results

| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Logistic Regression | 83.4% | 0.932 | 0.846 | 0.887 |
| Decision Tree | 95.0% | 0.972 | 0.963 | 0.967 |
| **Random Forest (tuned)** | **96.2%** | **0.975** | **0.976** | **0.975** |

Random Forest and Decision Tree substantially outperformed Logistic Regression, since the credit-score effect is threshold-based rather than linear — a pattern tree models capture naturally but linear models struggle with.

---

# 🚀 Hyperparameter Optimization

Random Forest performance was improved using:

## GridSearchCV

GridSearchCV automatically searches through different combinations of model parameters and selects the best configuration.

Parameters optimized:

* Number of trees (`n_estimators`)
* Maximum tree depth (`max_depth`)
* Minimum samples required for splitting
* Minimum samples required in leaf nodes

Optimization process:
Multiple Parameter Combinations
↓
5-Fold Cross Validation
↓
Best F1 Score Model
↓
Final Tuned Random Forest

Tuning improved the F1 score from 0.968 to **0.975**, with false negatives dropping from 36 to 23 on the test set.

Best parameters found: `n_estimators=200`, `max_depth=None`, `min_samples_split=2`, `min_samples_leaf=1`

---

# ⭐ Feature Importance

Random Forest feature importance was used to identify the most influential factors affecting loan approval.

Top 6 most important features:

| Rank | Feature | Importance |
|---|---|---|
| 1 | Debt-to-Income Ratio *(engineered)* | 0.203 |
| 2 | Annual Income | 0.164 |
| 3 | Monthly Income *(engineered)* | 0.160 |
| 4 | Credit Score | 0.107 |
| 5 | Existing Loans | 0.071 |
| 6 | Expense Ratio *(engineered)* | 0.063 |

---

# 🧰 Technologies Used

## Programming Language

* Python

## Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

## Environment

* Jupyter Notebook

---

# 📁 Project Structure
Loan-Approval-Prediction/
│
├── loan_dataset_messy.csv
├── Loan_Approval_Prediction.ipynb
├── README.md
│
└── requirements.txt

---

# 🔄 Machine Learning Pipeline
Raw Dataset
↓
Data Cleaning
↓
Exploratory Data Analysis
↓
Feature Engineering
↓
Encoding
↓
Train-Test Split
↓
Model Training
↓
Hyperparameter Tuning
↓
Model Evaluation
↓
Prediction

---

# 🎯 Project Outcome

This project demonstrates a complete Machine Learning workflow for a real-world classification problem.

The final tuned Random Forest model achieved **96.16% accuracy and a 0.975 F1 score**, identifying debt-to-income ratio, income, and credit score as the key financial factors driving approval outcomes — while demographic attributes (gender, marital status, education, property area) showed no meaningful influence, a reassuring fairness signal for a real-world loan model.

---

# 👨‍💻 Author

**Muhammad Talal Noor**

BS Artificial Intelligence Student

Machine Learning | Python | Data Science

GitHub: https://github.com/talalnoor