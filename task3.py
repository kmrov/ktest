import csv
import argparse
from sys import exit

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find a threshold value for given FDR."
    )
    parser.add_argument("filename", type=str)
    parser.add_argument("--fdr", type=float, default=0.05)
    args = parser.parse_args()

    reader = csv.reader(open(args.filename), delimiter="\t")
    next(reader)

    data = [
        (
            float(row[2]),
            1 if row[1] == "decoy" else 0
        ) for row in reader
    ]

    sorted_data = sorted(data, reverse=True)

    s = 0
    last_val = sorted_data[0][0]
    for (num, (val, is_decoy)) in enumerate(sorted_data, 1):
        s += is_decoy
        if s / num > args.fdr:
            print("Threshold value:", last_val)
            exit(0)
        last_val = val

    print("Threshold value not found.")
