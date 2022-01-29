import sys
import random
d = dict()

def main():
	with open(sys.argv[1], "r", encoding="utf-8") as f:
		for line in f:
			# считанную строку делим по символам ":"
			ln = line.split(":")
			# вычленяем ID и (фамилия, имя)
			ID, name  = ln[0], (ln[3], ln[1])
			# получаем рандомный username из имени пользователя
			username = ''.join(random.sample(name[1].lower(), len(name[1])))
			# записываем данные в словарь, где key - tuple(фамилия, имя), а value - tuple(ID, username)
			d[name] = (ID, username)

	# сортируем в алфавитном порядке(сначала по фамилии, а при совпадении первой буквы фамилии - по имени)
	arr = sorted(d, key=lambda x:(-ord(x[0][0]), -ord(x[1][0])), reverse=True)

	# выводим, в консоль, отформатированную шапку
	print("Name".ljust(30), "ID".center(6), "Username".ljust(10))
	# выводим, в консоль, черту отделяющую шапку, от результата
	print("".ljust(50, "_"))

	# проходим по, ранее отсортированному списку, подставляем значение как ключ, в ранее созданный, словарь
	for i in arr:
		name, ID, username = i, *d[i]
		# выводим, в консоль, отформатированный текст
		print(f"{name[0]}, {name[1]}".ljust(30, "."), f"({ID})".center(6), username.ljust(10))


if __name__ == '__main__':
	main()
