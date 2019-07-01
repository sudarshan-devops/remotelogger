from collections import Counter
import re
f=open("catalina.out","r")
a=[]
count=Counter()
for i in f:
    if(".start Server" in i):
        a=i.split()
        for word in a:
            count[word]+=1
f.close()
strdte=str(count)
print(count)


