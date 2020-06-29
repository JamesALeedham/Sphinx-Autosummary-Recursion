Welcome to Sphinx-Autosummary-Recursion
=======================================

This package demonstrates automatic package detection using the new ``:recursive:`` option
in ``sphinx.ext.autosummary`` version 3.1. See the `code on Github <https://github.com/JamesALeedham/Sphinx-Autosummary-Recursion>`_.

The goal is to:

* Point Sphinx at the top of the source code tree, and have it automatically find all the modules in the package, however deeply nested.
* For each module, list the attributes, functions, classes and exceptions in that module in summary tables.
* For each entry in a summary table, create a hyperlink to a new page containing the API documentation for that attribute, function, class or exception.
* For each class, document (my choice of) inheritence, public members, inherited members, and special members such as `__call__`.

.. autosummary::
   :toctree: _autosummary
   :caption: API Reference
   :template: custom-module-template.rst
   :recursive:

   mytoolbox
