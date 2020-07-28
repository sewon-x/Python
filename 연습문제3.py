infile=open('fireman2.txt','r')
wordCountList=[]
sm=infile.readlines()

for i in range(len(sm)):
    flist=sm[i].split()
    wordCountList.append(len(flist))

print(wordCountList)
infile.close