#!usr/bin/python

## Check if there are any aberrant methylation events in the non-coding regions of ccRCC genes

# ---------------------------------------------------------------------------
#               import libraries and specify paths
#----------------------------------------------------------------------------
import sys

path_methylation = '/home/tracey/Desktop/MASTERS_2014/ICGC/Methylation/ccRCC_methylation.tsv'
#Format promoter associated: promoter_meth_ccRCC.txt'
path_bed = '/home/tracey/Desktop/MASTERS_2014/ICGC/Bed_files_of_175_genes_using_UCSC/173_ccRCC_genes/promoter_173_ccRCC_genes_UNIQ.txt'
#Format: non_disease genes: bed_files_non_disease_175_random_genes/173_non_disease_genes/3UTR_173_non_disease_genes_UNIQ.txt' 
#Format disease genes: Bed_files_of_175_genes_using_UCSC/173_ccRCC_genes/promoter_173_ccRCC_genes_UNIQ.txt'

methyl_file = open(path_methylation)
bed_file = open(path_bed)
#print methyl_file

# ---------------------------------------------------------------------------
#    split and name columns in promoter methylation file and create list
#----------------------------------------------------------------------------

meth_list = []
for index, line in enumerate(methyl_file):
    if index == 0 : continue
    column = line.split('\t')
    ID_sample = column[1]
    sample_name = column[2]
    ID_tumour = column[3]
    probe_ID = column[8]
    chrom = column[10]
    position = int(column[11])
    gene = column[12]
    methylation = column[13]
    ave_beta_val_normal = column[14]
    beta_val = column[15]
    two_sided_pvalue = column[16].strip()
    meth_list.append([chrom, position, gene, methylation, beta_val, ave_beta_val_normal, two_sided_pvalue, probe_ID, ID_sample, sample_name, ID_tumour])
methyl_file.close()
#print meth_list
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

# ---------------------------------------------------------------------------------------------------------------------------
#    Find abberant promoter methylation coordinate in methylation file and match it to coordinates range within bed file
#---------------------------------------------------------------------------------------------------------------------------- 

sys.stdout = open ('/home/tracey/Desktop/MASTERS_2014/ICGC/Methylation/Results_ALL_methylation/173_ccRCC_genes/genomic_methyl_ccRCC_promoter', 'w')
#Format disease genes: 173_ccRCC_genes/methylation_in_promoter.txt', 'w')
#Format promoter associated, non-disease: Results_promoter_methylation/173_non_disease_genes/non_disease_methylation_in_promoter.txt', 'w')
#Format all methylation, non-disease: 173_non_disease_genes/genomic_methyl_non_disease_3UTR', 'w')
for meth in meth_list:
    for bed in bed_list:
        if meth[0] == bed[0] and meth[1] >= bed[1] and meth[1] <=bed[2]:
            print meth[0] + '\t' + str(meth[1]) + '\t' + meth[2] + '\t' + meth[3] + '\t' + meth[4] + '\t' + meth[5] + '\t' + meth[6] + '\t'+ meth[7] + '\t' + meth[8] + '\t' + meth[9] + '\t' + meth[10] + '\t' + bed[0] + '\t' + str(bed[1]) + '\t' + str(bed[2]) + '\t' + bed[3]   


### chrom, position, gene, methylation, beta_val, ave_beta_val_normal, two_sided_pvalue, probe_ID, ID_sample, sample_name, ID_tumour, chrm_bedfile, bed_start, bed_end, strand
