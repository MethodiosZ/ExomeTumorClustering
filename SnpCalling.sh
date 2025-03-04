for line in $(cat "deduped.txt"); do
  name = "${line:9:10}"
  name = "${name//.bam/}"
  echo "Snp calling running on $name"
  bcftools mpileup -f "ref.fna.gz" "$line" | bcftools call --threads 4 -v -m -Ob -o "./snpdata/$name.bcf"
  echo "Snp calling on $name finished."
done
