提示
=======

当您创建一个包时，系统会提示您输入这些值。

模板化值
----------------

在生成的项目的各个部分中将出现以下内容。

full_name
    你的全名。

email
    你的邮箱地址。

github_username
    你的 GitHub 账号。

project_name
    你的 Python 包项目名字。 这是在文档中使用的，所以这里的空格和任何字符都可以。
    
project_slug
    Python 包的名称空间。这应该是 Python 导入友好的。通常，它是 project_name 的暂缓版本。注意:您的 PyPi 项目和 Travi 链接将使用project_slug，因此在之后的 README 中更改它们。

project_short_description
   用一句话描述Python包的功能。

pypi_username
    您的Python包 PYPI 用户名。

version
    包的起始版本号。

选项
-------

以下包配置选项为项目设置不同的特性。

use_pytest
    是否使用 `pytest <https://docs.pytest.org/en/latest/>`_

use_pypi_deployment_with_travis
    使用使用 `Travis <https://travis-ci.org/>`_ 进行 PYPI 发布

add_pyup_badge
    是否包含 `pyup <https://github.com/pyupio/pyup>`_ 徽章

command_line_interface
    是否使用 Click 创建控制台脚本。控制台脚本入口点将匹配 project_slug。选项: ['Click',  'Argparse', 'No command-line interface']

create_author_file
    是否创建作者文件
    
open_source_license
    选择一个 `证书 <https://choosealicense.com/>`_. 选项: [1. MIT License, 2. BSD license, 3. ISC license, 4. Apache Software License 2.0, 5. GNU General Public License v3, 6. Not open source]
