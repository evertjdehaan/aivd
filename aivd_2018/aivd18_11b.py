from itertools import groupby

number = '149554087214664289545813515695286402233339701081845595280362829806993294677384116914834752509152758572737499296520884429057992394694292141612557548625371627496876172206474452242442881793196749137289109800753294410539546425609257468594408930562750601301763664664436344439312492666291833846522323701781919914006843850864368311058859764258893753580174283003166720000'

print(len(number))
groups3 = [int(number[i:i+3]) for i in range(0, len(number), 3)]
groups11 = [int(number[i:i+11]) for i in range(0, len(number), 11)]
groups33 = [int(number[i:i+33]) for i in range(0, len(number), 33)]
groups121 = [int(number[i:i+121]) for i in range(0, len(number), 121)]
print(groups3)

freq3 = {key: len(list(group)) for key, group in groupby(sorted(groups3))}
freq11 = {key: len(list(group)) for key, group in groupby(sorted(groups11))}
freq33 = {key: len(list(group)) for key, group in groupby(sorted(groups33))}
freq121 = {key: len(list(group)) for key, group in groupby(sorted(groups121))}

print(freq3)
print(freq11)
print(freq33)
print(freq121)

# Use the sum of the numbers to determine the alphabet letter
string = ''
for num in groups3:
  strnum = '0'*(3-len(str(num))) + str(num)
  string += chr(ord('a') + int(strnum[0]) + int(strnum[1]) + int(strnum[2]))
print(string)
# Nope

# Use the number as a rotation
string = ''
for num in groups3:
  string += chr(ord('a') + (num % 26))
print(string)
# Nope
