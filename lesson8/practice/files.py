
file = open('../../data.csv')
headers = file.readline()[:-1].split(',')
lines = file.read().split('\n')
file.close()
lines = [
    dict(zip(headers, line.split(',')))
    for line in lines if line
]
print(headers)
print(lines)

headers = ','.join(lines[0].keys())
print(headers)
lines = sorted(lines, key=lambda x: x['name'])
lines = [','.join(line.values()) for line in lines]
print(lines)

file = open('../../new.csv', 'w')
file.write(f'{headers}\n')
file.write('\n'.join(lines))
file.close()
