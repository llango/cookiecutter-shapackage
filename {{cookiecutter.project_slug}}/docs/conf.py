#!/usr/bin/env python
#
# {{ cookiecutter.project_slug }} 文档构建配置文件, 由sphinx-quickstart于 Fri Jun  9 13:47:02 2017 创建.
#
# 这个文件是execfile()d，当前目录设置为它的包含目录。
#
# 注意，并不是所有可能的配置值都在这个自动生成的文件中。
#
# 所有配置值都有一个默认值;
# 注释掉的值用于显示默认值。

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.

# 如果扩展名(或用autodoc编写文档的模块)在另一个目录中，
# 请将这些目录添加到 sys.path 中。
# 如果目录相对于文档根目录，则使用 os.abspath使其绝对，
# 如下所示。

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import {{ cookiecutter.project_slug }}

# -- 通用配置 ---------------------------------------------

# 如果您的文档需要一个最小的Sphinx版本，请在这里说明。
#
# needs_sphinx = '1.0'

# 在这里以字符串的形式添加任何Sphinx扩展模块名。它们可以是Sphinx(名为“Sphinx .ext.*”)自带的扩展，也可以是你的自定义扩展。
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']

# 在这里添加任何包含模板的路径，相对于这个目录。
templates_path = ['_templates']

# 源文件名的后缀。
# 可以指定多个后缀作为字符串列表:
#
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# 主 toctree 文档。
master_doc = 'index'

# 关于项目的一般信息。
project = '{{ cookiecutter.project_name }}'
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.full_name }}"
author = "{{ cookiecutter.full_name }}"

# 你正在记录的项目的版本信息，可以作为 | version | 和 | release | 的替代品，也可以在构建文档的其他地方使用。
#
# 短的X.Y版本。
version = {{ cookiecutter.project_slug }}.__version__
# 完整的版本，包括alpha/beta/rc标签。
release = {{ cookiecutter.project_slug }}.__version__

# 用于Sphinx自动生成内容的语言。有关支持的语言列表，请参阅文档。
#
# 如果您通过gettext目录进行内容翻译，也可以使用这种方法。通常在这些情况下，您可以从命令行设置“language”。
language = None

# 相对于源目录，匹配在查找源文件时要忽略的文件和目录的模式列表。
# 该模式也会影响到 html_static_path 和 html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# 要使用的 pygments 样式的名称(语法高亮显示)。
pygments_style = 'sphinx'

# 如果 “todo” 和 “todoList” 为真，那么它们就会产生产出，否则它们什么都不会产生。
todo_include_todos = False


# -- HTML 输出选项 -------------------------------------------

# HTML和HTML帮助页面使用的主题。有关内置主题的列表，请参阅文档。
#
html_theme = 'shaphinx'

# 主题选项是特定于主题的，并进一步自定义主题的外观和感觉。有关每个主题可用选项的列表，请参阅文档。
#
# html_theme_options = {}

# 在这里添加与此目录相关的任何包含自定义静态文件(如样式表)的路径。
# 它们被复制在内置静态文件之后，所以一个名为“default.css”的文件。将覆盖内置的"default.css"。
html_static_path = ['_static']


# -- HTMLHelp 输出选项 ---------------------------------------

# HTML帮助生成器的输出文件基名。
htmlhelp_basename = '{{ cookiecutter.project_slug }}doc'


# --LaTeX 输出选项 ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# 将文档树分组到 LaTeX 文件中。元组列表
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, '{{ cookiecutter.project_slug }}.tex',
     '{{ cookiecutter.project_name }} 文档',
     '{{ cookiecutter.full_name }}', 'manual'),
]


# -- manual 页面输出的选项 ------------------------------------

# 每个手册页一个条目。元组列表
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, '{{ cookiecutter.project_slug }}',
     '{{ cookiecutter.project_name }} 文档',
     [author], 1)
]


# -- Texinfo 输出选项 ----------------------------------------

# 将文档树分组到Texinfo 文件中。元组列表
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, '{{ cookiecutter.project_slug }}',
     '{{ cookiecutter.project_name }} 文档',
     author,
     '{{ cookiecutter.project_slug }}',
     '一行项目描述。',
     '其他项'),
]



