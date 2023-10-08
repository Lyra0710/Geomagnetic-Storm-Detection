# DSCOVR Project Report of work done by Aditya Hegde

## Project Overview

This README file contains the contributions of Aditya Hegde to this project as part of the NASA SpaceApps challenge. This project's primary objective is to employ advanced modeling techniques and official data sources to analyze and forecast space weather patterns by leveraging information gathered from the DSCOVR satellite.

## Datasets Used

### DSCOVR Official Dataset
- **Faraday-Cup Level-1 Data**
- **Magnetometer Level-1 Data**
  - Download Link: [DSCOVR Official Dataset](https://www.ngdc.noaa.gov/dscovr/portal/#/download)

### Kp Values
- **Kp values (kp1-kp8)**
- Calculated in 3-hour intervals, providing 8 Kp values per day.
  - Download Link: [Kp Values](https://kp.gfz-potsdam.de/app/files/Kp_ap_Ap_SN_F107_since_1932.txt)

## Final Dataset Used

The project's analysis is based on the **DSCOVR PlasMAG 2023 Data**. The finalized dataset is available in the following location:
```
./Aditya/Data/Merged_Kp.csv
```
Please note that other CSV files within the folders are intermediate data files used in the process of obtaining the final dataset.

## Models Used

Two models were employed in the project:

### LSTM Model
- This model did not perform well and had problems with implementation. Was continued by Harsh.

### Multiple Linear Regression, Polynomial Linear Regression, Decision Tree Regression, Random Forest Regression
- These models were implemented by Aditya and were tested on the older Dataset from DSCOVR. 
- Not good results.

### ARIMA Model
- Preliminary implementations showed promise. 
- Was continued on Harsh's implementation, refined, and then finalized for the project.

The notebook containing the imperfect ARIMA model implementation can be found here:
```
./Aditya/Old/Code_Only/other_models.ipynb
```

Additionally, the finalized ARIMA model has been exported and saved for reference:
```
./Harsh/Models/Exported-Final-Model/arima_model.pkl
```

---

Feel free to reach out if you have any questions or if you're interested in exploring the project further.
