# python-video-to-thumbnail

This is a simple python snippet to convert a specified video to a collection of thumbnails.


The following packages are needed for use of code snippet in addition to Python:

- FFMPEG
- FFMPY

To install FFMPEG, Homebrew was used on a Mac with the simple command:

    brew install ffmpeg

Additionally, the source code can be directly downloaded from https://ffmpeg.org/download.html.

Installation of the python package FFMPY can be completed by using:

    pip install ffmpy

Once both of these packages are succesfully installed, the code can be copied or downloaded to be used.

There are three options currently implemented as arguements for the code.

    -I path/to/file :the input file. (Required for code to run)
    -N # :the amount of time between thumbnails in seconds. 
    -V :a version flag to describe the version of the file.

To use this code simply run:

    Example:
    python thumbnail.py -I path/to/file

The thumbnails will be generated in a folder in the same directory as the python script. The folder will be titled whatever the video's title is + _frames.
This will use the default amount of time between thumbnails of 4 seconds. To change this simply add the option -N and the number of seconds between thumbnails.

    Example:
    python thumbnail.py -I path/to/file -N 60

    *This would generate one thumbnail every minute of the video.







