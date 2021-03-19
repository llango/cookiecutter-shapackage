PyPI 发布清单
======================

在首次发布之前
-------------------------

#. 在PyPI上注册该包:

    .. code-block:: bash

        python setup.py register

#. 访问PyPI确保该包注册了。

对于每个版本
-------------------

#. 更新 HISTORY.rst

#. 提交更改:

    .. code-block:: bash

        git add HISTORY.rst
        git commit -m "Changelog for upcoming release 0.1.1."

#. 更新版本数字 (can also be patch or major)

    .. code-block:: bash

        bump2version minor

#. 为本地开发重新安装包，但使用新的版本号::

    .. code-block:: bash

        python setup.py develop

#. 运行测试:

    .. code-block:: bash

        tox

#. Push 提交:

    .. code-block:: bash

        git push

#. Push 该 tags, 在GitHub和PyPI上创建新版本:

    .. code-block:: bash

        git push --tags

#. 检查 PyPI 列表页面，确保 README、发布说明和路线图正确显示。如果没有，试试如下:

    #. 复制并粘贴 RestructuredText 文本到  http://rst.ninjs.org/ 找出错误的格式。

    #. 检查本地 long_description :

        .. code-block:: bash

            pip install readme_renderer
            python setup.py check -r -s

#. 编辑发布在GitHub上 (e.g. https://github.com/llango/cookiecutter-shapackage/releases)。 将发行说明粘贴到发行版的发行版页面中，并为发行版提供一个标题。


