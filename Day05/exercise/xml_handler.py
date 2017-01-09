#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse("xml_test.xml")
root = tree.getroot()
print(root.tag)

# 遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print('\t', i.tag, i.text)

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('updated', 'yes')

tree.write('xml_test2.xml')

# 删除node
for country in root.findall('country'):
    if int(country.find('rank').text) > 50:
        root.remove(country)
tree.write('xml_test3.xml')