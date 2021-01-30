..
   Note: Items in this toctree form the top-level navigation. See `api.rst` for the `autosummary` directive, and for why `api.rst` isn't called directly.

.. toctree::
   :hidden:

   Home page <self>
   Jupyter tutorials <tutorials>
   API reference <_autosummary/mytoolbox>

Welcome to Sphinx-Autosummary-Recursion
=======================================

The primary goal of this repo is to demonstrate the new automatic package detection facility for Python API documentation available in Sphinx 3.1+. 
See the `code on Github <https://github.com/JamesALeedham/Sphinx-Autosummary-Recursion>`_.

A secondary goal is to showcase the integration of Jupyter Notebooks with Sphinx.


Automatically creating API documentation
----------------------------------------

From Sphinx 3.1, ``sphinx.ext.autosummary`` has a ``:recursive:`` option that iterates over a Python package automatically, so you no
longer have to hard code all your module names, or integrate a 3rd party extension to provide this functionality.

This repo demonstrates how to:

* Point Sphinx at the top of a Python source code tree, and have it automatically find all the modules in the package, however deeply nested.
* For each module, list the attributes, functions, classes and exceptions in that module in summary tables.
* For each entry in a summary table, create a hyperlink to a new page displaying the extracted docstrings for that attribute, function, class or exception.
* For each class, document (my choice of) inheritence, public members, inherited members, and special members such as ``__call__``. Other choices are available.


Integrating Jupyter Notebooks with Sphinx
-----------------------------------------

Jupyter Notebooks blend live code, text and visualizations. It's often useful to integrate them alongside API documentation to provide 
tutorial-style material.


Switching between different themes
----------------------------------

Since it's hosted on Readthedocs, the default theme (stylesheet) for the HTML that Sphinx outputs is ``sphinx-rtd-theme``. I've made a 
small alteration to this theme's CSS to make the page width slightly wider; see ``docs/_static/readthedocs-custom.css``.

Other themes are available; to see how to switch over to ``pydata-sphinx-theme``, examine ``conf.py``.
