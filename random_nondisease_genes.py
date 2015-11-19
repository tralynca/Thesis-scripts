import sys, random

path_non_disease_genes = '/home/tracey/Desktop/MASTERS_2014/ICGC/all_non-disease_genes+strand_UNIQ.txt'
#Format for 500 random lines: /ensembl_non_disease_genes.txt'
# all_non-disease_genes+strand_UNIQ.txt'
#Format for extracting 500 random lines from all ensemble IDs: SV_results/Non_coding_genes_hits/ensembl_non_disease_genes.txt'
sys.stdout = open('/home/tracey/Desktop/MASTERS_2014/ICGC/93_non_disease_genes.txt', 'w')

input_file = open(path_non_disease_genes)
lines = input_file.readlines()
#print (lines)
random_lines = random.sample(lines, 93)
#print (random_lines)
for line in random_lines:
    line = line.strip('\n')
    print (line)

