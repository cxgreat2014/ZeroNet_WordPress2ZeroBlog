# -*- coding: UTF-8 -*-
import xml.dom.minidom
import time
import json
import html2text
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Read config from config.ini file.
site_json_path = config.get('main', 'site_json_path')
wordpress_xml_path = config.get('main', 'wordpress_xml_path')

if not site_json_path or not wordpress_xml_path:
    print('Please read README.md and edit config.ini first!')
    exit(1)

h = html2text.HTML2Text()
site_json = open(site_json_path, encoding='utf-8').read()
open('site_data_json.bak', 'wb').write(site_json.encode())
site_json = json.loads(site_json)
current_post_id = site_json['next_post_id']
posts = site_json['post']
titles = []
for idx,title in enumerate(posts):
    titles.append(posts[idx]['title']) 

DOMTree = xml.dom.minidom.parse(wordpress_xml_path)
items = DOMTree.documentElement.getElementsByTagName("item")
for idx,item in enumerate(items):
    if not item.getElementsByTagName('content:encoded')[0].childNodes:
        continue
    post_title = item.getElementsByTagName('title')[0].childNodes[0].data
    post_time = items[idx].getElementsByTagName('pubDate')[0].childNodes[0].data
    post_time = time.mktime(time.strptime(post_time, '%a, %d %b %Y %H:%M:%S +0000'))  # 对齐三位小数 :P
    post_body = h.handle(item.getElementsByTagName('content:encoded')[0].childNodes[0].data)
    if post_title in titles:
        continue
    post = {"post_id": current_post_id, "title": post_title, "date_published": post_time,
            "body": post_body}
    posts.insert(0, post)
    current_post_id += 1

site_json['next_post_id'] = current_post_id
open(site_json_path, 'wb').write(json.dumps(site_json, ensure_ascii=False, indent="\t").encode())
print('Good! Convert Finished, Please sign site and published, then refresh the page, you will see your WordPress post')
