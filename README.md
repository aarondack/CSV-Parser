# csv-parser

Simple app that has some pre-defined parameters (headers) because custom built for someone. Can be extended as you please. Essentially has the skeleton
to connect to a MySQL database, read from a given table and order headers and data correctly. If data is not included in rows, it will insert a duplicate.
This was based on a bioinformatics problem and shows some basic concepts around reading and writing CSV files, specifically the CSV DictReader and DictWriter.

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

More tests needed 😅
