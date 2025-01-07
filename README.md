# Applied Data Science Capstone

This repository contains the final capstone project for my Applied Data Science journey. The goal of this project is to apply all the skills and techniques I have learned to solve a real-world problem using data science methodologies. The focus of this capstone is to analyze and predict the cost of conducting a space mission outside Earth's orbit, with specific emphasis on the success rate of SpaceX Falcon 9 first stage landings.

---

## Project Overview

**Problem Statement:**
A company looking to compete in the space industry needed a comprehensive analysis of factors influencing the cost of orbital missions. A key determinant of mission cost is whether the first stage of the Falcon 9 rocket successfully lands. This project aims to predict the success of the first-stage landings and analyze the resulting mission costs using historical SpaceX data.

---

## Key Features

### 1. **Data Acquisition**

- Data was obtained through multiple sources:
  - **APIs** for accessing SpaceX launch data.
  - **Web scraping** for supplementary information.
  - **SQL queries** for structured database retrieval.

### 2. **Data Wrangling**

- Cleaning and preprocessing raw data to ensure consistency and usability.
- Merging, transforming, and organizing datasets for analysis.

### 3. **Exploratory Data Analysis (EDA)**

- In-depth analysis of the factors affecting first-stage landings.
- Identification of trends and patterns in SpaceX launch data.

### 4. **Data Visualization**

- Interactive and static visualizations created using:
  - **Matplotlib** and **Seaborn** for traditional plots.
  - Folium for geospacial visuals
  - **Plotly** for dynamic and engaging visuals.

### 5. **Data Preprocessing**

- Feature engineering to create predictive variables.
- Handling missing values and categorical data.
- Scaling and normalization for machine learning readiness.

### 6. **Machine Learning Models**

- Built predictive models to estimate landing success probability:
  - Logistic Regression
  - Decision Tree
  - Support Vector Machines (SVM)
- Evaluated models using metrics such as accuracy, precision, recall, and F1 score.

### 7. **Dashboards and Storytelling**

- Developed interactive dashboards using **Dash** to present findings.
- Created a final storytelling presentation to deliver insights effectively to stakeholders.

---

## Technologies and Tools

- **Programming Language:** Python
- **APIs:** SpaceX API, Wikipedia web scrapping
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-learn, Dash, Folium
- **Data Storage:** SQL databases
- **Web Scraping:** BeautifulSoup
- **Machine Learning Models:** Logistic Regression, Random Forest, SVM

---


## Key Findings

- Successfully predicted the landing success of Falcon 9's first stage with high accuracy.
- Identified critical factors influencing the mission costs, including payload mass, launch site, and first-stage landing success.
- Developed actionable insights to guide the company's strategy in competing with SpaceX.

---

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/SebabsKHE/Applied-data-Science-Capstone.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Navigate to the `notebooks/` or `dashboards/` directory to explore the analysis or run the dashboards.

---

## Acknowledgments

- **SpaceX** for providing open data.
- The Applied Data Science curriculum for equipping me with the necessary tools and knowledge.

---

## License

This project is licensed under the [MIT License](LICENSE).

Sebastián Caicedo



