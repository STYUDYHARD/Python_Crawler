# 保持热爱 奔赴山海

import pprint
import requests
from bs4 import BeautifulSoup
import json

# 构造分页数字列表
page_indexs = range(0, 250, 25)
list(page_indexs)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

url = "https://movie.douban.com/subject/26581837/";


def download_movie_view():
    datas1 = []
    datas2 = []
    count = 0
    # 提取电影的subject ID
    subject_id = url.split('/')[-2]  # URL格式是https://movie.douban.com/subject/123456/
    # url.split('/') 会将字符串 url 按照斜杠 (/) 分割成一个列表。[-2] 是一个索引操作，用于获取这个列表中的倒数第二个元素。

    # 获取电影标题
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.select_one('h1 span').get_text()
    # 找到一个<h1>标签内的<span>标签，并获取它的文本内容

    comments = []
    for page in range(0, 5):  # 设置抓取页数，每页20条
        new_url = f"https://movie.douban.com/subject/{subject_id}/comments?start={page * 20}&limit=20&status=P&sort=new_score"
        # sort=new_score为最热评论，sort=time为最新评论
        # print("abc", new_url)
        response = requests.get(new_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for comment_item in soup.select('.comment-item'):
            comment = comment_item.find(class_="short").get_text()
            comments.append(comment)

    cleaned_comments = [comment.replace("\n", "").replace("\r", "") for comment in comments]
    datas1.append({
        "book_id": subject_id,
        "book_name": title,
    })
    datas2.append({
        "book_id": subject_id,
        "comment_content": cleaned_comments
    })
    print("get√:上海堡垒")

    return datas1,datas2


datas1,datas2 = download_movie_view()

json_data1 = json.dumps(datas1, ensure_ascii=False, indent=4)
with open('shanghaibaolei_comment_data.json', 'w', encoding='utf-8') as f:
    f.write(json_data1)

json_data2 = json.dumps(datas2, ensure_ascii=False, indent=4)
with open('shanghaibaolei_movies_data.json', 'w', encoding='utf-8') as f:
    f.write(json_data2)

# pprint.pprint(datas)













