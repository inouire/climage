#!/bin/bash
# Copyright 2010-2012 Edouard Garnier de Labareyre
#
# This file is the bootstrap script for climage
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
# along with climage.  If not, see <http://www.gnu.org/licenses/>.


[ -e '/usr/bin/python2' ] && _python='/usr/bin/python2' || _python='/usr/bin/python'
VERSION='0.4'

#help section
if [ $# -ge 0 ]; then
    if [ "$1" = "--help" ]||[ "$1" = "-h" ]||[ "$1" = "help" ]; then
        echo "climage (eyes for your shell) v"$VERSION
        echo "----------------------------------------------------------"
        echo "Usage:"
        echo "    + no argument: list images in the current directory"
        echo "    + 1 argument:"
        echo "        [directory]: list images in the given directory"
        echo "        [file]: display a single image given its path"
        echo "        [id]: display a single image given its id (id can be obtained from a directory listing)"
        echo "----------------------------------------------------------"
        echo "* Image files format can be either png, jpg, tiff, bmp...and more (see Python Imaging documentation)"
        echo "* Files which are not recognized as pictures will be ignored"
        echo "* [id] is the number diplayed next to each picture's name when using climage on a folder."
        echo "   Using an id is a fast and easy way to focus on a peculiar picture."
        exit 0
    fi
fi

#get number of columns in the current terminal
columns=$(tput cols)

#get number of pictures per line by..
pic_per_line=3 #default
source ~/.config/climage &> /dev/null #or from conf file

#get script path
script_path=$(cd -P $(dirname $0); pwd)

#case: "ls" on the current directory
if [ $# -eq 0 ]; then
    folder=$(pwd)
    echo "$folder" > /tmp/climage_mem_path
    $_python $script_path/climage/ls-climage.py $pic_per_line $columns
    exit $?
fi

#case: "cat" on one picture, with path or with id, or 
if [ $# -eq 1 ]; then
    if [ -d "$1" ]; then #"ls" on a directory
        #go to the concerned directory
        if [ $# -ge 1 ]; then
            cd "$1" 2> /dev/null
        fi
        #memorize folder for next execution
        folder=$(pwd)
        echo "$folder" > /tmp/climage_mem_path
        $_python $script_path/climage/ls-climage.py $pic_per_line $columns
        exit $?
    elif [ -f "$1" ]; then #"cat" on one picture from its path
        $_python $script_path/climage/cat-climage.py "$1" $columns
        exit $?
    else #"cat" on one single picture from its id
        if [ -e "/tmp/climage_mem_path" ]; then
            folder=$(cat /tmp/climage_mem_path)
            cd "$folder"
            $_python $script_path/climage/id-climage.py $1 $columns
            exit $?
        fi
        if [ $? -eq 2 ]; then
            echo "$1: File not found."
            exit 1
        fi
    fi
fi

exit 0

