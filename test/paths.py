import os

data_path = os.path.join('..', 'data')
bruto_path = os.path.join(data_path, 'bruto')
input_path = os.path.join(data_path, 'input')
output_path = os.path.join(data_path, 'output')

os.makedirs(bruto_path, exist_ok=True)
os.makedirs(input_path, exist_ok=True)
os.makedirs(output_path, exist_ok=True)

output_path_maps = os.path.join(output_path, 'maps')
output_path_gpkg = os.path.join(output_path, 'gpkg')
output_path_zips = os.path.join(output_path, 'zips')

os.makedirs(output_path_maps, exist_ok=True)
os.makedirs(output_path_gpkg, exist_ok=True)
os.makedirs(output_path_zips, exist_ok=True)
