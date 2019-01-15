for i in range(15000):
  square = i**2
  len_square = len(str(square))
  num_unique_nums = len(set(str(square)))
  highest_num = max(map(int, set(str(square))))
  lowest_num = min(map(int, set(str(square))))
  if len_square == num_unique_nums and highest_num <= len_square and lowest_num > 0:
    print(i, square, i**3)
