# Sphinx-Autosummary-Recursion

This repo contains a Python package demonstrating the new
[automatic package recursion functionality](https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html?highlight=%3Arecursive%3A#directive-autosummary) 
in `sphinx.ext.autosummary` version 3.1 (see the `:recursive:` option towards the bottom of the above link).

The goal of this demo is to:

* Point Sphinx at the top of a source code tree, and have it automatically find all the modules in the package, however deeply nested.
* For each module, list the attributes, functions, classes and exceptions in that module in summary tables.
* For each entry in a summary table, create a hyperlink to a new page containing the documentation for that attribute, function, class or exception.
* For each class, document (my choice of) inheritence, public members, inherited members, and special members such as `__call__`.

The resulting built API documentation is [available to view on ReadTheDocs](https://sphinx-autosummary-recursion.readthedocs.io/en/latest/).

Or you can clone the repo and build and view the API documentation locally:

1) Assuming a Python 3.x environment, install dependencies:

   `pip install -r docs/requirements.txt`
   
2) Change to the `docs` directory:

   `cd docs`

3) Build the documentation:

   `make html`

4) Run a web server:

   `python -m http.server`

5) View documentation locally by opening in a browser:

   http://localhost:8000/_build/html/
