import sys
with open("nomissmerged.vcf",'r') as input:
  for line in input:
    if line.startswith("##"):
      continue
    else:
      break
data=line
data=data.strip()
fdata=data.split("FORMAT\t")[1]
values=fdata.split("\t")
with open("names.txt",'w') as output:
  for value in values:
    output.write(value+"\n")
