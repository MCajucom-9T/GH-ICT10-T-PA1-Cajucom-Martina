# Working with Sets
from pyscript import display, document


Math = {'Casal', 'Aseo', 'Mergal', 'Cajucom'}
Science = {'Aseo', 'Mergal', 'Baylon', 'Cabatingan'}

display(Math | Science, target='one') # | pinagsabay, operator (shorter)>
display(Math & Science, target='both') # intersecting elements in both
display(Math - Science, target='first') 
display(Science - Math, target='second')
display(Math ^  Science, target='onlyone') # all anomalies


