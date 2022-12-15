import json
# import re
# from math import ceil
from lxml import html, etree
from lxml.html.builder import P

with open("applicationdata.json", encoding="utf-8") as f:
    data = json.load(f)

printhtml = html.parse("print.html")

for element in printhtml.iter():
    if "id" in element.attrib:
        if element.attrib["id"] == "company":
            element.text = data["employer"]["company"]
        if element.attrib["id"] == "name":
            element.text = data["employer"]["name"]
        if element.attrib["id"] == "street":
            element.text = data["employer"]["street"]
        if element.attrib["id"] == "city":
            element.text = data["employer"]["city"]
        if element.attrib["id"] == "placetime":
            element.text = data["placetime"]
        if element.attrib["id"] == "subject":
            element.text = data["subject"]
        if element.attrib["id"] == "salutation":
            element.text = data["salutation"]
        # if element.attrib["id"] == "closing":
        #     element.text = data["closing"]
        if element.attrib["id"] == "applicationtext":
            for p in data["applicationtext"]:
                element.append(P(p))
        

printstring = etree.tostring(printhtml, pretty_print=True).decode()

with open("print.html", "w", encoding="utf-8") as f:
    f.write(printstring)
