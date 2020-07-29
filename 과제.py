import csv

f=open('BostonHousing.csv','r')
s=f.readlines(13)

for i in range(len(s)):
    n=s[i].split(",")
    print(s)
    
    sum=0
    for j in range(len(s)):
        sum=sum+int(s[j])

    print("avg=",sum/len(s))
    print("max=",max(s))
    print("min=",min(s))