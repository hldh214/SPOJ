# http://www.spoj.com/problems/TEST/

output = ''
while 1:
    raw = input()
    if raw == '42':
        break
    output += raw + '\r\n'

print(output)