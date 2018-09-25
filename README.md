## a few statistics of IEEE ICIP 2018 https://2018.ieeeicip.org/default.asp

The number of accepted papers w.r.t. paper IDs

![Link Text](https://github.com/srtmsrtm/icip18_stats/blob/master/hist_icip18.png)

A wordcloud of paper titles

![Link Text](https://github.com/srtmsrtm/icip18_stats/blob/master/wordcloud_icip18.png)

## Installation

### Dockerfile
 
 $ docker build --file Dockerfile --tag icip18_stats:0.1 .

### Start container

 $ docker run -it icip18_stats:0.1
 
### Run

 $ cd /root/src
 
 $ python gen_hist.py

 $ python gen_wordcloud.py


