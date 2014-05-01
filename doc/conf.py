# coding: utf8

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'structures'
copyright = u'2012, Alexander Zelenyak'

# The short X.Y version.
version = '3.0'
# The full version, including alpha/beta/rc tags.
release = '3.0'

exclude_trees = ['_build']

pygments_style = 'sphinx'

html_theme = 'sphinxdoc'
html_static_path = ['_static']
htmlhelp_basename = 'structuresdoc'
