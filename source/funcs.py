import csv

def read_csv_file(file_path, csv_to_read):
    with open (file_path, 'r') as csv_file:
        read_csv = csv.DictReader(csv_file)
        csv_list = []
        for row in read_csv:
            csv_list.append(row) 
        return csv_list
    
def write_csv_file(file_path, list):
    with open(file_path, "w", newline='') as file:
        if list:
            writer = csv.DictWriter(file, fieldnames=list[0].keys())
            writer.writeheader()
            writer.writerows(list)
            
def append_dict(file_path, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_path, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = csv.DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)