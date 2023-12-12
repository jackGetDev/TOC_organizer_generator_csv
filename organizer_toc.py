import csv

def generate_csv_from_text(input_text_path, output_csv_path):
    with open(input_text_path, mode='r') as input_text:
        lines = input_text.readlines()
        csv_data = []
        parent_stack = [None]

        for line in lines:
            parts = line.split('. ', 1)
            step = parts[0]
            level = step.count('.')
            action = parts[1].strip()
            parent = parent_stack[level - 1] if level > 0 else None
            if level >= len(parent_stack):
                parent_stack.append(step)
            else:
                parent_stack[level] = step

            csv_data.append([level, step, action, parent if parent else None])

    with open(output_csv_path, mode='w', newline='') as output_csv:
        csv_writer = csv.writer(output_csv, delimiter=';')
        csv_writer.writerow(["Level", "Step", "Action", "Parent"])
        csv_writer.writerows(csv_data)

    print(f"CSV file generated: {output_csv_path}")

generate_csv_from_text("input.txt", "output.csv")
