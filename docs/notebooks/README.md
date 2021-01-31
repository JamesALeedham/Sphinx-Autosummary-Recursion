# Configuring Sphinx to integrate Jupyter Notebooks

See `requirements.txt` for required libraries.

See `conf.py` for Sphinx extensions and settings.

See `tutorials.rst` for placement of the Notebook in a `.. toctree::` directive.

# Running a Notebook interactively

Sphinx *executes* a Notebook when it builds the HTML doc set so it's not possible for users to edit/interact with live code.
Users can still play Jupyter Notebooks interactively by:

1. Cloning the repo and installing required dependencies:

   `pip install -r requirements.txt`

2. Navigating to the `docs/notebooks` directory.
   
4. Running the required Notebook:

   `jupyter-notebook <name-of-notebook>.ipynb`

# Creating a new Notebook

You can either create a Notebook as a regular Python ``.py`` file, or using the proprietary Jupyter ``.ipynb`` format. 

## Creating a new Notebook as a .py file

To collaborate with others when creating Notebooks, it might be easier to create and store ``.py`` files, and only convert 
to ``.ipynb`` when needed (for example, by Sphinx when building HTML documentation).

To do this, insert the following metadata at the top of a ``.py`` file:

    # -*- coding: utf-8 -*-
    # ---
    # jupyter:
    #   jupytext:
    #     cell_markers: '"""'
    #     formats: ipynb,py:percent
    #     text_representation:
    #       extension: .py
    #       format_name: percent
    #       format_version: '1.3'
    #       jupytext_version: 1.3.3
    #   kernelspec:
    #     display_name: Python 3
    #     language: python
    #     name: python3
    # ---

Make sure a text (ie. comment) cell is encapsulated as follows:

    # %% [markdown]
    """
    <your multi-line text goes here>
    """

Make sure a code cell is encapsulated as follows:

    # %%
    # Optional code comment
    def YourCodeGoesHere():
       pass

To test it as a Notebook, make sure Jupytext is installed (`pip install jupytext`) and run:

    jupytext --to notebook <your-new-file>.py

This creates `<your-new-file>.ipynb`. Run `jupyter-notebook <your-new-file>.ipynb` to make sure it formats 
and executes correctly in the IPython environment.

When ready, commit `<your-new-file>.py`. You can delete `<your-new-file>.ipynb`.

## Creating a new Notebook as a regular Notebook

You can run `jupyter-notebook` and press the **New** button to create a Notebook using the Jupyter UI. When ready, save and exit, and 
run the following command to convert `<your-new-file>.ipynb` file to `<your-new-file>.py` (with text cells formatted as multi-line comments):

    jupytext --update-metadata '{"jupytext": {"cell_markers": "\"\"\""}}' --to py:percent <your-new-file>.ipynb

When ready, commit `<your-new-file>.py`. You can delete `<your-new-file>.ipynb`.
