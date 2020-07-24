#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# nrfxlib documentation build configuration file, created by
# sphinx-quickstart on Mon Jun 11 11:28:40 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sys
import os
import os.path as path

if "NRF_BASE" not in os.environ:
    sys.exit("$NRF_BASE environment variable undefined.")
NRF_BASE = os.path.abspath(os.environ["NRF_BASE"])

if "NRF_OUTPUT" not in os.environ:
    sys.exit("$NRF_OUTPUT environment variable undefined.")
NRF_OUTPUT = os.path.abspath(os.environ["NRF_OUTPUT"])

if "NRF_RST_SRC" not in os.environ:
    sys.exit("$NRF_RST_SRC environment variable undefined.")
NRF_RST_SRC = os.path.abspath(os.environ["NRF_RST_SRC"])

if "NRFXLIB_BUILD" not in os.environ:
    sys.exit("$NRFXLIB_BUILD environment variable undefined.")
NRFXLIB_BUILD = os.path.abspath(os.environ["NRFXLIB_BUILD"])

if "NRFXLIB_OUTPUT" not in os.environ:
    sys.exit("$NRFXLIB_OUTPUT environment variable undefined.")
NRFXLIB_OUTPUT = os.path.abspath(os.environ["NRFXLIB_OUTPUT"])

if "NRFXLIB_RST_SRC" not in os.environ:
    sys.exit("$NRFXLIB_RST_SRC environment variable undefined.")
NRFXLIB_RST_SRC = os.path.abspath(os.environ["NRFXLIB_RST_SRC"])

if "KCONFIG_OUTPUT" not in os.environ:
    sys.exit("$KCONFIG_OUTPUT environment variable undefined.")
KCONFIG_OUTPUT = os.path.abspath(os.environ["KCONFIG_OUTPUT"])

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Let Sphinx find our extensions.
sys.path.append(os.path.join(NRF_BASE, 'scripts', 'sphinx_extensions'))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'breathe',
    'sphinx.ext.ifconfig',
    'sphinxcontrib.mscgen',
    'inventory_builder',
]

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['../_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'README'

# General information about the project.
project = 'nrfxlib'
copyright = '2019-2020, Nordic Semiconductor'
author = 'Nordic Semiconductor'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.3.99'
# The full version, including alpha/beta/rc tags.
release = '1.3.99'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'nrfxlib'
html_theme_path = ['{}/doc/themes'.format(NRF_BASE)]
html_favicon = '{}/doc/static/images/favicon.ico'.format(NRF_BASE)

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['{}/doc/static'.format(NRF_BASE)]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = True

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink =

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, license is shown in the HTML footer. Default is True.
html_show_license = True

# Link the Kconfig docs with Intersphinx so that references to Kconfig symbols
# (via :option:`CONFIG_FOO`) turn into links
intersphinx_mapping = {
    'kconfig': (
        path.relpath(KCONFIG_OUTPUT, NRFXLIB_OUTPUT),
        path.join(path.relpath(KCONFIG_OUTPUT, NRFXLIB_RST_SRC),
                  'objects.inv')),
}

# Allow linking to nrf documentation if available
if path.isfile(path.join(NRF_OUTPUT, 'objects.inv')):
    intersphinx_mapping['nrf'] = (
        path.relpath(NRF_OUTPUT, NRFXLIB_OUTPUT),
        path.join(path.relpath(NRF_OUTPUT, NRFXLIB_RST_SRC), 'objects.inv'),
    )

breathe_projects = {
    "nrfxlib": "{}/doxygen/xml".format(NRFXLIB_BUILD),
}
breathe_default_project = "nrfxlib"

# Qualifiers to a function are causing Sphinx/Breathe to warn about
# Error when parsing function declaration and more.  This is a list
# of strings that the parser additionally should accept as
# attributes.
cpp_id_attributes = ['__syscall', '__syscall_inline', '__deprecated',
    '__may_alias', '__used', '__unused', '__weak',
    '__DEPRECATED_MACRO', 'FUNC_NORETURN' ]

rst_epilog = """
.. include:: /doc/links.txt
.. include:: /doc/shortcuts.txt
"""


def setup(app):
    app.add_stylesheet("css/common.css")
    app.add_stylesheet("css/nrfxlib.css")
    app.add_js_file("js/ncs.js")
