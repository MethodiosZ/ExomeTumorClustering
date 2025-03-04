for line in $(cat "snps.txt"); do
  name="${line:2:4}"
  name="${name//./}"
  echo "Normalize running on $name"
  bcftools norm --write-index -m - -f "../ref.fna.bgz" "$line" -O b -o "${name}_norm.bcf"
  bcftools view --write-index -v snps "${name}_norm.bcf" -O b -o "{name}_snps.bcf"
  rm "$name"_norm.bcf "$name"_norm.bcf.csi
  echo "Normalize on $name finished."
done
