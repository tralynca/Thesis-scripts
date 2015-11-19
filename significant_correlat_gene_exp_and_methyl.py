#!usr/bin/python

## Check if there is an anti-correlation between abberantly methylated regions and their gene expression levels

# ---------------------------------------------------------------------------
#               import libraries and specify paths
#----------------------------------------------------------------------------
import sys

diff_exp_diff_methyl = open('/home/tracey/Desktop/MASTERS_2014/ICGC/Gene_expression_ICGC_and_COSMIC/Results_COSMIC_methylated_regions/173_non_disease_genes/GE_combined_non_coding_non_disease_genes')
#Format disease genes: 173_ccRCC_genes/gene_expr_at_methyl_region_combined_ccRCC.txt')

# For all tumour types: 'gene_expr_at_methyl_region_3UTR.txt'

# ------------------------------------------------------------------------------------------------------------------------
#   split file into columns and output hits where there is an anti-correlation between gene exp and aberrant methylation
#-------------------------------------------------------------------------------------------------------------------------
sys.stdout = open ('/home/tracey/Desktop/MASTERS_2014/ICGC/Gene_expression_ICGC_and_COSMIC/Results_COSMIC_methylated_regions/significant_gene_exp_and_methylation_correlation/173_non_disease_genes/non_disease_significant_gene_exp_and_methylation_correlation_combined.txt', 'w')
#Format disease genes: 173_ccRCC_genes/ccRCC_significant_gene_exp_and_methylation_correlation_combined.txt', 'w')

# Format input file:
## SCD	10	102107666	+	H	cg06400428	TCGA-AK-3440-01	normal	-1.209	introns

for line in diff_exp_diff_methyl:
    column = line.strip().split('\t')
    gene = column[0]
    chrm = column[1]
    position = column[2]
    strand = column[3]
    methylation = column[4]
    probe = column[5]
    patient_ID = column[6]
    gene_exp = column[7]
    z_score = column[8]
    genomic_region = column[9]
    if methylation == 'H' and gene_exp == 'under' or methylation == 'L' and gene_exp == 'over':
        print gene + '\t' + chrm + '\t' + position + '\t' + strand + '\t' + methylation + '\t' + probe + '\t' + patient_ID + '\t' + gene_exp + '\t' + z_score + '\t' + genomic_region






