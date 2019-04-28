# -*- coding: utf-8 -*- 

'''
'''

import glob
import os
import time
import shutil

def slow(str_fout_path, str_dir_path):
    '''
    # https://stackoverflow.com/questions/2512386/how-to-merge-200-csv-files-in-python
    '''

    # remove the out file if it already exists
    if os.path.exists(str_fout_path):

        os.remove(str_fout_path)

    else:

        pass

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

        for l in ftemp:

            fout.write(l)

        ftemp.close()

    fout.close()

def fast(str_fout_path, str_dir_path):
    '''
    # https://stackoverflow.com/questions/44791212/concatenating-multiple-csv-files-into-a-single-csv-with-the-same-header-python/44791368
    '''

    # remove the out file if it already exists
    if os.path.exists(str_fout_path):

        os.remove(str_fout_path)

    else:

        pass

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