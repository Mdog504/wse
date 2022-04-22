# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Worst Server Ever Docs'
copyright = '2022 - Present, Worst Server Ever'
author = 'JaroolFan69'

release = '1.0'
version = '0.9.1a'

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

html_static_path = ['_static']
html_title = 'Worst Server Ever Documentation'
html_short_title = 'WSE Docs'
html_favicon = 'WSE-icon.ico'
html_theme = 'sphinx_rtd_theme'
html_logo = 'WSE-banner.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
