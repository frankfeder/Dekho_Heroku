# Machine Learning Model Overview

### Preprocessing
The dataset our analysis uses was uploaded in three separate files, each describing unique records but containing some inconsistencies in the provided data. In our preprocessing stage, we discovered that the most inconsistently formatted of these files only held 300 records (out of a total of over 12,000) so we removed that dataset from our analysis. After narrowing our source data down to just two of the original three datasets, we improved the usability of a few of the fields by binning less-frequent data in categorical columns. After both datasets were consistently formatted, we combined them into one master dataframe, and added a column representing our target: the "price range" that each record's selling price belonged to. To prepare the data for use in our model, the categorical columns were One-Hot Encoded into binary columns.

### Feature Selection
The shared features between the two usable datasets only contained a handful of columns, so at first we attempted to use all of the provided data. However, we quickly realized that the field representing "car name" was too specific for use as a categorical column in training the model, so we cut it entirely. We returned to this data later to extract the Manufacturer for each record using Regular Expressions, and made a note to compare the success of our model with/without this relatively crowded categorical data. In the end, we ended up with the following features for modelling each car's selling price: manufacturing year, kilometers driven, fuel type, seller type, transmission type, number of owners, and manufacturer.

### Training and Testing Split
The data was split into training and testing subsets, the test data representing around 10% of the total data. In our testing, that number went as high as 20% and as low as 5%, but this seemed to be the balancing point to achieve maximal input data without overfitting. 

### Model Choice
Originally, we had decided to use Linear Regression to predict the specific selling price of each car - this level of specificity proved to be an impractical goal given our limited amount of working data. After exploring the distribution of the data, we decided to change our goal to predict the price range for each record, divided up into five bins representing equal ranges between 0 and 1,000,000 rupees. By redefining our goal this way, we shifted away from supervised linear regression and towards supervised multiclass classification. 

There are several multiclass classifiers available to python users, so we tested several different models including sklearn's DecisionTreeClassifier and RandomForestClassifier. 

### Model Training
Because SKLearn makes the syntax for training a model relatively simple, we were able to train the model against the training subset in one line of code. We worked through an iterative process of tweaking the input data (additional binning, or feature omission), the model parameters, (like DecisionTreeClassifier's max_depth) and the train/test split to improve the effectiveness of the training step. 

### Current Accuracy Score
Currently, our most successful DecisionTreeClassifier model's accuracy is around 37%, which we hope to improve by further tweaks to the input data and the model's parameters - part of that will include revisiting the EDA for additional insight into the source data.