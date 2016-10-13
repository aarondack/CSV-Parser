import csv


class CSVParser:
    def __init__(self, inputFile=None, outputFile=None):
        self.inputFile = inputFile
        self.outputFile = outputFile

    def format_csv_files(self):
        """
        Function that takes in the input and output file.

        The function reorganizes the column headers and data associated with
        it to match the correct order as advised in header_names. This is all
        written to the output file.

        This also checks the input file to make sure that SampleID's are not null for a given lane. If a SampleID
        is null for a given lane an error is thrown.
        """
        with open(self.inputFile, 'r') as inputcsv, open(self.outputFile, 'w+') as outputcsv:
            header_names = ['FCID', 'Lane', 'SampleID', 'SampleRef', 'Index', 'Description', 'Control', 'Recipe',
                            'Operator', 'SampleProject']
            csv_writer = csv.DictWriter(outputcsv, fieldnames=header_names)
            try:
                csv_writer.writeheader()
                for row in csv.DictReader(inputcsv):
                    if row['SampleID'] == '' or None:
                        raise LookupError('For every lane number there needs to be an existing SampleID, exiting...')
                    else:
                        csv_writer.writerow(row)
                print('Finished')
            except TypeError as e:
                print('Error', e)