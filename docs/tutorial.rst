教程
========

.. note:: 你觉得这些说明有什么让你困惑的吗? `Edit this file`_
          提交一个 pull 请求与您的改进!

.. _`Edit this file`: https://github.com/llango/cookiecutter-pypackage/blob/master/docs/tutorial.rst

首先，你需要一个 `GitHub account`_ 帐户和一个 `PyPI`_ 帐户。在开始学习本教程之前创建这些。  如果您是 Git 和 GitHub 新手的话，您可能需要花几分钟时间阅读`GitHub Help`_ 页面顶部的一些教程 。

.. _`GitHub account`: https://github.com/
.. _`PyPI`: https://pypi.python.org/pypi
.. _`GitHub Help`: https://help.github.com/


Step 1: 安装 Cookiecutter
----------------------------

首先, 您需要为包项目创建并激活一个虚拟环境， 使用你喜欢的方法，或者像这样为你的新包创建一个 虚拟环境:

.. code-block:: bash

    virtualenv ~/.virtualenvs/mypackage

这儿, ``mypackage`` 是你创建的包名。

激活你的环境:

.. code-block:: bash

    source bin/activate

Windows, 激活方式如下。您可能会发现使用命令提示符窗口比 gitbash 工作得更好。

.. code-block:: powershell

    > \path\to\env\Scripts\activate


安装 cookiecutter:

.. code-block:: bash

    pip install cookiecutter


Step 2: 生成你的包
-----------------------------

现在是时候生成Python包了。

使用 cookiecutter, 指向 cookiecutter-shapackage repo:

.. code-block:: bash

    cookiecutter https://github.com/llango/cookiecutter-shapackage.git

您将被要求输入一些值来设置这个包。
如果您不知道输入什么，请使用默认值。


Step 3: 创建一个 GitHub Repo
----------------------------

去 Github 账号下创建 ``mypackage``, ``mypackage`` 应当匹配你运行 cookiecutter 设置 ``[project_slug]`` 。这样才能让 Travis CI 和 pyup.io 能找到它。

``如果您的 virtualenv 文件夹在项目文件夹中，请确保将 virtualenv 文件夹名称添加到 .gitignore 文件中。``

你将发现一个以 ``[project_slug]``命名的文件夹。移动到这个文件夹，然后安装 git 来使用 GitHub repo 并上传代码:

.. code-block:: bash

    cd mypackage
    git init .
    git add .
    git commit -m "Initial skeleton."
    git remote add origin git@github.com:myusername/mypackage.git
    git push -u origin master

``myusername`` 和 ``mypackage`` 会根据您的用户名和包名进行调整。

你需要 sh 密钥push the repo. 你可以 `Generate`_ 一个密钥或 `Add`_ 一个现有的密钥。

.. _`Generate`: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
.. _`Add`: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/


Step 4: 安装开发环境
--------------------------------

在项目中应当包含 ``requirements_dev.txt`` 文件。

你的虚拟环境是激活的。如果不是，现在就激活它。安装新项目的本地开发依赖:

.. code-block:: bash

    pip install -r requirements_dev.txt


Step 5: 设置 Travis CI
------------------------

`Travis CI org`_ [*]_ 是一个持续集成工具，用于防止集成问题。 每次提交到主分支都会触发应用程序的自动构建。

使用您的 Github 凭据登录。它可能需要几分钟的 Travis CI 加载所有你的 GitHub reps。它们将被列在 repo 名称左侧的方框中，方框中有一个 ``X`` ，这意味着它与 Travis CI 没有关联。

添加公共 repo 到您的 Travis CI 帐户点击``X`` 打开它在 ``mypackage`` repo 旁边的框。不要试图遵循其他指示，这将在接下来处理。

在你的终端中，你的 虚拟环境仍然是激活的。如果不是，先激活它。运行T ravis CLI 工具进行 Travis CI 设置:

.. code-block:: bash

    travis encrypt --add deploy.password

这将:

* 加密你的 PyPI 密码在你的 Travis 配置上。
* 当你 push 一个新 tag 到主分支时，激活PyPI上的自动部署。

查看 :ref:`travis-pypi-setup` 获取更多信息。

.. [*] 对于私有项目可去 `Travis CI com`_

.. _`Travis CI org`: https://travis-ci.org/
.. _`Travis CI com`: https://travis-ci.com/


Step 6: 设置 Read the Docs
--------------------------

`Read the Docs`_ 为开源社区提供文档在线查看。 

 要使用它，请在 `Read the Docs`_ 上创建一个新帐户或登录到您现有的帐户。

如果你不在你的仪表盘上，选择右上方你的用户名旁边的下拉菜单，并选择“我的项目”。选择导入存储库的按钮并按照说明操作。

现在，当对包进行文档更改时，将重新构建文档。

.. _`Read the Docs`: https://readthedocs.org/

Step 7: 设置 pyup.io
----------------------

`pyup.io`_ 是一个帮助你保持你的需求文件最新的服务。 它会自动向你发送拉请求，每当有一个新版本的依赖。

要使用它，请在`pyup.io`_ 上创建一个新帐户或登录到您现有的帐户。

点击左上角的绿色``Add Repo`` 按钮，选择在步骤3中创建的回购。一个弹出窗口将询问您是否想固定依赖项。 点击 ``Pin`` 添加该 repo 。

一旦你的 repo 设置正确，  pyup.io 徽章将显示您当前的更新状态。

.. _`pyup.io`: https://pyup.io/

Step 8: 发布到 PyPI
-----------------------


Python包索引或 `PyPI`_ 是Python编程语言的官方第三方软件存储库。Python开发人员希望它成为所有开源Python包的全面目录。

准备好后，以标准的Python方式发布包。

有关提交包的更多信息，请参见`PyPI Help`_ 。

.. _`PyPI`: https://pypi.python.org/pypi
.. _`PyPI Help`: https://pypi.org/help/#publishing

