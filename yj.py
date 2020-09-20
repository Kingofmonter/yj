import requests
from lxml import etree
import jieba.analyse
import imageio

#目标页面
url = "https://bbs.nga.cn/read.php?tid=23308833&page={}"

#浏览器请求头
headers = {
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Cookie': 'UM_distinctid=1741198fcfc32c-06ec41051d002c-3323766-1fa400-1741198fcfd6c6; taihe_bi_sdk_uid=259580126747deb676e1c8380596b3b3; taihe=721b650c05fecd8f739f763b6a2b8d0c; UM_distinctid=174119a098447e-0944c084ffaca1-3323766-1fa400-174119a0985648; taihe_bi_sdk_session=aa9d3075619843fa89e2074ad2fa6b71; PHPSESSID=pc5u2jekdbvfctgusrtthhbqg1; ngacn0comUserInfo=%25B4%25F3%25CA%25A6%25D0%25D7%25BF%25AA%25B3%25B5%09%25E5%25A4%25A7%25E5%25B8%2588%25E5%2587%25B6%25E5%25BC%2580%25E8%25BD%25A6%0973%0973%09%0920%0915000%094%090%090%09128_150; ngaPassportUid=61282613; ngaPassportUrlencodedUname=%25B4%25F3%25CA%25A6%25D0%25D7%25BF%25AA%25B3%25B5; ngaPassportCid=X8sff16i8eehfds9vp85hd11hpg352l2tghp4ccm; CNZZDATA30043604=cnzz_eid%3D1753465460-1598019415-https%253A%252F%252Fbbs.nga.cn%252F%26ntime%3D1600504717; ngacn0comUserInfoCheck=a40cac2afb235bcce605479344a75286; ngacn0comInfoCheckTime=1600508785; lastvisit=1600508895; lastpath=/read.php?tid=23308833&page=2; bbsmisccookies=%7B%22pv_count_for_insad%22%3A%7B0%3A-14%2C1%3A1600534830%7D%2C%22insad_views%22%3A%7B0%3A1%2C1%3A1600534830%7D%2C%22uisetting%22%3A%7B0%3A%22e%22%2C1%3A1600509200%7D%7D; _cnzz_CV30043604=forum%7Cfid-34587507%7C0; ngaPassportUid=guest05f65a58b91c96; lastpath=/read.php?tid=23308833&page=3; lastvisit=1600508967',
  'Host': 'bbs.nga.cn',
  'Pragma': 'no-cache',
  'Referer': 'https://bbs.nga.cn/read.php?tid=23308833&page=3',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

#数据抓取部分
# all_words = []
# #循环抓取
# for i in range(0,54):
#   response = requests.request("GET", url.format(i), headers=headers, data = payload).text
#   #编码转换
#   res = response.encode("ISO-8859-1").decode('gbk')
#
#   html = etree.HTML(res)
#
#   # 提取网友发言
#   s = " ".join(html.xpath('/html/body//span[@class="postcontent ubbcode"]//text()'))
#   all_words.append(s)

# s = " ".join(all_words)
# #对发言进行分词处理，计算权重
# words = jieba.analyse.extract_tags(s,topK=100,withWeight=True)

#权重
tags = [('肉鸽', 0.1626972517374395), ('干员', 0.13579939306037542), ('ac', 0.09116408713166153), ('好玩', 0.07311504790255169), ('模式', 0.06898077621788826), ('希望', 0.06742995761464046), ('游戏', 0.060443721376068835), ('收藏品', 0.05734469955222173), ('体验', 0.05631870428263431), ('练度', 0.05025712495719803), ('随机性', 0.04618222734165323), ('开局', 0.044692344718948035), ('随机', 0.04300009910280686), ('改进', 0.04255633143695117), ('玩家', 0.041842949100857896), ('关卡', 0.040854106193711694), ('优化', 0.04021570631969497), ('但是', 0.03978382234201496), ('box', 0.03856942147877988), ('可以', 0.037694981447680506), ('不错', 0.03539245034320281), ('还是', 0.033111000304404364), ('常驻', 0.032439891185754514), ('玩法', 0.030427678918903064), ('招募', 0.0288534593164902), ('下次', 0.028386164617285523), ('尝试', 0.02778554469476463), ('期待', 0.027221372181699174), ('真的', 0.0264378580055492), ('很多', 0.02541116712034756), ('通关', 0.024463160174756804), ('上头', 0.024100595056870507), ('还有', 0.023822924482442196), ('奖励', 0.02370261505273305), ('活动', 0.023494711871696727), ('难度', 0.023303042452023755), ('事件', 0.023111461915622526), ('感觉', 0.02288911854195288), ('就是', 0.02251390359244855), ('一次', 0.02189022218272474), ('阵容', 0.020058783479135752), ('地图', 0.019992071620676052), ('职业', 0.019850946180730314), ('没有', 0.01978134934103241), ('需要', 0.01953816391465024), ('隐藏', 0.019196783124330548), ('地方', 0.01878000888628391), ('这个', 0.01865883493095615), ('有点', 0.018609376070919493), ('结局', 0.018543165220243435), ('藏品', 0.01746262811275847), ('有趣', 0.017423136792580046), ('方舟', 0.01734311088980789), ('第一次', 0.017305707103013147), ('墓碑', 0.01728070753560053), ('挺好玩', 0.016896698675714913), ('非常', 0.01677811069285819), ('缺点', 0.01640222357882974), ('未来', 0.01627976976466295), ('喜欢', 0.015889306299659775), ('问题', 0.01588737903859608), ('觉得', 0.015815464892243242), ('寒灾', 0.015778399695864496), ('选择', 0.015610733498522756), ('一个', 0.015563536190579753), ('一下', 0.015535168855174268), ('更好', 0.01542735403044288), ('空间', 0.015221878806437893), ('比如', 0.015184357009176322), ('医疗', 0.015110319843143668), ('暴毙', 0.015019287711746591), ('不够', 0.014935298545049127), ('卡其', 0.01474069543598768), ('军校生', 0.014609629348022683), ('蜜饼', 0.014609629348022683), ('一些', 0.014596530225547246), ('来说', 0.014209346905757442), ('阴间', 0.013977459744112039), ('运气', 0.013893536668713886), ('机制', 0.013827200882387447), ('作为', 0.013757020496194457), ('不过', 0.013697865140624725), ('打磨', 0.013492376142930048), ('a2', 0.013440859000180867), ('道具', 0.013191630065667497), ('开心', 0.013118627836630006), ('过于', 0.013095316284675172), ('近卫', 0.012959916881751968), ('虽然', 0.0129538087047133), ('yj', 0.01285647382625996), ('停不下来', 0.012834860099261866), ('这种', 0.01280978408117026), ('重装', 0.012747049551185415), ('保底', 0.012736360421528082), ('总体', 0.012703431727233221), ('有待', 0.01264943578456274), ('塔防', 0.012272088652339053), ('商店', 0.012095385331607762), ('上瘾', 0.01198040557020091), ('合约', 0.011911973852195338)]

#过滤词汇
stop_dict =[
'肉鸽',
'可以',
'但是',
'游戏',
'还是',
'ac',
'没有',
'就是',
'还有',
'a2',
'yj'
]

tags2 = []
for v, k in tags:
  if v not in stop_dict:
    tags2.append((v,k))

from pyecharts.charts import WordCloud

#云词创建
wordcloud = WordCloud()
wordcloud.add("", tags2, word_size_range=[20, 100])
wordcloud.render()