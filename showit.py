import os
import sys
if __name__ == "__main__":
    f_a = sys.argv[1]
    argu = sys.argv[2]
    argu2 = sys.argv[3]
    new_file = f_a.split(".")[0]+".csv"
    os.system(f"python toCSV.py {f_a}")
    os.system(f"python remNames.py {new_file} {argu}")
    os.system(f"python remNames.py {new_file} {argu2}")
    os.system(f"start {new_file}")
