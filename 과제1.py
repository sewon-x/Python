import sys
import pandas as pd
import numpy as np
sys.stdout = open('output.txt', 'w')
data = pd.read_csv('BostonHousing.csv')
ex3 = data.loc[:, ['CRIM', 'DIS', 'TAX', 'MEDV']]
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

arr=np.array(ex3)
for i in range(len(arr)):
    if arr[i,3]==50:
        cx=arr[i,0]
        dx = arr[i, 1]
        tx = arr[i, 2]
        for j in range(len(arr)):
            if arr[j, 3] == 5:
                cm = arr[j, 0]
                dm = arr[j, 1]
                tm = arr[j, 2]
                print("가장 비싼 집들은 각각 CRIM=", cx, "DIS=", dx, "TAX=", tx,
                      "이고, 가장 싼집은 각각 CRIM=", cm, "DIS=", dm, "TAX=", tm, "입니다.")
