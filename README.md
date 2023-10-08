# Predicting Geomagnetic Storms with the Oracle of DSCOVR 🌌⚡

![Geomagnetic Storm](storm.jpg)

## Brief Solution Description 🚀

Our team, as part of "Develop the Oracle of DSCOVR," is faced with the challenge of predicting Geomagnetic Storms in our Solar System. We've developed a solution to predict the value of the Kp index, calculated from geomagnetic field data across 13 locations on Earth and data from the DSCOVR satellite. We use an Autoregressive Moving Average model, ARIMA, to make these predictions based on Level 1 time series data provided by NASA. The Kp index prediction gives us valuable insights into current Geomagnetic Weather.

## How the Solution Was Formulated 📊

### Data Collection

Our project heavily relies on data from the DSCOVR satellite, which we initially collected from the NOAA portal's public access database. Initially, we received the files in .nc format that we coverted to csv fiels anf merged them as needed. We studied this data, including both Level 1 and Level 2 data from the past 6 months and 1 year, to predict Kp index values.

### Data Preprocessing

To handle the challenge of missing values, we took two approaches: imputing the Kp index values (with poor results) and using only 3-hourly entries in the geomagnetic field data. The latter approach proved more effective.

### Model Selection

We experimented with various regression models, including Support Vector Regression, Random Forest Regression, Multivariate LSTM, Linear Regression, ARIMA, DeepGPR, and GRU. After thorough testing, we found that ARIMA performed the best and was most suited for our datasets.

### Model Fine-Tuning

We fine-tuned the ARIMA model by optimizing packing and unpacking functions. We achieved the best R2 score (0.5329) with an order=(0,1,0), and packing-unpacking functions as cosh and arcsinh within the numpy package.

### Future Development

Our vision for this project includes creating a web application to deploy the model, with a user-friendly interface for passing real-time data to the backend. This will enable us to predict Kp values in advance, leading to better predictions of Geomagnetic Solar Storms.

## Technologies Used 🛠️

- Python (TensorFlow, NumPy, Pandas, SpacePy, and others) for development.
- Intending to use ReactJS, HTML/CSS, and Flask for deploying the website.

## Project Structure 📁

Here's an overview of the naiming conventions and their content:

- `data/`: Contains collected data.
- `models/`: Stores trained machine learning models.
- `code/`: Jupyter notebooks for data exploration and model development.

## Getting Started 🏁

To get started with the project, follow these steps:

1. Clone this repository.
2. Install the required Python libraries with the requirements.txt.
3. Explore the Jupyter notebooks in the `notebooks/` directory.
4. Stay tuned for updates on our web application!

## Contribution Guidelines 🤝

Contributions to this project are welcome! Feel free to submit issues or pull requests.

## License 📜

This project is licensed under ........

## Acknowledgments 🙏

We'd like to express our gratitude to NASA, NOAA, and the open data community for providing valuable resources for this project.

