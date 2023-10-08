# DSCOVR Project Report by Ananya

## Project Overview
This README file contains the contributions made by Ananya as part of the 2023 NASA Space Apps Challenge:
Develop the Oracle of DSCOVR. 
The objective was to analyze, find insights and test some models on the DSCOVR's 'Level 2' dataset. 
Prepr

## Datasets Used

### DSCOVR Official Dataset
- **Faraday-Cup Level-2 Data**
- **Magnetometer Level-2 Data**
  - Download Link: [DSCOVR Official Dataset](https://www.ngdc.noaa.gov/dscovr/portal/#/download)

### Kp Values
- **Kp values (kp1-kp8)**
- Calculated in 3-hour intervals, providing 8 Kp values per day.
  - Download Link: [Kp Values](https://kp.gfz-potsdam.de/app/files/Kp_ap_Ap_SN_F107_since_1932.txt)

 ## Final Dataset Used

The finalized dataset is available in the following location:
```
./Merged_Dataset.csv
```
## Data Prepocessing
Data was obtained, decompressed and was converted from .cdf to .csv. Find the corresponding notebook here:
```
./datasets.ipynb
```
## Models Used
Data was cleaned for null values and y-data profiling was done to obtain correlations, zeroes and imbalances. 
You can find the implementations in:
```
./Level_2_Models.ipynb
```
### SVM
The model did not perform well. The accuracy scores were poor.

### ARIMA NN
This model was promising. The Test RMSE score was 1.054. This model was hence used for the 'raw' DSCOVR 
data as well. 
