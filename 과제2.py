import pandas as pd
data = pd.read_csv('BostonHousing.csv')
ex3 = data.loc[:, ['CRIM', 'DIS', 'TAX', 'MEDV']]
# print(df_sample)
a=data.loc[:,['MEDV']]
medv = data.MEDV
a=data['MEDV']
total=a.sum()
average=round(total/a.count())
max_a=max(a)
min_a=min(a)
print("avg=",average)
print("max=",max_a)
print("min=",min_a)

# b=data['CRIM']
# c = data['DIS']
# d = data['TAX']

# for i in range(len(a)):
#     if a[i]==50:
#         print()

# import numpy
# for i in range(506):
#     if a[i] == max:
#         print('CRIM=',b[i],'DIS=',c[i],'TAX=',d[i])
#     elif a[i] == min:
#         print('CRIM=', b[i], 'DIS=', c[i], 'TAX=', d[i])
