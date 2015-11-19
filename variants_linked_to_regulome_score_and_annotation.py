#!usr/bin/python

## Script to match the variants that were given a good score in RegulomeDB (signifying high probablity of being deleterious), with the original variants in order find additional info. E.g. how many samples had these deleterious mutations, the mutation signatures (transitions and transversions), common genes etc.

# ---------------------------------------------------------------------------
#               import libraries and specify paths
#----------------------------------------------------------------------------
import sys

path_regulome = '/home/tracey/Desktop/MASTERS_2014/ICGC/Regulome_annotations/Results/Annotations_from_web_interface/promoter_regulomedb_results.bed'

path_sv = '/home/tracey/Desktop/MASTERS_2014/ICGC/SV_results/actual_hits/UNIQ/actual_hits_promoter_UNIQ.txt'

file_regulome = open(path_regulome)
file_sv = open(path_sv)

sys.stdout = open('/home/tracey/Desktop/MASTERS_2014/ICGC/Regulome_annotations/Results/Annotations_from_web_interface/regulome_annotation_matched_to_original_variant/all_scores/regulome_annotation_promoter_ALL.txt', 'w')

# -------------------------------------------------------------------------------------------
#           split into columns and find a match based on chromosome and genomic position
#--------------------------------------------------------------------------------------------

regulome_list = []
for reg_line in file_regulome:
    columns = reg_line.strip('\n').split('\t')
    reg_chrm = columns[0][3:]
    reg_position = columns[1]
    #rsid = columns[3].split(';')[0]
    score = columns[3].split(';')[1]
    regulome_list.append([reg_chrm, reg_position, score])
    #print regulome_list


sv_list = []
for sv_line in file_sv:
    column = sv_line.strip('\n').split('\t')
    gene_name = column[0]
    sv_chrm = column[1]
    start = column[2]
    end = column[3]
    '''if start != end:
        print start, end'''  #THIS WAS USED TO TEST IF I WAS DEALING WITH INDELS OR POINT MUTATIONS EACH TIME A NEW VARIANT FILE WAS SELECTED
    donor = column[4]
    sample = column[5]
    ref_allele = column[6]
    mutated_from = column[7]
    mutated_to = column[8]
    structural_annotation = column[9]
    ensembl_gene = column[10]
    sv_list.append([sv_chrm, start, end, donor, sample, ref_allele, mutated_from, mutated_to, structural_annotation, ensembl_gene, gene_name])
    #print sv_list

# --------------------------------------------------------------------------------------
#    Match variant to its regulome annotation entry and print side by side
#--------------------------------------------------------------------------------------- 

for annotation in regulome_list:
    for sv in sv_list: 
        if annotation[0] == sv[0] and annotation[1] == sv[1]:
            print sv[10] + '\t' + sv[0] + '\t' + sv[1] + '\t' + sv[2]  + '\t' + sv[3]  + '\t' + sv[4]  + '\t' + sv[5]  + '\t' + sv[6]  + '\t' + sv[7]  + '\t' + sv[8]  + '\t' + sv[9]  + '\t' +  annotation[0] + '\t' + annotation[1] + '\t' + annotation[2]
#annotation[0] + '\t' + annotation[1] '''








