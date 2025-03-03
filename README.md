# ExomeTumorClustering
## Author: Methodios Zacharioudakis
#### `find . -type f -name "*.fq.gz" | sort -u > rawdata.txt`
#### `./QualityControlRaw.sh`
#### `./DataTrimming.sh`
#### `cd trimmeddata/paired`
#### `find . -type f -name "*.fq.gz" | sort > trimdata.txt`
#### `./QualityControlTrimmed.sh`
#### `./MappingData.sh`
#### `cd mappeddata`
