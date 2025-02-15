import pandas as pd
import matplotlib.pyplot as plt

frame = pd.read_csv("breadprice.csv")
print(frame)

# Clean the dataset by replacing NaN with the mean of the mean of the other values in the row 
years = frame["Year"]
frame.drop(columns = "Year", inplace = True)
newValue = frame.loc[10].mean()
frame.fillna(newValue, inplace = True)
print(frame.tail())

averagesList = frame.mean(axis=1)
roundedAverages = list(map(lambda x: round(x, 2), averagesList))
print(roundedAverages)

plt.figure(figsize=(10, 5))
plt.plot(years, averagesList, marker='o', linestyle='-', color='b')

plt.xlabel("Year")
plt.ylabel("Average Bread Price")
plt.title("Trend of Average Bread Prices")
plt.grid(True)

# Show plot
plt.show()