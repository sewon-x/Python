infile=open('number2.txt','r')
n=infile.readline()
print('readline()=',n)

nlist=n.split()
print(nlist)
print(nlist[0])
print(int(nlist[0]))
