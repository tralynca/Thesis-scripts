# calculate the density of the hits in the distinct genomic regions

import sys

bed_path = '/home/tracey/Desktop/MASTERS_2014/ICGC/bed_files_non_disease_175_random_genes/UNIQ_bed_range/3UTR_93_non_disease_genes_UNIQ.txt'
#Format ccRCC genes:Bed_files_of_175_genes_using_UCSC/175GOI_3UTR_hg19_UNIQ.txt'
sv_path = '/home/tracey/Desktop/MASTERS_2014/ICGC/SV_results/Non_disease_genes_hits/Results/Actual_results/UNIQ/uniq_positions/uniq_positions_3UTR.txt'
#Format ccRCC genes: actual_hits/UNIQ/uniq_position/uniq_position_3UTR.txt'
#Format positions for all patients: /UNIQ/actual_hits_promoter_UNIQ.txt'

file_bed = open(bed_path)
file_sv = open (sv_path)


# ---------------------------------------------------------------------------
#           find the total number of bases within a bed list
#----------------------------------------------------------------------------      

bed_list= []                                                # create an empty list called bed_list, to be populated later
for bedline in file_bed:                                    # read the file in line by line
    bedfile_columns = bedline.strip().split()               # split blank spaces from both ends and split the lines on blank space to create columns
    bed_start = int(bedfile_columns[1])                     # extract the first coordinate of the bed file from the second column and convert integer
    bed_end = int(bedfile_columns[2])                       # extract the last coordinate of the bed file from the third column and convert integer
    val = bed_end - bed_start                                # calculate the total number of bases per line
    bed_list.append(val)                                    # add these values to a listx
    total = sum(bed_list)                                   # find the total of all values
print total
        
# ---------------------------------------------------------------------------
#      find the total number of hits(lines) in somatic variant file
#----------------------------------------------------------------------------     

lines = 0
for line in file_sv:
    lines +=1                                               # add one every time a new line is read
print(lines)

# --------------------------------------------------------------------------------
#      find the average number of hits within the total number of bases (density)
#---------------------------------------------------------------------------------

ave_hits  = float(lines)/total                         # average in percent4
print "{first:e}".format(first=ave_hits)                    # format to display number in scientific notation 
#print ("{:.4f}".format(ave_hits))                           
