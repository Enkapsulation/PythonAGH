#!/usr/bin/python3
from xml.dom.minidom import parse
import xml.dom.minidom
import xml.sax

def xml_parse_dom(filename):
    xml_tree = xml.dom.minidom.parse(filename)
    xml_content = xml_tree.documentElement

    breakfast_menu = xml_content.getElementsByTagName("food")

    for food in breakfast_menu:
        print("Food")
        name = food.getElementsByTagName('name')[0].firstChild.data
        price = food.getElementsByTagName('price')[0].firstChild.data
        desc = food.getElementsByTagName('description')[0].firstChild.data
        calories = food.getElementsByTagName('calories')[0].firstChild.data
        #print(f'{name} {price} {desc} {calories}')

        # mydata = xml.dom.minidom.tostring(data)
        # myfile = open("items2.xml", "w")
        # myfile.write(mydata)

def test():
    xml_to_parse = input("Type xml to parse: ")
    xml_parse_dom(xml_to_parse)

if __name__ == "__main__":
    test()