# -*- coding: utf-8 -*-
from datetime import datetime
import matplotlib.pyplot as plt, numpy as py, pandas as pd
import fix_yahoo_finance as yf
from pandas import ExcelWriter
import plotly as pt
from plotly.graph_objs import Scatter, Layout
#data.plot(y='Close')
#plt.title(ticker)

start = datetime(2015, 1, 1)
all_data = {ticker: yf.download(ticker,start)
            for ticker in ['0700.HK', '^HSI', '1398.HK']}
print(all_data)

price = pd.DataFrame({ticker: data['Adj Close']
                     for ticker, data in all_data.items()})
volume = pd.DataFrame({ticker: data['Volume']
                      for ticker, data in all_data.items()})


#returns = price.pct_change()
#print(returns.corr())
#print(returns.cov())
#returns.plot()

#file output process
"""
output_file = 'yf.xlsx'
writer = ExcelWriter(output_file)
price.to_excel(writer, 'adj_close')
volume.to_excel(writer, 'volume')
returns.corr().to_excel(writer, 'corr')
returns.cov().to_excel(writer, 'cov')
writer.save()
"""