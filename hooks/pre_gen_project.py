import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print('错误: 项目 slug (%s) 不是一个有效的Python模块名。请不要使用  - 而 _ 代替' % module_name)

    #退出取消项目
    sys.exit(1)
