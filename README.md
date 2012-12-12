climage (eyes for your shell)
=============================

climage is a small python program that allows you to display pictures with 256 colors, in a shell.
You can choose to display a single picture or the whole content of a folder.

## Requirements

climage needs:
* python2
* python-imaging
* bash

## Usage

``` bash
./climage.sh [arg]
```
where [arg] can be [image file] or [folder] or [id]

[image file] is the absolute or relative path to a png/jpg/tiff/bmp... file (see Python Imaging documentation to know all supported formats)
[folder] is the absolute or relative path to a folder
[id] is the number diplayed next to each picture's name when using climage on a folder.
Using an id is a fast and easy way to focus on a peculiar picture. 

Files which are not recognized as pictures will be ignored. 

## Clean setup

Clone climage repository somewhere on your disk
``` bash
git clone https://github.com/inouire/climage.git
```

If needed, make the main script executable
``` bash
chmod +x climage.sh
```

Create an alias for climage script by adding the following line to your ~/.bashrc file
``` bash
alias img='/path/to/climage/climage.sh'
```

Alias 'img' is now available on your system.
Enjoy browsing some pictures from your terminal:
``` bash
img /home/edouard/Images/holydays
img 2
img test_picture.jpeg
```


