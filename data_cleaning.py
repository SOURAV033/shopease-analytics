import pandas as pd
import numpy as np

def clean_ecommerce_data(filepath):
    print("Loading ShopEase raw transaction data...")
    
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

    # Standardize column names (avoid mismatch issues)
    df.columns = df.columns.str.strip().str.lower()

    # Required columns check
    required_cols = ['customer_id', 'order_date', 'delivery_date', 
                     'price', 'quantity', 'product_category']
    
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        print(f"Missing columns: {missing_cols}")
        return None

    # 1. Handle Missing Values
    print("Dropping rows with missing customer IDs...")
    df = df.dropna(subset=['customer_id']).copy()

    # 2. Convert Data Types safely
    print("Converting timestamps...")
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['delivery_date'] = pd.to_datetime(df['delivery_date'], errors='coerce')

    # Drop rows where dates failed to convert
    df = df.dropna(subset=['order_date', 'delivery_date'])

    # 3. Feature Engineering: Delivery Time
    df['delivery_lag_days'] = (df['delivery_date'] - df['order_date']).dt.days

    # Remove invalid delivery lag (negative values)
    df = df[df['delivery_lag_days'] >= 0]

    # 4. Remove Outliers / Invalid values
    df = df[(df['price'] > 0) & (df['quantity'] > 0)]

    # 5. Standardize Text Formatting
    df['product_category'] = (
        df['product_category']
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace('_', ' ', regex=False)
    )

    # Reset index after cleaning
    df.reset_index(drop=True, inplace=True)

    print(f"Cleaning complete. Final dataset shape: {df.shape}")
    return df


if __name__ == "__main__":
    # Example usage
    filepath = 'raw_data.csv'
    cleaned_data = clean_ecommerce_data(filepath)

    if cleaned_data is not None:
        cleaned_data.to_csv('cleaned_shopease_data.csv', index=False)
        print("Cleaned data saved successfully.")