#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

new_xml = ET.Element('NameList')
name = ET.SubElement(new_xml, 'name', attrib={'enrolled':'yes'})
name.text = 'Will'
age = ET.SubElement(name, 'age')
age.text = '18'
role = ET.SubElement(name, 'role')
role.text = 'Manage'

name2 = ET.SubElement(new_xml, 'name2', attrib={'hehe':'233'})
name2.text = 'idiot'
age = ET.SubElement(name2, 'age')
age.text = "1000"
role = ET.SubElement(name2, 'role')
role.text = 'homeless'

et = ET.ElementTree(new_xml)
et.write('xml_maked.xml', encoding='utf-8', xml_declaration=True)

ET.dump(new_xml)