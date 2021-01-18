# 绝对路径
import os

import yaml
from git_hub.untils.YamlUtils import YamlReadFlie

add = os.path.dirname(os.path.abspath(__file__))
file_path = add + "\config.yml"

a = YamlReadFlie(file_path)
c = a.moreFile()
print(c)
