# Machine_learning_templates
Template for machine learning models implementation.

The Purpose of this project is to create machine learning templates that are easy to implement and to use of the ordinary use each template will contain a simple easy to implement procedure for implementing a machine learning model or activity.
## 1. Preprocessing:
  This is the first set in the Machine Learning Process. In this step data is been prepared for machine learning. 
  The preprocess step includes some very important step this are:
  
    1. Data cleaning
    2. Data Intergration
    3. Data Transformation
    4. Data Reduction
    
### 1. Data Cleaning
Data that is to be analyze by data mining techniques can be incomplete (lacking attribute values or certain attributes of interest, or containing only aggregate data), noisy (containing errors, or outlier values  which  deviate  from  the  expected),  and  inconsistent  (e.g.,  containing  discrepancies  in  the  department  codes  used  to  categorize  items)

Some of the sources of data inconsistency can be:
* Attribute of interest may be missing completely for the dataset
* An attribute of interest may not have been considered to be important at the time of data capture
* Data may not have been recorded due to equipment failure during 
    * Data capture (ie. A measuring instrument)
    * Data Transmission (ie. limited buffer size hence poor synchronization)
* Inconsistencies introduced due to naming convention or data encoding (ie Dan - Daniel, Danny - Daniel yet al of the value refer to the same pension)

**Note:**
Data will always be dirty or have inconsistencies hence it important ti develop an data cleaning routing to use when implementing data mining models

1. Dealing with Missing Values
    Types of Missing values
       
       1. Missing at Random (MAR)
            There is a systematic relationship between propensity of missing values and the observed data, but not the missing data. The missing of data can 
            be predicted by other features in the dataset. it means that the observation which is missing has nothing ti do with the missing value but has a 
            correlation with observed variable.
            i.e In a survey on student performance student who perform poorly will fail to disclose there scores
            
       2. Missing Completely at Random (MCAR)
            It means there is no relationship between the missing of the data and the value observed or missing. There's no relationship between whether a data
            point is missing and any value in the dataset, missing or observed
            i.e The reason of value missing is independent of the observation is due to machine failure, failure to record by the data collector.
            
       3. Missing Not at Random (MNAR)
            It means the data missing is related to some observed data. To understand the reason for the missing data by checking the data gathering process
            further and try to understand why the information is missing. There is a distinct relationship between propensity of a value to be missing and it's value 
            The data we don't have is related to factors that we didn't account for or completely don't know
            
    Mathematical Definition:
    
    _y_ = response Vector
    
    X = N <sub>x</sub> _p_ (some of which are missing values)
    
    X <sub>obs</sub> = The observed entries in X
    
    Z = (_y_, X)
    
    Z<sub>obs</sub> = (_y_, X<sub>obs</sub>)
    
    R = indicator matrix with _ij_ entry 1
    
    if X<sub>_ij_</sub> is missing and zero otherwise the data is said to be missing at random (MAR) if the distribution of R depends on the data Z
    only through Z<sub>obs</sub>
    
    Pr(R|Z,θ) = Pr(R|Z<sub>obs</sub>, θ)
    
    where:
            θ are any parameters in the distribution R
            
    Data are said to be missing completely at random (MCAR) if the distribution of R doesn't depend on the observed or missing data
    
    Pr(R|Z,θ) = Pr(R|θ)
           
    They are many methods of filling cells with missing values some of the methods are as follows:

        * Ignore the Cells with missing values - This includes just dropping columns or rows that contain missing values. This strategy may
           introduce some anomalies to the model since the data drop can be of importance for the model ability to operate accurately
        * Filling in the Missing Values Manually - The problem with this method is it very time consuming especially when the data is large and some
           time the client may not want the data analyst to make changes to there data set
        * Using the attribute mean to fill in the missing values - The addition of mean values does not the data's measure of central tenancy but
           it may introduce some bias in the data.
        * Using the attribute mean for value in the same category / Class - This strategy has the same effects has the above technique
        * Using the most probable value to fill in the missing value - The value to use to fill the missing values is determined using inference statics 
        * Using a global constant to fill the missing values - This a simple way do deal with unknown value especial when there is default value in case 
          some values are missing