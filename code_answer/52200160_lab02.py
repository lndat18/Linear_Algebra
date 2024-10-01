import numpy as np

def Ex1():
    print('Exercise 1')
    a = list(range(51,101,2))
    print('Odd numbers: ',a)
    print('-'*50)


def Ex2():
    print('Exercise 2')
    a = list()
    for num in range(1500,2700+1):
        if num % 7 == 0 and num % 5 == 0:
            a.append(num)
    print(a)
    print('-'*50)


def Ex3():
    print('Exercise 3')
    a = list()
    for num in range(21):
        if num == 3 or num == 16:
            continue
        else:
            a.append(num)
    print(a)
    print('-'*50)


def Ex4():
    print('Exercise 4')
    numbers = [1,2,3,4,5,6,7,8,9]
    even = list()
    odd = list()
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print('Number of odd numbers  ', len(odd))
    print('Number of even numbers  ',len(even))
    print('-'*50)


def Ex5():
    print('Exercise 5')
    sum = 0
    for i in range(99):
        sum += (i+1)/(i+2)
    print(sum)
    print('-'*50)


def Ex6():
    print('Exercise 6')
    a = np.arange(12,39)
    print(a)
    print('-'*50)


def Ex7():
    print('Exercise 7')
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([4, 5, 6, 7, 8])

    common_values = np.intersect1d(array1, array2)

    print("Common values between the two arrays:", common_values)
    print('-'*50)

def main():
    Ex1()
    Ex2()
    Ex3()
    Ex4()
    Ex5()
    Ex6()
    Ex7()


if __name__ == '__main__':
    main()