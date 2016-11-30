
This is my github repository for code projects.  I also wrote blogs for many of these code projects.  To visit my blog site, click here [blog](https://peterco877.github.io/).  Thanks for visiting!   

Code Projects

Wine Taste Quality – Models based on ‘wine quality dataset’.  Methods include Linear Regression, Lasso Regression, Ridge Regression, and from scratch algorithms for Gradient Descent, Least Angle Regression and Stepwise Selection.  

Predicting Credit Risk – Models based on ‘German credit data’, and ‘Australian credit approval’.  See detailed table of contents below.  

Airport Traffic Delays – Models based on data from 3 FAA datasets.  Methods include Hierarchical Clustering, Kmeans Clustering and Principal Component Analysis.

State Liquor Sales – Time series forecast based on 'Iowa liquor sales' dataset.  Includes an ARIMA model.

Webscraping – scraping jobs data from Indeed.com 


###Table of Contents for Predicting Credit Risk

I.    Data

      a. Loading Data
         1. import modules/display options
         2. load data

      b. Data Cleaning
      
      c. Exploratory Data Analysis
         1. distinguish between numerical and qualitative features
         2. histograms(German)
         3. histograms(Australian)
         4. summary statistics
         5. class sizes

II.   Feature Analysis & Selection 

      a. Feature Analysis & Selection - Continuous Attributes                             
         1. hypothesis tests for 2 population means (German)                
         2. hypothesis tests for 2 population means (Australian)             
         3. remove features with pvalue above threshold, e.g., insignificant 
         4. check correlation between remaining numerical attributes        

      b. Feature Analysis & Selection - Qualitative Attributes              
         1. contingency table functions                                     
         2. contingency tables/chi-square tests (German)                    
         3. contingency tables/chi-square tests (Australian)                 
         4. remove features with pvalue above threshold e.g., insignificant 
      
      c. Other Changes to Features Dataset                                  
         1. set target variable                                             
         2. remove target variable from features dataset                    
         3. create a scaled version of the dataset                          

III.  Model Building, Non-Ensemble Models 

      a. K-Nearest Neighbors                                                
      b. Logistic Regression                                                
      c. Naive Bayes                                                        
      d. Decision Tree                                                      
        
IV.   Model Building, Ensemble Methods

      a. Bagging Classifier (German)                                        
      b. Bagging Classifier (Australian)                                     
      c. Extra Trees (German)                                               
      d. Extra Trees (Australian)                                            
      e. Random Forests (German)                                            
      f. Random Forests (Australian)                                        
      g. Gradient Boosting (German)                                         
      h. Gradient Boosting (Australian)                                      
     
V.    Model Scoring using Accuracy, F1 & ROC/AUC                                                     
 
VI.   Probability Predictions 

      a. Wrappers in conjunction with Cross_Val_Predict                               
      b. Probability Predictions                                            
    
VII.  Cost-Profit Considerations

      a. Confusion Matrix                                                                 
      b. Cost of False Positives                                            
      c. Threshold Function                                                 
          
VIII. Profits & Metrics using a Cost-Profit Ratio of 2-to-1

      a. Metrics & Unit Profits at 50% Thresholds                           
      b. Unit Profits Across Thresholds                                     
      c. Best Performing Model by Highest Unit Profit                       

IX.   Feature Importance & Model Descriptions

      a. Feature Importance                                                 
      b. Description of Learning Algorithms                                 

X.    Best Performing Models using other Cost-Profit Ratios

      a. Cost-Profit Ratios of 3-to-1 and 4-to-1 (German) 
      b. Cost-Profit Ratios of 5-to-1 and 6-to-1 (Australian)
      d. True Positive/False Positive Rates and the ROC Curve

