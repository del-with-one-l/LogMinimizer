import datetime

def parse_compressed_entry(entry):
    """Parse compressed entry and return timestamp and temperature."""
    entry_parts = entry.strip().split(', ')
    timestamp = datetime.datetime.strptime(entry_parts[0], '%Y-%m-%d %H:%M:%S')
    temperature = int(entry_parts[1][:-1])  # Remove the trailing semicolon
    return timestamp, temperature

def interpolate_log(compressed_file):
    """Interpolate compressed log file and print the reconstructed log."""
    with open(compressed_file, 'r') as infile:
        compressed_entries = [parse_compressed_entry(line) for line in infile]

    for i in range(len(compressed_entries) - 1):
        current_entry = compressed_entries[i]
        next_entry = compressed_entries[i + 1]

        # Interpolate between current and next entry
        delta_time = (next_entry[0] - current_entry[0]).total_seconds()
        delta_temperature = next_entry[1] - current_entry[1]

        # Interpolate every minute between the two entries
        for j in range(int(delta_time / 60)):  # Change here to interpolate every minute
            interpolated_timestamp = current_entry[0] + datetime.timedelta(minutes=j)
            interpolated_temperature = current_entry[1] + int(delta_temperature / delta_time * 60 * j)
            print(f"{interpolated_timestamp.strftime('%Y-%m-%d %H:%M:%S')}, {interpolated_temperature};")

    # Print the last entry from the compressed log
    last_entry = compressed_entries[-1]
    print(f"{last_entry[0].strftime('%Y-%m-%d %H:%M:%S')}, {last_entry[1]};")

# Example usage:
compressed_log_file = 'compressed_log.txt'
interpolate_log(compressed_log_file)
