from chardet import detect

with open('test_file.txt', 'rb') as text_file:
    content = text_file.read()
encoded_content = detect(content)
print(f"Содержимое файла:\n{content.decode('utf-8')}\n")
print(f"Кодировка файла: {encoded_content}")
