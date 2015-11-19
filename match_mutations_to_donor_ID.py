#!usr/bin/python

## Match the donor IDs that contained somatic variants to the donor file that contains the clinical data

# ---------------------------------------------------------------------------
#               import libraries and specify paths
#----------------------------------------------------------------------------
import sys

path_donor_and_mutations = '/home/tracey/Desktop/MASTERS_2014/ICGC/Regulome_annotations/Results/Annotations_from_web_interface/regulome_annotation_matched_to_original_variant/173_ccRCC_genes/vlookup_donor_no_and_types_of_mutations.txt'

path_donor_file = '/home/tracey/Desktop/MASTERS_2014/ICGC/donor.all_projects.tsv'

file_ID = open(path_donor_and_mutations)
donor_file = open(path_donor_file)
sys.stdout = open('/home/tracey/Desktop/MASTERS_2014/ICGC/Regulome_annotations/Results/Annotations_from_web_interface/regulome_annotation_matched_to_original_variant/173_ccRCC_genes/donor_clinical_AND_SM_info.txt', 'w')

# ---------------------------------------------------------------------------
#      Extract donor ID and matched mutations data and place into list
#----------------------------------------------------------------------------

#Format donor mutations file:
## Patient ID 	ALL non-coding	ALL CDS mutations	Deleterious mutations ONLY	
## DO46877	    221	                7	                10	

donor_mutations = []
for line in file_ID:
    columns = line.strip().split('\t')
    patient = columns[0]
    all_non_coding = columns[1]
    all_CDS = columns[2]
    deleterious_non_cod = columns[3]
    donor_mutations.append([patient,all_non_coding, all_CDS, deleterious_non_cod])
    #print donor_mutations

# ---------------------------------------------------------------------------
#                           place donor info into list
#----------------------------------------------------------------------------

donor_info_list = []
for item in donor_file:
    column = item.split('\t')
    #print column
    donor_ID = column[0]
    #project_code = column[1]
    sex = column[4]
    vital_status = column[5]
    disease_status_last_follow_up = column[6]
    relapse_type = column[7]
    age_at_diagnosis = column[8]
    #age_at_enrollment_at_last_follow_up = column[9]
    stage_at_diagnosis = column[14]
    #stage_suppl = column[15]
    survival_time_in_days = column[16]
    donor_info_list.append([donor_ID, sex, vital_status, disease_status_last_follow_up, relapse_type, age_at_diagnosis, stage_at_diagnosis, survival_time_in_days])
    #print donor_info_list

# ---------------------------------------------------------------------------
#       donor ID of samples with variants to the clinical info
#----------------------------------------------------------------------------

for IDs in donor_mutations:
    for donor in donor_info_list:
        if IDs[0] == donor[0]:
            print  IDs[0] + '\t' + IDs[1] +'\t' +IDs[2] +'\t' +IDs[3] + '\t' + donor[1] + '\t' + donor[2] + '\t' + donor[3] + '\t' + donor[4] + '\t' + donor[5] + '\t' + donor[6] + '\t' + donor[7] 
