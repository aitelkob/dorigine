import pandas as pd
import numpy as np
import xml.etree.cElementTree as et
import json 

tree=et.parse('test.xml')
dorigine = {}
root=tree.getroot()
i = 0
for childs in root.iter('item'):
    #print(child[6].tag,child[6].text)
    #print(child[8].tag,child[8].text)
    key = "item" + str(i)
    dorigine[key]= {}
    for child in childs:
        if child.tag == 'price':
            dorigine[key][child.tag] = child.text
        if child.tag == 'mpn':
            dorigine[key]['OAM'] = child.text
        if child.tag == 'product_type':
            dorigine[key][child.tag] = child.text
    i= i + 1
json_object = json.dumps(dorigine,indent = 4)

with open("sample.json", "w") as outfile:
    json.dump(dorigine, outfile, indent = 4)
