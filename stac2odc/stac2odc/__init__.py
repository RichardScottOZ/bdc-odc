import yaml
from collections import OrderedDict


def setup_yaml():
    """ https://stackoverflow.com/a/8661021 """

    def represent_dict_order(self, data): return self.represent_mapping(
        'tag:yaml.org,2002:map', data.items())

    yaml.add_representer(OrderedDict, represent_dict_order)


setup_yaml()

