#!/usr/bin/python3
from xml.dom.minidom import parse
from xml.sax.saxutils import XMLFilterBase, XMLGenerator
import xml.dom.minidom
import xml.sax

'''
    Class to parse xml file by sax method. 
'''
class SaxHandler(xml.sax.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self.name = ""
        self.country = ""
        self.price = ""
        self.description = ""
        self.ingedients = ""
        self.calories = ""

    def startElement(self, tag, attributes):
        self.currentTag = tag
        if tag == "food":
            print("\n*****\tfood\t*****\n")
            title = attributes["id"]
            print("Title:", title)

    def endElement(self, tag):
        if tag == "name":
            print("Name:", self.name)
        if tag == "country":
            print("Country:", self.country)
        elif tag == "description":
            print("Description:", self.description)
            self.description = ''
        elif tag == "calories":
            print("Calories:", self.calories)
        elif tag == "price":
            print("Price:", self.price)
        self.currentTag = ''

    def characters(self, content):
        self._charBuffer.append(content)
        if self.currentTag == "name":
            self.name = content
        if self.currentTag == "country":
            self.country = content
        elif self.currentTag == "price":
            self.price = content
        elif self.currentTag == "description":
            self.description += content
        elif self.currentTag == "calories":
            self.calories = content

class Modify(XMLFilterBase):
    def __init__(self, id, tagToEdit, text, parent=None):
        super().__init__(parent)
        self.id = id
        self.tagToEdit = tagToEdit
        self.text = text
        self.isThatElement = 0
        self.isThatTag = 0

    def editThis(self):
        return self.isThatElement == 1 and self.isThatTag == 1

    def startElement(self, tag, attributes):
        if tag == "food" and attributes["id"] == self.id:
            self.isThatElement += 1
        if tag == self.tagToEdit:
            self.isThatTag += 1

        super().startElement(tag, attributes)

    def endElement(self, tag):
        if tag == "food" and self.isThatElement == 1:
            self.isThatElement -= 1
        if tag == self.tagToEdit:
            self.isThatTag -= 1

        super().endElement(tag)

    def characters(self, content):
        if self.editThis():
            super().characters(self.text)
        else:
            super().characters(content)


def SaxAdder(file):
    HandlerToPrint = SaxHandler()
    viewer = xml.sax.make_parser()
    viewer.setContentHandler(HandlerToPrint)
    viewer.parse(file)

    dinner = Modify('fd5', 'name', 'Cabbage with sausage', viewer)

    with open('edited.xml', 'w') as f:
        handlerToEdit = XMLGenerator(f)
        dinner.setContentHandler(handlerToEdit)
        dinner.parse(file)

'''
    Method for DOM xml parse method
'''
def DOMAdder(file):
    DOMTree = xml.dom.minidom.parse(file)
    collection = DOMTree.documentElement
    if collection.hasAttribute("food"):
        print("Root element : %s" % collection.getAttribute("food"))

    foods = collection.getElementsByTagName("food")

    for food in foods:
        print("\n*****\tFood\t*****")
        name = food.getElementsByTagName('name')[0]
        print("Name: %s" % name.childNodes[0].data)
        country = food.getElementsByTagName('country')[0]
        print("Country: %s" % country.childNodes[0].data)
        description = food.getElementsByTagName('description')[0]
        print("Description: %s" % description.childNodes[0].data)
        calories = food.getElementsByTagName('calories')[0]
        print("Calories: %s" % calories.childNodes[0].data)
        price = food.getElementsByTagName('price')[0]
        print("Price: %s" % price.childNodes[0].data)


def test():
    # file = input("Which file name would you like to modify ?")
    file = "simple.xml"
    DOMAdder(file)
    # SaxAdder(file)

if __name__ == "__main__":
    test()