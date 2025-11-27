# Claire's Place Foundation - Data Analysis Consulting Project

## Project Overview

**Organization:** Claire's Place Foundation  
**Mission:** Supporting families affected by Cystic Fibrosis  
**Project Duration:** Spring 2024 (April - May)  
**Team Size:** 6 students (I served as Team Leader)  
**My Role:** Team Leader, Co-Lead Analyst for Work Proudly Program (WPP)

Claire's Place Foundation operates two primary support programs:
- **Emergency Healthcare Support Grant (EHSG)** - Financial assistance for CF patients
- **Work Proudly Program (WPP)** - Career development and certification support

## Objective

Analyze the effectiveness of both programs following major policy changes in 2023, identify key success metrics, and provide data-driven recommendations to maximize impact for CF patients and their families.

## Data & Methodology

### Datasets Analyzed
- **5 comprehensive datasets** covering:
  - EHSG patient applications and grants
  - WPP program applications
  - Initial & exit self-esteem surveys
  - 3-month and exit program surveys
  - WPP expense tracking

- **374 total EHSG applications** representing $579,362 in grants
- **Multiple years of longitudinal data** (2003-2024)

### Analytical Approach

**Tools:** R (tidyverse, ggplot2, statistical testing packages)

**Techniques Applied:**
1. **Data Wrangling & Cleaning**
   - Removed outliers (e.g., 2002 anomalies)
   - Joined multiple datasets by applicant ID to create comprehensive profiles
   - Standardized inconsistent data formats

2. **Survey Quantification**
   - Converted qualitative responses to numeric scales
   - Assigned values to Likert-scale responses (Strongly Disagree → Strongly Agree)
   - Context-dependent scoring (positive responses received higher values)

3. **Statistical Analysis**
   - Two-sample hypothesis testing (means and proportions)
   - Confidence interval calculations
   - Simple linear regression modeling
   - Confounding variable identification

4. **Visualization & Pattern Recognition**
   - Distribution analysis (identified right-skewed grant patterns)
   - Time-series trends (applications before/after policy changes)
   - Demographic segmentation and cross-tabulation

## Key Findings

### Emergency Healthcare Support Grant (EHSG)

**Program Impact Metrics:**
- **$579,362** total granted over analysis period
- **$1,549** average grant per application
- **59% of applicants** were minors
- **Geographic concentration:** California, Florida, and Texas represented majority of grants

**Policy Change Analysis (June 2023):**
- **Significant impact on grant amounts** (p < 0.05) - policy change affected average grant distribution in both directions
- **Declining application rates** observed post-policy change
- **New applicant success rate decreased significantly** (p = 0.000)
  - Finding: Despite policy goal of increasing accessibility, proportion of successful new applicants declined
- **Distribution pattern:** Right-skewed distribution indicated most applicants received below-average amounts

**Grant Patterns:**
- New applicants received slightly higher average grants than returning applicants
- California dominated grant distribution geographically

### Work Proudly Program (WPP)

**Participant Demographics:**
- **64% unemployed** vs 36% employed at program start
- **Gender:** Predominantly female (significant confounding factor identified)
- **Age:** 47% ages 26-35, 27% ages 17-25
- **Income:** 79% in $0-25,000 range
- **Average household size:** 2.9 people

**Program Categories & Performance:**

Created four certification categories based on task and salary similarities:
1. **Administrative/Legal** (medical billing, transcription, paralegal, grant writing)
2. **Technical/Professional** (data science, web development, sound engineering)
3. **Creative Design** (graphic design, social media marketing, proofreading)
4. **Customer Service**

**Statistical Findings:**
- **Gender as confounding variable** for both Employment Status and Household Size (both p < 0.05)
- **Program success varied by category**: Administrative/Legal programs showed significantly higher success ratings than Creative Design programs (p = 0.0429, 95% CI [0.0528, 2.89])
- **Career consultancy uptake increased** post-September 2023 program update (p = 0.003, 95% CI [0.0492, 0.225])
- **Self-esteem changes:** No significant increase in average self-esteem improvement post-policy change; some groups showed decline

**Career Outcomes:**
- Higher proportion of unemployed applicants showed interest in updated career consultancy approach
- All certification programs had similar content satisfaction ratings (~4/5)
- Positive correlation found between program satisfaction and applicant expenses (linear regression)

**Qualitative Insights from Survey Comments:**
- Participants desired more active career consultant involvement post-certification
- Multiple mentions of insufficient job search support
- Some participants unable to complete program
- Need for regular check-ins and progress tracking

## Strategic Recommendations

### For EHSG Impact Measurement
1. **Utilize application counts and grants awarded** as primary quantitative metrics
2. **Focus on new applicant acquisition** - declining new applicant success rate is concerning
3. **Geographic expansion** beyond CA, FL, TX to broaden support network
4. **Monitor grant distribution equity** - address right-skewed pattern to ensure fair resource allocation

### For WPP Success Metrics & Improvements

**Immediate Implementation:**
1. **Track certificate program content satisfaction** as numeric variable for ongoing assessment
2. **Monitor unemployed applicant volume trends** over time as program awareness indicator
3. **Implement post-certification employment tracking** - critical missing metric

**Program Structure Enhancements:**
1. **Strengthen career consultant engagement**
   - Move beyond initial calls to active, ongoing job search support
   - Schedule regular check-ins (suggested: monthly for 3 months post-certification)
2. **Provide targeted support for underperforming categories**
   - Creative Design programs showed lower success - investigate root causes
   - Consider curriculum adjustments or additional support resources
3. **Improve program completion rates**
   - Identify barriers preventing completion
   - Implement milestone tracking and intervention protocols

**Data Collection Improvements:**
1. **Mandate 3-month post-certification employment survey**
2. **Incentivize survey completion** (e.g., tie final expense reimbursement to survey completion)
3. **Gather outcome-centered data:** employment status, salary/income changes, job satisfaction
4. **Track long-term impact** (6-month, 12-month follow-ups)

**Equity Considerations:**
1. **Address gender disparities** - provide connections to female workforce leaders
2. **Income-based support customization** - different income brackets showed different program engagement patterns
3. **Consider household size** in program design and support offerings

## Business Impact

**Quantifiable Outcomes:**
- Identified statistically significant factors affecting program success
- Established baseline metrics for ongoing program evaluation
- Provided evidence-based framework for resource allocation decisions

**Strategic Value:**
- Recommendations presented directly to CEO and leadership team
- Created 3-phase strategic roadmap for program optimization
- Projected 25% increase in patient aid applications through recommended interventions

## Technical Skills Demonstrated

- **Statistical Analysis:** Hypothesis testing (two-sample means, two-sample proportions), confidence intervals, linear regression
- **Data Wrangling:** Multi-dataset joins, missing data handling, outlier detection and removal
- **Survey Analysis:** Qualitative-to-quantitative conversion, Likert scale analysis
- **Data Visualization:** Distribution analysis, time-series trends, demographic segmentation
- **R Programming:** tidyverse, ggplot2, statistical testing packages
- **Business Communication:** Translating technical findings into actionable recommendations for non-technical stakeholders
- **Project Management:** Led 6-person team through full analytical lifecycle, coordinated deliverables, presented to C-level leadership

## Project Leadership

As Team Leader, I:
- Coordinated team of 6 members across multiple analytical workstreams
- Designed project timeline and milestone structure
- Facilitated collaboration between EHSG and WPP analysis subgroups
- Led final presentation to Claire's Place Foundation CEO
- Synthesized technical findings into cohesive strategic narrative
- Managed all final deliverable submissions

## Reflections & Learnings

**Key Takeaways:**
1. **Real client work requires different analytical rigor** - unlike classroom exercises, our recommendations would directly impact vulnerable CF patients and families
2. **Policy changes need comprehensive evaluation frameworks** - both EHSG and WPP policy updates showed unintended consequences that only emerged through careful analysis
3. **Missing data is often the most important finding** - our inability to track post-certification employment highlighted a critical organizational gap
4. **Stakeholder communication is as important as technical accuracy** - translating complex statistical findings into clear, actionable recommendations for nonprofit leadership

**Challenges Overcome:**
- Working with incomplete and inconsistent nonprofit data
- Balancing statistical rigor with practical organizational constraints
- Coordinating team analysis across multiple interconnected datasets
- Addressing sensitive topics (income, employment, health) with appropriate care

## Confidentiality Note

*Due to confidentiality agreements with Claire's Place Foundation, specific data, detailed visualizations, and individual-level findings cannot be shared publicly. This case study presents the analytical approach, aggregated findings, and strategic recommendations at a high level.*

---

**Project Completion:** May 2024  
**Academic Context:** BUAD 312 - Statistics & Data Science for Business, USC Marshall School of Business
