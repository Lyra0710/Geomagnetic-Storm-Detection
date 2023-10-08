
# DSCOVR Project Report of work Done by Harsh Goyal

## Project Overview

Welcome to the DSCOVR project, by Harsh Goyal from India. This project focuses on analyzing and predicting space weather using data from the DSCOVR satellite. The project primarily utilizes datasets from official sources and applies advanced modeling techniques to understand and forecast space weather patterns.

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
./Harsh/Models/Data/Final-File-in-use.csv
```
Please note that other CSV files within the folders are intermediate data files used in the process of obtaining the final dataset.

## Models Used

Two models were employed in the project:

### LSTM Model
- Root Mean Square Error (RMSE): 1.985
- This model did not perform as well as expected on the dataset.

### ARIMA Model
- R-squared (R2) Score: 0.5345
- Outperformed the LSTM model and was selected as the final model.

The notebook containing the ARIMA model implementation can be found here:
```
./Harsh/Models/Codes/ARIMA-model.ipynb
```

Additionally, the finalized ARIMA model has been exported and saved for reference:
```
./Harsh/Models/Exported-Final-Model/arima_model.pkl
```

---

Feel free to reach out if you have any questions or if you're interested in exploring the project further. Thank you for your interest in the DSCOVR project by Harsh Goyal!
