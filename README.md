# SIB

## Authors:
* [António Duarte](https://github.com/anccduarte) | PG45464
* [Roberto Bullitta](https://github.com/rocobull) | PG45474
* [Vânia Miguel](https://github.com/vaniamiguel13) | PG45971

## Repository Guide:
* **Files** (folder) -> contains files generated during the (.txt and .csv); the following files could not be uploaded due to their large size:
  * **data_train.csv** -> training data (after feature extraction)
  * **data_test.csv** -> test data (after feature extraction)
  * **X_train_sc.csv** -> scaled training data (minmax scaler)
  * **X_train_sc_z.csv** -> scaled training data (standard scaler)
* **Experimental** (folder) -> contains experimental procedures (.ipynb)
  * **GBR_clust.ipynb** (file) -> train distinct models based on a previous clustering analysis
  * **MLP_hyper.ipynb** (file) -> optimize MLP hyper-parameters
* **feature_extraction.py** (file) -> contains functions for feature extraction
* **C_P_FE.ipynb** (file) -> context, preprocessing and feature extraction
* **AE.ipynb** (file) -> exploratory analysis
* **UL.ipynb** (file) -> unsupervised learning
* **SL.ipynb** (file) -> supervised learning
* **DL_MLP.ipynb** (file) -> deep learning (multilayer perceptron)
* **DL_CNN.ipynb** (file) -> deep learning (convolutional neural network)

## Content Guide:
* Contextualization
* Preprocessing 
* Feature Extraction
* Exploratory Analysis
* Unsupervised Learning
* Supervised Learning (shallow learning)
* Deep learning

### [Contextualization](https://github.com/vaniamiguel13/SIB/blob/main/C_P_FE.ipynb):
The data used in this report was retrived from KAGGLE: https://www.kaggle.com/c/novozymes-enzyme-stability-prediction  
Each data example consists of a protein sequence, a pH value and thermostability index. Predicting the thermostability is fundamental in enzyme engeneering for a wide variety of applications. Employing ML techniques is of great value to achieve the latter purpose as it saves time and money.

### [Preprocessing](https://github.com/vaniamiguel13/SIB/blob/main/C_P_FE.ipynb): 
* Data processing
* Identification of the train and test datasets
* Treatment of Missing values

### [Feature Extraction](https://github.com/vaniamiguel13/SIB/blob/main/C_P_FE.ipynb)
* Identification of the Descriptors with BioPython and ProPy

### [Exploratory Analysis](https://github.com/vaniamiguel13/SIB/blob/main/AE.ipynb)
* Outlier Treatment (dependent variable)
* Standardization
* Thermostability value distribution 
* Correlation Analysis (Pearson, Spearman, f_regression, mutual_information)
* Multicollinearity Analysis

### [Unsupervised Learning](https://github.com/vaniamiguel13/SIB/blob/main/UL.ipynb)
* PCA
* tSNE
* K-means

### [Supervised Learning](https://github.com/vaniamiguel13/SIB/blob/main/SL.ipynb)
* Cross-validation, Hyper-parameter tuning, and Model selection
* Linear Regression
* K-Nearest Neighbors
* Support Vector Machine
* Random Forest
* Adaptive Boosting
* Gradient Boosting

### Deep learning
* [MLP](https://github.com/vaniamiguel13/SIB/blob/main/DL_MLP.ipynb)
* [CNN](https://github.com/vaniamiguel13/SIB/blob/main/DL_CNN.ipynb)

## Credits:
* Curricular Unit Slides
* Deep Learning: https://machinelearningmastery.com/grid-search-hyperparameters-deep-learning-models-python-keras/
