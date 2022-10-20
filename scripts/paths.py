"""


"""


from pathlib import Path


# Project Path
project_path = Path(__file__).parents[1]

# scrapy_path = project_path / 'scrapy'
# scrapy_path.mkdir(exist_ok=True)

# logs_path = scrapy_path / 'logs'
# logs_path.mkdir(exist_ok=True)

# adds_path = scrapy_path / 'adds'
# adds_path.mkdir(exist_ok=True)


# Package Path
package_path = project_path / 'sp_piracicaba'

data_path = package_path / 'data'
data_path.mkdir(exist_ok=True)

input_path = data_path / 'input'
input_path.mkdir(exist_ok=True)

input_path_bruto = input_path / 'bruto'
input_path_bruto.mkdir(exist_ok=True)

input_path_extract = input_path / 'extract'
input_path_extract.mkdir(exist_ok=True)

output_path = data_path / 'output'
output_path.mkdir(exist_ok=True)

output_path_geojson = output_path / 'geojson'
output_path_geojson.mkdir(exist_ok=True)

output_path_gpkg = output_path / 'gpkg'
output_path_gpkg.mkdir(exist_ok=True)

# output_path_tab = output_path / 'tab'
# output_path_tab.mkdir(exist_ok=True)

output_path_map = output_path / 'map'
output_path_map.mkdir(exist_ok=True)

output_path_shp = output_path / 'shp'
output_path_shp.mkdir(exist_ok=True)

output_path_zip = output_path / 'zips'
output_path_zip.mkdir(exist_ok=True)


if __name__ == '__main__':
    print(project_path)
