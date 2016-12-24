"""
Sanitizing and Cleaning Up Text
"""
import unicodedata
import sys

s = 'python\fis\tawesome\r\n'
print(s)
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Delete
}
a = s.translate(remap)
print(a)

print()
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))

print()
digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))
# Arabic digits
s = '\u0661\u0662\u0663'
print(s.translate(digitmap))
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))


def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s
