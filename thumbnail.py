import os, sys
import argparse
import cv2
import shutil
from ffmpy import FFmpeg

def run_example():
    #creation of parser
    parser = argparse.ArgumentParser()  
    parser.add_argument("-V", "--version", help="show program version", action="store_true")
    parser.add_argument("-I", "--input", help="input file")
    
    # read arguments from the command line
    args = parser.parse_args()

    if args.version:  
        print("This is a thumbnail generator for videos, still in development.")
        sys.exit()

    if args.input:
        print('\nExecuting process on', args.input, '\n')
        video_input = args.input
        video_name = args.input.split('.')[0]
    else:
        print("\nFile not found or input not specified correctly. Be sure to include the -I flag for input.")
        sys.exit()
       
    #erase folders if filepath exists
    if os.path.exists(video_name+'_frames'):
        print('\nOverwriting existing directory...\n')
        shutil.rmtree(video_name+'_frames')
    os.makedirs(video_name+'_frames')

    #use FFmpeg to create thumbnails from video file.
    ff = FFmpeg(inputs={video_input: None}, outputs={video_name+"_frames/thumb_%d"+".png": ['-vf', 'fps=.5']})

    # print(ff.cmd)

    # Print result
    try:
        print("\nGenerating Thumbnails...\n")
        ff.run()
    except:
        print('\nError running thumbnail conversion.\n')
        sys.exit()

    print("\nThumbnails generated successfully.\n")


if __name__ == '__main__':
    run_example()