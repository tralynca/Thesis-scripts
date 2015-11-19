#!usr/bin/python

## Script check if the hits made between ICGC and the non-disease genes contained only the non-disease genes and not other genes that may overlap with my GOI

# ---------------------------------------------------------------------------
#               import libraries and specify paths
#----------------------------------------------------------------------------
import sys

path_ensembl_ID = '/home/tracey/Desktop/MASTERS_2014/ICGC/SV_results/Non_disease_genes_hits/ensembl_non_disease_genes_UNIQ.txt'
path_sv = '/home/tracey/Desktop/MASTERS_2014/ICGC/SV_results/Non_disease_genes_hits/Results/non_cod_CDS_icgc.txt'

file_ensembl_ID = open(path_ensembl_ID)
file_sv = open(path_sv)

# -------------------------------------------------------------------------------------------
#           split into columns and find a match based on chromosome and genomic position
#--------------------------------------------------------------------------------------------

ID_list = []
for line in file_ensembl_ID:
    ensembl_ID = line.strip()
    ID_list.append([ensembl_ID])
    #print ID_list


sv_list = []
for sv_line in file_sv:
    column = sv_line.strip('\n').split('\t')
    sv_chrm = column[0]
    #if start != end:
        #print start, end   #THIS WAS USED TO TEST IF I WAS DEALING WITH INDELS OR POINT MUTATIONS EACH TIME A NEW VARIANT FILE WAS SELECTED
    start = column[1]
    end = column[2]
    donor = column[4]
    sample = column[6]
    ref_allele = column[7]
    mutated_from = column[8]
    mutated_to = column[9]
    structural_annotation = column[13]
    UCSC_annot = column[14]
    ensembl_gene = column[15]
    strand = column[16]
    #transcript = column[15]
    sv_list.append([sv_chrm, start, end, donor, sample, ref_allele, mutated_from, mutated_to, structural_annotation, UCSC_annot , ensembl_gene, strand])
    #print sv_list

# --------------------------------------------------------------------------------------
#    Match variant to its regulome annotation entry and print side by side
#--------------------------------------------------------------------------------------- 
sys.stdout = open('/home/tracey/Desktop/MASTERS_2014/ICGC/SV_results/Non_disease_genes_hits/Results/Actual_results/actual_hits_CDS  .txt', 'w')
for ID in ID_list:
    for sv in sv_list: 
        if ID[0] == sv[10]:
            print ID[0] + '\t' +  sv[0] + '\t' + sv[1] + '\t' + sv[2]  + '\t' + sv[3]  + '\t' + sv[4]  + '\t' + sv[5]  + '\t' + sv[6]  + '\t' + sv[7]  + '\t' + sv[8]  + '\t' + sv[9]  + '\t' + sv[10]  + '\t' + sv[11] 
#annotation[0] + '\t' + annotation[1] + '\t' +'''




