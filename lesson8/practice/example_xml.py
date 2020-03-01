import xml.etree.ElementTree as eTree

file = open('../../example.xml')
tree = eTree.parse(file)
root = tree.getroot()
result = []
for user in root:
    result.append({child.tag: child.text for child in user.getchildren()})
print(result)

result_str = []

for child in result:
    s = """
    <user>
        <name>{name}</name>
        <age>{age}</age>
        <sex>{sex}</sex>
    </user>"""
    result_str.append(s.format(**child))

result_str = '\n'.join(result_str)
result_str = f'<root>\n{result_str}\n</root>'

file = open('../../new_file.xml', 'w')
file.write(result_str)
file.close()
