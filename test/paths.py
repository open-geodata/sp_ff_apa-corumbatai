import os

data_path = os.path.join('..', 'src', 'sp_ff_apa_corumbatai', 'data')

input_path = os.path.join(data_path, 'input')
os.makedirs(input_path, exist_ok=True)

bruto_path = os.path.join(input_path, 'bruto')
os.makedirs(bruto_path, exist_ok=True)

extract_path = os.path.join(input_path, 'extract')
os.makedirs(extract_path, exist_ok=True)

output_path = os.path.join(data_path, 'output')
os.makedirs(output_path, exist_ok=True)

output_path_maps = os.path.join(output_path, 'maps')
os.makedirs(output_path_maps, exist_ok=True)

output_path_gpkg = os.path.join(output_path, 'gpkg')
os.makedirs(output_path_gpkg, exist_ok=True)

output_path_zips = os.path.join(output_path, 'zips')
os.makedirs(output_path_zips, exist_ok=True)
