"""
1. Dealing with Missing Values
    They are many methods of filling cells with missing values some of the methods are as follows:

        * Ignore the Cells with missing values - This includes just dropping columns or rows that contain missing values. This strategy may
        introduce some anomalies to the model since the data drop can be of importance for the model ability to operate accurately
        * Filling in the Missing Values Manually - The problem with this method is it very time consuming especially when the data is large and some
        time the client may not want the data analyst to make changes to there data set
        * Using the attribute mean to fill in the missing values - The addition of mean values does not the data's measure of central tenancy but
        it may introduce some bias in the data.
        * Using the attribute mean for value in the same category / Class - This strategy has the same effects has the above technique
        * Using the most probable value to fill in the missing value - The value to use to fill the missing values is determined using inference statics
        * Using a global constant to fill the missing values - This a simple way do deal with unknown value especial when there is default value in case some values are missing"""

# Ignore the cell with missing values
# Example dataset
dataset =

"""
1. Missing at Random ( MAR )
    There is a systematic relationship between propensity of missing values and the observed data, but not the missing data. The missing of data can 
    be predicted by other features in the dataset. it means that the observation which is missing has nothing ti do with the missing value but has a 
    correlation with observed variable.
    i.e In a survey on student performance student who perform poorly will fail to disclose there scores

2. Missing Completely at Random ( MCAR )
    It means there is no relationship between the missing of the data and the value observed or missing. There's no relationship between whether a data
    point is missing and any value in the dataset, missing or observed
    i.e The reason of value missing is independent of the observation is due to machine failure, failure to record by the data collector.

3. Missing Not at Random (MNAR)
    It means the data missing is related to some observed data. To understand the reason for the missing data by checking the data gathering process
    further and try to understand why the information is missing. There is a distinct relationship between propensity of a value to be missing and it's value 
    i.e The data we don't have is related to factors that we didn't account for or completely don't know
"""