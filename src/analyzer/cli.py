import argparse
import sys


from analyzer.loader import load_data
from analyzer.report import print_report
from analyzer.stats import summarize

def build_parser():
    parser = argparse.ArgumentParser(
        description="Print mean, min and max of the numeric columns of a CSV file."
    )
    parser.add_argument("path", help="path to the CSV file")
    parser.add_argument("--columns", nargs="+",help="columns to analyze (default: all numeric columns)",)
    parser.add_argument("--group-by", help="column to group by (e.g Regionname)", )
    return parser

def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        df = load_data(args.path)
        summary = summarize(df, args.columns, args.group_by)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    except KeyError as error:
        print(f"Error: column not found: {error}", file=sys.stderr)
        return 1
    except TypeError:
        print("Error: all selected columns must be numeric", file=sys.stderr)
        return 1

    print_report(summary)
    return 0

if __name__ == "__main__":
    sys.exit(main())