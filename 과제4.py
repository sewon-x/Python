import pandas as pd
from pandas import DataFrame
df = pd.read_csv('BostonHousing.csv')

data=DataFrame(CRIM=df['CRIM'],DIS=df['DIS'],TAX=df['TAX'],MEDV=df['MEDV'])
print(data)

for df in filereader:
    