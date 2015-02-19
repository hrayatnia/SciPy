import pandas as pd
import matplotlib.pyplot as plt
years= range(1880,2013)
pieces=[]
col=['name','sex','births']
for year in years:
	path="names/yob{0}.txt".format(year)
	frame=pd.read_csv(path,names=col)
	frame['year']=year
	pieces.append(frame)
names=pd.concat(pieces,ignore_index=True)
total_births = names.pivot_table('births', rows='year',cols='sex', aggfunc=sum)
plot=total_births.plot(title='Total births by sex and year')
plt.show()
