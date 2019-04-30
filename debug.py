# -*- coding: utf-8 -*- 

import os
import csvConcat
import time

str_fout_path = os.path.join(os.getcwd(), 'concated.csv')

str_dir_path = os.path.join(os.getcwd(), 'data')

start       = 0.0
end         = 0.0
dur_slow    = 0.0
dur_fast    = 0.0

for i in range(0, 10):

    start = time.time()

    csvConcat.slow(str_fout_path, str_dir_path)

    end = time.time()

    dur_slow += (end - start)

print('Slow concat: ' + str(dur_slow/10.0))

start   = 0.0
end     = 0.0
dur     = 0.0

for i in range(0, 10):

    start = time.time()

    csvConcat.fast(str_fout_path, str_dir_path)

    end = time.time()

    dur_fast += (end - start)

print('Fast concat: ' + str(dur_fast/10.0))

print('Slow/Fast = ' + str(dur_slow/dur_fast))
