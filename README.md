# 📊 Page View Time Series Visualizer

## 📌 Overview

The **Page View Time Series Visualizer** is a Python-based data analysis project that explores daily website traffic data over multiple years. The main goal of this project is to analyze long-term growth, compare yearly performance, and identify seasonal trends using time series visualization techniques.

This project demonstrates practical skills in data cleaning, transformation, and visualization.

---

## 📂 Dataset

The dataset includes:

- **date** — Daily timestamp  
- **value** — Number of page views  

To ensure accurate analysis, extreme outliers were removed by filtering out values below the 2.5th percentile and above the 97.5th percentile. This helps focus on normal traffic patterns rather than unusual spikes.

---

## 📈 Visualizations

### 1️⃣ Line Plot — Overall Trend

A time series line chart displaying daily page views across the entire time period.

**Purpose:**
- Identify overall growth patterns  
- Observe traffic fluctuations over time  
- Understand long-term engagement trends  

---

### 2️⃣ Bar Plot — Monthly & Yearly Comparison

A grouped bar chart showing the average monthly page views for each year.

**Purpose:**
- Compare performance across years  
- Identify high and low traffic months  
- Detect seasonal variations  

---

### 3️⃣ Box Plots — Distribution & Seasonality

Two box plots are created:

- **Year-wise Box Plot** → Shows yearly distribution trends  
- **Month-wise Box Plot** → Shows seasonal distribution patterns  

**Purpose:**
- Analyze variability in traffic  
- Detect seasonal behavior  
- Compare distribution changes over time  

---

## 🛠 Technologies Used

- Python  
- Pandas  
- Matplotlib  
- Seaborn  

---

## 🎯 Key Learning Outcomes

- Time series data analysis  
- Data cleaning and outlier removal  
- Statistical visualization techniques  
- Trend and seasonality detection  

---

## 🗂 Project Structure

```
page-view-time-series-visualizer/
│
├── README.md                     # Project documentation
├── fcc-forum-pageviews.csv       # Dataset containing daily page views
├── main.py                        # Script to execute and generate visualizations
├── time_series_visualizer.py      # Contains functions for plotting graphs
└── test_module.py                 # Unit tests for validation
```


This project is ideal for understanding real-world time series analysis and improving data visualization skills using Python.
