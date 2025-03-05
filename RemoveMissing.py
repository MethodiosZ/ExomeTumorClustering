import sys
linecount=0
missing=0
headers=0
with open("nomissmerged.vcf",'w') as output, open("merged.vcf",'r') as input:
  for line in input:
    if line.startswith('#'):
      output.write(line)
      headers+=1
    elif "./." in line:
      missing+=1
    else
      output.write(line)
      linecount+=1
print("Lines: ",linecount)
print("Headers: ",headers)
print("Missing: ",missing)
