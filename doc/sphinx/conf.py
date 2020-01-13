# -*- coding: utf-8 -*-
# 字段具体含义请参考 https://www.sphinx.org.cn/index.html

import sys
import os
import datetime
# pip install sphinxcontrib-rtd-theme
import sphinx_rtd_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))

# pip install sphinxcontrib-bibtex
import bibstyle

# 生成配置
# ------------------------------------------------

# 设置 sphinx 编译的最小版本
#needs_sphinx = '1.0'

# sphinx 使用模块的字符串列表。可以是sphinx(名为 sphinx.ext.*)或自定义扩展
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinxcontrib.bibtex',
    ]

# 模板路径
templates_path = ['_templates']

# sphinx 的源文件后缀名，可以使用字符串列表来指定多个后缀
source_suffix = ['.rst']

# 源文件编码
#source_encoding = 'utf-8-sig'

# 目录树的根节点
master_doc = 'index'

# 项目生成信息
# --------------------------------------------------

# 项目名称
project = u'RTKLib 学习记录'

# 当前文档的标题
title = u'RTKLib 学习记录'

# 作者
author = u'zhaokai'

# 版权

# 版本
version = u'1.0.0'
release = version

# 文档的语言
language = 'zh-CN'

# 查找源文件时排除的目录
exclude_patterns = [
    ]

# 突出显示源代码的样式名称
pygments_style = 'sphinx'

# 突出显示的源代码的默认语言.
highlight_language = 'none'

# 代表事项
todo_include_todos = True

# HTML 输出选项
# -------------------------------------------

# HTML 输出样式
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# html 图标
# html_logo = 'image/navigation_96px_1201170_easyicon.net.png'

# 显示源码在右上角
html_show_sourcelink = True

latex_engine = 'xelatex'

latex_elements = {
    'preamble': r'''    
            \hypersetup{unicode=true}    
            \usepackage{CJKutf8}    
            \DeclareUnicodeCharacter{00A0}{\nobreakspace}    
            \DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}    
            \DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}    
            \DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}    
            \DeclareUnicodeCharacter{2713}{x}    
            \DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}    
            \DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}    
            \DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}    
            \DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}    
            \DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}    
            \begin{CJK}{UTF8}{gbsn}    
            \AtEndDocument{\end{CJK}}    ''',
}