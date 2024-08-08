
# House Price Prediction Model

## Overview

This project involves a house price prediction model using K-Nearest Neighbors (KNN) algorithm, deployed with a Streamlit web application. The model predicts house prices based on various features such as the number of bathrooms, balconies, and the total square footage. The Streamlit app provides an interactive user interface to input data and obtain predictions.

## Features

- Predicts the price per square foot of a house.
- Displays the total predicted price based on user inputs.
- Provides additional insights such as historical average prices and feature contributions.
- Allows users to input various house features and view predictions in real-time.

## Requirements

- Python 3.11 or higher
- Streamlit
- pandas
- numpy
- scikit-learn
- joblib

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the Streamlit App**

   ```bash
   streamlit run app.py
   ```

2. **Access the Application**

   Open your web browser and navigate to `http://localhost:8501` to use the app.

## How It Works

1. **Model Training**

   The KNN model is trained using the `idk.py` script with a dataset containing features such as `area_type`, `availability`, `location`, `size`, and more. The model is saved to `model_knn.pkl` using the `joblib` library.

2. **Streamlit Application**

   - **Input Fields**: Users enter the number of bathrooms, balconies, total square feet, and the number of BHKs.
   - **Prediction**: When the user clicks the "Predict" button, the model predicts the price per square foot based on the input features.
   - **Results**: The app displays the predicted price per square foot, total price, and other relevant outputs.

## Model Evaluation

- The model's performance is evaluated using the R² score, which measures how well the model's predictions match the actual data.

## Troubleshooting

- **Model Not Loaded**: Ensure that the `model_knn.pkl` file exists in the correct directory.
- **Feature Mismatch**: Verify that the features in the input data match those used during model training.

## Contributing

Feel free to submit issues, pull requests, or suggestions. Please ensure that your contributions follow the coding style and include appropriate tests.

## License

This project is licensed under the MIT License. See the (LICENSE) file for details.

## Contact

For any questions or feedback, please contact [unnatikadam50a@gmail.com].

---

You can adjust any sections based on specific details about your project or any additional features you might have.


