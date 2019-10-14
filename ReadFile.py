import csv


class CSVReader:
    @staticmethod
    def get_csv_as_2d_array(filename):
        datafile = open(filename, 'r')
        datareader = csv.reader(datafile, delimiter=',')
        data = []
        for row in datareader:
            data.append(row)
        return data
