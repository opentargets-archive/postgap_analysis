# Analysis of POSTGAP data
This repo contains some exploratory data analysis of the POSTGAP data. The intention is to make sure we design a front-end display with the cluster size ranges in mind.

## Key assumptions
* Only `gwas_source='GWAS Catalog'` records will be used.
* The set `['ld_snp_rsID', 'gwas_snp', 'gene_id', 'disease_efo_id', 'gwas_pmid']` is unique across rows, so can be used as a primary key.

## General observations
* The set `['ld_snp_rsID', 'gwas_snp', 'gene_id', 'disease_efo_id', 'gwas_pmid']` appears not to be unique. An example row in the original data file is in `non_unique_example.txt`.
* The `gwas_source='GWAS Catalog'` filtering significantly reduces the file size (the expanded full file is approximately 900MB, while the filtered version is 90MB).
* Some columns have unexpected entries (eg. the `sas_maf` column, and other `*_maf` columns contain floats mostly, but also `-:0.4826` appears).
* There are more chromosome identifiers than the 1-22, X, Y set. The extras appear to be alternative loci with names like `HSCHR2_1_CTG12`.
* THere are rows where the gene and LD SNP are on different chromosomes.

## Technical note
Without the `gwas_source='GWAS Catalog'` filtering, the POSTGAP data file is significantly larger. To run the notebook on the full data file might require using, eg. [dask](http://dask.pydata.org/en/latest/dataframe.html), which wraps most `pandas` functionality and processes the data in chunks.
