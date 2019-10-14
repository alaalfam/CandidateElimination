from ReadFile import *
from CandidateElimination import *


def main():
    # TODO :data.csv 100%
    #   data1.csv 90%
    #   data2.csv 100%
    #   data3.csv 100%
    filename = "data1.csv"
    table = get_table(filename)
    candidate_elimination_obj = CandidateElimination(table)
    candidate_elimination_obj.start_calculate()


def get_table(filename):
    return CSVReader.get_csv_as_2d_array(filename)


main()
