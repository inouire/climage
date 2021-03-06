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

def getValue2(c,a):
	"""Return threshold value from color + alpha"""
	color =c
	if(a<=5):
		color=255

	if color < 50:
		return 0
	elif color < 115:
		return 1
	elif color < 155:
		return 2
	elif color < 195:
		return 3
	elif color < 235:
		return 4
	else:
		return 5

def getValue1(color):
	"""Return threshold value from color"""
	if color < 50:
		return 0
	elif color < 115:
		return 1
	elif color < 155:
		return 2
	elif color < 195:
		return 3
	elif color < 235:
		return 4
	else:
		return 5

def getCode4(r,g,b,a):  
	"""Return color code from rgb & alpha"""
	return 16+(36*getValue2(r, a)+6*getValue2(g,a)+getValue2(b,a))

def getCode3(r,g,b):  
	"""Return color code from rgb"""
	return 16+(36*getValue1(r)+6*getValue1(g)+getValue1(b))

def missingLibMessage():
	print "python-imaging libray not found.\nInstall it on your system and launch climage again."
	return
