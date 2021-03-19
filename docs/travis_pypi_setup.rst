.. _travis-pypi-setup:

Travis/PyPI 设置
=================

可选地, 当您 push 一个新的 tag 到主分支时，您的包可以自动在PyPI上发布。

安装 Travis CLI tool
---------------------------

macOS
------

安装方式:

```
brew install travis
```

Windows and Linux
------------------

按照您的操作系统的官方 Travis CLI 安装说明进行安装:

https://github.com/travis-ci/travis.rb#installation

如何使用
------------

一旦你安装了 `travis` 命令行工具安装, 在你的项目根目录中可以这么做::

    travis encrypt --add deploy.password

这将加密您本地存储的PyPI密码，并将其保存到 travis.yml 文件中。将更改提交到git。


你的发布过程
--------------------

如果您正在使用这个特性，那么这就是您将如何发布 patch 的方法:

.. code-block:: bash

    bump2version patch
    git push --tags

这将导致:

* mypackage 0.1.1 showing up in your GitHub tags/releases page
* mypackage 0.1.1 getting released on PyPI

你也可以 用 `minor` 和 `major` 替换路径。


更多信息
------------

您可以阅读更多关于使用 Travis 进行 PyPI 部署的内容:
https://docs.travis-ci.com/user/deployment/pypi/
