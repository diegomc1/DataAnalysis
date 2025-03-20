import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data
data = {
    "Country Name": ["Mexico"] * 4,
    "Country Code": ["MEX"] * 4,
    "Series Name": [
        "Income share held by lowest 20%", "School enrollment, secondary (% gross)",
        "GDP (current US$)", "GDP growth (annual %)"
    ],
    "Series Code": ["SI.DST.FRST.20", "SE.SEC.ENRR", "NY.GDP.MKTP.CD", "NY.GDP.MKTP.KD.ZG"],
    "1990 [YR1990]": [3.4, 56.6920013427734, 261253675692.838, 5.25004329944582],
    "2000 [YR2000]": [3.4, 71.1195831298828, 742061329643.37, 5.02928399378261],
    "2014 [YR2014]": [4.7, 97.3196868896484, 1364507717614.13, 2.50376350288664],
    "2015 [YR2015]": [5, 100.982269287109, 1213294467716.88, 2.70232342550646],
    "2016 [YR2016]": [5, 102.871368408203, 1112233497452.7, 1.77249323845399],
    "2017 [YR2017]": [5.2, 105.11018371582, 1190721475906, 1.87172853327193],
    "2018 [YR2018]": [5.2, 105.964653015137, 1256300182879.73, 1.97208210249194],
    "2019 [YR2019]": [5.3, 105.515609741211, 1304106203694.81, -0.392690521579212],
    "2020 [YR2020]": [5.3, 102.58154296875, 1121064767261.88, -8.3540345574586],
    "2021 [YR2021]": [5.6, 98.3202514648438, 1316569466932.59, 6.04848344290505],
    "2022 [YR2022]": [5.6, 98.3576583862305, 1464312692331.58, 3.68911109348025],
    "2023 [YR2023]": [5.6, 98.3576583862305, 1789114434843.46, 3.19998116598492]
}

# Reshape the data into a tidy format
df = pd.DataFrame(data)
df = df.melt(id_vars=["Country Name", "Country Code", "Series Name", "Series Code"],
             var_name="Year", value_name="Value")

# Pivot the table to have Series Name as columns
df = df.pivot_table(index=["Country Name", "Country Code", "Year"],
                    columns="Series Name", values="Value", aggfunc="first").reset_index()

# Clean up column names
df.columns.name = None

# Drop rows with missing values
df = df.dropna()

# Define features (X) and target (y)
X = df[["GDP (current US$)"]]
y = df["School enrollment, secondary (% gross)"]

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Get the coefficients and intercept
slope = model.coef_[0]
intercept = model.intercept_
print(f"Slope (Coefficient): {slope}")
print(f"Intercept: {intercept}")

# Calculate R-squared
r_squared = model.score(X, y)
print(f"R-squared: {r_squared}")

# Plot the data and regression line
plt.scatter(X, y, color="blue", label="Data Points")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.xlabel("GDP (current US$)")
plt.ylabel("School Enrollment, Secondary (% gross)")
plt.title("Linear Regression: GDP vs School Enrollment")
plt.legend()
plt.show()