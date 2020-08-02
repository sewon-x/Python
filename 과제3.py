import pandas as pd
df = pd.read_csv('BostonHousing.csv')
# idx_col='MEDV'
# print(data)
# print(data[13])
# total=df['MEDV'].sum()
# avg=round(total/df['MEDV'].count())
# max_m=df['MEDV'].max()
# min_m=df['MEDV'].min()
# print("avg=",avg)
# print("max=",max_m)
# print("min=",min_m)
# subset(df,MEDV==50,select=c('CRIM','DIS','TAX'))

# is_max=df['MEDV']== 50
# cdt=df[is_max]
# print(cdt)
data1 = df['MEDV']
data2 = df['CRIM']
data3 = df['DIS']
data4 = df['TAX']
   
# subset(df['MEDV'],50)
#      print(df['CRIM'])
# ex3 = df.loc[:, ['CRIM', 'DIS', 'TAX', 'MEDV']]
# max_medv=df.loc[[50],['CRIM','DIS','TAX']]
# max_crim = df.loc[[50], ['CRIM']]
# max_dis = df.loc[[50], ['DIS']]
# max_tax = df.loc[[50], ['TAX']]
# print("가장 비싼 집들은 각각 CRIM=",data2,"DIS=",data3,"TAX=",data4,"입니다.")
# # # min_medv = data.loc[[5], ['CRIM', 'DIS', 'TAX']]
# min_crim = data.loc[[5], ['CRIM']]
# min_dis = data.loc[[5], ['DIS',]]
# min_tax = data.loc[[5], ['TAX']]
# print(min_crim)
# print(min_dis)
# print(min_tax)
