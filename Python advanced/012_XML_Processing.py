# XML Processing
# Extensible Markup Language

# We're always stored our data into simple files or into professional database
# Sometimes we need a structured way to save files, but we don't want to build a big professional database
# Just to keep the data into a structured way locally on our computer

# It's a great way to hierarchically structure our data, and it's also platform independent
# imagine I build a program in Python that saves stuff into an XML file or outputs data into an XML file,
# I can also have a Cplusplus application that reads in that data and,
# be able to processes that data so It's not limited to just one programming language/applications/operating system

#SAX: simple API for XML
#DOM: document object model
# Use API when you have a limited memory,
# the different to DOM is that if never loads to full XML file into RAM

#SAX
import xml.sax

class GroupHandler(xml.sax.ContentHandler):

    # When our handler processes and elements so when we get into an element
    # this is the first function that called it
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("===== PERSON =====")
            print("ID: {}".format(attrs["id"]))

    # Head Topics
    def characters(self, content):
        if self.current:
            if self.current == "name":
                self.name = content
            elif self.current == "age":
                self.age = content
            elif self.current == "weight":
                self.weight = content
            elif self.current == "height":
                self.height = content

    # Descriptions
    def endElement(self, name):
        if self.current == "name":
            print("Name: {}".format(self.name))
        elif self.current == "age":
            print("Age: {}".format(self.age))
        elif self.current == "weight":
            print("Weight: {}".format(self.weight))
        elif self.current == "height":
            print("Height: {}".format(self.height))
        self.current = None

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("data.xml")

print()
print("SAX & DOM")
print()

#DOM
import xml.dom.minidom

domtree = xml.dom.minidom.parse("data.xml")
group = domtree.documentElement

persons = group.getElementsByTagName("person")

for person in persons:
    print("===== PERSON =====")
    if person.hasAttribute("id"):
        print("ID: {}".format(person.getAttribute("id")))

    print("Name: {}".format(person.getElementsByTagName("name")[0].firstChild.nodeValue))
    print("Age: {}".format(person.getElementsByTagName("age")[0].firstChild.nodeValue))
    print("Weight: {}".format(person.getElementsByTagName("weight")[0].firstChild.nodeValue))
    print("Height: {}".format(person.getElementsByTagName("height")[0].firstChild.nodeValue))

# Change elements
persons[2].getElementsByTagName("name")[0].childNodes[0].nodeValue = "Nattawut Boonnoon"
persons[0].setAttribute("id", "100")
persons[3].getElementsByTagName("age")[0].childNodes[0].nodeValue = "-10"
domtree.writexml(open("data.xml", "w"))

# Add new elements to the object files
newperson = domtree.createElement('person')
newperson.setAttribute('id', '6')

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode("Paul Green"))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode("19"))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode("80"))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode("179"))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

exists = False
# persons come from: group.getElementsByTagName("person") that we declares aboves
for p in persons:
    if p.getAttribute("id") == "6":
        exists = True
        break

if not exists:
    group.appendChild(newperson)

# For delete person on the lists!
# first_person = persons[0]
# group.removeChild(first_person)

with open("data.xml", "w") as f:
    f.write(domtree.toprettyxml(indent="  "))