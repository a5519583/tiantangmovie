目标：爬取天堂电影院：本站首页>电影>最新电影，共183页/4568条记录的电影详情
关键字：译名、片名、年代、产地、类别、语言、字幕、上映日期、IMDb评分、豆瓣评分、文件格式、视频尺寸、文件大小、片长、导演编剧、主演、标签、简介、获奖情况

思路：
    获取183个页面的所有影片的链接，共4568条
    实现每条的关键字提取

问题：
    4568条记录的关键字提取，效率问题

重要函数：
strip()
map()
lambda
enumerate()
replace()
startswith()
