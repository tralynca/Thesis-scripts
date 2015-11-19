#!usr/bin/python

## Find all the non-coding somatic mutations in the genomic regions of ccRCC genes 

# ---------------------------------------------------------------------------
#               import libraries and specify paths
#----------------------------------------------------------------------------

import sys

path_icgc = '/home/tracey/Desktop/MASTERS_2014/ICGC/simple_somatic_mutation.open.RECA-EU.tsv'
path_bed = '/home/tracey/Desktop/MASTERS_2014/ICGC/Bed_files_of_175_genes_using_UCSC/175GOI_introns_hg19_UNIQ.txt'

icgc_file = open(path_icgc)
bed_file = open(path_bed)

# ---------------------------------------------------------------------------
#           split and name columns in icgc files and create list
#---------------------------------------------------------------------------- 
icgc_list = []

for index, line in enumerate(icgc_file):
    if index == 0:
        continue
    icgc_column = line.split('\t')
    donor =  icgc_column[1]
    specimen = icgc_column[3]
    sample = icgc_column[4]
    chromosome = icgc_column[8]
    start = int(icgc_column[9])
    end = int(icgc_column[10])
    strand = icgc_column[11]
    strand = icgc_column[11]
    ref_allele = icgc_column[14]
    mutated_from = icgc_column[15]
    mutated_to = icgc_column[16]
    quality_score = icgc_column[17]
    total_read_count = icgc_column[19]
    mutant_allele_read_count = icgc_column[20]
    genomic_reg_conseq_type = icgc_column[25]
    ensemb_gene = icgc_column[28]
    ensemb_transcript = icgc_column[29]
    icgc_list.append([chromosome, start, end, strand, donor, specimen, sample, ref_allele, mutated_from, mutated_to, quality_score, total_read_count, mutant_allele_read_count, genomic_reg_conseq_type, ensemb_gene, ensemb_transcript])
icgc_file.close()
#print icgc_list
# ---------------------------------------------------------------------------
#           split and name columns in .bed files and create list
#----------------------------------------------------------------------------  
bed_list= []                                                # create an empty list called bed_list, to be populated later
for bedline in bed_file:                                    # read the file in line by line
    bedfile_columns = bedline.strip().split()               # split blank spaces from both ends and split the lines on blank space to create columns
    bed_start = int(bedfile_columns[1])                     # extract the first coordinate of the bed file from the second column and convert integer
    bed_end = int(bedfile_columns[2])                       # extract the last coordinate of the bed file from the third column and convert integer
    chrm_no = bedfile_columns[0]                            # extract the chromosome number from the first column (format chr19)
    if '_' in chrm_no:  
        chrm_bedfile = chrm_no[3:5].split('_')[0]           # in some cases this columns contains additional comments separeted by "_"
    else:
        chrm_bedfile =  chrm_no[3:5]                        # extract only the third and fourth elements in the first column as the chromosome
    strand = bedfile_columns[5]                             # extract the strand (+ or -) from the 6th column
    bed_list.append([chrm_bedfile, bed_start, bed_end, strand])     # add the necessary items to the list called bed_list
bed_file.close()
#print bed_list

# --------------------------------------------------------------------------------------
#    Find variant from icgc file and match it to coordinates range within bed file
#--------------------------------------------------------------------------------------- 
sys.stdout = open ('/home/tracey/Desktop/MASTERS_2014/ICGC/SV_results/SV_results_introns.txt', 'w')
for icgc in icgc_list:
    for bed in bed_list:
        if icgc[0] == bed[0] and icgc[1] >= bed[1] and icgc[2] <= bed[2] and bed[3] == '+':
            print icgc[0] + '\t' + str(icgc[1]) + '\t' + str(icgc[2]) + '\t' + icgc[3] + '\t' + icgc[4] + '\t' + icgc[5] + '\t' + icgc[6] + '\t' + icgc[7] + '\t' + icgc[8] + '\t' + icgc[9] + '\t' + icgc[10] + '\t' + icgc[11] + '\t' + icgc[12] + '\t' + icgc[13] + '\t' + icgc[14] + '\t' + icgc[15] + '\t' + bed[0] + '\t' + str(bed[1]) + '\t' + str(bed[2]) + '\t' + bed[3] 

