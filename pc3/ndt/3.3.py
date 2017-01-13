"""
Formatting Numbers for Output
"""
x = 1234.56789
# Two decimal places of accuracy
print(format(x, '0.2f'))
# Right justified in 10 chars, one-digit accuracy
print(format(x, '>10.1f'))
# Left juestified
print(format(x, '<10.1f'))
# Centered
print(format(x, '^10.1f'))
# Inclusion of thousands sepaarator
print(format(x, ','))
print(format(x, '0,.1f'))

print(format(x, 'e'))
print(format(x, '0.2e'))
print('The value is {:0,.2f}'.format(x))

print(format(x, '0.1f'))
print(format(-x, '0.1f'))

swap_separators = { ord('.'):',', ord(','):'.' }
print(format(x, ',').translate(swap_separators))
