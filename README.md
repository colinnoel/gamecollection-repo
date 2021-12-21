# Game Collection Project Summary

The primary goal of this project is to:

  1. Pull current and relatively accurate market prices of physical media video games 
  2. Summarize and assign these market prices to a given game collection dataset
  3. Analyze price fluctuations and trends over time
  
The primary use case of this project is for someone who is:

  1. Looking to easily estimate the value of their entire collection on any given date
  2. Tired of manually logging the value of their collection
  3. Interested in making buying/selling decisions based on pricing trends and analysis


Context:
  
  I have been buying, selling, and collecting physical media video games for years as a hobby. Similar to how people collect records, 
  there is something quite nostalgic to owning a physical media release that holds value, both emotional and financial, over time.
  
  Once a collectible has been phased out of print, the original retail price fails to capture the second-hand market value.
  Hence, there are websites and projects that capture an estimated market value based on averaging recently sold listing prices on marketplaces such as eBay, Amazon, and others.
  
  One of these websites, PriceCharting.com, will serve as the source for our live market data that we can then assign to the individual items in our provided collection dataset.
  
  There are a number of shortfalls in the project for relying on an external website for live market data:
  
    1. Market prices of games with low transaction volume will have less accurate pricing.
    2. PriceCharting.com only pulls from a limited amount of marketplaces and their public transactions: only eBay, Gamestop, and Amazon.
    3. We are relying on PriceCharting.com's backend to accurately and consistently capture transactions from marketplaces.
    4. We are assuming PriceCharting.com's system for calculating the market price of games is the best. We don't know how they are averaging recent and historical transactions into one number.
  
    
