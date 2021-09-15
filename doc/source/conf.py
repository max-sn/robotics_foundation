# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import re
import os
import sys
sys.path.insert(0, os.path.abspath('../../python'))


# -- Project information -----------------------------------------------------

project = 'Robotics Foundation'
copyright = '2021, M.J.W. Snippe'
author = 'M.J.W. Snippe'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinxcontrib.matlab',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

add_module_names = False

autodoc_typehints = "description"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Autodoc extension configuration -----------------------------------------

autodoc_mock_imports = ['numpy']

# -- Mathjax extension configuration -----------------------------------------

mathjax3_config = {'tex': {'macros': {}}}

with open('math_cmds.tex', 'r') as f:
    for line in f:
        macros = re.findall(
            r'\\newcommand{\\(.*?)}(\[(\d)\])?(\[(.*?)\])?{(.+)}', line)
        for macro in macros:
            if len(macro[1]) == 0:
                mathjax3_config['tex']['macros'][macro[0]] = macro[5]
            elif len(macro[3]) == 0:
                mathjax3_config['tex']['macros'][macro[0]] = [macro[5],
                                                              macro[2]]
            else:
                mathjax3_config['tex']['macros'][macro[0]] = [macro[5],
                                                              macro[2],
                                                              macro[4]]

# -- Matlab domain extension configuration -----------------------------------

matlab_src_dir = os.path.abspath('../../matlab')
