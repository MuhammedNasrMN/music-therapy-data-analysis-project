import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = 28
df = pd.read_csv("E:\\python\\project\\Music-and-Therapy-survey-1.csv")

print(df.dtypes)  #making sure every column is the right type
print(df.describe())
df.drop(['BPM'],axis=1, inplace=True) # dropping a column that will not be used in the analysis with a lot of missing values
df.dropna(how='all', axis=1, inplace=True) #removes any empty column
df.dropna(inplace=True) #removes any rows with any missing values


df.boxplot(column='Hours per day') #plotting a box plot to spot any outliers
upper_limit=df['Hours per day'].mean()+3*df['Hours per day'].std() #calculating the upper limit for the hours per day column
lower_limit=df['Hours per day'].mean()-3*df['Hours per day'].std() #calculating the upper limit for the hours per day column
print('upper limit', upper_limit, '\n lower limit', lower_limit)
df2 = df[df['Hours per day'] <= upper_limit]

print(df2.head(20)) #printing a sample of the cleaned data
df2.to_csv("E:\\Python\\project\\Cleaned-Music-and-Therapy-Survey-1.csv") #saving the cleaned data ti a csv file

plt.show()
