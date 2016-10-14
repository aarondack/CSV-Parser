import unittest
import csv
from bin.parser import CSVParser

class ParserTestCase(unittest.TestCase):

    def setUp(self):
        self.input_file = 'test_input.csv'
        self.output_file = 'test_output.csv'
        self.csv_test = CSVParser(self.input_file, self.output_file)

    def test_csv_headers(self):
        self.csv_test.format_csv_files()
        with open(self.output_file, 'r') as output_file:
            parsed_data = [row for row in csv.reader(output_file.read().splitlines())]
            self.assertEqual(parsed_data[0], ['FCID','Lane','SampleID','SampleRef','Index','Description','Control','Recipe','Operator','SampleProject'])

    def test_reordering_headers(self):
        with open(self.output_file, 'w+') as output_file:
            header_names = header_names = ['Lane', 'SampleID','Index','SampleRef','Description', 'Control', 'Recipe',
                            'Operator', 'SampleProject', 'FCID']
            csv_writer = csv.DictWriter(output_file, fieldnames=header_names)
            csv_writer.writeheader()
        self.csv_test.format_csv_files()

        with open(self.output_file, 'r') as output_file:
            parsed_data = [row for row in csv.reader(output_file.read().splitlines())]
            self.assertEqual(parsed_data[0], ['FCID','Lane','SampleID','SampleRef','Index','Description','Control','Recipe','Operator','SampleProject'])

    def test_data_is_ordered(self):
        self.csv_test.format_csv_files()

        with open(self.output_file, 'r') as output_file:
            parsed_data = [row for row in csv.reader(output_file.read().splitlines())]
            self.assertEqual(parsed_data[1], ['H9EX','1','123-T','HUMAN','CGATGT','Tumor','N','l','AY|John;Doe|M123|Male','IMPACTv3-20140001'])
