# 5.	Используя lambda и map, преобразуйте список строк так, чтобы все строки стали заглавными. Например,
# из ['python', 'code'] сделать ['PYTHON', 'CODE'].

words = ['python', 'code']
upper_words = list(map(lambda w: w.upper(), words))
print("Слова в верхнем регистре:", upper_words)