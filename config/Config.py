#绝对路径
import os

import yaml

add = os.path.dirname(os.path.abspath(__file__))
print(add)

file_path = add + "/config.yml"


with open(file_path) as f:
    a = yaml.safe_load(f)
    print(a)




