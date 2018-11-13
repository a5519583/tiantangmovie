import requests
from lxml import etree


HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
def get_hrefs(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    _hrefs = html.xpath('//div[@class="co_content8"]//ul//table//a/@href')
    hrefs = map(lambda urls: 'https://www.dytt8.net' + url, _hrefs)
    return hrefs

def get_details(href):
    response = requests.get(url=href, headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    infos = html.xpath('//*[@id="Zoom"]//p[1]/text()')
    movie = {}
    for index, info in enumerate(infos):

        # 译名 translated_name
        if info.startswith('◎译　　名'):
            translated_name = info.replace('◎译　　名','').strip()
            movie['translated_name'] = translated_name

        # 片名 name
        if info.startswith('◎片　　名'):
            name = info.replace('◎片　　名','').strip()
            movie['name'] = name

        # 年代 year
        if info.startswith('◎年　　代'):
            year = info.replace('◎年　　代','').strip()
            movie['year'] = year

        # 产地 origin_place
        if info.startswith('◎产　　地'):
            origin_place = info.replace('◎产　　地','').strip()
            movie['origin_place'] = origin_place

        # 类别 type
        if info.startswith('◎类　　别'):
            type = info.replace('◎类　　别','').strip()
            movie['type'] = type

         # 语言 language
        if info.startswith('◎语　　言'):
            language = info.replace('◎语　　言','').strip()
            movie['language'] = language

        # 字幕 caption
        if info.startswith('◎字　　幕'):
            caption = info.replace('◎字　　幕','').strip()
            movie['caption'] = caption

        # 上映时间 release_time
        if info.startswith('◎上映日期'):
            release_time = info.replace('◎上映日期','').strip()
            movie['release_time'] = release_time

        # IMDb评分 IMDb_mark
        if info.startswith('◎IMDb评分'):
            IMDb_mark = info.replace('◎IMDb评分','').strip()
            movie['IMDb_mark'] = IMDb_mark

        # 豆瓣评分 douban_mark
        if info.startswith('◎豆瓣评分'):
            douban_mark = info.replace('◎豆瓣评分','').strip()
            movie['douban_mark'] = douban_mark

        # 文件格式 document_format
        if info.startswith('◎文件格式'):
            document_format = info.replace('◎文件格式', '').strip()
            movie['document_format'] = document_format

        # 视频尺寸 video_size
        if info.startswith('◎视频尺寸'):
            video_size = info.replace('◎视频尺寸', '').strip()
            movie['video_size'] = video_size

        # 文件大小 file_size
        if info.startswith('◎文件大小'):
            file_size = info.replace('◎文件大小', '').strip()
            movie['file_size'] = file_size

        # 片长 length_film
        if info.startswith('◎片　　长'):
            length_film = info.replace('◎片　　长', '').strip()
            movie['length_film'] = length_film

        # 导演 director
        if info.startswith('◎导　　演'):
            director = info.replace('◎导　　演', '').strip()
            movie['director'] = director

        # 编剧 scriptwriter
        if info.startswith('◎编　　剧'):
            scriptwriter = info.replace('◎编　　剧', '').strip()
            movie['scriptwriter'] = scriptwriter

        # 演员 actors
        if info.startswith('◎主　　演'):
            index_actors = index
            act = info.replace('◎主　　演','').strip()
        if info.startswith('◎标　　签'):
            index_label = index
            label = info.replace('◎标　　签', '').strip()
            movie['label'] = label
            actors = [act]
            actors_list = infos[index_actors+1: index_label]
            for i in actors_list:
                actors.append(i.strip())
            movie['actors'] = actors

        # 电影简介 intro
        if info.startswith('◎简　　介'):
            index_intro = index
        if info.startswith('◎获奖情况'):
            index_prize = index
            movie['intro'] = infos[index_intro+1: index_prize][0].strip()

    img = html.xpath('//*[@id="Zoom"]//img[1]')[0].xpath('@src')
    movie['img'] = img
    return movie

if __name__ == '__main__':
    m = get_details('https://www.dytt8.net/html/gndy/dyzz/20181108/57761.html')
    # 待爬取的url：
    urls = []
    for i in range(1,184):
        urls.append('https://www.dytt8.net/html/gndy/dyzz/list_23_' + str(i) + '.html')

    for i in urls:
        get_hrefs(i)