======================
Cookiecutter ShaPackage
======================

.. image:: https://pyup.io/repos/github/llango/cookiecutter-shapackage/shield.svg
    :target: https://pyup.io/repos/github/llango/cookiecutter-shapackage/
    :alt: 更新

.. image:: https://travis-ci.org/llango/cookiecutter-shapackage.svg?branch=master
    :target: https://travis-ci.org/github/llango/cookiecutter-shapackage
    :alt: 构建状态

.. image:: https://readthedocs.org/projects/cookiecutter-shapackage/badge/?version=latest
    :target: https://cookiecutter-shapackage.readthedocs.io/en/latest/?badge=latest
    :alt: 文档状态

Cookiecutter_ Python包的模板

* GitHub : https://github.com/llango/cookiecutter-shapackage/
* 文档: https://cookiecutter-shapackage.readthedocs.io/
* 开源协议: BSD license

特征
--------

* 使用 ``unittest`` 和 ``python setup.py test`` 或 ``pytest`` 进行测试
* Travis-CI_: 准备好进行Travis持续集成测试
* Tox_ testing: 易于测试 Python 3.5, 3.6, 3.7, 3.8 的设置
* Sphinx_ docs: 用于生成文档， 例如 `Read the Docs`_
* bump2version_: 使用单个命令进行预配置的版本冲突。
* 自动发布到 PyPI_ 当你 push 一个新的 tag 版本时。 (可选)
* 命令行界面使用 Click (可选)

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter


快速入门
----------

安装最新版 Cookiecutter::

    pip install -U cookiecutter

生成一个Python包项目::

    cookiecutter https://github.com/llango/cookiecutter-shapackage.git

然后:

* 创建一个 repo，然后放在那里。
* 添加 repo 到你的 Travis-CI_ 账号里去。
* 在虚拟环境安装依赖 (``pip install -r requirements_dev.txt``)
* Register_ 在 PyPI 注册你的项目。
* 运行Travis CLI命令 ``travis encrypt --add deploy.password`` 加密您的PyPI密码在Travis配置和激活自动部署在PyPI当您推送一个新标签到主分支。
* 添加 repo 到你的 `Read the Docs`_ 账号里去 + 打开Read the Docs服务钩子。
* 通过推送到一个新的tag 到 master来发布您的包。
* 添加一个 ``requirements.txt`` 指定项目将需要的包及其版本的文件。要了解更多信息，请参见 `pip docs for requirements files`_.
* 在 `pyup.io`_ 激活你的项目。

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

要了解更多信息，请参见 `cookiecutter-shapackage 教程`_.

.. _`cookiecutter-shapackage 教程`: https://cookiecutter-shapackage.readthedocs.io/en/latest/tutorial.html


