infile=open('num2.csv','r')
n=infile.readlines()
print('readlines=',n)

for i in range(len(n)):
    s=n[i].split(",")
    print(s)

    sum=0
    for j in range(len(s)):
        sum=sum+int(s[j])

    print("평균=",sum/len(s))
    print()

infile.close()