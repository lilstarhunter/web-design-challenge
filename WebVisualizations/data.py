import pandas as pd

# Read the csv file in
df = pd.read_csv("Resources/lms_assets/City_Data.csv")

# Save to file
df.to_html('data_convert.html', index=False)

# Assign to string
table = df.to_html()
print(table)
