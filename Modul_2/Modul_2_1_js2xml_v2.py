import json
import xml.etree.ElementTree as xmlTree
import re
import urllib.request

file = urllib.request.urlopen("https://www.bibsonomy.org/json/search/discrimination?items=1000&duplicates=merged")
result = file.read().decode('utf-8')
data = json.loads(result)
# with open('C:/Users/Petra/Downloads/discrimination.json', encoding='utf-8 -*-') as json_file:
#     data = json.load(json_file)

# def indent c/p von https://stackoverflow.com/questions/3095434
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

    # xml Wurzelelement
root = xmlTree.fromstring('<records></records>')
counter_list = 0
for item in data['items']:
    if item['type'] == 'Publication':
        record = xmlTree.SubElement(root,'record')
        counter_list += 1
        xmlTree.SubElement(record,'recordID').text = str(counter_list)
    # titel
        if 'label' in item:
            xmlTree.SubElement(record,'title').text = item['label']
        else:
            pass

    # creators
        if 'authors' in item:
            authors = xmlTree.SubElement(record,'authors')
            if any('|' in x for x in item['author']):
                author_alt = item['author']
                for i in range(len(author_alt)):
                    author_index = item['author'][i]
                    author_corr = re.sub(r'( \|)',r', ',author_index).split(', ')
                    for i in range(len(author_corr)):
                        author = author_corr[i]

                        xmlTree.SubElement(authors,'author').text = author.strip()

            elif 'authors' in item:
                author_list = item['authors']
                for index in range(len(author_list)):
                    authors_first = item['authors'][index]['first']
                    authors_last = item['authors'][index]['last']
                    author = authors_first + " " + authors_last
                    xmlTree.SubElement(authors,'author').text = author

        elif 'editors' in item:
            editors = xmlTree.SubElement(record,'editors')
            editor_list = item['editors']
            for index in range(len(editor_list)):
                editors_first = item['editors'][index]['first']
                editors_last = item['editors'][index]['last']
                editor = editors_last + ", " + editors_first
                xmlTree.SubElement(editors,'editor').text = editor
        else:
            pass

        if 'isbn' in item:
            if re.match(r'\d{4}-\d{4}',item['isbn']):
                xmlTree.SubElement(record,'issn').text = item['isbn']
            else:
                xmlTree.SubElement(record,'isbn').text = item['isbn']
        else:
            pass

        if 'year' in item:
            xmlTree.SubElement(record,'year').text = item['year']
        else:
            pass

        if 'journal' in item:
            xmlTree.SubElement(record,'journal').text = item['journal']
        else:
            pass

        if 'pages' in item:
            xmlTree.SubElement(record,'pages').text = item['pages']
        else:
            pass

        if 'url' in item:
            if item['url'].startswith('http'):
                xmlTree.SubElement(record,'url').text = item['url']
            else:
                pass
        else:
            pass

        if 'tags' in item:
            tag_list = item['tags']
            for i in range(len(tag_list)):
                xmlTree.SubElement(record,'tags').text = item['tags'][i]

        tree = xmlTree.ElementTree(root)
        indent(root)
        tree.write('C:/Users/Petra/Downloads/bibsonomy.xml',encoding="UTF-8")