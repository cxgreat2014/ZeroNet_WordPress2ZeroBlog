
# ZeroNet_WordPress2ZeroBlog
Convert WordPress post to ZeroBlog

## Usage

install `html2text` python package first.

`pip3 install html2text`

### Convert

If you want to convert your WordPress posts to ZeroBlog once only, follow the guide below.
1. Export your wordpress posts to a xml file.
2. download this repo and edit the first two variables in `config.ini` ( `site_json_path` and  `wordpress_xml_path` ). 
3. run `python3 convert.py`, wait it finished, sign your site and published it.then refresh webpage, you will see your post.

### Sync

If you want to sync your WordPress posts to ZeroBlog, which means after you published a new post on WordPress, your ZeroBlog can be updated automatically, follow this guide.

1. Download this repo and edit all variables except `wordpress_xml_path` in `config.ini`.
2. setup a crontab task `bash run.sh`.
