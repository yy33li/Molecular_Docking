# Molecular Docking on Compute Canada
## The scripts are designed to perform docking analysis using modules available on Compute Canada and simplier commands.
## Environment:
* Python package in used: Pandas (Please ensure it is installed in your python environment)
* Autodock Vina
* openbabel
## Usage:

After specifying the input file path and directory in the bash script, it is ready for submission to Compute Canada.
## Important commands in the bash script:
### 1. Required input files:
* The CSV file that store SMILES for all the compounds (input_smiles)
* The receptor/protein PDB file
* The configuration file that stores center and size of the grid box (confpath)
### 2. Required input directory to store output results:
* A file path to store both assigned name and SMILES for all the compounds (output_csv)
* An empty directory where the all output results will be restored (store_path)
* A file path to store docking result (result_csv)
### 3. Process input file - Compounds
* prepare_compounds.py

Args:
* input_smiles
* smiles_col: Column name that stores compound SMILES
* output_csv
* store_path

E.g.
```bash
python prepare_compounds.py input_smiles smiles_col output_csv store_path
```
### 4. Process input file - Receptor/protein

OpenBabel is used to prepare receptor/protein file for docking

E.g.
```bash
obabel receptor.pdb -O receptor.pdbqt -xr -p 7.4 --partialcharge eem
```
### 5. Docking

Autodock Vina is used to estimate binding affinity of given compound and receptor/protein

E.g. 
```bash
vina --config confpath --ligand com.pdbqt --receptor receptor.pdbqt --out out.pdbqt --log log.txt
```
### 6. Collect results
* collect_results.py

Args:
* store_path
* result_csv

E.g.
```bash
python collect_results.py store_path result_csv
```
### Tip for performing docking on large database

The input SMILES file can be divided into multiple smaller files, allowing you to run the job in parallel
