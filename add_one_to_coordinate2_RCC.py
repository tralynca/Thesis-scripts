#---------------------------------------------------------------------------------------------------------------
# Add 1 to the last coordinate in order to create a one-coordinate-based bed file for submission to RegulomeDB
#---------------------------------------------------------------------------------------------------------------

import sys

path_variants = '/home/tracey/Desktop/MASTERS_2014/ICGC/SV_results/actual_hits/173_non_disease_genes/uniq_positions/actual_hits_175_non_disease_introns_UNIQ_positions.txt'

#Format diseaase genes: 173ccRCC_genes/uniq_positions/actual_hits_175_ccRCC_promoter_UNIQ_positions.txt'
variant_file = open(path_variants)

sys.stdout = open('/home/tracey/Desktop/MASTERS_2014/ICGC/Regulome_annotations/Files_for_input_to Regulome_webfront/non_disease_genes/regulome_coord_coverted_non_disease_introns.txt', 'w')

# Format for disease genes:ccRCC_disease_genes/regulome_coord_coverted_ccRCC_promoter.txt', 'w')

#------------------------------------------------------------------------------------------------------
#  Create columns and extract the chromosome, first and last coordinates
#------------------------------------------------------------------------------------------------------

for line in variant_file: 
    column= line.strip().split('\t')                # separate based ont ab delimiter and create columns 
    chrm =  column[1]                               # extract chromosome
    first = int(column[2])                          # extract start coordinate
    last =  int(column[3])                          # extract last coordinate

#------------------------------------------------------------------------------------------------------
# Add 1 to the last coordinate in where necessary
#------------------------------------------------------------------------------------------------------

    if last == first: 
        last = last +1    #if the last coordinate = the first coordinate, add 1 to the last coordinate
    else: 
        last = last + 0               # add nothing if the last coordinate exceeds the first
    print chrm, first, last


        

