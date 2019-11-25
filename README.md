# Machine_learning_templates
Template for machine learning models implementation.
The Purpose of this project is to create machine learning templates that are easy to implement and to use of the ordinary use each template will contain a simple easy to implement procedure for implementing a machine learning model or activity.
## 1. Preprocessing:
  This is the first set in the Machine Learning Process. In this step data is been prepered for machine learning. 
  The preprocesing step includes some very inportant step this are:
  
    1. Understanding the application Domaing and formulating a task
    2. Data cleaning
    3. Data Transformation
    4. Data Intergration
    5. Data Selection
    
## 2 Models
  This section will contain all the models that have been implemented in this project the models will fall into two categories
    
    1. Basic Implementation usually from a Python library 
    2. Expert implemetation where the model will be implemented bottom up.
    
 ### 2.1 Regression Models
 Regression analysis is a form of predictive modelling technique which investigates the relationship between a dependent (target) and independent variable (s) (predictor).
 
    In this section we will implement the following models:
    
      1. Simple Linear Regression
      2. Multiple Linear Regression
      3. Polynomial Regression
      4. Support Vector for Regression
      5. Decision Tree Classification
      6. Random Forest Classification
     
#### 2.1.1 Simple Linear Regression
    Simple linear regression is a statistical method for obtaining a formula to predict values of one variable from another where there is a causal relationship between the two variables. Central to the simple linear regresion is the eqution of a line.
          y = mx + b
     where:
     y = The Dependent Variable Vector (The Values of study, the Outcome)
     x = independent Variable (Matrix of Features)
     m = The Slope of the graph
     b = constant (The point where the line closses the x axies
     
#### 2.1.2 Multiple Linear Regression
  Assumptions of Linear Regression:
    1. Lineaity
    1. Heteroscedasiticity
    1. Multivariate normality
    1. Muticollinearity
   Dummy Variable Trap - its a scenario in which two or more variabe are highly correlated
                         i.e one varable can be predited from the other
     
     Method of Building a mutiple linear regression model
     1. All in case - it a scenario where you include all the varable in the model
     1. Backward Elimination - Its a stepwise regresion approch, that begins with full set of variables from the dataset from the model find a reduced model that best explains the data.
     1. Forward Selection - Involves starting with no variables in the model testing the addition on each variable using a chosen model and evaluating the impact of the added column on the overal accuracy of the model 
     1. Bidirectional - Its a combination of forward selection and backward selection 
     
     Note: All the mothodes will be implemented in template and the diffrent approches expained here in detail
