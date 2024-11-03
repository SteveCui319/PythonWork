import matplotlib.pyplot as plt

# X 值和对应的概率
# X_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
#
# # 绘制 PMF
# plt.bar(X_values, probabilities, color='lightblue')
# plt.title('Probability Mass Function of X')
# plt.xlabel('X (First Score - Second Score)')
# plt.ylabel('Probability')
# plt.show()


X_values_1 = [1, 2, 3, 4, 5]
prob = [0.10, 0.40, 0.25, 0.15, 0.10]

plt.bar(X_values_1, prob, color='lightblue')
plt.title('Probability Mass Function of X')
plt.xlabel('X (Hotels occupied in a particular year)')
plt.ylabel('Probability')


# plt.show()

print('Recipe for Boiled Water')
print('-----------------------')
print()
print('Ingredients')
print('-----------')
print('2 C water')
print('1 kettle')
print()
print('Instructions')
print('------------')
print('\t1. Pour the water into the kettle.')
print('\t2. Set the kettle on the stove.')
print('\t3. Turn the stove on "high".')
print('\t4. It is done when the water is bubbling and steaming, so when that happens, turn off the stove.')


print()



def printStr(x, y):
    print('Hello' + x + ' ' + y)


# first_name = input('input your first name: ')
# surname = input('input your surname: ')
# printStr(first_name, surname)


n = input('enter a number: ')
print('you entered: ' + n)
n3 = int(n) * 3
print("three time you number: ", n3)
