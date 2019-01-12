number0 = 715140684628284199
number1 = 27799359960895951622945294228650160556473581133507282258716324517526331387881422051374048992068531165469465793
number2 = 612242109049354757693703731756141884122575855425310699918367263271480642730811111952684256523677275662759320997

def find_divisor(num):
  # Get the length of the number
  len_num0 = len(str(num))
  # The divisor is in the number itself, make substrings of the number and check if it is a divisor
  for len_div in range(2, int(len_num0/2)+1):
    for i in range(len_div):
      div = int(str(num)[i:i+len_div])
      if num % div == 0:
        print(num, div, int(num / div))

find_divisor(number0)
find_divisor(number1)
find_divisor(number2)
