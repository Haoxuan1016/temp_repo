#!/usr/bin/env python3
"""Generate Unit 5 quiz PDF from PPT exercise content."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    KeepTogether,
)

FONT_PATH = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
OUTPUT_PATH = "/workspace/第五单元小测.pdf"

pdfmetrics.registerFont(TTFont("WQY", FONT_PATH, subfontIndex=0))


def build_styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontName="WQY",
            fontSize=18,
            leading=24,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=11,
            leading=16,
            alignment=TA_CENTER,
            spaceAfter=14,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Heading2"],
            fontName="WQY",
            fontSize=13,
            leading=18,
            spaceBefore=10,
            spaceAfter=6,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=11,
            leading=18,
            spaceAfter=6,
        ),
        "question": ParagraphStyle(
            "Question",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=11,
            leading=18,
            leftIndent=0,
            spaceAfter=4,
        ),
        "answer": ParagraphStyle(
            "Answer",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=10,
            leading=16,
            leftIndent=12,
            textColor="#333333",
            spaceAfter=3,
        ),
        "answer_title": ParagraphStyle(
            "AnswerTitle",
            parent=base["Heading1"],
            fontName="WQY",
            fontSize=16,
            leading=22,
            alignment=TA_CENTER,
            spaceBefore=12,
            spaceAfter=10,
        ),
    }


def p(text, style):
    return Paragraph(text.replace("\n", "<br/>"), style)


def section(title, questions, styles):
    items = [p(title, styles["section"])]
    for q in questions:
        items.append(p(q, styles["question"]))
        items.append(Spacer(1, 0.15 * cm))
    return items


QUESTIONS = [
    (
        "一、课文内容",
        [
            "1. 根据课文《胡萝卜先生的长胡子》，完成填空。",
            "课文讲述了胡萝卜先生________后的一段有趣的经历。这根胡子吸收了果酱的营养，长得很________，先后被小男孩用来________，被鸟太太用来________，被胡萝卜先生用来________，让我们感受到想象不仅能创造出奇妙的情节，还能传递出________。",
            "2. 根据课文《我变成了一棵树》，完成填空。",
            "课文讲述了“我”________之后发生的一连串奇妙的事情：小动物们住进________，妈妈坐在鸟窝里________，“我”馋得________。",
        ],
    ),
    (
        "二、我会认",
        [
            "1. 给下列生字注音。",
            "《胡萝卜先生的长胡子》：萝（　　）  卜（　　）  愁（　　）  晾（　　）  尿（　　）  肩（　　）  掏（　　）",
            "《我变成了一棵树》：嗓（　　）  痒（　　）  椭（　　）  菱（　　）  鳄（　　）  震（　　）  零（　　）  肠（　　）  啃（　　）  醋（　　）  馋（　　）",
            "2. 选出加点字正确的读音，画“√”。",
            "愁苦（chóu　cóu）　　椭圆（tuǒ　duǒ）　　嗓子（sǎnɡ　sǎn）",
            "吃醋（chù　cù）　　　啃食（kěn　kěnɡ）　菱形（lín　línɡ）",
            "鳄鱼（è　èr）　　　　嘴馋（cán　chán）　　晾晒（liànɡ　liàn）",
            "3. 下列词语中加点字跟“系绳子”中的“系”读音相同的一项是（　　）。",
            "A. 关系　　B. 系扣　　C. 联系　　D. 系列",
        ],
    ),
    (
        "三、我会写",
        [
            "1. 读语段，看拼音写词语。",
            "我在充满 xī wàng（　　　）的乐园中遨游，这里藏着吃不完的 líng shí（　　　）与数不清的秘密：xíng zhuàng（　　　）各异的 qiǎo kè lì（　　　）、云朵捏成的 xiāng cháng（　　　）和 miàn bāo（　　　），还有十分奇妙的糖果城堡——城堡的门上没有系锁链，门会随着微风轻轻旋转。我 què shí（　　　）很 xǐ huān（　　　）这个充满惊喜的乐园。在这里漫步，任思绪飞扬，连快乐都变得格外 róng yì（　　　）。",
            "2. 下面有四组词语，只有一组书写完全正确，它是（　　）。",
            "A. 面包　相念　但心　　B. 发愁　确定　眼晴",
            "C. 洁实　一段　震惊　　D. 形状　牛奶　互相",
        ],
    ),
    (
        "四、词语积累与运用",
        [
            "1. 把词语和意思连一连（在括号里填序号）。",
            "词语：A. 发愁　B. 浓密　C. 足够　D. 机灵",
            "意思：① 达到应有的或能满足需要的程度。",
            "　　　② 多指枝叶、烟雾、须发等距离短、空隙小。",
            "　　　③ 因为没有主意或办法而愁闷。",
            "　　　④ 聪明伶俐，机智。",
            "A（　　）　B（　　）　C（　　）　D（　　）",
            "2. 把词语和意思连一连（在括号里填序号）。",
            "词语：A. 陆续　B. 持续　C. 继续　D. 连续",
            "意思：① 长时间保持某种状态，不中断（多指时间、天气、情况）。",
            "　　　② 停下来之后，接着往下做原来的事。",
            "　　　③ 一个接着一个，中间不停、没有间断。",
            "　　　④ 先后一个接一个，有先有后、中间有间隔，不是同时。",
            "A（　　）　B（　　）　C（　　）　D（　　）",
            "3. 选词填空：陆续　持续　继续　连续",
            "月光洒落，小精灵们________现身，魔法派对开始了。派对会一直________到天亮，第二天晚上月亮升起时，精灵们会________狂欢。",
            "4. 写出下列词语的近义词。",
            "发愁—（　　　）　浓密—（　　　）　必须—（　　　）　发现—（　　　）　结实—（　　　）",
            "机灵—（　　　）　希望—（　　　）　担心—（　　　）　失望—（　　　）",
            "5. 写出下列词语的反义词。",
            "浓密—（　　　）　匆匆忙忙—（　　　）　继续—（　　　）　秘密—（　　　）",
            "6. 下面是“密”在字典中的意思，我知道“秘密”中“密”的意思是（　　）。",
            "① 事物间距离短，空隙小，跟“稀”“疏”相对。",
            "② 关系近；感情好。",
            "③ 不公开。",
            "④ 秘密的事物。",
            "7. 选择恰当的词语填在括号里。",
            "小朋友们（　　）走进体育馆。乒乓球单打比赛中，两个运动员高超的球技博得观众一片喝彩，掌声（　　）了一分钟。",
            "A. 陆续　　B. 继续　　C. 持续　　D. 连续",
            "8. “我”变成了一棵树。下面句子中画线部分不能用词语（　　）来形容。",
            "我变的树上长满了各种形状的鸟窝：三角形的、正方形的，还有长方形的、圆形的、椭圆形的、菱形的……",
            "A. 各种各样　　B. 形态各异　　C. 五彩缤纷　　D. 奇形怪状",
        ],
    ),
    (
        "五、句子赏析",
        [
            "1. 阅读句子，完成填空。",
            "于是，胡萝卜先生一步一步走的时候，这根胡子就在一点儿一点儿地变长。只要看看胡萝卜先生走了多长的路，就可以知道他的这根胡子已经长了多长了。",
            "胡萝卜先生的胡子能________，并且能跟他走的路一样长，这是作者的________，显示出了________的神奇有趣。",
            "2. 风一吹，它们就在枝头跳起了舞。",
            "“它们”指的是长在树上的各种形状的________。鸟窝在枝头跳起了舞，这是运用了________的修辞手法，反映了英英________________________。",
            "3. 她不知道我变成了树！我有点儿高兴，又有些失望。",
            "这两句话写出了“我”________的心情：“我”高兴的是________________________；“我”失望的是________________________。",
            "4. 你怎么住进来？别担心，我会弯下腰，让鸟窝离你很近很近，你只需轻轻一跳或者轻轻一爬，就像平时上你的小床那么容易。",
            "这是一个________句，先引发思考，再通过奇特的想象，写“我”变成的树会弯下腰，让“你”轻松地住进来，解答了这一疑问。同时还体现出“我”是一棵________的树。",
        ],
    ),
    (
        "六、拓展练习",
        [
            "1. 下面问句的句式与其他三项不同的是哪一项？（　　）",
            "A. 是你的牛奶打翻了吗？",
            "B. 小馋猫，肚子饿了，对吧？",
            "C. 你猜，我变的树上会长什么？当然不是苹果啦，梨也不对——对了，鸟窝！",
            "D. 哎呀，她是怎么知道我的秘密的？",
            "2. 下列哪一项内容不属于想象描写？（　　）",
            "A. 暑假里，我和家人去海滩上捡贝壳，抓小螃蟹，有趣极了！",
            "B. 小哪吒踏着风火轮来到21世纪，带着我进行了一场刺激的大冒险。",
            "C. 小明发现自己能听懂动物的语言，于是他帮小动物们实现了它们的愿望。",
            "D. 琳琳来到了外星球，和外星人做了好朋友。",
            "3. 下面和例句所运用的修辞手法不同的是哪一项？（　　）",
            "例：风一吹，它们就在枝头跳起了舞。",
            "A. 巨浪伸出双臂把我猛地托起。",
            "B. 海棠果摇动着它那圆圆的小脸，冲着你点头微笑。",
            "C. 美丽的彩虹就像一座七彩的桥一样高挂在雨后的天空。",
            "D. 宁静的夜晚，只有那天上的星星在窃窃私语。",
        ],
    ),
    (
        "七、梳理与交流",
        [
            "1. 根据课文内容，写出胡萝卜先生的长胡子在课文中分别被用来做什么（写出三种用途）。",
            "（1）小男孩用来当________　（2）鸟太太用来当________　（3）胡萝卜先生用来当________",
            "2. 手指印姑娘会七十二变，她会变成小猪、小兔子、小青蛙……她还会变成什么呢？会做什么或想些什么呢？写一写。",
            "________________________________________________________________________",
            "________________________________________________________________________",
        ],
    ),
    (
        "八、初试身手与习作",
        [
            "1. 根据事物的特点发挥想象。",
            "铅笔躲进菜园里，想在青叶间，长成长长的豆角，或伪装成嫩嫩的丝瓜。",
            "小皮球躲进菜园里，想在青叶间，长成________________，或伪装成________________。",
            "2. 结合场景特点想象。",
            "胡萝卜先生继续往前走，当他走过________________，学生们正在找________。________________，________________。",
            "3. 把自己想象成别的事物。",
            "如果我是一支铅笔，我想跑到小河边变成孩子手中的钓竿和鱼儿做游戏。",
            "如果我是________________，我想________________________________________。",
        ],
    ),
]

ANSWERS = [
    (
        "一、课文内容",
        [
            "1. 漏刮了一根胡子；很长很长；放风筝；晾尿布；系眼镜；善意与美好",
            "2. 变成一棵树；各种形状的鸟窝；给小动物分食物；直流口水",
        ],
    ),
    (
        "二、我会认",
        [
            "1. luó bo；chóu；liàng；niào；jiān；tāo；sǎng；yǎng；tuǒ；líng；è；zhèn；líng；cháng；kěn；cù；chán",
            "2. chóu；tuǒ；sǎng；cù；kěn；línɡ；è；chán；liànɡ",
            "3. B",
        ],
    ),
    (
        "三、我会写",
        [
            "1. 希望；零食；形状；巧克力；香肠；面包；确实；喜欢；容易",
            "2. D",
        ],
    ),
    (
        "四、词语积累与运用",
        [
            "1. A—③；B—②；C—①；D—④",
            "2. A—④；B—①；C—②；D—③",
            "3. 陆续；持续；继续",
            "4. 犯愁；稠密；务必；发觉；坚固；伶俐；期望；担忧；失落",
            "5. 稀疏；不慌不忙；中止；公开",
            "6. ③",
            "7. A；C",
            "8. C",
        ],
    ),
    (
        "五、句子赏析",
        [
            "1. 不断变长；想象；想象",
            "2. 鸟窝；拟人；丰富的想象力和快乐的心情",
            "3. 复杂；妈妈没有发现“我”的秘密；妈妈竟然没有发现“我”的变化",
            "4. 设问；热情好客",
        ],
    ),
    (
        "六、拓展练习",
        [
            "1. C",
            "2. A",
            "3. C",
        ],
    ),
    (
        "七、梳理与交流",
        [
            "1. 风筝线；晾衣绳；眼镜绳",
            "2. 示例：她会变成小鸟，在枝头叽叽喳喳，唱着“风雨过后天空会更蓝”。（答案不唯一）",
        ],
    ),
    (
        "八、初试身手与习作",
        [
            "1. 圆圆的包菜；金黄的南瓜",
            "2. 学校的操场；跳绳；学生们剪了一段胡子；甩起来当跳绳",
            "3. 一条鱼；在大海里自由自在地游玩（答案不唯一，合理即可）",
        ],
    ),
]


def build_pdf():
    styles = build_styles()
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title="第五单元小测",
    )

    story = [
        p("语文 · 三年级下册", styles["subtitle"]),
        p("第五单元小测", styles["title"]),
        p("姓名：__________　　班级：__________　　得分：__________", styles["subtitle"]),
        Spacer(1, 0.3 * cm),
    ]

    for title, questions in QUESTIONS:
        story.extend(section(title, questions, styles))
        story.append(Spacer(1, 0.2 * cm))

    story.append(PageBreak())
    story.append(p("参考答案", styles["answer_title"]))

    for title, answers in ANSWERS:
        story.append(p(title, styles["section"]))
        for ans in answers:
            story.append(p(f"　{ans}", styles["answer"]))
        story.append(Spacer(1, 0.15 * cm))

    doc.build(story)
    print(f"Generated: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
