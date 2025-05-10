import pandas as pd
import requests
from pathlib import Path

# Set the path for data
root_path = Path(__file__).parent.parent
data_path = root_path / "data" / "raw" / "swiggy.csv"

# Prediction endpoint
predict_url = "http://127.0.0.1:8000/predict"

# Read a clean sample row from the CSV
try:
    df = pd.read_csv(data_path)
    df_clean = df.dropna()  # Drop rows with any missing values
    if df_clean.empty:
        raise ValueError("All rows have NaNs. Provide at least one complete row for testing.")

    sample_row = df_clean.sample(1)
    print("✅ Sample row selected.")

    # Extract the target value for comparison
    target_value = sample_row.iloc[:, -1].values.item().replace("(min) ", "")
    print("🎯 The target value is:", target_value)

    # Prepare data for API (drop target column)
    data = sample_row.drop(columns=[sample_row.columns[-1]]).squeeze().to_dict()

    # Clean data (strip spaces and convert "NaN" to None)
    def sanitize(value):
        if isinstance(value, str):
            value = value.strip()
            if value.lower() == 'nan':
                return None
        return value

    cleaned_data = {k: sanitize(v) for k, v in data.items()}
    print("🧹 Cleaned input data:")
    for key, val in cleaned_data.items():
        print(f"  {key}: {val}")

    # Send POST request
    response = requests.post(url=predict_url, json=cleaned_data)
    print("\n🔄 Sending data to API...")

    # Handle response
    print("🌐 Status code:", response.status_code)
    if response.status_code == 200:
        prediction = float(response.text)
        print(f"✅ Predicted Delivery Time: {prediction:.2f} min")
    else:
        print("❌ API Error:", response.status_code)
        print("Details:", response.text)

except Exception as e:
    print("❌ Exception occurred while preparing or sending prediction request:")
    print(e)
