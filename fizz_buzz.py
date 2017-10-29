def print_integers():
    for i in range(1, 100001):
        print('Fizz'*(i % 3 == 0) + 'Buzz'*(i % 5 == 0) or i)

if __name__ == '__main__':
    print_integers()
