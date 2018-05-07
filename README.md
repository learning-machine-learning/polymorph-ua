# Code Directory
Please see our report for results and discussion on numbers and findings.

## /aws-scripts/
Contains code that formats the data from s3://adsnative-sigmoid. These scripts were used to filter the raw data (e.g. filter and keep only requests with empty bid_requests lists) and combine filtered data files into combined hourly and daily files.

## /EDA-Exploratory-Data-Analysis
Contains notebooks for visualizing feature distributions and other visualizations on the data. Done only for direct auctions.

## /FFMs/
Contains code for field-aware factorization machines.

Relevant Files:
* `FFM_Boris.ipynb` contains  



## /logistic regression w/ SGD/
Contains code for logistic regression with stochastic gradient descent.

Relevant Files: 
*`Polymorph_Jihan.ipynb` contains


## /naive-logistic/
Contains code for naive logistic regression.

Relevant Files:
* `LogisticRegression_AllCols.ipynb` contains
* `LogisticRegression_DropCols.ipynb` contains


## /old_code/
Most of the code from mid-semester deliverable and before. All of this data was trainined and tested with only direct CPC auctions. Contains old preprocessing notebooks, as well as utility functions used to preprocess the data, such as a time conversion function and url handling function. Also contains work done to score publishers and advertisers.

## /preprocessing/
Contains code that does all the preprocessing on the data. E.g. drops unwanted columns and saves processed data into .h5 files for further use.

Relevant Files:
* `Jihan_Preprocess.ipynb` contains
* `preprocess_script.py` contains 


## /Random-Forest/
Contains code for random forests.

Relevant Files:
* `Random Forest Hyper-parameter Kush.ipynb` contains 

## /xgboost/
Contains code for gradient boosting with xgboost. Gradient boosting was approached by 3 people, so work from all 3 of these members are included in here.

Relevant Files:

* `GradientBoost_Logistic.ipynb` contains
* `Xgboost_Kush - No Feature Drop.ipynb` contains
* `XGBoost_Skyler.ipynb` contains
* `XgboostKush-Final.ipynb` contains
* `XgboostNew.ipynb` contains 
