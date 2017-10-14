# Analysis of POSTGAP data
This repo contains some exploratory data analysis of the POSTGAP data. The intention is to make sure we design a front-end display with the cluster size ranges in mind.

## Key assumptions
* Only `gwas_source='GWAS Catalog'` records will be used.
* The set `['ld_snp_rsID', 'gwas_snp', 'gene_id', 'disease_efo_id', 'gwas_pmid']` is unique across rows, so can be used as a primary key.
