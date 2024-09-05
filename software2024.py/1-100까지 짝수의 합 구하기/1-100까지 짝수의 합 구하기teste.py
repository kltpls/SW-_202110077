def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')




total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number

print("짝수의 합:", total)





even_sum = sum([number for number in range(1, 101) if number % 2 == 0])

print("짝수의 합:", even_sum)





a = 2
l = 100
n = (l - a) // 2 + 1
even_sum = n * (a + l) // 2

print("짝수의 합:", even_sum)





even_sum = sum(range(2, 101, 2))

print("짝수의 합:", even_sum)
