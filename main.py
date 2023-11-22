"""task 1. Нахождение наименьшего избыточного числа"""


def get_divisors(n):
    divisors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def abundant(h):
    abundant_number = None
    abundance = 0

    for i in range(h, 1, -1):
        divisors_sum = sum(get_divisors(i))
        if divisors_sum > i:
            abundant_number = i
            abundance = divisors_sum - i
            break

    return [[abundant_number], [abundance]]


print(abundant(15))
print(abundant(19))

"""task 2. Напишите код, что реализует функцию filter_by_values, 
которая фильтрует список словарей (origin) по уникальным значениям указанных ключей (keys).
Если keys не предоставлен, то функция использует ключи из первого словаря в списке."""


def filter_by_values(origin, keys=None):
  if not origin:
    return []

  if keys is None:
    keys = list(origin[0].keys())

  unique_values = {}
  result = []

  for item in origin:
    key_tuple = tuple(item[key] for key in keys)
    print(key_tuple)
    if key_tuple not in unique_values:
      unique_values[key_tuple] = item
      result.append(item)

  return result


res = filter_by_values([
  {"x": 1, "y": 2, "z": 3},
  {"x": 0, "y": 2, "z": 3},
  {"x": 0, "y": 4, "z": 5}],
  keys=["x", "y", "z"]
)

print(res)


""" task 3. Вам известен номер квартиры, этажность дома и количество квартир на этаже.
Задача: написать функцию, которая по заданным параметрам напишет вам, в какой подъезд
и на какой этаж подняться, чтобы найти искомую квартиру."""


def find_apartment(intro=int(input("Enter flat number: "))):
    floors = 9
    count_flat = floors * 4
    entrance = intro // count_flat + 1
    floor = 1 + (intro-1) % count_flat / 4
    return f"get up {entrance} entrance and {round(floor)} flor"


outro = find_apartment()
print(outro)


"""task 4. Входным данным является целое число. Необходимо:

написать проверку, чтобы в работу пускать только положительные нечетные числа
для правильного числа нужно построить бриллиант из звездочек или любых других символов
и вывести его в консоли. Для числа 1 он выглядит как одна взездочка, для числа три он выглядит как звезда,
потом три звезды, потом опять одна, для пятерки - звезда, три, пять, три, одна..."""


def check_number(number=int(input("Enter the number: "))):
    s = ' '
    for i in range(number):
        if number % 2 and number > 0:
            mid = min(i + 1, number - i)
            star = s * (number - mid) + "*" * (mid * 2 - 1)
            print(star)


check_number()

"""Task 5. Файл-тест. Есть файл, в котором хранятся числа в следующем формате:

2 4 5;3 2
3 2 1;2 0
6 5 2 1 2;3 1
.....
Цифры до точки с запятой надо суммировать, потом делить на их количество.
В первой строке сумма будет 11, разделить на их количество, т.е. на 3,
получается 3 целых и в остатке 2. Аналогичным образом во второй строке 6 делим на три,
ровно два и в остатке ноль, в третьей строке сумма 16, на 5 делим, получаем 3 и 1 в остатке."""


def func_test():
    valid = True

    with open('file_test.txt', 'r') as f:
        for line in f.readlines():
            numbers = line.strip().split(';')
            first = numbers[0]
            st = [int(num) for num in first.split()]

            new_list = [first, str(sum(st) // len(st)) + ' ' + str(sum(st) % len(st))]
            if numbers != new_list:
                valid = False
    return valid


r = func_test()
print(r)


"""Task 6. Написати програму, яка виводить сама себе"""

with open(__file__, 'r') as f:
    print(f.read())

"""Task 7. Написати програму, яка виводить саму себе задом наперед"""

with open(__file__, 'r') as f:
    lines = f.readlines()
    for line in reversed(lines):
        print(line.strip()[::-1])


"""Task 8. Банкомат видає суму максимально можливими купюрами"""


def get_bancnotes_dict(amount):
    dict_bancnotes = {}
    bancnotes = [20, 50, 100, 200, 500, 1000]

    for bancnote in reversed(bancnotes):
        count = amount // bancnote

        if count != 0:
            dict_bancnotes[bancnote] = count

        elif amount % bancnote == 0:
            break

        amount -= bancnote * count

    return dict_bancnotes


res = get_bancnotes_dict(1500)

print(res)


"""Task 9. Написати fizzbuzz для 20 комплектів по три числа, які записані в файл.
    Читайте із файлу перший рядок з трьома числами, беріть із нього числа, 
    рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файла."""


def fizzbuzz_from_file(file_path):
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            numbers = line.split()
            fizz = numbers[0]
            buzz = numbers[1]
            remainder = numbers[2]

        results = []
        for num in range(1, int(remainder) + 1):
            target = ''

            if num % int(fizz) == 0:
                target += 'F'
            if num % int(buzz) == 0:
                target += 'B'
            if not target:
                target = str(num)

            results.append(target)

    return ' '.join(results)


res = fizzbuzz_from_file('fizzbuzz.txt')
print(res)

"""Task 10. Переробити другу задачу так, щоб результат писався в інший файл. Додаємо list comprehension, 
    map та інші свіжеотримані знання до виконання завдання."""


def fizzbuzz_from_file(input_file, output_file):
    with open(input_file, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            numbers = line.split()
            fizz = numbers[0]
            buzz = numbers[1]
            remainder = numbers[2]

        results = []
        for num in range(1, int(remainder) + 1):
            target = ''

            if num % int(fizz) == 0:
                target += 'F'
            if num % int(buzz) == 0:
                target += 'B'
            if not target:
                target = str(num)

            print(target, end=' ')
            results.append(target)

        with open(output_file, 'a') as my_file:
            my_file.write(' '.join(results))


"""Task 11"""


def scoreboard(st):
    scores = {'nil': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    return [scores[x] for x in st.split() if x in scores]


a = scoreboard("four nil")
print(a)