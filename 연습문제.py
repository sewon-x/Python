ex=open('number.txt')
s=ex.readlines()
total=0
avg=0
for i in range(len(s)):
    total=total+int(s[i])
avg=total/len(s)
print('Numberlist=',s,'Total=',total,'average=',round(avg,2))
