import string

a = string.ascii_letters
print(a)
b = a[1:] + a[0]
print(b)
tab = str.maketrans(a,b)

msg = '''Esse texto será traduzido'''
print(msg)

print(str.translate(msg, tab))