#!/bin/bash
#SBATCH --time=01:00:00        #format: hh:mm:ss
#SBATCH --mem-per-cpu=1024M    
#SBATCH --account=def-hallett-ab           
#SBATCH --nodes=1              #number of cpus
#SBATCH --mail-user=yanyi.li@mail.utoronto.ca --mail-type=BEGIN       

#load required modules
module load StdEnv/2020 autodock_vina/1.1.2 openbabel

#data file contains compound SMILES
input_smiles=

#name of column that stores compound SMILES
smiles_col=

#file path to store modified csv
output_csv=

#receptor PDB file
receptor=

#configuration text file
confpath=

#an empty directory where the all output results will be restored
store_path=
mkdir -p $store_path

#file path to store docking results
result_csv=

#python path that has pandas installed (e.g. venv/bin/python)
python_path=

#directory where scripts are stored
docking_dir= 

#generate 3D compounds
$python_path $docking_dir/prepare_compounds.py $input_smiles $smiles_col $output_csv $store_path

#prepare receptor file 
obabel $receptor -O ${receptor%.*}.pdbqt -xr -p 7.4 --partialcharge eem

#get all folder names in the parent directory and store them in a list
folders=($(find "$store_path" -maxdepth 1 -type d -not -path "$store_path"))

#loop through each folder and execute the job
for g in "${folders[@]}"; do
  if [ "$g" != "$store_path" ]; then
    echo "Executing job in folder: $folder"

    cd $g

      timeout 800 /bin/bash <<EOF
      vina --config $confpath --ligand com.pdbqt --receptor ${receptor%.*}.pdbqt --out out.pdbqt --log log.txt
EOF
    
    fi

$python_path $docking_dir/collect_results.py $store_path $result_csv

done
