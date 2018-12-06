import copy

arr = [2, 2, 2, 3, 3, 3]
arr1 = [2, 2, 2, 3, 9]
arr2 = [2, 2, 3, 3, 6]
arr3 = [2, 3, 3, 3, 4]
options = [arr1, arr2, arr3]

for option in options:
  opt = copy.deepcopy(option)
  opt.append(1)

  for j in range(len(opt)):
    for k in range(len(opt)):
      if j < k:
        opt_new = []
        opt_new.extend(opt[:j])
        opt_new.extend(opt[j+1:k])
        opt_new.extend(opt[k+1:])
        opt_new.append(opt[j]*opt[k])
        opt_new.sort()
        if opt_new not in options:
          options.append(opt_new)
    
for option in options:
  print(option, sum(option))
