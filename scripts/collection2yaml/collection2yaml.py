import stac
from collections import OrderedDict
import yaml
import click

# Fontes:
# https://github.com/opendatacube/datacube-core/tree/0650038d113f8d7f5f4a47075eea706fe24a84fb/docs/config_samples/dataset_types


def setup_yaml():
    """ https://stackoverflow.com/a/8661021 """

    def represent_dict_order(self, data): return self.represent_mapping(
        'tag:yaml.org,2002:map', data.items())
    yaml.add_representer(OrderedDict, represent_dict_order)


setup_yaml()


def generate_product_type(collection):
    return "{}_{}_{}".format(
        collection['properties']['bdc:temporal_composition']['schema'],
        collection['properties']['bdc:temporal_composition']['step'],
        collection['properties']['bdc:temporal_composition']['unit'])


def convert_bdc_collection(collection, constants):

    product_type = generate_product_type(collection)

    odc_config = OrderedDict()
    odc_config['name'] = collection['id']
    odc_config['description'] = collection['description']
    odc_config['metadata_type'] = constants['metadata_type']

    odc_config['storage'] = OrderedDict()
    
    # remove +datum in some cases
    crs_proj4 = re.sub('\+datum=(\S)*\s', '', collection['properties']['bdc:crs'])
    odc_config['storage']['crs'] = crs_proj4
    
    odc_config['storage']['resolution'] = OrderedDict()
    first_band = next(iter(collection['properties']['bdc:bands']))
    odc_config['storage']['resolution']['x'] = int(
        collection['properties']['bdc:bands'][first_band]['resolution_x'])
    odc_config['storage']['resolution']['y'] = int(
        collection['properties']['bdc:bands'][first_band]['resolution_y'])*-1

    def measurements(tag, data):
        m = OrderedDict()
        m['name'] = tag # data['name']
        m['aliases'] = [data['name'], ]
        m['dtype'] = data['data_type'].lower()
        m['nodata'] = data['fill']
        m['units'] = constants['units']
        return m

    odc_config['metadata'] = OrderedDict()
    odc_config['metadata']['platform'] = {'code': constants['platform_code']}
    odc_config['metadata']['instrument'] = {'name': collection['id']}
    odc_config['metadata']['product_type'] = product_type
    odc_config['metadata']['format'] = {'name': constants['format_name']}
    odc_config['measurements'] = [measurements(k, v)
                                  for k, v in collection['properties']['bdc:bands'].items() if k not in constants['ignore']]
    return odc_config  # default_flow_style=None


@click.command()
@click.option('-c', '--collection', required=True, help='Collection name (Ex. C4_64_16D_MED).')
@click.option('-t', '--type', default='eo', help='Metadata type.')
@click.option('-p', '--code', default='BDC', help='Platform code.')
@click.option('-f', '--format', default='GeoTiff', help='Format name.')
@click.option('--units', default='1', help='Units.')
@click.option('--url', default='http://brazildatacube.dpi.inpe.br/bdc-stac/0.8.0/', help='BDC STAC url.')
@click.option('-o', '--outfile', default=None, help='Output file')
@click.option('-i', '--ignore', default=['quality'], help='List of bands to ignore')
def main(collection, type, code, format, units, url, outfile, ignore):
    constants = {
        'metadata_type': type,
        'platform_code': code,
        'format_name': format,
        'units': units,
        'ignore': ignore
    }
    s = stac.STAC(url, True)
    c = s.collection(collection)
    yaml_content = convert_bdc_collection(c, constants)
    if outfile is None:
        print(yaml.dump(yaml_content))
    else:
        with open(outfile, 'w') as f:
            yaml.dump(yaml_content, f)


if __name__ == '__main__':
    main()
