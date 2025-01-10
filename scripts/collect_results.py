import os
import csv
import sys

base_folder = sys.argv[1]
result_csv = sys.argv[2]

binding_affinities = {}

# iterate through each comand folder (com0, com1, ..., com99)
for i in range(100):  # Assuming you have folders com0 to com99
    com_folder = os.path.join(base_folder, f'com{i}')
    output_file = os.path.join(comand_folder, 'out.pdbqt')
    
    if os.path.exists(output_file):
        with open(output_file, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 2:  # ensure the file is not empty
                # extract the binding affinity from the second line
                second_line = lines[1].strip()
                if second_line.startswith("REMARK VINA RESULT:"):
                    value = second_line.split(":")[1].strip()
                    affinity = float(value.split(" ")[1].strip())
                    binding_affinities[f'com{i}'] = affinity

#store extracted values to csv file

with open(result_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Compound', 'Binding Affinity (kcal/mol)'])
    for comand, affinity in binding_affinities.items():
        writer.writerow([comand, affinity]) #comand here is com0, com1, com2,...
    
    csvfile.close()

# clear command line arguments list
sys.argv = []