import numpy as np
import pandas as pd

df = pd.read_csv(r"YourFileHere.csv")

def retailer_affinity(df, focus__brand):
	""" returns the strongest affinity to other brands"""
	summary=df.groupby(['Retailer', 'Parent Brand']).agg({'Item Units':'sum'})
	##level=0 is required because it has a hierarchical index (MultiIndex). level=0 is the retailers.
	affinity_pcts=summary.groupby(level=0).apply(lambda x: 100*x/float(x.sum()))
	print (affinity_pcts)
	##converts the df to a dict with keys=retailer,brand and values=percentage
	##dictionary makes it possible to loop through and find the focus_brand at each retailer and compare the percentage
	##the loop returns the retailer that had the highest percentage of sales of the focus_brand
	scores = affinity_pcts.to_dict()
	maxaffinity = 0
	topretailer = None
	
	for (store, brand), pct in scores['Item Units'].items():
		if brand == focus__brand:
			if pct > maxaffinity:
				topretailer = store
				maxaffinity = pct
	
	return topretailer

def count_hhs(df, brand=None, retailer=None, start_date=None, end_date=None):
	""" returns the number of households"""
	#each if statement filters by the optional arguments fed into the function and modifies the df
	if brand: 
		df = df[df['Parent Brand'] == brand]
	if retailer:
		df = df[df['Retailer'] == retailer]
	if start_date:
		df = df[df['Date'] >= start_date]
	if end_date:
		df = df[df['Date'] <= end_date]	
		#creates a pivot table and returns length of userid's. (look at docs for pivot table )
	table=pd.pivot_table(df,index=["User ID"])
	return len(table)
		
def top_buying_brand(df):
	"""identifies brand with top buying rate measured as $ spent/HH"""
	df['Dollars']=df['Item Dollars'].str[1:].astype(int) #converts $4 to 4
	df['Total'] =df['Item Units']*df['Dollars'] #multiplies item units times dollars to get a subtotal
	
	Brands=['5 Hour Energy', 'Rockstar', 'Red Bull', 'Monster']
	topspending = 0
	topbrand = None 
	for brand in Brands:
		spending = pd.pivot_table(df[df['Parent Brand'] == brand], index=['User ID'], aggfunc={"Total":np.sum}).mean()['Total']
		if spending > topspending:
			topbrand = brand
			topspending = spending
	
	return topbrand

	
	

		
##Test case for retailer_affinity:
print ("Topretailer for {0} is {1} " .format('Rockstar', retailer_affinity(df, 'Rockstar')))
##Test case for def count_hhs:
print ('The number of households is: {!r}.'.format(count_hhs(df, brand='Monster', retailer='Kroger', start_date=None, end_date=None)))	
##Test case for top_buying_brand:
print ('The top brand is: {0}'.format(top_buying_brand(df)))