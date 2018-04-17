# python-video-to-thumbnail

This is a simple python snippet to convert a specified video to a collection of thumbnails.

*Additional information on code and original idea located here:
https://1mhassan.wordpress.com/2017/05/08/using-ffmpeg-to-create-video-thumbnails-in-python/

The following packages are needed for use of code snippet in addition to Python:

- FFMPEG
- FFMPY

To install FFMPEG, Homebrew was used on a Mac with the simple command:

    brew install ffmpeg

Additionally, the source code can be directly downloaded from https://ffmpeg.org/download.html.

Installation of the python package FFMPY can be completed by using:

    pip install ffmpy

Once both of these packages are succesfully installed, the code can be copied or downloaded to be used.

There are two flags currently implemented as arguements for the code.

    -I :a flag for the input file. (Required for code to run)
    -V :a simple version flag to describe the version of the file.

To use this code simply run:

    python thumbnail.py -I 'path/to/file'

The thumbnails will be generated in a folder in the same directory as the python script. The folder will be titled whatever the video's title is + _frames. 




