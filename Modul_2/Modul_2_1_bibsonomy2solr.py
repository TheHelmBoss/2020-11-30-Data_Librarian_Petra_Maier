import json

with open('discrimination.json',encoding='utf-8')  as json_file:
    data = json.load(json_file)

    data.pop('properties')
    data.pop('types')

    for item in data['items']:
        del_list = ['abstract', 'acmid', 'address', 'archiveprefix', 'asin', 'authors', 'bdsk-url-1', 'bibtexKey', 'booktitle', 'changeDate', 'citeulike-article-id', 'citeulike-linkout-0', 'citeulike-linkout-1', 'citeulike-linkout-2', 'citeulike-linkout-3', 'count', 'date', 'description', 'ean', 'editors', 'ee', 'eprint', 'file', 'groups', 'id', 'interHash', 'intraHash', 'location', 'mendeley-tags', 'note', 'notes', 'number', 'numpages', 'owner', 'pages', 'pagetotal', 'pdf', 'pii', 'pluralLabel', 'pmid', 'posted-at', 'ppn_gvk', 'priority', 'publisher', 'refid', 'shorttitle', 'size', 'timestamp', 'urldate', 'user', 'username', 'valueType', 'volume']
        for i in del_list:
            if i in item:
                del item[i]
        item['title'] = item.pop('label')
        data_filter = [item for item in data['items'] if (item['type'] == 'Publication')]

    with open('bibsonomy_to_solr.json','w', encoding='utf8') as outfile:
        json.dump(data_filter,outfile,ensure_ascii=False,indent=4)