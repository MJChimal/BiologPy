#! /usr/bin/python

__author__ = 'M. Chimal & Pauley'

"""
This script drops duplicate sequence records in a fasta file, keeping only unique records. 
Uses Biopy modules 
"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def drop_duplicates_fasta(f_fasta,unique=False,separator='&'):
	"""
	Drops duplicate sequence records in a fasta file, keeping only unique records
	Parametes
	---------
	f_fasta : str
		fasta file name
	unique  : bool
		True  := drop duplicate sequence records
		False := creates unique ids for all records
	separator: str
		if user sets "unique" argument to True, it will add an & + index (by default) to all records. This makes every
		record unique

	Output
	------
	fasta file  
	"""
	if unique == False:
		d_seq = {record.id:record for record in SeqIO.parse(f_fasta,'fasta')}
		pass
	elif unique == True:
		d_seq  ={'%s%s%i'%(record.id.strip(),separator,i):record for i,record in enumerate(SeqIO.parse(f_fasta,'fasta'))}
		pass 
	SeqIO.write([SeqRecord(record.seq ,id=record.id,name=record.name,description=record.description) for key,record in d_seq.items()],'%s_clean'%(f_fasta),'fasta')
	print "It's done"
	return 1	


