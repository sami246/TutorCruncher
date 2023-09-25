def format_serial_number(input, group_length):
    # Remove any existing hyphens
    remove_existing_hyphens = input.replace("-", "")

    # Capatalise everything
    capitalised = remove_existing_hyphens.upper()

    # Initialize the result string
    result = ""

    # Start from the end of the capitalised string and take group_length until the whole string is used
    for i in range(len(capitalised), 0, -group_length):
        # Calculate the starting index of the current group
        # Use max to ensure the value is never negative
        start_index = max(i - group_length, 0)
        # Extract a group of characters (up to group_length)
        group = capitalised[start_index:i]
        # Add the group to the result string
        result = group + "-" + result if result else group

    return result

# TESTING:
formatted_serial_1 = format_serial_number('7Hnwad9Jk', 4)
print(formatted_serial_1) # Output: "7-HNWA-D9Jk"

formatted_serial_2 = format_serial_number('6F2k-1d-0-z', 4)
print(formatted_serial_2) # Output: "6F2K-1D0Z"

formatted_serial_3 = format_serial_number('14k-9-b', 2)
print(formatted_serial_3) # Output: "1-4K-9B"