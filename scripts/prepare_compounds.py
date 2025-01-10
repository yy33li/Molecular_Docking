import os
import sys
import pandas as pd
import subprocess

input_csv = sys.argv[1] 
column_name = sys.argv[2]
output_csv = sys.argv[3]
output_dir = sys.argv[4]


data = pd.read_csv(input_csv)
smiles = data[column_name]

#generate 2D structure for each SMILES
com_list = []
for idx, smi in smiles.items():
    
    #assign unique and simple name for each SMILES
    com = 'com' + str(idx) #e.g. com0, com1, com2,...
    com_list.append(com)

    #directory for storing all output files
    save_path = os.path.join(output_dir, com)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    command = ["obabel", "-:" + smi, "-h", "--gen3D", "-O", os.path.join(save_path, 'com.pdbqt')]
    subprocess.run(command, check=True)
#store assgined com name to csv file
new_data = pd.DataFrame(data, columns=['comand', 'smiles'])
new_datato_csv(output_csv, index=False)

# clear command line arguments list
sys.argv = []
