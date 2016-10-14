# csv-parser

Simple app that has some pre-defined parameters because custom built for someone. Can be extended as you please. Essentially has the skeleton
to connect to a MySQL database, read from a given table and order headers and data correctly. If data is not included in rows, it will insert a duplicate.
This was based on a bioinformatics problem. 

```
python main.py

Usage:
    python main.py -f
    python main.py -db
    python main.py -h
Options:
    -h Shows help screen
    -f Takes two files, input and output file
    -db Takes an output file

Examples:
    python main.py -f '/my/path/to/file', '/my/path/to/outputfile'
    python main.py -db '/my/path/to/outputfile'
```
