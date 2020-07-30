import pandas as pd
data = pd.read_csv('BostonHousing.csv')
medv = data.MEDV
a=data['MEDV']
total=a.sum()
average=round(total/a.count())
print("avg=",average)
print("max=",max(a))
print("min=",min(a))