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
#### `./MarkDuplicates.sh`
#### `find . -type f -name "*.bam" | sort > deduped.txt`
#### `./SnpCalling.sh`
#### `cd snpdata`
#### `find . -type f -name "*.bcf" | sort > snps.txt`
#### `./Normalize.sh`
#### `bcftools merge --write-index --threads 8 MB1_snps.bcf MB2_snps.bcf MB3_snps.bcf MB4_snps.bcf MB5_snps.bcf MB6_snps.bcf MB7_snps.bcf MB8_snps.bcf MB9_snps.bcf MB10_snps.bcf -O b -o merged.bcf`
#### `bcftools view --threads 8 merged.bcf > merged.vcf`
