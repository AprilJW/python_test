from collections import defaultdict
import os
from pathlib import Path
import importlib
import sys

sys.path.append(os.path.abspath('../../../python_test/2D_data_Preprocessing/src'))
print('src:', os.path.abspath('../../../../python_test/2D_data_Preprocessing/src'))
_init_file_name = '__init__.py'

class GenerateConfig:

    density_gennum_params = ['SeedNum', 'MaxDensity', 'MinDensity', 'Gennum']

    def __init__(self):
        self.seed_path = None
        self.dest_path = None
        self.label_to_items = {}
        self.label_to_density_gennum = {}
        self.operator_type_to_operator = {}
        self.operator_to_params = {}

    def generate_label_to_density_gennum(self):
        return {i: 0 for i in self.density_gennum_params}

    def update_label_to_density_gennum(self, label_to_items, config_json=None):
        if config_json:
            density_gennum_dict = config_json.density_gennum_dict
        else:
            density_gennum_dict = self.generate_label_to_density_gennum()

        for k, v in label_to_items:
            self.label_to_density_gennum[k] = density_gennum_dict
            self.label_to_density_gennum[k]['SeedNum'] = len(v)

    def update_operator_type_to_operator(self):
        dir_path = Path(os.path.dirname(__file__))
        file_package_path = os.listdir(dir_path)
        print(file_package_path)
        for i in file_package_path:
            init_file_path = dir_path / i / _init_file_name
            print(type(init_file_path))
            #init_file_path = dir_path / i / 'Crop.py'
            print(init_file_path)
            if not init_file_path.is_file():
                continue
            print('8000')
            spec = importlib.util.spec_from_file_location(_init_file_name, init_file_path)
            print(spec)
            operator_init = importlib.util.module_from_spec(spec)
            print(operator_init)
            spec.loader.exec_module(operator_init)
            print(operator_init.operator_type_operator)
            self.operator_type_to_operator.update(operator_init.operator_type_operator)
        print(self.operator_type_to_operator)

if __name__ == '__main__':
    generate_config = GenerateConfig()
    #generate_config.update_label_to_density_gennum()
    #generate_config.test()
    generate_config.update_operator_type_to_operator()