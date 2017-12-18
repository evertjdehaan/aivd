import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

numbers = [330189942390, 165094971195, 55031657065, 11006331413, 1572333059]

for i in range(len(numbers)-1):
    print(str(numbers[i]) + '\t' + str(numbers[i+1]) + '\t' +
          str(numbers[i]/numbers[i+1]))

print(numbers[-1]/11)
