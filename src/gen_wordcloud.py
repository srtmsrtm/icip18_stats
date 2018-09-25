# -*- coding:utf-8 -*-

"""
generate a tag cloud from accepted paper titles of ICIP18
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg")
import os
import codecs
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import pandas as pd

url      = "https://2018.ieeeicip.org/Papers/AcceptedPapers.asp"
tables   = pd.read_html(url)
txt_path = "titles_icip18.txt"
f = codecs.open(txt_path, "w", "utf-8")
for i in range(len(tables[0][0])):
    #print("{}, {}".format(tables[0][0][i], tables[0][1][i]))
    #line = "{},{}\n".format(tables[0][0][i], tables[0][1][i])
    line = "{}\n".format(tables[0][1][i])
    f.write(line)
f.close()

"""
# raw frequency
word_dict = {}
for i in range(len(tables[0][0])):
    es = tables[0][1][i].split(" ")
    for e in es:
        if not e in word_dict:
            word_dict[e] = 0
        word_dict[e] += 1
for k,v in sorted(word_dict.items(), key=lambda x:x[1], reverse=True):
    print("{} {}".format(k,v))
"""

# Read the whole text.
text = open(txt_path).read()
# Set stopwords
stopwords = set(STOPWORDS)
stopwords.add("FOR")
stopwords.add("OF")
stopwords.add("AND")
stopwords.add("A")
stopwords.add("IN")
stopwords.add("USING")
stopwords.add("WITH")
stopwords.add("BASED")
stopwords.add("ON")
stopwords.add("FROM")
stopwords.add("THE")
stopwords.add("VIA")
stopwords.add("TO")
stopwords.add("BY")
stopwords.add("AN")
# Plot
wc = WordCloud(background_color="white", width=1600, height=900, max_words=1000, stopwords=stopwords, max_font_size=200, min_font_size=20, random_state=42)
#wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring, stopwords=stopwords, max_font_size=40, random_state=42)
wc.generate(text)
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
#plt.show()
plt.savefig("wordcloud_icip18.png", dpi=300)

