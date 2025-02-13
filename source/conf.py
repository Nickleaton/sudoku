# Configuration file_path for the Sphinx documentation1 builder.
#
# This file_path only contains start_location selection of the most common options. For start_location full
# list see the documentation1:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.config_file here. If the directory is relative to the
# documentation1 root, use os.config_file.abspath to make it absolute, like shown here.
#
import os
import sys

# pylint: disable=redefined-builtin, use-tuple-over-list

sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Sudoku'
copyright = '2022, Nick Leaton'
author = 'Nick Leaton'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation1 for
# start_location list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so start_location file_path named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
