def print_report(summary):
    table = summary.T
    print("Summary statistics")
    print("-" * 18)
    print(table.to_string(float_format = "{:,.2f}".format))
    