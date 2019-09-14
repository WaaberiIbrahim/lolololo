import sympy.sandbox.tests.test_indexed_integrals
import sys


def readable(old_data):
    new_data = []
    for line in old_data:
        new_data.append(line.split(","))
    return new_data


def remNames(filename, rowname):
    data = readable(open(filename, 'r').read().split("\n"))
    idxrow = data[0].index(rowname)
    for line in data:
        for stuff in line:
            if line.index(stuff) == idxrow:
                try:
                    line.pop(idxrow)
                except:
                    print("", end="")
    new_csv = ""
    for line in data:
        new_csv += ",".join(line)+"\n"
    new_d = open(filename, 'w')
    new_d.write(new_csv)
    new_d.close()


if __name__ == "__main__":
    remNames(sys.argv[1], sys.argv[2])
