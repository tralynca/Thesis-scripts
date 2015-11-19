#!usr/bin/python

## Extract all data for the 95 random patients from the gene expression file with ccRCC and 173 GOI data

# ---------------------------------------------------------------------------
#               import libraries and specify paths
#----------------------------------------------------------------------------
import sys

file_exp_data = open('/home/tracey/Desktop/MASTERS_2014/ICGC/Gene_expression_ICGC_and_COSMIC/combined_ccRCC_tissue_ALL_disease_and_non_disease_GE_data.txt')
file_95_patients =  open('/home/tracey/Desktop/MASTERS_2014/ICGC/Gene_expression_ICGC_and_COSMIC/Results_ICGC_and_COMSIC_gene_exp_and_SV/random_95_patients_ALL_disease_and_non_disease_genes.txt')
sys.stdout = open('/home/tracey/Desktop/MASTERS_2014/ICGC/Gene_expression_ICGC_and_COSMIC/Results_ICGC_and_COMSIC_gene_exp_and_SV/ccRCC_COSMIC_gene_exp/ALL_GE_data_for_95_random_patients_173_disease_and_non_disease_genes.txt', 'w')

patient_list = []
for entry in file_95_patients:
    patient  = entry.strip().split()[1]
    patient_list.append(patient)
    #print patient_list

for line in file_exp_data:
    for patient_ID in patient_list:
        if patient_ID in line:
            print line.strip('\n')
