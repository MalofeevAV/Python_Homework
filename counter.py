def arr_creator():
	arr = []
	s = " "
	while s:
		s = input("Enter number: ")
		if s != "":
			arr.append(int(s))
	return arr


if __name__ == '__main__':
	lst = arr_creator()
	print(*lst)
	print(len(lst), sum(lst), min(lst), max(lst), sum(lst)/len(lst), sep="\n")