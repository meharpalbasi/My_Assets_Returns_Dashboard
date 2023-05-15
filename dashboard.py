# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 23:17:22 2022

@author: mehar
"""

import streamlit as st
import yfinance as yf
import pandas as pd



st.title('Finance Dashboard')

tickers = ('LGEN', 'MNG', 'MSFT', 'AFRM' , 'RIOT', 'AMD', 'CRWD', 'AAPL', 'GOOGL', 'RIO', 'GSK',  'BTC-USD', 'ETH-USD', 'LINK-USD', 'AVAX-USD' )

dropdown = st.multiselect('Pick your assets',
                          tickers)

start = st.date_input('Start', value = pd.to_datetime('2015-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))

#the date part of the dropdown 

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret




if len(dropdown) > 0:
    #df = yf.download(dropdown,start,end)['Adj Close']
    df = relativeret(yf.download(dropdown,start,end) ['Adj Close'])
    
    
   
    
   
    st.line_chart(df)
    

st.write('App built by [Meharpal Basi] (https://www.meharpalbasi.com/) ')
