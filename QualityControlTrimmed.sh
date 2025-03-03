for line in $(cat "trimdata.txt"); do
  echo "FastQC running on $line"
  fastqc "$line"
done
