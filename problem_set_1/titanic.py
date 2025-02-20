import sys
import pandas
from naive_classifier import simple_heuristic as sh


def main(f):
    df = pandas.read_csv(f)
    data = df.set_index('PassengerId')['Survived'].to_dict()
    results_1 = {k: v for (k, v) in sh(df).items() if v == data[k]}
    print(len(results_1) / len(data))


if __name__ == "__main__":
    main(str(sys.argv[1]))
