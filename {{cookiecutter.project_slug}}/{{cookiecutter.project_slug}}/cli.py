"""关于 {{cookiecutter.project_slug}} 的控制脚本。"""

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
    """关于 {{cookiecutter.project_slug}} 控制脚本。"""
    click.echo("替换该信息的方式：将你的代码放入 "
               "{{cookiecutter.project_slug}}.cli.main"
               " 之中")
    click.echo("可以在 https://click.palletsprojects.com/ 查看文档。")
    return 0
{%- endif %}

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    """关于 {{cookiecutter.project_slug}} 的控制脚本。"""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("参数: " + str(args._))
    print("替换该信息的方式：将你的代码放入 "
          "{{cookiecutter.project_slug}}.cli.main"
          " 之中")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # 编译指示: 没有覆盖
