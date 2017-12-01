import unittest
import itertools
import numpy as np
import pandas as pd
from pandas import DataFrame

from .config import POSTGAP_FILE

VALID_CHROMOSOMES = [*[str(chr) for chr in range(23)], 'X', 'Y']


# class PostgapBase(unittest.TestCase):

#     has_loaded_file = False

#     def setUpClass(self):
#         print('PostgapBase.setUpClass')
#         if not has_loaded_file:
#             PostgapBase.pg = pd.read_csv(POSTGAP_FILE, sep='\t', na_values=['None'])
#             has_loaded_file = True

#     # def test_base(self):
#     #     print('PostgapBase.setUpClass')

# class PostgapSingleton()

# class TestPostgapBase(unittest.TestCase):

#     def setUp(self):
#         self.pg = pd.read_csv(POSTGAP_FILE, sep='\t', na_values=['None'])

class TestPostgapRow(unittest.TestCase):
    
    def setUp(self):
        self.pg = pd.read_csv(POSTGAP_FILE, sep='\t', na_values=['None'])

    def is_in_range(self, series, low, high):
        # check if all values in series are in the range [low, high]
        # but if not, print the first exception
        between = series.between(low, high)
        all_between = between.all()
        self.assertTrue(all_between, series[~between].head(1).to_string(index=False))

    def test_score_range(self):
        self.is_in_range(self.pg.score, 0, 6)

    def test_r2_range(self):
        self.is_in_range(self.pg.r2, 0.7, 1.0)

    def test_gwas_pval_range(self):
        self.is_in_range(self.pg.gwas_pvalue, 0.0, 1.0)

    # def test_afr_maf_range(self):
    #     self.is_in_range(self.pg.afr_maf, 0.0, 1.0)

    # def test_amr_maf_range(self):
    #     self.is_in_range(self.pg.amr_maf, 0.0, 1.0)

    # def test_eas_maf_range(self):
    #     self.is_in_range(self.pg.eas_maf, 0.0, 1.0)

    # def test_eur_maf_range(self):
    #     self.is_in_range(self.pg.eur_maf, 0.0, 1.0)

    # def test_sas_maf_range(self):
    #     self.is_in_range(self.pg.sas_maf, 0.0, 1.0)

class TestPostgapPerDisease(unittest.TestCase):
    
    def setUp(self):
        self.pg = pd.read_csv(POSTGAP_FILE, sep='\t', na_values=['None'])
        self.per_disease = self.pg.groupby('disease_efo_id')

    def is_unique(self, groupbyseries):
        # check if values in a groupbyseries are unique
        # if not, print the first exception
        counts = groupbyseries.nunique()
        counts_are_one = (counts == 1)
        self.assertTrue(counts_are_one.all(), counts[~counts_are_one].head(1))

    def test_disease_efo_and_name_combination_unique(self):
        self.is_unique(self.per_disease.disease_name)

    def test_disease_efo_and_name_combination_unique(self):
        self.is_unique(self.per_disease.disease_name)


class TestPostgapPerGene(unittest.TestCase):
    
    def setUp(self):
        self.pg = pd.read_csv(POSTGAP_FILE, sep='\t', na_values=['None'])
        self.per_gene = self.pg.groupby('gene_id')

    def is_unique(self, groupbyseries):
        # check if values in a groupbyseries are unique
        # if not, print the first exception
        counts = groupbyseries.nunique()
        counts_are_one = (counts == 1)
        self.assertTrue(counts_are_one.all(), counts[~counts_are_one].head(1))

    def test_gene_id_and_symbol_combination_unique(self):
        self.is_unique(self.per_gene.gene_symbol)

    def test_gene_id_and_chrom_combination_unique(self):
        self.is_unique(self.per_gene.gene_chrom)

    def test_gene_id_and_tss_combination_unique(self):
        self.is_unique(self.per_gene.gene_tss)

    def test_gene_chrom_is_valid(self):
        self.assertTrue(all(str(chr) in VALID_CHROMOSOMES
                            for chr in self.pg.gene_chrom.unique()))


class TestPostgapPerLdSnp(unittest.TestCase):
    
    def setUp(self):
        self.pg = pd.read_csv(POSTGAP_FILE, sep='\t', na_values=['None'])
        self.per_ld_snp = self.pg.groupby('ld_snp_rsID')

    def is_unique(self, groupbyseries):
        # check if values in a groupbyseries are unique
        # if not, print the first exception
        counts = groupbyseries.nunique()
        counts_are_one = (counts == 1)
        self.assertTrue(counts_are_one.all(), counts[~counts_are_one].head(1))

    def test_ld_snp_id_and_chrom_combination_unique(self):
        self.is_unique(self.per_ld_snp.chrom)

    def test_ld_snp_id_and_pos_combination_unique(self):
        self.is_unique(self.per_ld_snp.pos)

    def test_ld_snp_chrom_is_valid(self):
        self.assertTrue(all(str(chr) in VALID_CHROMOSOMES
                            for chr in self.pg.chrom.unique()))


class TestPostgapPerGeneAndLdSnp(unittest.TestCase):
    
    def setUp(self):
        self.pg = pd.read_csv(POSTGAP_FILE, sep='\t', na_values=['None'])
        self.per_gene_and_ld_snp = self.pg.groupby(['gene_id', 'ld_snp_rsID'])

    def is_unique(self, groupbyseries):
        # check if values in a groupbyseries are unique
        # if not, print the first exception
        counts = groupbyseries.nunique()
        counts_are_one = (counts == 1)
        self.assertTrue(counts_are_one.all(), counts[~counts_are_one].head(1))

    def test_score_unique_per_gene_and_ld_snp(self):
        self.is_unique(self.per_gene_and_ld_snp.score)

    def test_vep_unique_per_gene_and_ld_snp(self):
        self.is_unique(self.per_gene_and_ld_snp.VEP)

    def test_regulome_unique_per_gene_and_ld_snp(self):
        self.is_unique(self.per_gene_and_ld_snp.Regulome)

    def test_pchic_unique_per_gene_and_ld_snp(self):
        self.is_unique(self.per_gene_and_ld_snp.PCHiC)

    def test_gtex_unique_per_gene_and_ld_snp(self):
        self.is_unique(self.per_gene_and_ld_snp.GTEx)

    def test_fantom5_unique_per_gene_and_ld_snp(self):
        self.is_unique(self.per_gene_and_ld_snp.Fantom5)

    def test_dhs_unique_per_gene_and_ld_snp(self):
        self.is_unique(self.per_gene_and_ld_snp.DHS)

    def test_nearest_unique_per_gene_and_ld_snp(self):
        self.is_unique(self.per_gene_and_ld_snp.Nearest)

    def test_chroms_match(self):
        # take first row's gene_chrom and chrom
        # (other tests check this is reasonable)
        firsts = self.per_gene_and_ld_snp.first()
        chroms_match = (firsts.gene_chrom == firsts.chrom)
        self.assertTrue(chroms_match.all(), firsts[~chroms_match].head(1))


# TODO:
# * print entity counts
# * print window count and sizes (per gwas_snp)
# * test for chrom/gene_chrom mismatches


if __name__ == '__main__':
    unittest.main()
