Random Forest Dataset: https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data

This dataset classifies people described by a set of attributes as good or bad credit risks. 
Comes in two formats (one all numeric). Also comes with a cost matrix.

Random Forest algorithm was used to predict and classify users, according to a series of
attributes, would default in their payments.

Two variants are being used:

1) Using a cost_matrix = {0: 1, 1: 5} punishing heavier for bad credit classification error
2) Using sklearn.linear_mode Logistic regression's built in, "balanced" class weight.

The results for 1)

![ConfussionMatrixCostMatrix.](https://github.com/diegomc1/DataAnalysis/blob/master/RandomForest/ConfussionMxCostMx.png)

| Metric       | Class 0 (Good Credit) | Class 1 (Bad Credit) | Accuracy | Macro Avg | Weighted Avg |
|--------------|-----------------------|-----------------------|----------|-----------|--------------|
| Precision    | 0.97                  | 0.42                  | -        | 0.69      | 0.81         |
| Recall       | 0.44                  | 0.97                  | -        | 0.70      | 0.59         |
| F1-score     | 0.60                  | 0.58                  | 0.59     | 0.59      | 0.60         |
| Support      | 141                   | 59                    | 200      | 200       | 200          |

For Class 0 (Good Credit):<br>
Precision	0.97	=> Of all customers predicted as "Good", 97% were actually good. <br>
Recall	0.44 =>	The model correctly identified 44% of truly good customers.<br>
F1-score	0.60 =>	Balance between precision and recall (closer to 1 = better).<br>

For Class 1 (Bad Credit):<br>
Precision	0.42 =>	Of all customers predicted as "Bad", only 42% actually defaulted.<br>
Recall	0.97 =>	The model caught 97% of true defaulters.<br>
F1-score	0.58 =>	Moderate performance for the "Bad" class.<br>

Accuracy => 59% of all predictions were correct.

ROC-AUC: 0.82

This are the top 10 reasons for defaulting with its coefficient plotted in image.

![Top10CostMatrix.](https://github.com/diegomc1/DataAnalysis/blob/master/RandomForest/Top10CostMx.png)

1. Attribute1_A14 => A1: Status of existing checking account => A14 : no checking account
2. Attribute2 => Duration in month
3. Attribute5 => Credit amount
4. Attribute13 => Age in years
5. Attribute3_A34 => A3: Credit history => A34 : critical account/
		    other credits existing (not at this bank)
6. Attribute4_A43 => A4: Purpose => A43: radio/television
7. Attribute14_A143 => A14: Other installment plans => A143 : none
8. Attribute15_A152 => A15: Housing => A152 : own 
9. Attribute4_A41 => A4: Purpose => A41 : car (used)
10. Attribute6_A65 => A6: Savings account/bonds =>  A65 : No Savings Account

The results for 2)

![ConfussionMatrixBalanced.](https://github.com/diegomc1/DataAnalysis/blob/master/RandomForest/ConfussionMxBalanced.png)


| Metric       | Class 0 (Good Credit) | Class 1 (Bad Credit) | Accuracy | Macro Avg | Weighted Avg |
|--------------|-----------------------|-----------------------|----------|-----------|--------------|
| Precision    | 0.88                  | 0.54                  | -        | 0.71      | 0.78         |
| Recall       | 0.72                  | 0.76                  | -        | 0.74      | 0.73         |
| F1-score     | 0.79                  | 0.63                  | 0.73     | 0.71      | 0.75         |
| Support      | 141                   | 59                    | 200      | 200       | 200          |

For Class 0 (Good Credit):<br>
Precision	0.88	=> Of all customers predicted as "Good", 88% were actually good. <br>
Recall	0.72 =>	The model correctly identified 72% of truly good customers.<br>
F1-score	0.79 =>	Balance between precision and recall (closer to 1 = better).<br>

For Class 1 (Bad Credit):<br>
Precision	0.54 =>	Of all customers predicted as "Bad", only 42% actually defaulted.<br>
Recall	0.76 =>	The model caught 97% of true defaulters.<br>
F1-score	0.63 =>	Moderate performance for the "Bad" class.<br>

Accuracy => 73% of all predictions were correct.

ROC-AUC: 0.83

This are the top 10 reasons for defaulting with its coefficient plotted in image.

![Top10Balanced.](https://github.com/diegomc1/DataAnalysis/blob/master/RandomForest/Top10Balanced.png)

1. Attribute1_A14 => A1: Status of existing checking account => A14 : no checking account
2. Attribute5 => Credit amount
3. Attribute2 => Duration in month
4. Attribute13 => Age in years
5. Attribute3_A34 => A3: Credit history => A34 : critical account/
		    other credits existing (not at this bank)
6. Attribute4_A43 => A4: Purpose => A43: radio/television
7. Attribute14_A143 => A14: Other installment plans => A143 : none
8. Attribute6_A65 => A6: Savings account/bonds =>  A65 : No Savings Account
9. Attribute15_A152 => A15: Housing => A152 : own 
10. Attribute4_A41 => A4: Purpose => A41 : car (used)

An additional benchmarking was done using GridSearchCV which suggested to use: <br>
Best params: {'max_depth': 7, 'min_samples_split': 5, 'n_estimators': 100} <br>
In the randomForest algorithm. However this tunning improves in some categories but <br>
is worse others, so depending on your objective different variants can be used.

Heatmap image of comparisons:

![Benchmark.](https://github.com/diegomc1/DataAnalysis/blob/master/RandomForest/BenchmarkBalanced.png)

