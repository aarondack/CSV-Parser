import csv

class CSVParser:
    def __init__(self, inputFile=None, outputFile=None):
        self.inputFile = inputFile
        self.outputFile = outputFile

    def open_csv_file(self):
        """
        Function that takes in the input and output file.

        The function reorganizes the column headers and data associated with
        it to match the correct order as advised in header_names. This is all
        written to the output file.

        This also checks the input file to make sure that SampleID's are not null for a given lane.
        """

        with open(self.inputFile, 'r') as inputcsv, open(self.outputFile, 'r+') as outputcsv:
            header_names = ['FCID', 'Lane', 'SampleID', 'SampleRef', 'Index', 'Description', 'Control', 'Recipe',
                            'Operator', 'SampleProject']
            csv_writer = csv.DictWriter(outputcsv, fieldnames=header_names)
            try:
                csv_writer.writeheader()
                self.check_csv_errors(inputcsv)
                for row in csv.DictReader(inputcsv):
                    csv_writer.writerow(row)
                inputcsv.close()
                outputcsv.close()
                print('Finished')
            except Exception as e:
                print('Unexpected Error', e)

    def check_csv_errors(self, inputcsv):
        """
        This function checks the input file to see if the SampleID is populated.
        If the SampleID is populated the file is sane and is closed.
        """
        for row in csv.DictReader(inputcsv):
            if (row['SampleID'] == '' or None):
                raise LookupError('For every lane number there needs to be an existing SampleID, exiting...')