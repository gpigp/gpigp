import feedparser, datetime

url          = "https://gpigp.github.io/taehyun/feed.xml"
url_feed     = feedparser.parse(url)
MAX_POST_NUM = 5
latest_list  = ""

for idx, feed in enumerate(url_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    
    mon_ = ""
    day_ = ""
    
    if feed_date.tm_mon < 10:
        mon_ = str(feed_date.tm_mon).zfill(2)
    else :
        mon_ = str(feed_date.tm_mon)
    if feed_date.tm_mday < 10:
        day_ = str(feed_date.tm_mday).zfill(2)
    else:
        day_ = str(feed_date.tm_mday)
        
    latest_list += '<a href="' + feed['link'] + '">' + feed_date.tm_year + '.' + mon_ + '.' + day_ + '\t' + feed['title'] + '</a><br>\n'

markdown_1 = """[![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=150&section=header&text=KIM%20TAEHYUN%20🌱&fontSize=40&fontColor=392f31)](https://gpigp.github.io/taehyun)

[![TAEHYUN's GitHub stats](https://github-readme-stats.vercel.app/api?username=gpigp&show_icons=true&theme=vue)](https://github.com/gpigp)

## 📋Recent Blog Post<br>```html
"""

markdown_2 = """```
## 🛠 Skills 🛠  

### Languages
<div>
<img src="https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=Python&logoColor=white" height="27">
<img src="https://img.shields.io/badge/C++-00599C.svg?&style=flat-square&logo=C%2B%2B&logoColor=white" height="27">
<img src="https://img.shields.io/badge/C-A8B9CC.svg?&style=flat-square&logo=C&logoColor=white" height="27">
<img src="https://img.shields.io/badge/Java-007396.svg?&style=flat-square&logo=Java&logoColor=white" height="27">
</div>
  
### Tools
<div>
<img src="https://img.shields.io/badge/GitHub-181717.svg?&style=flat-square&logo=GitHub&logoColor=white" height="27">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?&style=flat-square&logo=Docker&logoColor=white" height="27">
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?&style=flat-square&logo=Jupyter&logoColor=white" height="27">
<img src="https://img.shields.io/badge/PyTorch-EE4C2C.svg?&style=flat-square&logo=PyTorch&logoColor=white" height="27">
</div>

<hr>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fgpigp&count_bg=%231D6A96&title_bg=%2385B8CB&icon=bilibili.svg&icon_color=%23283B42&title=2DAY&edge_flat=true)](https://hits.seeyoufarm.com)"""

readme_text = f"{markdown_1}{latest_list}{markdown_2}"

f = open("README.md", mode="w", encoding="utf-8")
f.write(readme_text)
f.close()
