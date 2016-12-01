import xml.dom.minidom
import time
import json
import html2text

site_json_path = ""
# Example: site_json_path = "N:\\ZeroBundle\\ZeroNet\\data\\1NtyUa8gvLkwJeHYebVkZXA9hespXvTRFv\\data\\data.json"
WordPress_ExportXML_Path = ""
# Your WordPress Export XML File Path
if not site_json_path or not WordPress_ExportXML_Path:
    print('Please Edit Me And Set site_json_path and WordPress_ExportXML_Path')
    exit(1)

h = html2text.HTML2Text()
site_json = open(site_json_path, encoding='utf-8').read()
open('site_data_json.bak', 'wb').write(site_json.encode())
site_json = json.loads(site_json)
current_post_id = site_json['next_post_id']
posts = site_json['post']

DOMTree = xml.dom.minidom.parse(WordPress_ExportXML_Path)
items = DOMTree.documentElement.getElementsByTagName("item")
for item in items:
    if not item.getElementsByTagName('content:encoded')[0].childNodes:
        continue
    post_title = item.getElementsByTagName('title')[0].childNodes[0].data
    post_time = items[1].getElementsByTagName('wp:post_date')[0].childNodes[0].data
    post_time = time.mktime(time.strptime(post_time, '%Y-%m-%d %H:%M:%S')) + 0.001  # 对齐三位小数 :P
    post_body = h.handle(item.getElementsByTagName('content:encoded')[0].childNodes[0].data)
    post = {"post_id": current_post_id, "title": post_title, "date_published": post_time,
            "body": post_body}
    posts.insert(0, post)
    current_post_id += 1

site_json['next_post_id'] = current_post_id
open(site_json_path, 'wb').write(json.dumps(site_json, ensure_ascii=False, indent="\t").encode())
print('Good! Convert Finished, Please sign site and published, then refresh the page, you will see your WordPress post')
