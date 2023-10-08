# Exploring and Analyzing the L1 and L2 Data🌌📊

## Repository Files 📁📄

In this section, you can find detailed information about the files included in this repository:

### 1. Folders 📊
- **L2_FirstLook**: This folder has the cleaned datasets - filled_dataset.csv, filled_kp.csv, filled_nokp, merged_both_csv and the models used on them along with the ydataprofiling report of the final dataset used. The files related the L1 Data are the following (stored in L2_FirstLook):

1. Merged_Kp.csv
2. Models.ipynb
3. test_report.zip

- **L2_Data**: This folder contains the detailed analysis report, the .ipynb file for analysis techniques used and final cleaned data files along with the ydataprofiling report. In this case it is the Merged_Kp.csv.


## Part 1: Exploring L2 Data 🚀

### Cleaning and Analyzing L2 Data 🧹🔍

In this part of the project, we focused on exploring and cleaning Level 2 (L2) data. We conducted a thorough analysis of the data, identifying patterns, outliers, and missing values if any.

### Experimenting with Models on L2 Data 🤖🧪

Experimented with various machine learning models on the L2 data, including:
- Pure LSTM
- Multivariate LSTM
- GRU
- Attention Mechanism

While the results showed some promise, the models tested on L2 data were not significant enough to make reliable predictions.

## Part 2: Exploring L1 Data 🪐

### Detailed Analysis of Attribute Relationships 📈🔗

In this section, we delved into Level 1 (L1) data. We conducted a detailed analysis of the relationships between attributes using Recursive Feature Elimination (RFE) and Random Forest Regressor (RF Regressor) techniques.

### Feature Selection Using RFE and RF Regressor 🧐✂️

The feature selection analysis on L1 data led us to prioritize the following features:

#### Method 1 - RF Feature Importance:
Features: 'x', 'e', 'ac', 'u', 't', 'r', 'y', 's', 'd', 'a', 'k'

#### Method 2 - RFE Feature Ranking:
Features: "r", "x", "t", "u", "ac", "k", "y", "d", "s"

#### Correlation Values with Kp:

1. 'x' - Correlation: 0.564222
2. 'y' - Correlation: 0.560131
3. 'ab' - Correlation: 0.542513
4. 'w' - Correlation: 0.533065
5. 'z' - Correlation: 0.532973
6. 'aa' - Correlation: 0.529855
7. 'ac' - Correlation: 0.527724

Considering both the feature importance rankings and correlation values, you can prioritize the following features:

1. 'x' (Method 1 and Correlation)
2. 'y' (Method 2 and Correlation)
3. 'ac' (Method 1 and Correlation)
4. 'ab' (Correlation)
5. 'w' (Correlation)
6. 'z' (Correlation)
7. 'aa' (Correlation)

These feature selection methods were employed to identify better features for our predictive models.

### Significance of Full-Fledged GRU Model on L1 Data 🤔

It's important to note that despite our efforts to implement a full-fledged GRU model on L1 data, we encountered dimensional errors that affected the significance of the results. Due to these issues, the full potential of the GRU model on L1 data remains unexplored.

## Conclusion 🚀🌠

The work involved exploring and analyzing both L2 and L1 data, experimenting with various machine learning models, and conducting rigorous feature selection analysis. While L2 models showed limited significance, our L1 data analysis provided valuable insights into feature prioritization for improved forecasting.

