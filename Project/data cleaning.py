import pandas as pd


pd.options.display.max_columns = 28
df = pd.read_csv("E:\\Python\\project\\Music_and_Therapy_Survey.csv")
df.dropna(how='all', axis=1, inplace=True) #remove any empty column
df.dropna(inplace=True) #removes any row with missing values
print(df.dtypes)  #making sure every column is the right type
print(df.head(5)) #printing a sample of the cleaned data
df.to_csv("E:\\Python\\project\\Cleaned_Music_and_Therapy_Survey.csv")
