import datetime

def parse_log_entry(entry):
    """Parse log entry and return timestamp and temperature."""
    entry_parts = entry.strip().split(', ')
    timestamp = datetime.datetime.strptime(entry_parts[0], '%Y-%m-%d %H:%M:%S')
    temperature = int(entry_parts[1][:-1])  # Remove the trailing semicolon
    return timestamp, temperature

def compress_log(input_file):
    """Compress log file by only logging changes and print the result."""
    with open(input_file, 'r') as infile:
        prev_entry = None
        for line in infile:
            current_entry = parse_log_entry(line)
            if prev_entry is None or current_entry[1] != prev_entry[1]:
                print(f"{current_entry[0].strftime('%Y-%m-%d %H:%M:%S')}, {current_entry[1]};")
            prev_entry = current_entry

# Example usage:
input_log_file = 'your_input_log_file.txt'
compress_log(input_log_file)
