header_delimiter = "================================================================================================\n"
header_delimiter_len = len(header_delimiter)

def print_file_header(header_text):
    white_space = " " * int((header_delimiter_len - len(header_text) - 2) / 2)
    print("\n================================================================================================\n")
    print(white_space + header_text + white_space)
    print("\n================================================================================================\n")

def print_separator():
    print("\n--------------------------------\n")