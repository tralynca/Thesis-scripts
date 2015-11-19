#!usr/bin/python

## Check if there was any change in gene expression for the somatic variants (RegulomeDb score 2-7)

# ---------------------------------------------------------------------------
#               import libraries and specify paths
#----------------------------------------------------------------------------
import sys

path_exp_data = '/home/tracey/Desktop/MASTERS_2014/ICGC/Gene_expression_ICGC_and_COSMIC/Results_ICGC_and_COMSIC_gene_exp_and_SV/ccRCC_COSMIC_gene_exp/ALL_GE_data_for_95_random_patients_173_disease_and_non_disease_genes.txt'

path_variants = '/home/tracey/Desktop/MASTERS_2014/ICGC/Regulome_annotations/Results/Annotations_from_web_interface/regulome_annotation_matched_to_original_variant/173_non_disease_genes/uniq_non-disease_genes_CDS.txt'

#Format ccRCC disease genes and non-coding: 173_ccRCC_genes/combined_uniq_non_coding_genes.txt'
#Format ccRCC disease genes and CDS: 173_ccRCC_genes/uniq_genes_CDS.txt'
#Format non-disease genes and non-coding:173_non_disease_genes/combined_uniq_non_disease_non_coding_genes.txt'
#Format non-disease genes and CDS:173_non_disease_genes/uniq_non-disease_genes_CDS.txt'

file_exp_data = open(path_exp_data)
file_SV = open(path_variants)

#print file_exp_data
# ---------------------------------------------------------------------------------------------
#     Create a list to navigate through the coordinates within the gene expression file
#----------------------------------------------------------------------------------------------

gene_exp_list = []
for lines in file_exp_data:
    columns = lines.strip().split('\t')
    gene = columns[0]
    sample_name = columns[1]
    regulation = columns[2]
    z_score = columns[3]
    gene_exp_list.append([gene, sample_name, regulation, z_score])
    #print gene_exp_list


file_exp_data.close()

# ---------------------------------------------------------------------------------------------
#                 Create a list to navigate through SV with regulome score 2-3 
#----------------------------------------------------------------------------------------------
## Format input file: 
## ABCA6	17	67080155	67080155	DO46885	SA507332	T	T	C	introns	ENSG00000154262	7
sv_list = []
for sv_line in file_SV:
    gene_name = sv_line.strip().split('\t')[0]
    #print gene_name


# used for all hits
    '''column = sv_line.strip('\n').split('\t')
    gene_name = column[0]
    #print gene_name
    sv_chrm = column[1]
    start = column[2]
    donor = column[4]
    ref_allele = column[6]
    mutated_from = column[7]
    mutated_to = column[8]
    structural_annotation = column[9]
    UCSC_struc_annot = column[10]
    ensembl_gene = column[11]
    #regulome_score = column[12].strip('\n')'''
    sv_list.append(gene_name)
#([gene, ensembl_gene, sv_chrm, start, donor, ref_allele, mutated_from, mutated_to, structural_annotation, UCSC_struc_annot, regulome_score])
#print sv_list

#file_SV.close()

   
# ---------------------------------------------------------------------------------------------
#     Compare two lists and find ensemble gene IDs that match and their fold change
#----------------------------------------------------------------------------------------------
sys.stdout = open('/home/tracey/Desktop/MASTERS_2014/ICGC/Gene_expression_ICGC_and_COSMIC/Results_ICGC_and_COMSIC_gene_exp_and_SV/173_non_disease_genes/GE_combined_CDS_non_disease_genes.txt', 'w')
# Format ccRCC and non-coding:173_ccRCC_genes/GE_combined_non_coding_ccRCC_genes.txt', 'w')
# Format ccRCC and CDS: 173_ccRCC_genes/GE_combined_CDS_ccRCC_genes.txt', 'w')
#Format non-disease genes and non-coding:173_non_disease_genes/GE_combined_non_coding_non_disease_genes.txt', 'w')
#Format non-disease genes and CDS:173_non_disease_genes/GE_combined_CDS_non_disease_genes.txt', 'w')


for SV in sv_list: 
    #print SV
    for entry in gene_exp_list:
        if SV == entry[0] and entry[2] == 'over' or SV == entry[0] and entry[2] == 'under':
            print entry[0] + '\t' + entry[1] + '\t'  + entry[2] + '\t'  + entry[3]


#SV[1] + '\t' + SV[2] + '\t' + SV[3] + '\t' + SV[4] + '\t' + SV[5] + '\t' + SV[6] + '\t' + SV[7] + '\t' + SV[8] + '\t' + SV[10] + '\t' + SV[9] + '\t' + entry[0] + '\t' + entry[1] + '\t'  + entry[2] + '\t'  + entry[3]








    

