  # ExomeTumorClustering
Author: Methodios Zacharioudakis

find . -type f -name "*.fq.gz" | sort -u > rawdata.txt \n
./QualityControlRaw.sh \n
./DataTrimming.sh \n
cd trimmeddata/paired
