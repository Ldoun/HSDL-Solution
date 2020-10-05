'''import os
a=os.listdir("C:/Users/Lee/Desktop/a/people")
d=[]
for i in a:
    d.append(i[:-3])

print(d)'''

'''A={'AA':1,'BB':2}

A['AA']=A['AA']+1
print(A['AA'])'''
import os
peopleImageFolder="C:/Users/Lee/Desktop/a/people/"
people=os.listdir(peopleImageFolder)   

people=[peopleImageFolder+i for i in people]

print(people)