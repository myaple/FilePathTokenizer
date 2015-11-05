# -*- coding: utf-8 -*-
"""Author: Matt Yaple (myaple@vt.edu)
   Date: 20150725
"""

import argparse as ap
import os
import sys

from FilePathTokenizer import FilePathTokenizer as FPT

def parser():
    """Parses arguments when called from the command line

    Creates an ArgumentParser object then parses the arguments passed
    from the command line. Also checks if the user input a valid file.

    Returns:
        An object of the arguments passed from the command line
        
    Raises:
        IOError - If the file does not exist, raises an IOError
    """
    
    
    parser = ap.ArgumentParser(description='Parsing some file names in various forms')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f','--filepaths',dest='filepaths',metavar='PATH1,PATH2,...',type=str,
                        help='Input a string or list of strings. ex. '
                        '"C:\\Users\\Matt\\Desktop\\FireEyeCodingSample\\learn.txt",'
                        '"foo\\bar\\fudge"''Note: On Unix systems, you need quotes or you need to escape your escape characters.'
                        'Otherwise, your resultant tokens may be incorrect.')
    group.add_argument('-i','--input',dest='file',metavar='TEXTFILE',type=str,
                        help='Input a valid file path to a text file of '
                        'paths. ex. '
                        '"C:\\Users\\Matt\\Desktop\\FireEyeCodingSample\\learn.txt"')
    
    
    args = parser.parse_args()

    if args.file and not os.path.isfile(args.file):
        raise OSError('This file does not exist - please input a valid file path')
                
    return args

if __name__ == "__main__":
    """ When called from the command line, call parser method to parse 
        arguments given.
        
        After retrieving the args object from the parser method, checks to
        see if a file or file path or file paths have been input. After
        deciding what argument has been given, call the appropriate
        method from FilePathTokenizer. Finally, print the keys and values
        from the resultant dictionary to the command line.
    """
    
    args = parser()
    tokenizer = FPT()
    
    if not args.filepaths:
        if not args.file:
            print('Error: Empty string or no input provided. Exiting...')
            sys.exit( 1 )

        text_file = args.file.strip("\'").strip('\"')

        fd = os.open(text_file,os.O_RDWR)
        token_dict = tokenizer.tokenize_fd(fd)

    else:
        filepaths = args.filepaths

        if not filepaths:
            print('Error: Empty string or no input provided. Exiting...')
            sys.exit( 1 )
        if sys.platform != "win32" and "\\" not in filepaths:
            print("Error: Due to how Linux handles escape chars, please put quotes around the file path to get the correct tokens.")
            sys.exit( 1 )
            

        filepaths = filepaths.strip("\'").strip('\"')
        filepath_list = filepaths.split(',')
        
        if len(filepath_list) == 1:
            token_dict = tokenizer.tokenize_file_path(filepath_list[0])
        else:
            token_dict = tokenizer.tokenize_file_paths(filepath_list)
        
    for keys in token_dict:
        print('{} : {}'.format(keys, token_dict[keys]))
        