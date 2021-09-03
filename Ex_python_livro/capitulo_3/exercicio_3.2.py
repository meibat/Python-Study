def do_twice(f, a):
     f(a)
     f(a)

def print_spam(a):
     print(a)
     print(a)


def do_four(f, a):
     do_twice(f, a)
     do_twice(f, a)


do_twice(print, 'Spam')
print('')
do_four(print, 'Spam')