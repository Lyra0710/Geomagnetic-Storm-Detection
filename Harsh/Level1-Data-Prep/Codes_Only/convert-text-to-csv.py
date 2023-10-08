import csv

# Input file name and output file name
input_file = "./Real_Time_KP_Data.txt"
output_file = "Real_Time_KP_Data.csv"

# Read data from the input file and convert it into a list of lists
data = []
with open(input_file, "r") as infile:
    lines = infile.readlines()[1:]  # Skip the header line
    for line in lines:
        # Split the line into individual elements and convert them to appropriate data types
        row = line.strip().split()
        row = [row[0]] + [int(row[i]) if i == 1 else float(row[i]) for i in range(1, len(row))]
        data.append(row)

# Write data to CSV file
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    header = ["Timestamp", "Source", "Bt", "Bx", "By", "Bz", "Phi", "Theta", "Dens", "Speed", "Temp"]
    writer.writerow(header)
    # Write rows
    writer.writerows(data)

print(f"CSV file '{output_file}' has been created.")
