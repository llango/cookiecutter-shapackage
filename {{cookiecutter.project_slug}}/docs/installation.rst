.. highlight:: shell

============
安装
============


稳定版本
--------------

为了安装 {{ cookiecutter.project_name }}, 在你的控制台运行如下命令:

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

该方法将按照 {{ cookiecutter.project_name }} 稳定版本。

如果你没有安装 `pip`_ ,  `Python 安装指南`_ 能指导你完成 `pip`_ 安装。

.. _pip: https://pip.pypa.io
.. _Python 安装指南: http://docs.python-guide.org/en/latest/starting/installation/


源码安装
------------

{{ cookiecutter.project_name }} 可以从 `Github repo`_ 进行下载。

你也可以克隆 public repository:

.. code-block:: console

    $ git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

或者下载 `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master

一旦你有了源代码，你可以用如下进行安装:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
.. _tarball: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master
