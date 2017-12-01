# POSTGAP Specification (for Open Targets)
This document collects our assumptions about the POSTGAP dataset. Each assumption should ideally become a test on the incoming dataset (ie. `postgap.<date>.txt.gz`). Some of the assumptions are at the level of individual rows, but others may be about the whole file.

## Individual row level
* Open Targets will ignore the `cluster_id` field
* Each `r2` is in `[0.7, 1]`
* Each `gwas_pvalue` is in `[0, 1]`
* Each `gwas_odds_ratio` is in `[0, Inf]`
* Each `gwas_beta` is in `[0, Inf]`
* Each `gwas_size` is in `[0, Inf]`

## Per gene level
* Each `gene_id` always appears with the same (`gene_symbol`, `gene_chrom`, `gene_tss`)
* Each `gene_chrom` is one of `{1-22, X, Y}`

## Per LD SNP level
* Each `ld_snp_rsID` always appears with the same (`chrom`, `pos`)
* Each `ld_snp_rsID` always appears with the same (`afr_maf`, `amr_maf`, `eas_maf`, `sas_maf`)

## Per GWAS SNP level
* Each `gwas_snp` always appears with the same 

## Per disease level
* Each `disease_efo_id` always appears with the same `disease_name`

## Per GWAS PubMed ID level


## Per (gene, LD SNP) level
* Each (`gene_id`, `ld_snp_rsID`) always appears with the same (`score`, `VEP`, `Regulome`, `PCHiC`, `GTEx`, `Fantom5`, `DHS`, `Nearest`)
* Each (`gene_id`, `ld_snp_rsID`) always appears with the same VEP fields (`vep_terms`, `vep_sum`, `vep_mean`, `vep_reg`)
* Each (`gene_id`, `ld_snp_rsID`) always appears with matching `gene_chrom` and `chrom`

## Per (LD SNP, GWAS SNP) level

## Per (GWAS SNP, GWAS PubMed ID, disease)



## Per (gene, LD SNP, GWAS SNP, disease, GWAS PubMed ID, )