import numpy as np
import re
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn import preprocessing as prp
import scipy.cluster.hierarchy as sch
from sklearn.decomposition import PCA

labels=[]
with open("names.txt",'r') as names:
  for line in names:
    labels.append(line.strip())
samples=len(labels)
print(samples)

def tfrm_str(instr):
  outstr=re.sub(r'0\/0','a',instr)
  outstr=re.sub(r'0\/1','b',outstr)
  outstr=re.sub(r'1\/0','b',outstr)
  outstr=re.sub(r'1\/1','c',outstr)
  outstr=re.sub(r'[0-9]\/[0-9]','d',outstr)
  outstr=re.sub(r'\./\.:.','e',outstr)
  outstr=re.sub(r'[0-9,:\s./]','',outstr)
  pattern=re.compile(r'\s/')
  result=re.sub(pattern,'',outstr)
  return result

mapping = {'a':0,'b':1,'c':2,'d':3}
alllist=[]

with open("nomissmerged",'r') as input:
  for line in input:
    if line.startswith('#'):
      continue
    pattern=re.compile(r'^(\S+)\s+(\d+)\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+(GT|GT:PL)\s(.+)$')
    match=pattern.match(line)
    if match:
      chrm=match.group(1)
      pos=match.group(2)
      gtorgtpl=match.group(3)
      rest=match.group(4)
      mdstr=tfrm_str(rest)
      if len(mdstr)!=int(samples):
        print("Error: Incorrect format inside vcf!")
        break
      resultlist=[]
      for i in mdstr:
        if i=='e':
          print("Error: Missing found!")
          break
        if i.isnumeric():
          resultlist.append(int(i))
        else:
          resultlist.append(mapping[i])
      if not len(resultlist)==int(samples):
        print("Error: Sample missing in vcf!")
        break
      elif 3 not in resultlist:
        alllist.append(result.list)

resultarr=np.array(alllist)
tparr=np.transpose(resultarr)
norm_data=prp.normalize(tparr)

ncol=norm_data.shape[1]
nrow=norm_data.shape[0]
linkage_data=linkage(norm_data,method='complete')
clusters=fcluster(linkage_data,2,criterion='maxclust')
tags=[]
for sample,clustlbl in enumarate(clusters):
  tags.append(clustlbl)
maxclust=max(clusters)
dist=linkage_data[:,2]
sortdist=sorted(dist)
threshold=sortdist[-maxclust+1]
dendrogram(linkage_data,labels=labels)
plt.savefig("HierClust.png")
plt.close()
print("Hierarchical clustering finished.")

pca=PCA(n_components=2)
principal_components=pca.fit_transform(norm_data)
print(principal_components)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("2 Components PCA")
colors=np.array(["black","dimgray","red","sienna","darkorange","green","teal","deepskyblue","navy","darkviolet"])
plt.scatter(principal_components[:,0],principal_components[:,1],c=colors,label=labels)
plt.grid()
plt.legend(title="Samples",bbox_to_anchor=(1.05,1),loc='upper left',ncol=1)
plt.savefig("PCA.png")
plt.close()
print("PCA finished.")
