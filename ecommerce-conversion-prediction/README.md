# E-Commerce Conversion Prediction

Machine learning system for predicting customer purchase behavior in online shopping environments using K-Nearest Neighbors classification.

## Project Overview

**Course:** TAC 216 - Applied Python for Data Science, USC  
**Objective:** Build an end-to-end ML pipeline to analyze e-commerce customer behavior and predict purchase probability  
**Techniques:** K-Nearest Neighbors (KNN), feature scaling, train-test validation

## Problem Statement

Online retailers need to understand which website visitors are likely to make purchases to optimize marketing spend, personalize experiences, and improve conversion rates. This project analyzes customer session data to predict whether a visitor will complete a transaction.

## Dataset

**Source:** [Online Shoppers Purchasing Intention Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset)  
**Size:** 12,000+ customer sessions  
**Features Used:**
- `PageValues` - Average value of pages visited during session
- `ExitRates` - Rate at which users exit from pages
- `ProductRelated_Duration` - Time spent on product pages (seconds)
- `VisitorType` - New vs. Returning visitor
- `Revenue` - Target variable (Boolean: purchase made or not)

**Data Characteristics:**
- 1000+ data points meeting Big Data criteria
- Majority numeric features for ML compatibility
- Real-world e-commerce behavior patterns
- Imbalanced classes (most sessions don't result in purchases)

## System Architecture

### Class Design: `ShopAnalytics`

**Object-Oriented Structure:**
```python
class ShopAnalytics:
    - df_shoppers: DataFrame (cleaned customer data)
    - model: KNeighborsClassifier (trained ML model)
    - scaler: StandardScaler (feature normalization)
    - X_test, y_test, y_pred: Test data and predictions
```

**Pipeline Methods:**
1. `wrangle()` - Data loading, cleaning, filtering
2. `computation()` - Statistical analysis and aggregation
3. `run_ml()` - Model training and evaluation
4. `visualise()` - Interactive visualization generation

## Technical Implementation

### 1. Data Wrangling

**Data Cleaning Process:**
- Load raw CSV with 12,000+ sessions
- Select relevant features for purchase prediction
- Rename columns to snake_case convention
- Remove rows with missing values
- Filter malformed data (negative durations)

**Feature Engineering:**
- Convert visitor type to categorical variable
- Normalize continuous features for KNN
- Create train-test splits with stratification

### 2. Scientific Computation

**Statistical Analysis:**
- Group sessions by visitor type (New vs. Returning)
- Calculate average page values and session duration
- Identify behavioral differences between user segments

**Key Insight:** Returning visitors show significantly higher average page values, indicating stronger purchase intent.

### 3. Machine Learning Model

**Algorithm: K-Nearest Neighbors (KNN)**

**Why KNN?**
- Non-parametric: Makes no assumptions about data distribution
- Interpretable: Classifies based on similar customer sessions
- Effective for behavioral patterns with clear boundaries

**Model Configuration:**
- **k = 15 neighbors** (optimized for balance between bias and variance)
- **Features:** Page values, exit rates, product browsing duration
- **Target:** Binary classification (purchase: yes/no)

**Training Process:**
```python
# 75-25 train-test split with stratification
train_test_split(X, y, test_size=0.25, stratify=y)

# Feature scaling (essential for KNN)
StandardScaler().fit_transform(X_train)

# Model training
KNeighborsClassifier(n_neighbors=15).fit(X_train, y_train)
```

**Model Evaluation:**
- Confusion matrix visualization
- Classification report (precision, recall, F1-score)
- Separate analysis for new vs. returning visitors

### 4. Data Visualization

**Two-Panel Analysis System:**

**Panel 1: Real Data Distribution (Blue)**
- Scatter plot: Page Values vs. Exit Rates
- Shows actual customer behavior patterns
- Identifies clusters of high-value sessions

**Panel 2: Model Predictions (Orange)**
- Confusion matrix heatmap
- Visual assessment of classification accuracy
- True Positives, False Positives, True Negatives, False Negatives

**Interactive Features:**
- User can select visitor type subset:
  1. Returning Visitors
  2. New Visitors  
  3. All Visitors
- Generates separate analysis for each segment
- Saves visualizations with unique filenames

## Key Findings

### Customer Behavior Insights

**Returning Visitors:**
- Higher average page values (stronger purchase signals)
- Lower exit rates (more engaged browsing)
- Longer product page durations (deeper consideration)
- **Higher conversion probability**

**New Visitors:**
- Lower page values (exploratory browsing)
- Higher exit rates (higher bounce probability)
- Shorter session durations
- **Lower conversion probability**

### Model Performance

**Classification Metrics:**
- **Precision:** Percentage of predicted purchases that were correct
- **Recall:** Percentage of actual purchases correctly identified
- **F1-Score:** Harmonic mean of precision and recall

**Business Impact:**
Model enables targeted interventions:
- Show promotions to high-probability converters
- Offer incentives to low-probability browsers before they exit
- Personalize experience based on predicted behavior

## Technologies Used

**Core Libraries:**
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **scikit-learn** - Machine learning algorithms and metrics
- **matplotlib** - Data visualization

**ML Components:**
- `KNeighborsClassifier` - Core prediction algorithm
- `StandardScaler` - Feature normalization
- `train_test_split` - Dataset partitioning
- `confusion_matrix` - Model evaluation
- `classification_report` - Performance metrics

## Usage

### Running the Program

```bash
python main.py
```

### Interactive Menu

```
--- Visualisation Menu ---
1. View Returning Visitors
2. View New Visitors
3. View All Visitors
4. Quit
```

**Workflow:**
1. Program loads and cleans data automatically
2. Computes statistical aggregations
3. Trains KNN model on 75% of data
4. User selects visitor segment to analyze
5. Generates dual-panel visualization (real vs. predicted)
6. Saves plot to file (e.g., `analysis_Returning_Visitors.png`)
7. User can repeat for different segments

## Project Structure

```
ecommerce-conversion-prediction/
├── main.py                    # Main program with ShopAnalytics class
├── shoppers.csv              # Dataset (12,000+ sessions)
├── analysis_All_Visitors.png         # Generated visualization
├── analysis_Returning_Visitors.png   # Returning visitor analysis
├── analysis_New_Visitors.png         # New visitor analysis
└── README.md                         # This file
```

## Skills Demonstrated

**Machine Learning:**
- Supervised learning (classification)
- Feature engineering and selection
- Data preprocessing and scaling
- Train-test validation methodology
- Model evaluation metrics (confusion matrix, classification report)

**Data Science:**
- Exploratory data analysis
- Statistical aggregation and grouping
- Data cleaning and wrangling
- Visualization of results

**Software Engineering:**
- Object-oriented programming (OOP)
- Class-based architecture
- Error handling and validation
- Code documentation (docstrings)
- Modular function design

**Python Proficiency:**
- pandas DataFrame manipulation
- numpy array operations
- scikit-learn ML pipeline
- matplotlib plotting
- File I/O and error handling

## Future Enhancements

**Model Improvements:**
- Experiment with other algorithms (Random Forest, Logistic Regression, Gradient Boosting)

**Feature Engineering:**
- Include temporal features (day of week, time of day, season)
- Add user engagement metrics (bounce rate, pages per session)
- Incorporate product category preferences

**Business Applications:**
- Real-time scoring for live website traffic
- Integration with marketing automation platforms
- A/B testing framework for intervention strategies
- ROI analysis for conversion optimization

**Visualization Enhancements:**
- Interactive dashboards with Plotly/Dash
- Real-time prediction monitoring
- Customer journey visualization
- Cohort analysis over time

## Technical Challenges & Solutions

### Challenge 1: Class Imbalance
**Problem:** Most sessions don't result in purchases (~85% non-purchasers)  
**Solution:** Stratified train-test split ensures both classes represented proportionally

### Challenge 2: Feature Scaling
**Problem:** Page values range 0-100+ while durations range 0-10,000+ seconds  
**Solution:** StandardScaler normalization ensures equal feature influence in KNN

### Challenge 3: Model Interpretability
**Problem:** Users need to understand why predictions were made  
**Solution:** KNN is inherently interpretable - predictions based on similar historical sessions

## Academic Context

**Course Requirements Met:**
- ✅ Big Data: 12,000+ sessions exceeding 1,000 data point minimum
- ✅ Scientific Computation: Statistical aggregation by visitor type
- ✅ Machine Learning: KNN classification with train-test validation
- ✅ Visualization: Dual-panel plots (real data + predictions)
- ✅ User Interaction: Menu-driven subset selection

**Code Constraints:**
- Original work following academic integrity policies
- Proper attribution of dataset source
- Professional code structure and documentation

## Conclusion

This project demonstrates end-to-end machine learning workflow from data loading through model deployment. The KNN classifier achieves meaningful purchase prediction accuracy, enabling targeted business interventions to improve e-commerce conversion rates.

**Key Takeaway:** Understanding customer behavior patterns through data analysis and machine learning enables retailers to optimize the shopping experience and increase revenue through personalized engagement strategies.

---

**Course:** TAC 216 - Applied Python, USC  
**Date:** Fall 2025
