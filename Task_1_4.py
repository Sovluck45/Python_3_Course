word_list = ["разработка", "администрирование", "protocol", "standard"]
for i in word_list:
    dec_w = i.encode('utf-8')
    print(f"Закодированное слово '{i}': {dec_w}\n"
          f"Декодированное слово '{i}': {dec_w.decode('utf-8')}\n")
