for line in $(cat "snps.txt"); do
  name="${line:2:4}"
  name="${name//./}"
  echo "Normalize running on $name"
  bcftools norm --write-index -m - -f "../ref.fna.bgz" "$line" -O b -o "${name}_norm.bcf"
  echo "Normalize on $name finished."
done
