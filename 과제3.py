import pandas as pd
data = pd.read_csv('BostonHousing.csv')
idx_col='MEDV'
ex3 = data.loc[:, ['CRIM', 'DIS', 'TAX', 'MEDV']]
# print(ex3)
# max_medv=data.loc[[50],['CRIM','DIS','TAX']]
max_crim = data.loc[[50], ['CRIM']]
max_dis = data.loc[[50], ['DIS']]
max_tax = data.loc[[50], ['TAX']]
print(max_crim)
print(max_dis)
print(max_tax)
# min_medv = data.loc[[5], ['CRIM', 'DIS', 'TAX']]
min_crim = data.loc[[5], ['CRIM']]
min_dis = data.loc[[5], ['DIS',]]
min_tax = data.loc[[5], ['TAX']]
print(min_crim)
print(min_dis)
print(min_tax)
