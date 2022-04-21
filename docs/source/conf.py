# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Worst Server Ever Docs'
copyright = '2022 - Present, Worst Server Ever'
author = 'JaroolFan69'

release = '0.1'
version = '0.8.4b'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_logo = 'https://media.discordapp.net/attachments/877207380625096734/966768887603548180/WSE_3.png'
html_favicon = 'WSE-icon.ico'
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
