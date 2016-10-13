#!/usr/bin/env python
__author__ = 'Aaron Dack'
__email__ = 'adackbusiness@gmail.com'

import argparse, os
from parser import CSVParser
from database import MSKCCDatabase

class MSKCCApplication:
    @staticmethod
    def valid_file_path(parser, arg):
        try:
            if os.path.isfile(arg): return arg
        except IOError:
            print('This file does not exist', arg)

    def arguments(self):
        parser = argparse.ArgumentParser(
            description='Takes in CSV files or connects to a MySQL database and returns a formatted CSV')
        parser.add_argument(
            '-f',
            dest="filenames",
            nargs=2,
            help="Input an absolute path to your input file, output file",
            type=lambda x: self.valid_file_path(parser, x)
        )
        parser.add_argument(
            '-db',
            dest="output",
            nargs=1,
            help="Reads from MySQL database and outputs to designated file",
            type=lambda x: self.valid_file_path(parser, x)
        )
        return parser.parse_args()

    def run(self):
        args = self.arguments()
        if(args.filenames):
            csvobject = CSVParser(args.filenames[0], args.filenames[1])
            csvobject.format_csv_files()
        elif(args.output):
            print('We are connecting to the database...')
            db = MSKCCDatabase() # Here is where we would pass in the getDBHandle()
            db.write_to_file('SELECT * from samplesheet',args.output[0])
        else:
            assert False, "Unhandled"

if __name__ == "__main__":
    app = MSKCCApplication()
    app.run()

