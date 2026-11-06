import pandas as pd
import sklearn
import xgboost

print(f"pandas {pd.__version__} | sklearn {sklearn.__version__} | xgboost {xgboost.__version__}")

df = pd.read_csv("data/raw/hotel_bookings.csv")
print(df.shape)
print(df["is_canceled"].mean().round(3))