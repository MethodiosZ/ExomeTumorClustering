while IFS= read -r line1 && IFS= read -r line2; do
  echo "BWA running on lines $line1 $line2"
  part="${line1:2:4}"
  name="${part//_/}"
  name="${name////}"
  bwa mem -M -t 16 -R "@RG\tID:$name\tSM:$name" "refseq.fna.gz" "$line1" "$line2" > "./mappeddata/aligned-$name.sam"
done < "trimdata.txt"
