# Code Directory
Please see our report (included in the repo) for results and discussion on numbers and findings.

Mid-semester deliverable presentation can be found at: https://docs.google.com/presentation/d/1oWV5I8Jf-VWqd2ZWzUoYeQO1sQXaV7NzCJWDQ8yOyGA/edit?usp=sharing

Final deliverable presentation can be found at: https://docs.google.com/presentation/d/1lQrbbgPwFtSiX0Fj5ig7xUyr2FzzAFk6AtOSM2jBgRY/edit?usp=sharing

## Important note for loading in data
In order to run correctly, all models need two things:
* `columns_keep.pkl`, which contains the columns to keep as a result of preprocessing.
* Actual data to train on, which is in the format of an `.h5` file. `.h5` format is used, as reading an `.h5` file is way faster than reading a .json file.

`columns_keep.pkl` is already in the `preprocessing/data/` folder in the repo, so all that is left in order to run each model is to create an .h5 file of data. To do this, please run `preprocessing_script.py`, which is also in the `preprocessing/` folder. Make sure the input is a .json file. Move the resulting .h5 files into the `preprocessing/data/` folder (or wherever you want to store the input data).

Lastly, in the model's code (in each `.ipynb` notebook), change the path of the .h5 file to point to whatever relative path your  `/data` folder is in. This will be `../preprocessing/data/[filename].h5` if using the current repository structure.


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
* `Polymorph_Jihan.ipynb` contains a variety of documented functions. The first half of the functions deal with generating batch one hot encoding labels, and using those labels to get batches of batch one hot encoded data. These functions are followed by the code that performs the actual batch training, using 14 different presaved models in the models/ folder. The rest of the notebook contains functions pertaining to the mid-semester deliverable, including feature scoring, logistic regression grid search, and low level EDA.
* The `models` folder contains files for all the models used for logistic with SGD. These model files are stored as pickle files, and can be loaded as such. The _v2 models were trained on features excluding those we deemed to be potentially calculated after the impression, and the other 7 were trained on all features. They each have log loss with a l2 penalty and alpha level of 0.1^i, where i is the model number.


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
* `Jihan_Preprocess.ipynb` contains the same overall process as preprocess_script.py, but it explores and contains analysis on how and why decisions for preprocessing were made, as well as some EDA into post-mid-semester deliverable data, which contained new features such as keywords and url.
* `preprocess_script.py` contains everything needed to preprocess the original json files for NaN values, storing the resulting preprocessed data as an h5 file. Documentation on how to run the script is commented in the top of the file.
* The `data` folder contains a .pkl file of all the columns we decided to keep.


## /Random-Forest/
Contains code for random forests.

Relevant Files:
* `Random Forest Hyper-parameter Kush.ipynb` contains feature selection, filtering and hyparameter tuning for a Random Forest model run on the pre-midsemester deliverable data. Contains documentation about the best scores achieved with this model and why we moved away from it.

## /xgboost/
Contains code for gradient boosting with xgboost. Gradient boosting was approached by 3 people, so work from all 3 of these members are included in here.

Relevant Files:

* `Xgboost_Kush - No Feature Drop.ipynb` contains XGboost model trained on 80:1 data ratio and using all columns. Resulted in very high f1 score, but on a smaller subset of the data. Can change dropna parameter at top to change number of used columns.
* `XGBoost_Skyler.ipynb` contains multiple XGBoost implementations with balanced/biased training sets, batch training, and adjusted hyperparameters
* `XgboostKush-Final.ipynb` contains XGBoost final implmention trained and tested on latest data using best preprocessing techniques. This implementation used the XGBoost sklearn wrapper, so potentially may result in different performance. Also contains the probability to CTR conversion functions.
* `XgboostNew.ipynb` contains XGBoost implemented from its sparse matrices in xgb.DMatrix. The OHE encoding is still using the older version of the function and not the newer one, which allows it to train and test a much larger dataset. Shows the predictions predicted from the testing data, which varies more evenly between 0 and 1 given a balanced training set.

