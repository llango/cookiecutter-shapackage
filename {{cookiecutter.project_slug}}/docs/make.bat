@ECHO OFF

pushd %~dp0

REM Sphinx文档的命令文件

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=python -msphinx
)
set SOURCEDIR=.
set BUILDDIR=_build
set SPHINXPROJ={{ cookiecutter.project_slug }}

if "%1" == "" goto help

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.Sphinx模块没有找到，确保你安装了sphinx。
	echo.然后将SPHINXBUILD环境变量设置为指向“sphinx-build”可执行文件的完整路径。 
	echo.此外你可以将Sphinx目录添加到PATH中。
	echo.
	echo.如果你没有安装Sphinx，你可以从
	echo.http://sphinx-doc.org/
	echo.获取。
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%

:end
popd
