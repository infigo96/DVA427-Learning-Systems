import numpy as np

a = np.array([7, 3, 1, 8, 2, 4, 6, 5])
b = np.array([7, 5, 2, 8, 4, 3, 1, 6])
print(a)
print(b)
indexToSwitch = 5 #len(a)-takeAwayWidth -indexToSwitch > 0
takeAwayWidth = 8

toSwitch1 = a[indexToSwitch:indexToSwitch+takeAwayWidth]
toSwitch2 = b[indexToSwitch:indexToSwitch+takeAwayWidth]
print('To Switch: ' +str(toSwitch1))
print('To Switch: ' +str(toSwitch2))

cutOutA = a[~np.in1d(a,toSwitch2)]
cutOutB = b[~np.in1d(b,toSwitch1)]
print(cutOutA)
print(cutOutB)

# print(a)
print(np.insert(cutOutA, indexToSwitch, toSwitch2))
print(np.insert(cutOutB, indexToSwitch, toSwitch1))

# print(np.insert(a, 1, 0))
# print(np.insert(a, 2, 0))
