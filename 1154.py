sum = 0
avg = 0

while True:
    n = int(input())

    if n < 0:
        break

    else:
        sum += n
        avg += 1

result = sum / avg

print(f'{result:.2f}')