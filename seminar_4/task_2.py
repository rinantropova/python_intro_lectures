# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

import re
new_string = ("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells"
              " sea shells on the sea shore I'm sure that the shells are sea shore shells")

words = [word.lower() for word in re.split('[. ]', new_string) if word]
print(words)
print(len(words))

unique_words = len(set(words))
print(set(words))
print(unique_words)
# print(len(set(my_list)))
