# ExomeTumorClustering
## Author: Methodios Zacharioudakis
#### `find . -type f -name "*.fq.gz" | sort > rawdata.txt`
#### `./QualityControlRaw.sh`
#### `./DataTrimming.sh`
#### `cd trimmeddata/paired`
#### `find . -type f -name "*.fq.gz" | sort > trimdata.txt`
#### `./QualityControlTrimmed.sh`
#### `./MappingData.sh`
#### `cd mappeddata`
#### `find . -type f -name "*.sam" | sort > mapped.txt`
