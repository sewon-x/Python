import pandas as pd
#---------2----------
# c1=[1,2,3]
# df1=pd.DataFrame(c1)
# print(df1)
#--------3-------------
# c1=[1,2,3]
# c2=[4,5,6]
# dict1={'a':c1,'b':c2}
# df1=pd.DataFrame(dict1)
# print(df1)

from IPython.display import display
df3=pd.DataFrame(data=[4,5,6,7])
display(df3)

df4=pd.DataFrame(data=[4,5,6,7],index=[10,11,13,14])
display(df4)

df5=pd.DataFrame(data=[4,5,6,7],index=[10,11,13,14],columns=['A'])
display(df5)