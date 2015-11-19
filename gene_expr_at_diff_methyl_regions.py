#!usr/bin/python

## Extract gene expression data for the genes where there were aberrant methylation signatures

# ---------------------------------------------------------------------------
#               import libraries and specify paths
#----------------------------------------------------------------------------
import sys

path_methyl = '/home/tracey/Desktop/MASTERS_2014/ICGC/Methylation/Results_promoter_methylation/173_non_disease_genes/combined_non_coding_non_disease_methylation.txt'
#Format disease genes: 173_ccRCC_genes/UNIQ/combined_methylation_in_non_coding_regions.txt'
path_cosmic_exp = '/home/tracey/Desktop/MASTERS_2014/ICGC/Gene_expression_ICGC_and_COSMIC/ALL_GE_data_for_95_random_patients_173_disease_and_non_disease_genes.txt'

#The file below was used to extract gene expression data across many tumour types
#COSMIC_gene_exp_175_GOI.txt'

file_methyl = open(path_methyl)
file_gene_exp = open(path_cosmic_exp)


# ---------------------------------------------------------------------------------------------
#     Create a list to navigate through the coordinates that were aberrantly methylated
#----------------------------------------------------------------------------------------------
# Format input file: 
## 11	145589783	Promoter_Associated	H	849	271	0	cg01950958	2193941	TCGA-B0-5700-01	2062219	introns	+	NBPF10

#Format non-disease:

## 3	44753948	Promoter_Associated	H	804	259	0	cg17279458	1779833	TCGA-B0-5100-01	1683832	3	44753134	44754134	+	ZNF502
methyl_list = []
for line in file_methyl:
    column = line.strip().split('\t')
    chrm = column[0]
    position = column[1]
    strand = column[13]
    #strand = column[12]
    diff_methyl = column[3]
    probe = column[7]
    patient_ID = column[9] 
    #region = column[11]
    gene_name = column[15]
    #gene_name = column[13]
    methyl_list.append([gene_name, chrm, position, strand, diff_methyl, probe, patient_ID])
    #print methyl_list

# ---------------------------------------------------------------------------------------------
#     Create a list to navigate through the coordinates within the gene expression file
#----------------------------------------------------------------------------------------------

gene_exp_list = []
for lines in file_gene_exp:
    columns = lines.strip().split('\t')
    gene = columns[0]
    sample_name = columns[1]
    regulation = columns[2]
    z_score = columns[3]
    gene_exp_list.append([gene, sample_name, regulation, z_score])
    #print gene_exp_list

# ---------------------------------------------------------------------------------------------
#     Find the regulation profile of the differentially methylated positions
#----------------------------------------------------------------------------------------------
sys.stdout = open('/home/tracey/Desktop/MASTERS_2014/ICGC/Gene_expression_ICGC_and_COSMIC/Results_COSMIC_methylated_regions/173_non_disease_genes/gene_expr_at_methyl_region_combined_non_disease.txt', 'w')
#Format disease genes: 173_ccRCC_genes/gene_expr_at_methyl_region_combined_ccRCC.txt', 'w')
for methyl in methyl_list:
    for expr in gene_exp_list:
        if methyl[0] == expr[0] and methyl[6] == expr[1]:
            print methyl[0] + '\t' + methyl[1] + '\t' + methyl[2] + '\t' + methyl[3] + '\t' + methyl[4] + '\t' + methyl[5] + '\t' + methyl[6]  + '\t' + expr[2] + '\t' + expr[3] 
#+ '\t' + methyl[7]




