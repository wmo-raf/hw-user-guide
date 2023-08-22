# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Hazards Watch User Guide'
copyright = '2023, WMO RAF'
author = 'Erick Otenyo'
release = '1.0.0'

# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name="Hazards Watch User Guide",
    github_url="https://github.com/wmo-raf/hw-user-guide/",
    footer_links=",".join([
        "Demo|http://20.56.94.119",
    ]),
    logo="images/logo.png",
    logo_alt="Hazards Watch",
    logo_height=60,
    logo_width=60,
)

html_show_copyright = True
html_last_updated_fmt = "%b %d, %Y"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "sphinx_wagtail_theme",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_wagtail_theme'
html_static_path = ['_static']

html_css_files = ["css/custom.css"]

# The suffix of source filenames.
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = "index"


def setup(app):
    app.add_js_file("js/banner.js")
