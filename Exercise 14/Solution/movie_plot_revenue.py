#! /bin/python
# Name:        movie_plot_ratings.py
# Author:      Donald Cameron
# Revision:    v1.0
# Description: This program will display a plot of the rating for each
# film in a CSV using Pandas and MatPlotLib
"""
    Movie Rating Plot
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into DataFrame.
dataf = pd.read_csv("C:\Labs\Module 6 Python labs\Exercises\Exercise 14\Starter\movie_revenue.csv")

# Print DataFrame (columns = Rank, Title and Box Office) to STDOUT.
print(dataf.loc[:, ["Rank", "Title", "Box Office"]])

# Plot Horizontal Bar Chart with Film Title and Box Office Revenues in
# Rank order.
dataf.plot(sort_columns="Rank", x="Title", y="Box Office",
           kind="barh", title="Revenue (Millions)")

# Display plot until a button is pressed.
plt.waitforbuttonpress()