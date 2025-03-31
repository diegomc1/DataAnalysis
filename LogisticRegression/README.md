Logistic Regression
Dataset: https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data

This dataset classifies people described by a set of attributes as good or bad credit risks. 
Comes in two formats (one all numeric). Also comes with a cost matrix

Logistic regression is used to predict if a client is going to default given a set of Attributes

Two variants are being used:
1) using a cost_matrix = {0: 1, 1: 5} punishing heavier for bad credit classification error
2) using sklearn.linear_mode Logistic regression's built in, "balanced" class weight.

The results for 1)

| Metric       | Class 0 (Good Credit) | Class 1 (Bad Credit) | Accuracy | Macro Avg | Weighted Avg |
|--------------|-----------------------|-----------------------|----------|-----------|--------------|
| Precision    | 0.88                  | 0.41                  | -        | 0.64      | 0.74         |
| Recall       | 0.50                  | 0.83                  | -        | 0.67      | 0.60         |
| F1-score     | 0.64                  | 0.55                  | 0.60     | 0.60      | 0.61         |
| Support      | 141                   | 59                    | 200      | 200       | 200          |

For Class 0 (Good Credit):
Precision	0.88	=> Of all customers predicted as "Good", 88% were actually good.
Recall	0.50 =>	The model correctly identified 50% of truly good customers.
F1-score	0.76 =>	Balance between precision and recall (closer to 1 = better).

For Class 1 (Bad Credit):
Precision	0.41 =>	Of all customers predicted as "Bad", only 41% actually defaulted.
Recall	0.83 =>	The model caught 83% of true defaulters.
F1-score	0.55 =>	Moderate performance for the "Bad" class.

Accuracy => 60% of all predictions were correct.

Image: confusionMxCostMatrix.png

ActualGood: 0	  71 (TN)	    70 (FP)
ActualBad: 1  	10 (FN)	    49 (TP)
        PredictedGood: 0	PredictedBad: 1

Image: Top10FeaturesCostMatrix.png

This are the top 10 reasons for defaulting with its coefficient plotted in image.

1. Attribute1_A14 => A1: Status of existing checking account => A14 : no checking account
2. Attribute4_A41 => A4: Purpose => A41 : car (used)
3. Attribute20_A202 => A20: foreign worker => A202 : no
4. Attribute4_A48 => A4: Purpose =>  A48 : retraining
5. Attribute3_A34 => A3: Credit history => A34 : critical account/
		    other credits existing (not at this bank)
6. Attribute14_A143 => A14: Other installment plans => A143 : none
7. Attribute1_A13 => A1: Status of existing checking account => A13: >= 200 DM /
		     salary assignments for at least 1 year
8. Attribute4_A410 => A4: Purpose => A410: others
9. Attribute4_A43 => A4: Purpose => A43: radio/television
10. Attribute9_A93 => A9: Personal status and sex => A93: male: single

The results for 2):

| Metric       | Class 0 (Good Credit) | Class 1 (Bad Credit) | Accuracy | Macro Avg | Weighted Avg |
|--------------|-----------------------|-----------------------|----------|-----------|--------------|
| Precision    | 0.87                  | 0.50                  | -        | 0.69      | 0.76         |
| Recall       | 0.68                  | 0.76                  | -        | 0.72      | 0.70         |
| F1-score     | 0.76                  | 0.60                  | 0.70     | 0.68      | 0.72         |
| Support      | 141                   | 59                    | 200      | 200       | 200          |

For Class 0 (Good Credit):
Precision	0.87	=> Of all customers predicted as "Good", 87% were actually good.
Recall	0.68 =>	The model correctly identified 68% of truly good customers.
F1-score	0.76 =>	Balance between precision and recall (closer to 1 = better).

For Class 1 (Bad Credit):
Precision	0.50 =>	Of all customers predicted as "Bad", only 50% actually defaulted.
Recall	0.76 =>	The model caught 76% of true defaulters.
F1-score	0.60 =>	Moderate performance for the "Bad" class.

Accuracy => 70% of all predictions were correct.

Image: confusionMxBalanced.png

ActualGood: 0	  96 (TN)	    45 (FP)
ActualBad: 1  	14 (FN)	    45 (TP)
        PredictedGood: 0	PredictedBad: 1

Image: Top10FeaturesBalanced.png

This are the top 10 reasons for defaulting with its coefficient plotted in image.

1. Attribute1_A14 => A1: Status of existing checking account => A14 : no checking account
2. Attribute4_A41 => A4: Purpose => A41 : car (used)
3. Attribute3_A34 => A3: Credit history => A34 : critical account/
		    other credits existing (not at this bank)
4. Attribute20_A202 => A20: foreign worker => A202 : no
5. Attribute4_A48 => A4: Purpose =>  A48 : retraining
6. Attribute1_A13 => A1: Status of existing checking account => A13: >= 200 DM /
		     salary assignments for at least 1 year
7. Attribute4_A43 => A4: Purpose => A43: radio/television
8. Attribute14_A143 => A14: Other installment plans => A143 : none
9. Attribute6_A64 => A6: Savings account/bonds =>  A64 : >= 1000 DM
10. Attribute9_A93 => A9: Personal status and sex => A93: male: single

