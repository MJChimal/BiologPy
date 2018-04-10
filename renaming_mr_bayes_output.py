#! /usr/bin/python
__author__ = 'M. Chimal'

"""
Instituto de Ciencias Nucleares, UNAM
Manuel Chimal 
mjchimal@gmail.com
"""

"""

This code subtitutes branch tip names  of a Mr. Bayes output ( .nex.con.tre format ) for a list of names in a csv file
"""

# ============================ #
# Modules

from pandas import read_csv, Series
import subprocess
from shutil import copyfile
import os

# ============================ #

def renaming_mr_bayes_output(f_csv_index,f_tree,new_names='original',id='id'):
	"""
	Parameters
	----------
	f_csv_index : str 
		CSV file name with list of names should have two columns: 1) new_names , 2) identifier given by Mr. Bayes output 
	f_tree      : str
		.nex.con.tre output file name
	new_names   : str
		column name that contains the new names in CSV file 1) 
	id          : str
		column name that contains the Mr. Bayes output names 2)
	"""
	copyfile(f_tree, 'original_%s'%f_tree)
	df = read_csv(f_csv_index,index_col='Unnamed: 0')
	df[new_names] = Series(['\/'.join(row) for row in df[new_names].str.split('/').tolist()],index=range(1,len(df[new_names])+1))
	d_index = df.to_dict()
	for i in range(len(df[new_names]),0,-1):
		p = subprocess.call(["sed -i -e 's/%s/%s/g' %s"%(d_index[id][i],d_index[new_names][i],f_tree)],shell=True)
		if p != 0:
			print 'ERROR Substitution: %s, %s'%(stdout,stderr)
	print "It's done"
	return 1
