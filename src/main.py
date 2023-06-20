from src.utils import load_json_file, five_last_operations, output_information

if __name__ == "__main__":
    file_name1 = "operations.json"
    all_operations_list = load_json_file(file_name1)
    last_operations = five_last_operations(all_operations_list)
    print(output_information(last_operations))
