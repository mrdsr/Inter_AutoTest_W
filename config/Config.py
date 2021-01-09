# 绝对路径
import os

import yaml

# add = os.path.dirname(os.path.abspath(__file__))
#
# file_path = add + "\config.yml"
#
# with open(file_path, encoding="utf-8") as f:
#     a = yaml.safe_load_all(f)
#
#     for i in a:
#         print(i)
from git_hub.untils.YamlUtils import YamlReadFlie

add = os.path.dirname(os.path.abspath(__file__))
file_path = add + "\config.yml"

a = YamlReadFlie(file_path)
c = a.moreFile()
print(c)
for i in c:
    print(i)