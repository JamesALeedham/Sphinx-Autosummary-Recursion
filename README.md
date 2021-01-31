# Sphinx-Autosummary-Recursion

The primary goal of this repo is to demonstrate the new automatic package detection 
facility for Python API documentation available in Sphinx 3.1+. See 
[this StackOverflow answer](https://stackoverflow.com/questions/2701998/sphinx-autodoc-is-not-automatic-enough/62613202#62613202) for context.

A secondary goal is to showcase the integration of Jupyter Notebooks with Sphinx.

The resulting Sphinx-built HTML doc set is [available to view on ReadTheDocs](https://sphinx-autosummary-recursion.readthedocs.io/en/latest/).


## Automatically creating API documentation

From Sphinx 3.1, `sphinx.ext.autosummary` has a `:recursive:` option that iterates over a Python 
package automatically, so you no longer have to hard code all your module names, or integrate a 3rd party 
extension to provide this functionality. Scroll down 
[this Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html?highlight=%3Arecursive%3A#directive-autosummary) 
for more information. 

This repo demonstrates how to:

1. Point Sphinx at the top of a Python source code tree, and have it automatically find all the modules in the package, however deeply nested.

2. For each module, list the attributes, functions, classes and exceptions in that module in summary tables.

3. For each entry in a summary table, create a hyperlink to a new page displaying the extracted docstrings for that attribute, function, class or exception.

4. For each class, document (my choice of) inheritance, public members, inherited members, and special members such as `__call__`. Other choices are available.

For more information, start with `docs/README`.

## Integrating Jupyter Notebooks with Sphinx

Jupyter Notebooks blend live code, text and visualizations. It’s often useful to integrate them alongside API documentation to provide tutorial-style material.

For more information, start with `docs/notebooks/README`.

## Switching between different HTML themes

Since it’s hosted on Readthedocs, the default theme (stylesheet) for the HTML doc set is `sphinx-rtd-theme`. 
There's a small alteration to this theme’s CSS to make the page width slightly wider; see `docs/_static/readthedocs-custom.css`.

Other themes are available; settings to switch over to the popular `pydata-sphinx-theme` are commented out in `docs/conf.py.`

