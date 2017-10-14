import gzip
import csv

IN_FILE = 'postgap.20170825.txt.gz'
OUT_FILE = 'postgap.20170825.flat.txt.gz'

GWAS_COLS = ['gwas_snp', 'gwas_source', 'gwas_pmid', 'gwas_reported_trait', 'gwas_size', 'gwas_pvalue', 'gwas_odds_ratio', 'gwas_beta', 'r2']
# single_entry_cols = [c for c in x.columns if c not in multi_entry_cols]

if __name__ == '__main__':
    # read line by line and output a zipped file where GWAS_COLS with multiple entries
    # have been split out...
    with gzip.open(IN_FILE) as f1, gzip.open(OUT_FILE, 'w') as f2:
        reader = csv.DictReader(f1, dialect=csv.excel_tab)
        
        i = 0
        for row in reader:
            i += 1
            if i == 1:
                # print row
                cols = row.keys()
                non_gwas_cols = [c for c in cols if c not in GWAS_COLS]
                writer = csv.DictWriter(f2, cols, dialect=csv.excel_tab)
                writer.writeheader()

            # split gwas cols on |
            splits = {col: row[col].split('|') for col in GWAS_COLS}
            split_count = len(splits[GWAS_COLS[0]])
            singles = {col: row[col] for col in non_gwas_cols}

            if split_count == 1:
                # write as is
                writer.writerow(row)
            else:
                # divide into several rows
                for j in range(split_count):
                    new_row = {col: splits[col][j] for col in GWAS_COLS}
                    new_row.update(singles)
                    writer.writerow(new_row)
