Tutorials
=========

Jupyter Notebooks can be integrated into Sphinx using the ``nbsphinx`` extension; 
see `conf.py <https://github.com/JamesALeedham/Sphinx-Autosummary-Recursion/blob/master/docs/conf.py>`_.

To prevent having to store proprietary Notebook ``.ipynb`` files in GitHub, I'm using ``jupytext`` to 
convert Notebooks at build time, and storing them as plain ``.py`` files instead; see 
`Makefile <https://github.com/JamesALeedham/Sphinx-Autosummary-Recursion/blob/master/docs/Makefile>`_.

Note that Sphinx `executes` Notebook code and displays the results of that code in HTML form. Users can still `interact` 
with live code by cloning the repo, navigating to the ``docs/notebooks`` directory, and converting the Notebook themselves; see 
`docs/notebooks/README.md <https://github.com/JamesALeedham/Sphinx-Autosummary-Recursion/blob/master/docs/notebooks/README.md>`_.
 

.. toctree::
   :caption: Introductory tutorials
   :maxdepth: 1

   notebooks/intro

.. toctree::
   :caption: Advanced tutorials
   :maxdepth: 1
