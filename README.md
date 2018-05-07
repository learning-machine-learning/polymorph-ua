# Code Directory
Please see our report for results and discussion on numbers and findings.

Mid-semester deliverable presentation can be found at: https://docs.google.com/presentation/d/1oWV5I8Jf-VWqd2ZWzUoYeQO1sQXaV7NzCJWDQ8yOyGA/edit?usp=sharing

Final deliverable presentation can be found at: https://docs.google.com/presentation/d/1lQrbbgPwFtSiX0Fj5ig7xUyr2FzzAFk6AtOSM2jBgRY/edit?usp=sharing

## /aws-scripts/
Contains code that formats the data from `s3://adsnative-sigmoid`. These scripts were used to filter the raw data (e.g. filter and keep only requests with empty bid_requests lists) and combine filtered data files into combined hourly and daily files.

Relevant Files:


New Scripts (from most recent merged-logs data):
* `filterer-negatives-only.py`	filters data from all auctions and keeps .2% of all negatives. `filterer-positives-only.py` filters data from all auctions and keeps positives (clicks) from all auctions.
* `combiner-hourly-negs-merged-logs.py` combines all 128 parts of every hour for negatives into one file and `combiner-hourly-pos-merged-logs.py`	does the same with positives.
* `combiner-daily-merged-logs.py`combines all 24 hours of data in a day into one file.





Old Scripts (from initial data):
* `filterer-all-cpc.py`	filters and keeps only ad requests with rate_metric of CPC and empty bid_requests lists. `combiner-all-days.py` combines data from all days into one file, `combiner-daily-old.py` combines data from all 24 hours of a day into one file, `combiner-hourly-old.py` combines data from all 128 parts of an hour into one file. `grouped_cnts` groups publisher and advertiser counts for publisher and advertiser analysis.


## /EDA-Exploratory-Data-Analysis
Contains notebooks for visualizing feature distributions and other visualizations on the data. Done only for direct auctions.


## /FFMs/
Contains code for field-aware factorization machines.

Relevant Files:
* `FFM_Boris.ipynb` contains all the code required to create the FFM model (i.e. feature engineering, text file conversion, training and testing).


## /logistic regression w/ SGD/
Contains code for logistic regression with stochastic gradient descent.

Relevant Files: 
* `Polymorph_Jihan.ipynb` contains
* The `models` folder contains files for all the models used for logistic with SGD. These model files are stored as ...


## /naive-logistic/
Contains code for naive logistic regression.

Relevant Files:
* `LogisticRegression_AllCols.ipynb` contains all the code required to one hot encode the preprocessed data, train the Naive Logistic Regression model using all features, and produce the results for the testing data. It also contains the code to perform grid search to find optimal hyper-parameters.  

* `LogisticRegression_DropCols.ipynb` contains all the code required to one hot encode the preprocessed data, train the Naive Logistic Regression model excluding count columns, and produce the results for the testing data. It also contains the code to perform grid search to find optimal hyper-parameters.  


## /old_code/
Most of the code from mid-semester deliverable and before. All of this data was trainined and tested with only direct CPC auctions. Contains old preprocessing notebooks, as well as utility functions used to preprocess the data, such as a time conversion function and url handling function. Also contains work done to score publishers and advertisers.

## /preprocessing/
Contains code that does all the preprocessing on the data. E.g. drops unwanted columns and saves processed data into .h5 files for further use.

Relevant Files:
* `Jihan_Preprocess.ipynb` contains
* `preprocess_script.py` contains 
* The `data` folder contains a .pkl file of all the columns we decided to keep.


## /Random-Forest/
Contains code for random forests.

Relevant Files:
* `Random Forest Hyper-parameter Kush.ipynb` contains 

## /xgboost/
Contains code for gradient boosting with xgboost. Gradient boosting was approached by 3 people, so work from all 3 of these members are included in here.

Relevant Files:

* `Xgboost_Kush - No Feature Drop.ipynb` contains
* `XGBoost_Skyler.ipynb` contains multiple XGBoost implementations with balanced/biased training sets, batch training, and adjusted hyperparameters
* `XgboostKush-Final.ipynb` contains
* `XgboostNew.ipynb` contains XGBoost implemented from its sparse matrices in xgb.DMatrix. The OHE encoding is still using the older version of the function and not the newer one, which allows it to train and test a much larger dataset. Shows the predictions predicted from the testing data, which varies more evenly between 0 and 1 given a balanced training set.

