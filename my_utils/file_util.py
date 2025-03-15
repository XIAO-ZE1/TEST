def print_file_info(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"File Name: {file_name}")
            print(f"File Content:\n{content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file(file_name,data):
    try:
        with open(file_name, 'a') as file:
            file.write(data)
            print(f"Data appended to '{file_name}' successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_file_info('test.txt')