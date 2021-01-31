..
   Note: Items in this toctree form the top-level navigation. See `api.rst` for the `autosummary` directive, and for why `api.rst` isn't called directly.

.. toctree::
   :hidden:

   Home page <self>
   Jupyter tutorials <tutorials>
   API reference <_autosummary/mytoolbox>

Welcome to Sphinx-Autosummary-Recursion documentation
=====================================================

This Sphinx-built HTML doc set uses the new ``:recursive:`` option available in ``sphinx.ext.autosummary``. From version 3.1. Sphinx can now iterate 
over a Python package automatically, so you no longer have to hard code all your module names, or integrate a 3rd party extension to provide this functionality.

You can:

* Point Sphinx at the top of a Python source code tree, and have it automatically find all the modules in the package, however deeply nested.
* For each module, list the attributes, functions, classes and exceptions in that module in summary tables.
* For each entry in a summary table, create a hyperlink to a new page displaying the extracted docstrings for that attribute, function, class or exception.
* For each class, document (my choice of) inheritence, public members, inherited members, and special members such as ``__call__``. Other choices are available.

It's also relatively easy to integrate Jupyter Notebooks with Sphinx, to provide tutorial-style material.

To see how to configure Sphinx to do all this, start with the `Github repo README <https://github.com/JamesALeedham/Sphinx-Autosummary-Recursion>`_.
