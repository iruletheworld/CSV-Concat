# CSV-Concat
This repo is for concatenating CSV files. This repo provides two functions for concatenation. One slow, one fast. 

The functions would concat the CSV files found in the given directory and concat them into the given output file. The functions assume all CSV files have the same format and the same header. Only the header from the first file found would be kept (this is based on a glob search).

The "fast" function uses shutil, while the "slow" function is pure Python.

On average, the "fast" function is 2.5 to 5 times faster than the "slow" function.

## Prerequisites

* **Python 3.5+**
* **glob**
* **os**
* **shutil**

## Version

**1.0.0**

## Example

### Concat all CSV files in the "data" folder into a file named "concated.csv" in the current working directory

```python
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
```

## Contributing

高斯羽 博士 (Dr. Gao, Siyu)