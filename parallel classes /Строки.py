# Длинна строки len

S = 'Hello'
print(len(S))


# Срезы - извлечение из данной строки одного символа
# или некоторого фрагмента подстроки или подпоследовательности

# Метод FIND and RFIND

S = 'Hello'
print(S.find('e'))
# 1
print(S.find('ll'))
# 2
print(S.find('L'))
# -1

S = 'Hello'
print(S.find('l'))
# 2

print(S.rfind('l'))
# 3

# Метод REPLACE

'Hello'.replace('l', 'L')
# 'HeLLo'

'Abrakadabra'.replace('a','A',2)
# 'AbrAkAdabra'

# CAUNT


S = input()
print(S[2])
print(S[-2])
print(S[:5])
print(S[:-2])
print(S[::2])
print(S[1::2])
print(S[::-1])
print(S[-1::-2])
print(len(S))


