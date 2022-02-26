import yaml
dict_to_yaml = {"®": ['action', 'to', 'from', 'encoding', 'message'], "§": 45, "æ": {'action': 'msg', 'to': 'account_name'}}
print(f"Список: {dict_to_yaml}")

with open("file.yaml", "w", encoding="utf-8") as file_yaml:
    yaml.dump(dict_to_yaml, file_yaml, default_flow_style=True,  allow_unicode=True, sort_keys=False)

with open("file.yaml", "r", encoding="utf-8") as file_read:
    yaml_content = yaml.load(file_read, Loader=yaml.FullLoader)
    print(f"Содержимое файла: {yaml_content}")
