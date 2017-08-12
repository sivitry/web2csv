
# coding: utf-8

# In[129]:

import collections, re
import json, csv
documents = []
with open("VivianChen_PaperList.csv") as f:
    for line in f:
        documents.append(line.split(",")[1])

document = "\'"+document+"\'"

bagsofwords = [ collections.Counter(re.findall(r'\w+', txt)) for txt in documents]
sumbags = sum(bagsofwords, collections.Counter())
#print(bagsofwords)
#rint(sumbags)
#print(list(sumbags))
print(sumbags.items())

csvfp = open("output.csv", "w")
csvwriter = csv.writer(csvfp)
csvwriter.writerows(sumbags.items())
csvfp.close()

