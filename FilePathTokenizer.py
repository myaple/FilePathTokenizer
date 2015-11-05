# -*- coding: utf-8 -*-
''' Author: Matt Yaple (myaple@vt.edu)
    Date: 20150725
'''
import os

class FilePathTokenizer:
    """This class takes in file paths from a file descriptor or strings and
       tokenizes it.

        This class is an example for a coding exercise with FireEye. It will
        implement three methods, tokenize_file_paths, tokenize_fd, and 
        tokenize_file_path. The inputs are described within the methods.
    
    Attributes:
        token_dict: A dictionary containing the full path as the key and a 
                    list of tokens as the value
    """

    def __init__(self):
        """Inits FilePathTokenizer with an empty dictionary"""
        self.token_dict = {}

    def tokenize_file_paths(self,file_paths):
        """Tokenizes both relative and absolute file paths

        Args:
            file_paths: A list of file_paths

        Returns:
            A dict mapping absolute paths to a list of tokens. For example:

            {'C:\\path\\to\\foo.txt': ['C:\\', 'path', 'to', 'foo']}
        """
        
        # Running the tokenize_file_path method on each of the paths
        for path in file_paths:
            tokenized_dict = self.tokenize_file_path(path)
            self.token_dict[path] = tokenized_dict[path]
        return self.token_dict
            
            

    def tokenize_fd(self,filename):
        """Tokenizes both relative and absolute file paths

        Takes in a file descriptor (not a file object!), opens it, then 
        saves the stripped string in a list and calls the previous
        tokenize_file_paths method.

        Args:
            filename: file descriptor of file containing paths

        Returns:
            A dict mapping absolute paths to a list of tokens. For example:

            {'C:\\path\\to\\foo.txt': ['C:\\', 'path', 'to', 'foo']}

        Raises:
            IOError: No such file or directory.
        """

        with os.fdopen(filename) as f:
            file_list = [ lines.strip() for lines in f.readlines() ]
            self.token_dict = self.tokenize_file_paths(file_list)
            return self.token_dict

    def tokenize_file_path(self,file_path):
        """Tokenizes a single file path (both absolute and relative)

        Takes in a file path, splits it into it's pieces, then formats
        the inner path and file name and extension and adds all of the
        arguments to a dictionary.

        Args:
            file_path: string of a file path to be tokenized

        Returns:
            A dict mapping absolute paths to a list of tokens. For example:

            {'C:\path\to\foo.txt': ['C:', 'path', 'to', 'foo.txt', 'foo', 'txt', 'path\\to\\']}
        """
        
        if file_path in self.token_dict:
            return { file_path: self.token_dict[file_path] }

        # Splitting the name where seperated by a '\' - beware escape chars
        output_dict = {}
#        if '\\' not in file_path:
#            file_path = file_path.replace('/', '\\')
        
        split_path = file_path.split('\\')
        
        # Tokenizing the file name itself and inner path
        inner_path = ''
        tokens = []
        for fnames in split_path:
            fnames = fnames.strip()
            tokens.append(fnames)
            # If theres a period or colon, it's not the inner path
            if '.' not in fnames and ':' not in fnames:
                inner_path += ( fnames+'\\' )
            # If there's a period, we tokenize the filename and extension
            elif '.' in fnames:
                split_file = fnames.split('.')
                filename = split_file[0]
                extension = split_file[1]
                tokens.append(filename)
                tokens.append(extension)
        tokens.append(inner_path.replace("\\\\","\\"))
        
        output_dict[file_path] = tokens
        return output_dict
