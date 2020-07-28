infile=open('fireman.txt','r')
outfile=open('numword.txt','w')
sm=infile.readlines()

for i in range(len(sm)):
    fline=sm[i]
    flist=fline.split()
    outfile.write(str(len(flist))+'\n')

infile.close()
outfile.close()

infile=open('fireman.txt','r')
outfile=open('numword.txt','r')
print(infile.readlines())
print(outfile.readlines())
