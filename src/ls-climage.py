# Copyright 2010-2012 Edouard Garnier de Labareyre
#
# This file is part of climage.
#
# Climage is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#  
# Climage is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with Climage.  If not, see <http://www.gnu.org/licenses/>.

from colors import *
import sys
import os
import pickle
try:
	from PIL import Image
except ImportError:
	missingLibMessage()
	sys.exit(2)

	
def completeWithSpaces(s,n):
	if len(s)==n:
		return s
	elif len(s)<n:
		for k in range(n-len(s)):
			s+=" "
		return s
	elif len(s)>n:
		return s[0:n]

def createSeparator(w):
	s=""
	for k in range(w):
		s+="_"
	return s
	
def createNamesString(cli,w,ppl,id):
	"""create a string with the list of climages, knowing the terminal width"""
	s=""
	k=id
	for cl in cli:
		s+=completeWithSpaces("["+str(k)+"] "+cl[0],w//ppl)
		k+=1
	return s
	
def createClimage(pic,w,h):
	"""create a climage in memory"""
	
	#opening picture
	try:
		im=Image.open(pic)
	except IOError:
		return (0,0)
		
	S = im.size
	i_W = S[0] #image width
	i_H = S[1] #image height
	t_W = w
	step = (2*i_W//t_W)
	if step*t_W < i_W*2:
		step+=1
	p_H = i_H//step
	#load image
	pix = im.load()

	#is there an alpha channel?
	try:
		if len(pix[0,0])==4:
			alpha=1
		else:
			alpha=0
	except TypeError:
		return (0,0)
	
	#the lines of the picture
	lines=[]
	a=""
	empty=""
	for l in range(t_W//2):
		tmp = 2*l*step//2
		try:
			P=pix[tmp,0]
			empty+="  "
		except IndexError:
			lll=0
		
	for k in range(h):
		if k >= p_H:
			lines.append(empty)
		else:
			for l in range(t_W//2):
				tmp = 2*l*step//2
				try:
					P=pix[tmp,k*step]
					if alpha==1:
						a+="\x1b[48;5;"+str(getCode4(P[0],P[1],P[2],P[3]))+"m  "
					else:
						a+="\x1b[48;5;"+str(getCode3(P[0],P[1],P[2]))+"m  "
				except IndexError:
					lll=0
			a+="\x1b[0;m"
			lines.append(a)
			a=""
	
	#compute real height (if less than max one)
	if p_H < h:
		height=p_H
	else:
		height=h
		
	return (pic,lines,height)
	
	
if len(sys.argv)<3:
	print "Some arguments are missing. Expected: pic per line, terminal width"
	exit(1)
	
#get number of pic per line
ppl = int(sys.argv[1])

#get terminal width
t_W = int(sys.argv[2])

#compute width & height per image
wi = t_W//ppl
hi = 3*wi//8

#list files in this directory
files_list=os.listdir(".")

#create list of tupple (name + climages)
climage_list=[]
for pic in files_list:
	try:
		tmp=createClimage(pic,wi,hi)
		if len(tmp)==3:
			print "=",
			sys.stdout.flush()
			climage_list.append(tmp)
	except IOError:
		lll=0#ie do nothing
if len(climage_list)!=0:
	print ">"
else:
	print "climage can't display anything in this folder."
	sys.exit(1)
	
#create a sub-tupples list
n=len(climage_list)//ppl
r=len(climage_list)%ppl

climage_sublist=[]
for i in range(n):
	climage_sublist.append(climage_list[ppl*i:ppl*i+ppl])

if r!=0:
	climage_sublist.append(climage_list[ppl*n:])


#concatenate climages
#print createSeparator(t_W)
id=1
for L in climage_sublist:
	max=0
	for cl in L:
		if cl[2]>max:
			max=cl[2]
		
	for k in range(max):
		a=""
		for cl in L:
			try:
				a+=cl[1][k]
			except IndexError:
				lll=0

		print a
	print createNamesString(L,t_W,ppl,id)
	print createSeparator(t_W)
	id+=ppl


#memorize id
k=1

P=[]
for cl in climage_list:
	P.append((k,cl[0]))
	#logfile.write(str(k)+" "+cl[0]+"\n")
	k+=1

logfile = open('/tmp/climage_mem_id', 'w')
pickle.dump(P,logfile)
logfile.close()

