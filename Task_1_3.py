w_1 = b"attribute"
w_2 = b"класс"  # SyntaxError: bytes can only contain ASCII literal characters.
w_3 = b"функция"  # SyntaxError: bytes can only contain ASCII literal characters.
w_4 = b"type"

# Слова "класс" и "функция" нельза преобразовать в байтовый формат, так как они написаны на кириллице
