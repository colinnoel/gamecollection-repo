# Game Collection Project Summary

<h3>The Problem:</h3>
<p> Do you have a cardboard box of old video games in your garage?<br>
Do you see articles online about someone finding a $10,000 game in their attic? Do you ever wonder if that could be you?<br>
Well, unfortunately, that's quite unlikely. But there is definitely a chance that your collection is worth something.</p>

<p>Now how would you actually go about pricing your collection? <br>
One way to go about it is searching eBay or Amazon for each game, and looking at recently sold listings.<br>
That could work, but you would spend alot of time on this.</p>

**Even if you know where to look, researching and pricing each video game in your collection is tedious and tiresome.**

<h3>Goal:</h3>

1. Pull current and relatively accurate market prices of physical media video games 
2. Summarize and assign these market prices to a given game collection dataset
3. Analyze price fluctuations and trends over time
  
<h3>Primary Use Case:</h3>

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
      4. We are assuming PriceCharting.com's system for calculating the market price based on recent and historical transactions is the best. 
           
  

