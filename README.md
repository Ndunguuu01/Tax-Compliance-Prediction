\# 📉 Corporate Income Tax (CIT) Loss Prediction

\### Group 9 Capstone Project | Moringa School



<img width="100%" alt="Header Image" src="https://github.com/user-attachments/assets/093ba018-e048-479e-9959-274aeffcb24b" />



!\[Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge\&logo=python\&logoColor=white)

!\[Scikit-Learn](https://img.shields.io/badge/Library-Scikit\_Learn-orange?style=for-the-badge\&logo=scikit-learn\&logoColor=white)

!\[Streamlit](https://img.shields.io/badge/Deployment-Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)

!\[Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)



---



\## 1. 📖 Executive Summary

This project develops an end-to-end machine learning system for predicting \*\*Corporate Income Tax (CIT) risk\*\*. The system analyzes historical corporate financial and compliance data to classify taxpayers into risk categories and is deployed as a web-based decision support tool.



The project demonstrates the complete data science lifecycle:

`Problem Definition` → `Data Engineering` → `EDA` → `Modeling` → `Evaluation` → `Deployment` → `Business Impact`



---



\## 2. 💼 Business Understanding



\### 2.1 Problem Statement

Tax authorities face critical challenges:

\* \*\*Identification:\*\* Difficulty identifying non-compliant taxpayers early.

\* \*\*Resources:\*\* Inefficient allocation of audit resources.

\* \*\*Volume:\*\* Handling large volumes of corporate data manually.

\* \*\*Limitations:\*\* Traditional rule-based systems are limited and reactive.



\### 2.2 Business Objective

To build a predictive system that:

1\.  Estimates the probability of CIT non-compliance.

2\.  Supports risk-based audit selection.

3\.  Improves tax compliance efficiency.



---



\## 3. 🎯 Project Objectives



| Technical Objectives | Business Objectives |

| :--- | :--- |

| 1. Clean and prepare corporate tax data. | 1. Improve audit targeting. |

| 2. Perform Exploratory Data Analysis (EDA). | 2. Reduce compliance enforcement costs. |

| 3. Engineer meaningful predictive features. | 3. Enable data-driven tax policy decisions. |

| 4. Train and evaluate ML models. | |

| 5. Deploy the best-performing model. | |



---



\## 4. 📊 Data Understanding

The dataset contains \*\*313,870 rows\*\* and \*\*61 columns\*\*. It includes anonymized corporate records such as Turnover categories, Industry classification, Filing frequency, and Loss/profit status.



\*\*Data Characteristics:\*\*

\* ✅ Mixed numerical and categorical variables.

\* ✅ Class imbalance (more compliant than non-compliant firms).

\* ✅ No personally identifiable information (PII).



---



\## 5. 🛠️ Tools \& Technologies



| Category | Tools Used |

| :--- | :--- |

| \*\*Programming\*\* | Python |

| \*\*Data Handling\*\* | Pandas, NumPy |

| \*\*Visualization\*\* | Matplotlib, Seaborn |

| \*\*Modeling\*\* | Scikit-learn, XGBoost |

| \*\*Explainability\*\* | SHAP |

| \*\*Deployment\*\* | Streamlit |

| \*\*Serialization\*\* | Joblib |

| \*\*Version Control\*\* | Git \& GitHub |



---



\## 6. 🔍 CRISP-DM Methodology



\### 6.1 Data Engineering

\* \*\*Missing Value Treatment:\*\* Imputed or removed missing data.

\* \*\*Correction:\*\* Fixed data types and inconsistencies.

\* \*\*Outliers:\*\* Detected and handled extreme values.

\* \*\*Scaling:\*\* Feature scaling and encoding applied.



\### 6.2 Exploratory Data Analysis (EDA)

We analyzed distributions, correlations, and risk profiles by turnover and industry.



<div align="center">

&nbsp; <img width="48%" alt="EDA 1" src="https://github.com/user-attachments/assets/e10d8f5f-73d2-4d45-b6fc-e42d4b4884ba" />

&nbsp; <img width="48%" alt="EDA 2" src="https://github.com/user-attachments/assets/dd95905f-a16d-4d9c-926b-066b32aa783d" />

</div>



\### 6.3 Feature Engineering

\* Created Turnover Quantiles.

\* One-hot encoding of categorical variables.

\* Normalization of numeric features.



---



\## 7. 🤖 Modeling

We implemented and evaluated four models:

1\.  \*\*Logistic Regression\*\* (Baseline)

2\.  \*\*Random Forest\*\*

3\.  \*\*Gradient Boosting\*\*

4\.  \*\*XGBoost\*\* (Champion Model)



<div align="center">

&nbsp; <img width="80%" alt="Model Results" src="https://github.com/user-attachments/assets/df949f9b-e513-40c1-97fd-fa7321c1f081" />

</div>



\*\*Model Selection:\*\*

We selected the champion model based on \*\*ROC-AUC\*\*, Precision, Recall, and Business Interpretability.



---



\## 8. 🚀 Deployment

<img width="738" height="905" alt="Screenshot 2026-01-23 233537" src="https://github.com/user-attachments/assets/f7b234a4-1950-43ec-bba3-705af96d66b3" />


The model is deployed using \*\*Streamlit\*\* to provide a user-friendly interface for tax officers.



\*\*Workflow:\*\*

`User` → `Web Interface` → `Trained Model` → `Prediction Engine` → `Risk Output`



\### How to Run Locally



\*\*Step 1: Clone Repository\*\*

git clone \[https://github.com/Ndunguuu01/Tax-Compliance-Prediction.git](https://github.com/Ndunguuu01/Tax-Compliance-Prediction.git)

cd Tax-Compliance-Prediction



Step 2: Install Dependencies

pip install -r requirements.txt



Step 3: Run Application

streamlit run app.py



\## 9. 📂 Project Structure

├── data/

├── notebook/

│   └── CIT\_Loss\_Prediction\_Notebook.ipynb

├── models/

│   └── cit\_model.pkl

├── app.py

├── requirements.txt

└── README.md



\## 10. 🔮 Future Enhancements



🔌 API integration with live tax systems.

🔄 Automated retraining pipelines.

📊 Integration with BI tools (Power BI/Tableau).

☁️ Cloud deployment (AWS/Azure/GCP).



⚠️ Ethical \& Legal Considerations



No personal data was used in this analysis.

Predictions are advisory only.

Human oversight is required for all enforcement actions.

