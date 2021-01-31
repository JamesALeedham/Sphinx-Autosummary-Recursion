# ---
# jupyter:
#   jupytext:
#     cell_markers: '"""'
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
"""
# Introducing Jupyter Notebooks

First, set up the environment:
"""

# %%
import matplotlib
import matplotlib.pyplot as pl
import numpy as np

try:
    from IPython import get_ipython
    get_ipython().run_line_magic('matplotlib', 'inline')
except AttributeError:
    print('Magic function can only be used in IPython environment')
    matplotlib.use('Agg')

pl.rcParams["figure.figsize"] = [15, 8]

# %% [markdown]
"""
Then, define a function that creates a pretty graph:
"""

# %%
def SineAndCosineWaves():
    # Get a large number of X values for a nice smooth curve. Using Pi as np.sin requires radians...
    x = np.linspace(0, 2 * np.pi, 180)
    # Convert radians to degrees to make for a meaningful X axis (1 radian = 57.29* degrees)
    xdeg = 57.29577951308232 * np.array(x)
    # Calculate the sine of each value of X
    y = np.sin(x)
    # Calculate the cosine of each value of X
    z = np.cos(x)
    # Plot the sine wave in blue, using degrees rather than radians on the X axis
    pl.plot(xdeg, y, color='blue', label='Sine wave')
    # Plot the cos wave in green, using degrees rather than radians on the X axis
    pl.plot(xdeg, z, color='green', label='Cosine wave')
    pl.xlabel("Degrees")
    # More sensible X axis values
    pl.xticks(np.arange(0, 361, 45))
    pl.legend()
    pl.show()

# %% [markdown]
"""
Finally, call that function to display the graph:
"""

# %%
SineAndCosineWaves()
