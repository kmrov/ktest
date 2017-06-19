import csv
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Enumerate bacteria features."
    )
    parser.add_argument("filename", type=str)
    parser.add_argument("output", type=str)
    args = parser.parse_args()

    reader = csv.reader(open(args.filename), delimiter="\t")
    next(reader)

    data = list(reader)

    bacteria = {}
    for (name, feature, value) in data:
        if name in bacteria:
            bacteria[name].append((feature, value))
        else:
            bacteria[name] = [(feature, value)]

    writer = csv.writer(open(args.output, "w"), delimiter="\t")
    writer.writerow(("species", "feature", "value", "rank"))

    for name, features in bacteria.items():
        for (rank, (feature, value)) in enumerate(
            sorted(features, key=lambda item: float(item[1])),
            1
        ):
            writer.writerow(
                (name, feature, value, rank)
            )
