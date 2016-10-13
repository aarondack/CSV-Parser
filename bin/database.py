import csv

class MSKCCDatabase:
    def __init__(self, db_connection):
        """
        Currently a skeleton of connecting to a MySQL database. This class assumes that
        a db_connection is going to be passed into it. The function getDBHandle() passed in
        will return the correct connection.
        """
        self.db_connection = db_connection
        self.db_cursor = self.db_connection.cursor()

    def query_database(self, query):
        return self.db_cursor.execute(query)

    def close_connection(self):
        self.db_connection.close()

    @staticmethod
    def dictionary_all(cursor):
        """
        Returns all rows from the db cursor as a list of dicts to operate on
        """
        desc = cursor.description
        return [dict(zip([col[0] for col in desc], row))
                for row in cursor.fetchall()]

    def write_to_file(self, sql, file):
        """
        Runs a SQL Query and outputs a correctly formatted CSV file.
        Checks for if the SampleID in either Lane 1 or 2 exists, if it doesn't it inserts the
        correct corresponding SampleID. Also outputs the column headers correctly ordered.
        """
        with open(file, 'w+') as output_csv:
            header_names = ['FCID', 'Lane', 'SampleID', 'SampleRef', 'Index', 'Description', 'Control', 'Recipe',
                            'Operator', 'SampleProject']
            writer = csv.DictWriter(output_csv, fieldnames=header_names)
            writer.writeheader()

            try:
                self.query_database(sql)
                results = self.dictionary_all(self.db_cursor)

                counter = 0
                for row in results:
                    if(row['Lane'] == '2'):
                        if(row['SampleID'] == '' or None):
                            row['SampleID'] = results[counter]['SampleID']
                            print('A sample ID was missing, added')
                            counter += 1
                        elif(results[counter]['SampleID'] == '' or None):
                            results[counter]['SampleID'] = row['SampleID']
                            print('A sample ID was missing, added')
                            counter += 1

                for row in results:
                    writer.writerow(row)
                self.close_connection()
                print('Successful write!')
            except TypeError as e:
                print(e)