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

def printImage(f):
	#open image
	try:
		im = Image.open(f)
	except IOError:
		print "Error: "+f+" is not recognized as an image file."
		sys.exit(1)
		
	S = im.size
	i_W = S[0] #image width
	i_H = S[1] #image height

	t_W = 80 #terminal width
	if(len(sys.argv)>2):
		t_W = int(sys.argv[2])

	step = (2*i_W//t_W)
	if step*t_W < i_W*2:
		step+=1
	p_H = i_H//step

	#load image
	pix = im.load()
	#is there an alpha channel?
	alpha=0
	try:
		if len(pix[0,0])==4:
			alpha=1
		else:
			alpha=0
	except TypeError:
		print "Error: "+sys.argv[1]+" is not recognized as an image file."
		sys.exit(1)
	a=""
	for k in range(p_H):
		for l in range(t_W//2):
			tmp = 2*l*step//2
			if tmp < i_W:
				P=pix[tmp,k*step]
				if alpha==1:
					a+="\x1b[48;5;"+str(getCode4(P[0],P[1],P[2],P[3]))+"m  "
				else:
					a+="\x1b[48;5;"+str(getCode3(P[0],P[1],P[2]))+"m  "
		
		a+="\x1b[0;m\n"

	print a
	
	print f

#print a climage from id

#number of arguments doesn't match
if len(sys.argv)!= 3:
	sys.exit(2)

#test if id is an integer
try:
	id=int(sys.argv[1])
except ValueError:
	sys.exit(2)
	
#get information about previously opened files
try:
	logfile = open('/tmp/climage_mem_id', 'r')
	P = pickle.load(logfile)
except IOError:
	print "You should launch climage on a directory before calling a picture with its id"

#print picture associated to the id
for C in P:
	if C[0]==id:
		printImage(C[1])
		sys.exit(0)
		
sys.exit(2)
    



