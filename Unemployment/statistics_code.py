import csv
import argparse

# Function to parse command line arguments
def parse_args():
    # Create Argument parser
    parser = argparse.ArgumentParser(
        description="Calculate unemployment statistics for a given country."
    )
    parser.add_argument(
        "input_file", help="Input CSV file containing unemployment data"
    )
    parser.add_argument("--country", required=True, help="Country to find unemployment")
    parser.add_argument(
        "-o", choices=["avg", "min", "max"], default="avg", help="Operation to perform)"
    )
    parser.add_argument("--from", dest="start_year", type=int, help="Starting year")
    parser.add_argument("--to", dest="end_year", type=int, help="Ending year")

    return parser.parse_args()

# Function to read data from the CSV file
def read_data(input_file, country, start_year, end_year):
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)
        data = [
            float(row["Unemployment"])
            for row in reader
            if row["Entity"] == country
            and (start_year is None or int(row["Year"]) >= start_year)
            and (end_year is None or int(row["Year"]) <= end_year)
        ]
    return data

# Function to calculate the specified statistic (average, minimum, or maximum)
def calculate_statistic(data, operation):
    if not data:
        return None
    if operation == "avg":
        return sum(data) / len(data)
    elif operation == "min":
        return min(data)
    elif operation == "max":
        return max(data)

# Main function
def main():
    args = parse_args()
    data = read_data(args.input_file, args.country, args.start_year, args.end_year)
    result = calculate_statistic(data, args.o)
    if result is not None:
        print(f"The {args.o} unemployment rate for {args.country} is {result:.2f}")
    else:
        print(f"No data available for {args.country} in the specified range.")

if __name__ == "__main__":
    main()

# python statistics_code.py unemployment-rate.csv --country Belgium --from 2010 --to 2018 -o avg
