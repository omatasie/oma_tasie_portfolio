# Nigeria Education Access Analysis

An exploratory data analysis examining educational access, gender disparities, and literacy trends in Nigeria from 2000-2024 using World Bank Development Indicators data.

## Project Overview

This project analyzes two decades of educational data from Nigeria to understand:
- Primary school enrollment trends and gender gaps
- Adult literacy rates and gender disparities
- Pupil-teacher ratios and classroom capacity challenges
- Data infrastructure limitations in educational monitoring

As a Nigerian student passionate about education equity, I wanted to examine the data behind educational access in my home country and identify key challenges facing the next generation.

## Key Findings

### 1. Female Education Crisis
- Female primary enrollment **declined** from 59% to 57% between 2000-2010
- Persistent **12-point gender gap** in primary enrollment (male: 70%, female: 58%)
- **16-point gap** in adult literacy (male: 78%, female: 62%)

### 2. Progress in Adult Literacy
- Total adult literacy improved from 54% (2003) to 70% (2024)
- Represents approximately **25 million more literate adults** over two decades
- However, gender disparities remain significant

### 3. Classroom Capacity Challenges
- Pupil-teacher ratios frequently exceeded UNESCO's recommended 40:1 maximum
- Ratio ranged from 43:1 (2000) to 38:1 (2010)
- During enrollment spikes, teacher supply couldn't keep pace, compromising quality

### 4. Data Infrastructure Gaps
- Limited enrollment data availability after 2010
- Literacy measured only periodically, not annually
- Highlights need for improved educational monitoring systems

## Dataset

**Source:** World Bank Development Indicators  
**Coverage:** Nigeria, 2000-2024  
**Indicators:**
- School enrollment, primary (% net) - total, female, male
- School enrollment, secondary (% net) - total, female, male
- Literacy rate, adult (ages 15+) - total, female, male  
- Pupil-teacher ratio, primary

**Data Quality Note:** Significant gaps exist in enrollment data post-2010, reflecting challenges in educational data collection infrastructure.

## Methodology

### Tools & Technologies
- **Python 3.12**
- **pandas** - Data manipulation and cleaning
- **matplotlib & seaborn** - Data visualization
- **Jupyter Notebook** - Analysis environment

### Analysis Steps
1. **Data Collection:** Downloaded data from World Bank DataBank
2. **Data Cleaning:** Reshaped from wide to long format, handled missing values
3. **Exploratory Analysis:** Created visualizations to identify trends and patterns
4. **Interpretation:** Connected findings to policy implications and development context

## Visualizations

1. **Primary Enrollment Trends** - Line chart showing enrollment by gender over time
2. **Gender Gap Analysis** - Visualization of the male-female enrollment gap
3. **Adult Literacy Rates** - Trends in literacy by gender across two decades
4. **Pupil-Teacher Ratio** - Classroom capacity relative to UNESCO standards
5. **Summary Dashboard** - Integrated view of all key metrics

## Project Structure
```
nigeria-education-analysis/
├── data/
│   └── nigeria_education_data.csv
├── notebooks/
│   └── Nigeria_Education_Analysis.ipynb
├── images/
│   ├── primary_enrollment_trends.png
│   ├── gender_gap_analysis.png
│   ├── literacy_rates.png
│   ├── pupil_teacher_ratio.png
│   └── summary_dashboard.png
└── README.md
```

## Key Insights for Policy

**Investment Priority:** Nigeria faces not just an access problem but a **sustained access problem** - enrollment gains aren't maintained, pointing to economic barriers, infrastructure gaps, and cultural factors (especially affecting girls).

**Teacher Recruitment Critical:** Expanding enrollment without expanding teaching capacity creates overcrowded classrooms that undermine learning quality.

**Focus on Girls:** With female enrollment declining while male enrollment holds steady, targeted interventions for girls' education are essential to prevent generational gender gaps.

## Limitations

- Enrollment data limited to 2000-2010 period
- National averages mask significant regional disparities (North vs. South, urban vs. rural)
- Analysis focuses on access (enrollment) rather than outcomes (learning, completion)
- Secondary school data too sparse for meaningful analysis

## Future Research Directions

- Regional disaggregation to examine North-South disparities
- Correlation analysis with economic indicators (poverty rates, GDP per capita)
- Examination of completion rates and learning outcomes
- Comparative analysis with peer countries (Ghana, Kenya, Senegal)
- Qualitative research on barriers to girls' education

## About

This project was completed as part of my data science portfolio while pursuing a BS in Business Administration (Finance) with minors in Data Science and Applied Analytics at USC Marshall School of Business.

**Context:** As someone from Nigeria applying to graduate programs in data science and business analytics, I wanted to apply my analytical skills to understanding educational challenges in my home country. This project combines my technical skills with my passion for education equity.

## Contact

**Omasirichi (Oma) Tasie-Amadi**  
[LinkedIn](https://www.linkedin.com/in/oma-ta) | omatasie@usc.edu

---

*Analysis completed November 2025*
