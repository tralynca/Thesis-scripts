import sys, random

path_gene_exp = '/home/tracey/Desktop/MASTERS_2014/ICGC/Gene_expression_ICGC_and_COSMIC/uniq_patient_gene_exp_data_for_ccRCC_andGOI.txt'
sys.stdout = open('/home/tracey/Desktop/MASTERS_2014/ICGC/Gene_expression_ICGC_and_COSMIC/Results_ICGC_and_COMSIC_gene_exp_and_SV/ccRCC_COSMIC_gene_exp/random_95_patients_gene_exp_data_for_ALL_gene_exp_data.txt', 'w')

input_file = open(path_gene_exp)
lines = input_file.readlines()
#print (lines)

random_lines = random.sample(lines, 95)
#print (random_lines)
for line in random_lines:
    line = line.strip('\n')
    print (line)
