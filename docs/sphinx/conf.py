# Configuration file for the Sphinx documentation builder.

import os
import sys
# Add project root to path so modules can be imported
sys.path.insert(0, os.path.abspath(".."))

project = "Pydoll"
author = "Your Name"
release = "1.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode"
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
