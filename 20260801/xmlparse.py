import xml.etree.ElementTree as xmltree

tree = xmltree.ElementTree(file='my.xml')
root = tree.getroot()
print(root.tag)                      # class

# 走訪下兩層
for a in root:                       # morning, afternoon
    print(a.tag, a.attrib, a.text)
    for b in a:                      # item
        print(b.tag, b.attrib, b.text)
print('-------------------------------')
# 找出所有 item（不分層）
for item in root.iter('item'):
    print(item.attrib, item.text)

# 只找 morning 底下的 item
for item in root.findall('./morning/item'):
    print(item.tag, item.attrib, item.text)