# -*- coding:utf-8 -*-

"""
generate a histogram of accepted papers w.r.t. paper IDs
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg")
import os
import codecs
import pandas as pd

url    = "https://2018.ieeeicip.org/Papers/AcceptedPapers.asp"
tables = pd.read_html(url)

ids_accepted = []
for i in range(len(tables[0][0])):
    ids_accepted.append(int(tables[0][0][i]))
bins      = np.linspace(min(ids_accepted), max(ids_accepted), 10) # min/max id are both unknown...
histogram = np.histogram(np.array(ids_accepted), bins)[0]

plt.hist(np.array(ids_accepted), bins=10, histtype="step")
plt.title("# of accepted papers w.r.t paper IDs")
plt.xlabel("Paper ID")
plt.ylabel("# of accepted papers")
plt.savefig("hist_icip18.png", dpi=300)

