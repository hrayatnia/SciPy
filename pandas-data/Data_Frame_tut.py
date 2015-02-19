import pandas as DF

names=['Human','African elephant','Tarsius','Rat','False killer whale','Horse']
cash_bad=[23000000000,11000000000,310000000,21000000,10500000000,1200000000]
details=['''For average adult
            The average number
             of neocortical
            neurons was 19
             billion in female
    brains and 23 billion
     in male brains.''',
         "","","","",""]
cash_tbl=list(zip(names,cash_bad,details))
cash_tbl=DF.DataFrame(data=cash_tbl,columns=['names',' neuron in Cerebral cortex',"details"])
cash_tbl.to_latex('file/panda/file.tex')
cash_tbl.to_csv('file/panda/file.csv')
cash_tbl.to_html('file/panda/file.html')
cash_tbl.to_excel('file/panda/file.xlsx')