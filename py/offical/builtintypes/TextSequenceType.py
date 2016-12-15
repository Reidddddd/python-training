import re

print(str(b'Zoot!'))
print('01\t012\t0123\t01234'.expandtabs())
print('01\t012\t0123\t01234'.expandtabs(4))
print('Py' in 'Python')
print("The sum of 1 + 2 is {0}".format(1 + 2))
print()


class Default(dict):
    def __missing__(self, key):
        return key


print('{name} was born in {country}'.format_map(Default(name='Guido')))
print('  spacious  **'.lstrip())
print('www.example.com'.lstrip('cmowz.'))
print('**  spacious    '.rstrip())
print('mississippi'.rstrip('ipz'))
print('1,2,3'.split(','))
print('1,2,3'.split(',', maxsplit=1))
print('1,2,,3,'.split(','))
print('1 2 3'.split())
print('1 2 3'.split(maxsplit=1))
print('  1  2  3 '.split())
print()

print('ab c\n\nde fg\rkl\r\n'.splitlines())
print('ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True))
print("".splitlines())
print("One line\n".splitlines())
print('Two lines\n'.split('\n'))
print()

print('  spacious  '.strip())
print('www.example.com'.strip('cmowz.'))
print()

print('Hello world'.title())
print("they're bill's friends from the UK".title())


def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)

print(titlecase("they're bill's friends."))
print()

print("42".zfill(5))
print("-42".zfill(5))
print("+42".zfill(5))
print()

print('%(language)s has %(number)03d quote types.' %
      {'language':"Python","number":2})
