# Sphinx-Autosummary-Recursion

This repo contains a Python package demonstrating the new automatic package recursion facility in `sphinx.ext.autosummary` version 3.1.

Assuming a Python 3.x environment, to compile and view the API documentation locally:

1) Install dependencies:

   `pip install -U sphinx==3.1.1 sphinx_rtd_theme sphinx_autodoc_typehints`
   
2) Change to the `docs` directory:

   `cd docs`

3) Compile the documentation:

   `make html`

4) Run a web server:

   `python -m http.server`

5) Check documentation locally by opening in a browser:

   http://localhost:8000/build/html/
