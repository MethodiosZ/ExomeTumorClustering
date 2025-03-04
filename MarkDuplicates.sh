for line in $(cat "mapped.txt"); do
  name = "${line:9:10}"
  name = "${name//.sam/}"
  echo "Mark duplicates running on $name"
  samtools view -@ 4 -b -F 4 "$line" | samtools collate -@ 4 -O - | samtools fixmate -@ 4 -m -r - - | samtools sort -@ 4 - | samtools markdup -@ 4 -S -r -s - "{$name}_dedup.bam"
  echo "Mark duplicates on $name finished."
done
