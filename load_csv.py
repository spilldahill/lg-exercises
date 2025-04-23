import pandas as pd

url = "https://drive.google.com/uc?id=1phaHg9objxK2MwaZmSUZAKQ8kVqlgng4&export=download"
df = pd.read_csv(url)

print(df.head())

print(df.shape[0])

print(df.nunique())