for line in $(cat "rawdata.txt"); do
  echo "FastQC running on $line"
  fastqc "$line"
done
