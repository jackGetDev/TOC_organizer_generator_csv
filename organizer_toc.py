
import csv

json_data = [
    {
        "Topic": "A",
        "Colors": [
            {"Color": "Red", "Value": 100},
            {"Color": "Green", "Value": 50},
            {"Color": "Blue", "Value": 25}
        ]
    },
    {
        "Topic": "B",
        "Colors": [
            {"Color": "Cyan", "Value": 128},
            {"Color": "Yellow", "Value": 256},
            {"Color": "Brown", "Value": 1024}
        ]
    }
]

# Group data by "Topic"
grouped_data = {}
for item in json_data:
    topic = item["Topic"]
    colors = item["Colors"]
    if topic not in grouped_data:
        grouped_data[topic] = {"Color": [], "Value": []}
    for color_data in colors:
        grouped_data[topic]["Color"].append(color_data.get("Color", None))
        grouped_data[topic]["Value"].append(color_data.get("Value", None))

# Create a CSV file with semicolon as the delimiter
csv_file_path = "output.csv"

# Open the CSV file in write mode with semicolon as the delimiter
with open(csv_file_path, mode='w', newline='') as csv_file:
    # Create a CSV writer with semicolon as the delimiter
    csv_writer = csv.writer(csv_file, delimiter=';')

    # Write the header row
    csv_writer.writerow(["Topic", "Color", "Value"])

    # Iterate through the grouped data and write rows
    for topic, data in grouped_data.items():
        colors = data["Color"]
        values = data["Value"]
        for color, value in zip(colors, values):
            # For repeated "Topic" values, fill in null for "Topic"
            csv_writer.writerow([topic if colors.index(color) == 0 else None, color, value])

print(f"CSV file generated: {csv_file_path}")

import csv

def generate_csv_from_text(input_text_path, output_csv_path):
    # Read the input text file
    with open(input_text_path, mode='r') as input_text:
        # Read lines from the text file
        lines = input_text.readlines()

        # Initialize CSV data list
        csv_data = []

        # Initialize a stack to keep track of the parent at each level
        parent_stack = [None]

        # Parse table of contents and convert to CSV format
        for line in lines:
            parts = line.split('. ', 1)
            step = parts[0]
            level = step.count('.')
            action = parts[1].strip()

            # Determine parent step
            parent = parent_stack[level - 1] if level > 0 else None

            # Update the parent stack
            if level >= len(parent_stack):
                parent_stack.append(step)
            else:
                parent_stack[level] = step

            # Append to CSV data
            csv_data.append([level, step, action, parent if parent else None])

    # Write the output CSV file with semicolon as the delimiter
    with open(output_csv_path, mode='w', newline='') as output_csv:
        csv_writer = csv.writer(output_csv, delimiter=';')
        csv_writer.writerow(["Level", "Step", "Action", "Parent"])
        csv_writer.writerows(csv_data)

    print(f"CSV file generated: {output_csv_path}")

# Example usage
generate_csv_from_text("input.txt", "output.csv")
