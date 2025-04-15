Logistic Regression and Random Forest are 2 machine learning algorithms which were applied in a German Bank dataset with clients with different attributes which are believed to cause the client to default. This algorithms give which attributes weigh the most for client default, as well as try to categorize which clients are most likely to default.

---------------------------------------------------------------------------------------------------------------------------

For MonsterHunterAttkVsCrit.py, the results are the images CritEye=5.png and CritEye=0.png which compares in terms of 
percentage +/- plotting in which cases is better to have more attack boost vs critical boost, considering critical_eye 
which is an item that gives more affinity.

Conclusion: For lower attack (raw + bonus raw) is better to have high attack bonus vs critical bonus, but as damage goes up
critical boost and critical eye escalate better to output higher total damage.

---------------------------------------------------------------------------------------------------------------------------

For LinearRegressionGDPvsSchoolMex.py, it is a linear regression done for correlating variables, in this case the two variables
are GDP and secondary school enrollment in Mexico, data was substracted from the worldbank https://databank.worldbank.org

The results can be seen plotted in LinearRegressionGDPvsSchoolMex.png.

The results are:
Slope (Coefficient): 3.2472062978574136e-11
Intercept: 57.01519370651685 
R-squared: 0.6459939422733928

1. Slope (Coefficient):
The slope of the regression line is 3.2472062978574136e-11.
Interpretation: For every $1 increase in GDP, School Enrollment increases by 3.24e-11. This is an extremely small effect, practically close to zero.
Conclusion: There is no meaningful linear relationship between GDP and School Enrollment based on this dataset. 
GDP does not appear to have a significant impact on School Enrollment.

2. Intercept:
The intercept is 57.01519370651685.
Interpretation: When GDP is $0, the predicted School Enrollment is 56.692%.
Conclusion: The intercept represents the baseline level of School Enrollment, but it is not meaningful in this context because GDP cannot realistically be $0.

3. R-squared:
The R-squared value is 0.6459939422733928.
Interpretation: 64% of the variance in School Enrollment is explained by GDP.
Conclusion: While the R-squared value is high, it is misleading in this case because the slope is practically zero.

---------------------------------------------------------------------------------------------------------------------------
