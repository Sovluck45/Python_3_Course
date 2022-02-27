import csv
import os
import re
from chardet import detect

text_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
current_directory = os.path.dirname(os.path.abspath(__file__))


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    test_list = []
    main_data = [["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]]
    for i in text_list:
        with open(f"{i}", "rb") as info_:
            info_content = info_.read()
        encoded_content = detect(info_content)["encoding"]
        with open(f"{i}", "r", encoding=encoded_content) as info_file:
            read_info = info_file.readlines()
            for line in read_info:
                test_list += re.findall(r'^(\w[^:]+).*:\s+([^:\n]+)\s*$', line)
    for item in test_list:
        os_prod_list.append(item[1]) if item[0] == main_data[0][0] else None
        os_name_list.append(item[1]) if item[0] == main_data[0][1] else None
        os_code_list.append(item[1]) if item[0] == main_data[0][2] else None
        os_type_list.append(item[1]) if item[0] == main_data[0][3] else None
    for i in range(3):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])
    return main_data


def write_to_csv(filepath):
    info_data = get_data()
    directory, filename = os.path.split(filepath)
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(current_directory, directory, filename)
    with open(filepath, "w", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=" ", quoting=csv.QUOTE_NONNUMERIC)
        for line in info_data:
            csv_writer.writerow(line)


write_to_csv("csv_folder/file.csv")
