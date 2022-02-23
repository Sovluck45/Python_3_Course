word_list = [b"class", b"function", b"method"]
for i in word_list:
    print(f"Слово: {i}\n"
          f"Тип слова: {type(i)}\n"
          f"Длина слова: {len(i)}\n"
          f"-----------------------")

# ниже пытался сделать преобразование через eval, но не вышло
'''word_list = ["class", "function", "method"]
for i in word_list:
    b_w = eval("'b' + i")
    print(f"Слово в байтовом формате: {b_w}\n"
          f"Тип слова: {type(b_w)}\n"
          f"Длина слова: {len(b_w)}\n"
          f"-----------------------")'''
