import xml.etree.ElementTree as ET

tree = ET.parse('plik_xml.xml')
root = tree.getroot()
for x in root[0]:
     print(x.tag, x.attrib)
for ele in root.iter('price'):
     uppdated_price = str(ele.text)+'(old one) 3.5 $(new one)'
     ele.text = str(uppdated_price)
tree.write('updated_xml.xml')
