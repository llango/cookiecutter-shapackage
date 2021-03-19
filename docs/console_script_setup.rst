.. _console-script-setup:


控制台脚本设置
=================

您的包可以使用 Click 或 argparse 包含控制台脚本 (Python 3.2+).

它是如何工作的
------------

在设置中如果 'command_line_interface' 选项设置为 ['click'] 或 ['argparse'] , cookiecutter 将添加一个
 'cli.py' 文件在 project_slug 字目录中。  在setup.py中添加了一个入口点，它指向cli.py中的主函数。

使用
------------
在开发中使用控制台脚本:

.. code-block:: bash

    pip install -e projectdir

'projectdir' 应该是带有 setup.py 文件的顶级项目目录。

将生成没有参数和 --help 输出的脚本 。

--help
    显示帮助菜单并退出

Known Issues
------------
使用 Click, 使用如下安装在项目的开发环境中:

.. code-block:: bash

    python setup.py develop

不能正确设置入口点。这是 Click 的一个已知问题。
以下工作将按预期进行:

.. code-block:: bash

    python setup.py install
    pip install mypackage

根据具体项目调整 'mypackage' 。


更多信息
------------

关于 Click 更多详情请点击:
http://click.pocoo.org/
