# stockPredictor

# Stock Market Prediction App

A web-based application that predicts stock market trends using machine learning. The app uses historical stock data to visualize trends and make price predictions using an LSTM (Long Short-Term Memory) neural network.

## Features

- Real-time stock data fetching using Yahoo Finance API
- Interactive stock symbol input
- Multiple visualization options:
  - Basic closing price trends
  - 100-day moving average
  - 200-day moving average comparison
- Machine learning-based price predictions using LSTM
- Descriptive statistics for the selected stock
- Visual comparison between predicted and actual prices

## Technologies Used

- **Python 3.x**
- **Streamlit**: Web application framework
- **TensorFlow/Keras**: Deep learning model implementation
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib**: Data visualization
- **scikit-learn**: Data preprocessing
- **yfinance**: Yahoo Finance API wrapper
- **pandas-datareader**: Financial data access

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

Note: Create a `requirements.txt` file with the following dependencies:
```
numpy
pandas
matplotlib
pandas-datareader
yfinance
scikit-learn
keras
tensorflow
streamlit
```

## Usage

1. Ensure you have the trained model file `keras_model.h5` in your project directory.

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Access the web interface through your browser (typically at `http://localhost:8501`)

4. Enter a stock ticker symbol (default is 'AAPL' for Apple Inc.)

## Model Details

The application uses an LSTM neural network model for predictions with the following characteristics:

- Training data: 70% of historical data
- Testing data: 30% of historical data
- Prediction window: 100 days
- Data preprocessing: MinMaxScaler normalization
- Time period: 2012-2022

## Data Visualization

The app provides multiple visualization options:
1. Raw closing price data
2. 100-day moving average comparison
3. Both 100-day and 200-day moving averages
4. Predicted vs. actual price comparison

## Project Structure

```
├── app.py                 # Main application file
├── keras_model.h5         # Pre-trained LSTM model
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Important Notes

- The model file (`keras_model.h5`) must be present in the project directory
- Internet connection is required for fetching real-time stock data
- Historical data range is set from 2012 to 2022
- The prediction accuracy may vary depending on market conditions



## Disclaimer

This application is for educational purposes only. The predictions should not be used as financial advice. Always conduct thorough research and consult with financial professionals before making investment decisions.
