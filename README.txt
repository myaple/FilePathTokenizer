Author: Matt Yaple (myaple@vt.edu)
Date: 20150725

How To Use

This object is meant to be a command line tool. In order to 
tokenize a file path, first recognize what form your file paths are in. 

If you have a text document of file paths, please format it with one file path per 
line and use the -i or --input argument. An example file is given in the test.txt 
file provided. An example command line execution is below, using the -i argument:

C:\Users\Matt\Desktop\FireEyeCodingSample>python main.py -i C:\Users\Matt\Desktop\FireEyeCodingSample\test.txt
C:\file\path\here\foobar.py  :  ['C:', 'file', 'path', 'here', 'foobar.py', 'foobar', 'py', 'file\\path\\here\\']
C:\file\path\here\foo.py  :  ['C:', 'file', 'path', 'here', 'foo.py', 'foo', 'py', 'file\\path\\here\\']
C:\file\path\here\bar.py  :  ['C:', 'file', 'path', 'here', 'bar.py', 'bar', 'py', 'file\\path\\here\\']

If you are looking to tokenize a file path string or strings, please use the -f 
or --filepaths arguments. Two example command line executions are below, using the -f argument:

C:\Users\Matt\Desktop\FireEyeCodingSample>python main.py -f C:\file\path\here\foobar.py
C:\file\path\here\foobar.py  :  ['C:', 'file', 'path', 'here', 'foobar.py', 'foobar', 'py', 'file\\path\\here\\']

C:\Users\Matt\Desktop\FireEyeCodingSample>python main.py -f C:\file\path\here\foobar.py,C:\file\path\here\foo.py
C:\file\path\here\foobar.py  :  ['C:', 'file', 'path', 'here', 'foobar.py', 'foobar', 'py', 'file\\path\\here\\']
C:\file\path\here\foo.py  :  ['C:', 'file', 'path', 'here', 'foo.py', 'foo', 'py', 'file\\path\\here\\']


Note: On Unix systems, you need quotes or you need to escape your escape characters.Otherwise, your
resultant tokens may be incorrect.
