import pandas as pd
import numpy as np
import xml.etree.cElementTree as et
import json 

def filexml_to_dict(file):
    tree=et.parse(file)
    dorigine = {}
    root=tree.getroot()
    i = 0
    for childs in root.iter('item'):
        for child in childs:
            if child.tag == 'price':
                price = child.text
            if child.tag == 'mpn':
                key = child.text
                dorigine[key]= {}
                dorigine[key] = price
        i = i + 1
    return dorigine

dorigine = {}
dorigine.update(filexml_to_dict('test1.xml'))
dorigine.update(filexml_to_dict('test2.xml'))
dorigine.update(filexml_to_dict('test3.xml'))
dorigine.update(filexml_to_dict('test4.xml'))
dorigine.update(filexml_to_dict('test5.xml'))

with open("sample12.json", "w") as outfile:
    json.dump(dorigine, outfile, indent = 4)
