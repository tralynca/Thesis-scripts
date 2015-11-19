#!usr/bin/python

## Check if any of the somatic variants are located within ENCODE predicted TFBS 

# ---------------------------------------------------------------------------
#               import libraries and specify paths
#----------------------------------------------------------------------------
import sys

path_deleterious_SV = '/home/tracey/Desktop/MASTERS_2014/ICGC/Regulome_annotations/Results/Annotations_from_web_interface/regulome_annotation_matched_to_original_variant/173_non_disease_genes/non_disease_regulome_annotation_CDS_sv.txt'
# Format non-coding variants: 173_ccRCC_genes/combined_non_coding_regulome_annotation_of_sv.txt 
# Format coding variants: 173_ccRCC_genes/173_ccRCC_regulome_annotation_CDS_sv.txt
# Format non-disease and non-coding: 173_non_disease_genes/combined_non_disease_non_coding_regulome_annot_of_sv.txt'
path_TFBS = '/home/tracey/Desktop/MASTERS_2014/ICGC/TFBS/wgEncodeRegTfbsClusteredV3.bed'

file_delet_SV = open (path_deleterious_SV)
file_TFBS  = open(path_TFBS)

# ---------------------------------------------------------------------------------------------
#                 Create a list to navigate through SV with regulome score 2-3 
#----------------------------------------------------------------------------------------------
# Format of somatic mutations file
## ABCA6	17	67080155	67080155	DO46885	SA507332	T	T	C	introns	ENSG00000154262	7
sv_list = []
for sv_line in file_delet_SV:
    column = sv_line.strip('\n').split('\t')
    gene_name = column[0]
    sv_chrm = column[1]
    start = int(column[2])
    end = int(column[3])
    donor = column[4]
    ref_allele = column[6]
    mutated_from = column[7]
    mutated_to = column[8]
    UCSC_struc_annot = column[9]
    ensembl_gene = column[10]
    regulome_score = column[11]
    sv_list.append([sv_chrm, start, end, donor, ref_allele, mutated_from, mutated_to, UCSC_struc_annot, ensembl_gene, gene_name, regulome_score])
#print sv_list


# ---------------------------------------------------------------------------------------------
#          Create a list to navigate through the coordinates of the TFBS
#----------------------------------------------------------------------------------------------

tfbs_list = []                                              # create an empty list called tfbs_list, to be populated later
for line in file_TFBS :                                      # read in the content of the file line by line
    columns = line.strip().split('\t')                          # create columns by stripping both ends of the line from blank space and then split on blank space
    chrm_TFBS = columns[0][3:]                              # extract the chromosome for column 1 (format chr14), use only the part of the item after chr, i.e. from the 3rd elemnt in the column
    TFBS_start = int(columns[1])                            # extract the start coordinate of the TFBS from column 2 and convert it to an integer
    TFBS_end = int(columns[2])                              # extract the end coordinate of the TFBS from column 3 and convert it to an integer
    TF = columns[3]                                  # extract the gene name from column 4
    tfbs_list.append([chrm_TFBS, TFBS_start, TFBS_end, TF])          # add the necessary items to the list called tfbs_list
    #print tfbs_list

# ---------------------------------------------------------------------------------------------
#          Create a list to navigate through the coordinates of the TFBS
#----------------------------------------------------------------------------------------------
sys.stdout = open('/home/tracey/Desktop/MASTERS_2014/ICGC/TFBS/Results/173_non_disease_genes/non_disease_CDS_mut_in_TFBS.txt', 'w')
# Format non_coding variants: non_cod_mut_in_TFBS.txt' 
# Format CDS variants:CDS_mut_in_TFBS.txt'
# Format non-disease and non-coding: 173_non_disease_genes/non_disease_non_coding_mut_in_TFBS.txt'
for SV in sv_list:
    for TF in tfbs_list:
        if SV[0] == TF[0] and SV[1] >= TF[1] and SV[2] <= TF[2]:
            print SV[9] + '\t' +  SV[8] + '\t' +  SV[0] + '\t' + str(SV[1]) + '\t' + str(SV[2]) + '\t' +  SV[3] + '\t' + SV[4] + '\t'  + SV[5] + '\t' + SV[6] + '\t' + SV[7] + '\t' +  SV[10] + '\t' +  TF[0] + '\t' +  str(TF[1]) + '\t' +  str(TF[2]) + '\t' +  TF[3]



