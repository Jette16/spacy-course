import spacy

nlp = spacy.load("zh_core_web_sm")

text = "写入历史了：苹果是美国第一家市值超过一万亿美元的上市公司。"

# 处理文本
doc = ____

# 对识别出的实体进行遍历
for ent in ____.____:
    # 打印实体文本及标注
    print(ent.____, ____.____)
