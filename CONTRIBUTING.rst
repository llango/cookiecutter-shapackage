.. highlight:: shell

============
贡献
============

欢迎提交你的贡献。

你可以通过多种方式进行贡献:

贡献类型
----------------------

提交 Bugs 
~~~~~~~~~~~

可以在 https://github.com/llango/cookiecutter-shapackage/issues 提交 bug 。

当你提交 bug，建议你说明一下几点：

* 你的操作系统机器版本。
* 对故障排除有帮助的任何详细信息。
* 重现 bug 的详细步骤。

修复 Bugs 
~~~~~~~~

查看Github issues 任何有关 bug 信息，然后进行修复提交。

实现功能
~~~~~~~~~~~~~~~~~~

查看Github issues 任何有关功能实现的信息。 标有 "enhancement" 和 "help wanted" 是对想要实现这功能开放。

编写文档 
~~~~~~~~~~~~~~~~~~~

欢迎丰富  Cookiecutter ShaPackage 文档 。 

提交反馈
~~~~~~~~~~~~~~~

最好提交反馈的方式在：
https://github.com/llango/cookiecutter-shapackage/issues.

如果你想提出一个功能:

* 详细解释它是如何工作的。
* 尽量缩小范围，使其更容易实现。
* 请记住，这是一个由志愿者驱动的项目，欢迎你的贡献:)

开始
------------

做好准备贡献了吗? 这里是安装 `cookiecutter-shapackage` 进行本地开发的。

1. 从 Github `cookiecutter-shapackage`  克隆：

::

2. 克隆到本地：:

   .. code-block:: bash

    $ cd path_for_the_repo
    $ git clone git@github.com:YOUR_NAME/cookiecutter-pypackage.git

::

3. 将您的本地副本安装到你的Python 虚拟环境中。假设您已经安装了virtualenvwrapper，你可以如下方式操作::

   .. code-block:: bash

        $ virtualenv cookiecutter-shapackage-env
        $ source cookiecutter-shapackage-env/bin/activate

   修改后看起来如下:

   .. code-block:: bash

        (cookiecutter-shapackage-env) $

::

4. 给本地开发创建一个分支:

   .. code-block:: bash

        $ git checkout -b name-of-your-bugfix-or-feature

   现在你可以本地修改你的代码了。

::

5. 当你完成了开发，检查你的修改是否通过了 flake8 和 测试，包括使用 tox 测试其他 Python 版本:

   .. code-block:: bash

        $ flake8 ./tests

::

6. 下一步将是运行测试用例。 `cookiecutter-pypackage` 使用 pytest, 您可以运行PyTest。在运行pytest之前，应该确保安装了所有依赖项:

   .. code-block:: bash

        $ pip install -r requirements_dev.txt
        $ pytest ./tests

  如果在安装加密包时出现任何错误(类似于' #include <openssl/aes.h> ')。请更新您的pip版本并重试:

   .. code-block:: bash

        # Update pip
        $ pip install -U pip

::

7. 在提出pull请求之前，还应该运行tox。这将在不同版本的Python中运行测试:

   .. code-block:: bash

        $ tox

   如果你缺少 flake8, pytest 或 tox，只需“pip install”它们到你的 virtualenv 中.

::

8. 如果您的贡献是一个bug修复或新特性，您可能想要向现有的测试套件添加一个测试。有关详细信息，请参阅下面的添加新测试一节。

::

9. 提交你的修改并将你的分支推到GitHub上:

   .. code-block:: bash

        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

::

10. 通过GitHub网站提交pull请求

::


Pull 请求操作
-----------------------

在你提交 pull 请求之前，检查它是否符合这些条件:

1. pull 请求应该包括测试。

2. 如果 pull 请求增加了功能，则应该更新文档。把将新功能添加到带有 docstring 的函数中，并且将该功能添加到 README.rst 的列表中。
   
3. pull 的功能应该满足Python 3.5, 3.6, 3.7 and 3.8, and for PyPy. 检查
   https://travis-ci.org/llango/cookiecutter-pypackage/pull_requests
   并确保测试通过了所有支持的Python版本。


添加新测试
--------------

在修复bug或添加特性时，最好的做法是添加一个测试来演示修复或新特性的预期行为。这些测试应该集中在一小部分功能上，并证明更改是正确的。

要编写并运行您的新测试，请遵循以下步骤:

1. 将新测试添加到' tests/test_bake_project.py '中。将测试集中在特定的bug或新特性的一小部分上

::

2. 如果您已经对代码进行了更改，请保存更改并确认已存储所有更改:

   .. code-block:: bash

        $ git stash
        $ git stash list

::

3. 运行测试并确认测试失败。如果您的测试没有失败，重新编写测试，直到它在原始代码上失败:

   .. code-block:: bash

        $ pytest ./tests

::

4. (可选)使用tox运行测试，以确保代码更改能够正常工作在不同的Python版本:

   .. code-block:: bash

        $ tox

::

5. 继续处理错误修复或新特性或恢复更改。恢复已存储的更改并确认它们的恢复:

   .. code-block:: bash

        $ git stash pop
        $ git stash list

::

6. 重新运行测试并确认测试通过。如果它通过了,恭喜你!

.. cookiecutter: https://github.com/llango/cookiecutter-shapackage
.. virtualenv: https://virtualenv.pypa.io/en/stable/installation
.. git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

