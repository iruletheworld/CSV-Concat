# -*- coding: utf-8 -*- 

'''
Module Name : csvConcat

Author : 高斯羽 博士 (Dr. GAO, Siyu)

Version : 1.0.0

Last Modified : 2019-04-30

This module has two functions to allow CSV file concatenation (column extension with no extra header). The "slow" function is implemented with pure Python, while the "fast" function employs shutil.

On average, the "fast" function is about 2.5 to 5 times faster than the "slow" function.

Change Log
----------------------
* **Notable changes:**
    + Version : 1.0.0
        - First version.

Reference
----------------------
https://stackoverflow.com/questions/2512386/how-to-merge-200-csv-files-in-python
https://stackoverflow.com/questions/44791212/concatenating-multiple-csv-files-into-a-single-csv-with-the-same-header-python/44791368

List of functions
----------------------

* slow_
* fast_
'''

import glob
import os
import shutil

def slow(str_fout_path, str_dir_path):
    '''
    .. _slow :

    Concatenate CSV file. Slow. Pure Python.
    
    https://stackoverflow.com/questions/2512386/how-to-merge-200-csv-files-in-python

    Parameters
    ----------
    str_fout_path : str
        Output CSV file path.

    str_dir_path : str
        Input CSV files' path.

        The CSV files found in this path will be concatnate into the output CSV file.

    Raise
    -------
    IOError : when fail to delete the existing CSV output file.
    IOError : when fail concat the CSV input files.

    Returns
    -------
    None.
    '''

    try:

        # remove the out file if it already exists
        if os.path.exists(str_fout_path):

            os.remove(str_fout_path)

        else:

            pass

    except:

        raise IOError('Failed to remove existing CSV file.')

    try:

        # find all the files in the given directory
        list_csv_file = glob.glob(os.path.join(str_dir_path, '*.csv'))

        # open the output file in append mode
        fout = open(str_fout_path, 'a')

        for line in open(list_csv_file[0]):

            fout.write(line)

        # skip the header line for rest of the csv files
        for i in range(1, len(list_csv_file)):

            ftemp = open(list_csv_file[i])

            next(ftemp)

            for line in ftemp:

                fout.write(line)

            ftemp.close()

        fout.close()

    except:

        raise IOError('Failed to concat CSV files.')

def fast(str_fout_path, str_dir_path):
    '''
        .. _fast :

    Concatenate CSV file. Fast. Use shutil.
    
    https://stackoverflow.com/questions/44791212/concatenating-multiple-csv-files-into-a-single-csv-with-the-same-header-python/44791368

    Parameters
    ----------
    str_fout_path : str
        Output CSV file path.

    str_dir_path : str
        Input CSV files' path.

        The CSV files found in this path will be concatnate into the output CSV file.

    Raise
    -------
    IOError : when fail to delete the existing CSV output file.
    IOError : when fail concat the CSV input files.

    Returns
    -------
    None.
    '''

    try:

        # remove the out file if it already exists
        if os.path.exists(str_fout_path):

            os.remove(str_fout_path)

        else:

            pass

    except:

        raise IOError('Failed to remove existing CSV file.')

    try:

        # find all the files in the given directory
        list_csv_file = glob.glob(os.path.join(str_dir_path, '*.csv'))

        # use the shell utility to concate
        with open(str_fout_path, 'wb') as outfile:

            for i, fname in enumerate(list_csv_file):

                # Throw away header on all but first file
                with open(fname, 'rb') as infile:

                    if i != 0:

                        infile.readline()

                    # Block copy rest of file from input to output without parsing
                    shutil.copyfileobj(infile, outfile)

    except:

        raise IOError('Failed to concat CSV files.')