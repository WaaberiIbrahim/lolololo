
import os
import sys
import openpyxl


def toCSV(filename):
    somename = filename.split(".")[0]+".csv"
    xlsx = openpyxl.load_workbook(filename)
    sheet = xlsx.active
    data = sheet.rows
    csv = open(somename, "w+")

    for row in data:
        l = list(row)
        for i in range(len(l)):
            if i == len(l) - 1:
                csv.write(str(l[i].value))
            else:
                csv.write(str(l[i].value) + ',')
        csv.write('\n')

    # close the csv file
    csv.close()


if __name__ == "__main__":
    globals()["toCSV"](sys.argv[1])
