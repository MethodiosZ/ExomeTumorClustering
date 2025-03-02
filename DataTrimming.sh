counter=1
while IFS= read -r line1 && IFS= read -r line2; do
  echo "Trimmomatic running on lines $line1 $line2"
  TrimmomaticPE -threads 16 "$line1" "$line2" -baseout "MB$counter.fq.gz" ILLUMINACLIP:TruSeq3-PE.fa:2:30:10
  ((counter++))
done < "rawdata.txt"
