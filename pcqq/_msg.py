import pcqq.utils as utils

def FaceToStr(faceID:int)->str:
    return "[PQ:face=" + {14: '微笑', 1: '撇嘴', 2: '色', 3: '发呆', 4: '得意', 5: '流泪', 6: '害羞', 7: '闭嘴', 8: '睡', 9: '大哭', 10: '尴尬', 11: '发怒', 12: '调皮', 13: '呲牙', 0: '惊讶', 15: '难过', 16: '酷', 96: '冷汗', 18: '抓狂', 19: '吐', 20: '偷笑', 21: '可爱', 22: '白眼', 23: '傲慢', 24: '饥饿', 25: '困', 26: '惊恐', 27: '流汗', 28: '憨笑', 29: '悠闲', 30: '奋斗', 31: '咒骂', 32: '疑问', 33: '嘘', 34: '晕', 35: '折磨', 36: '衰', 37: '骷髅', 38: '敲打', 39: '再见', 97: '擦汗', 98: '抠鼻', 99: '鼓掌', 100: '糗大了', 101: '坏笑', 102: '左哼哼', 103: '右哼哼', 104: '哈欠', 105: '鄙视', 106: '委屈', 107: '快哭了', 108: '阴险', 305: '右亲亲', 109: '左亲亲', 110: '吓', 111: '可怜', 172: '眨眼睛', 182: '笑哭', 179: 'doge', 173: '泪奔', 174: '无奈', 212: '托腮', 175: '卖萌', 178: '斜眼笑', 177: '喷血', 180: '惊喜', 181: '骚扰', 176: '小纠结', 183: '我最美', 245: '加油必胜', 246: '加油抱抱', 247: '口罩护体', 260: '搬砖中', 261: '忙到飞起', 262: '脑阔疼', 263: '沧桑', 264: '捂脸', 265: '辣眼睛', 266: '哦哟', 267: '头秃', 268: '问号脸', 269: '暗中观察', 270: 'emm', 271: '吃瓜', 272: '呵呵哒', 277: '汪汪', 307: '喵喵', 306: '牛气冲天', 281: '无眼笑', 282: '敬礼', 283: '狂笑', 284: '面无表情', 285: '摸鱼', 293: '摸锦鲤', 286: '魔鬼笑', 287: '哦', 288: '请', 289: '睁眼', 294: '期待', 295: '拿到红包', 296: '真好', 297: '拜谢', 298: '元宝', 299: '牛啊', 300: '胖三斤', 301: '好闪', 303: '右拜年', 302: '左拜年', 304: '红包包', 322: '拒绝', 323: '嫌弃', 311: '打call', 312: '变形', 313: '嗑到了', 314: '仔细分析', 315: '加油', 316: '我没事', 317: '菜狗', 318: '崇拜', 319: '比心', 320: '庆祝', 321: '老色痞', 49: '拥抱', 66: '爱心', 63: '玫瑰', 64: '凋谢', 187: '幽灵', 146: '爆筋', 116: '示爱', 67: '心碎', 60: '咖啡', 185: '羊驼', 192: '红包', 137: '鞭炮', 138: '灯笼', 136: '双喜', 76: '赞', 124: 'OK', 118: '抱拳', 78: '握手', 119: '勾引', 79: '胜利', 120: '拳头', 121: '差劲', 77: '踩', 122: '爱你', 123: 'NO', 201: '点赞', 203: '托脸', 204: '吃', 202: '无聊', 200: '拜托', 194: '不开心', 193: '大笑', 197: '冷漠', 211: '我不看', 210: '飙泪', 198: '呃', 199: '好棒', 207: '花痴', 205: '送花', 206: '害怕', 208: '小样儿', 308: '求红包', 309: '谢红包', 310: '新年烟花', 290: '敲开心', 291: '震惊', 292: '让我康康', 226: '拍桌', 215: '糊脸', 237: '偷看', 214: '啵啵', 235: '颤抖', 222: '抱抱', 217: '扯一扯', 221: '顶呱呱', 225: '撩一撩', 241: '生日快乐', 227: '拍手', 238: '扇脸', 240: '喷脸', 229: '干杯', 216: '拍头', 218: '舔一舔', 233: '掐一掐', 219: '蹭一蹭', 244: '扔狗', 232: '佛系', 243: '甩头', 223: '暴击', 279: '打脸', 280: '击掌', 231: '哼', 224: '开枪', 278: '汗', 236: '啃头', 228: '恭喜', 220: '拽炸天', 239: '原谅', 242: '头撞击', 230: '嘲讽', 234: '惊呆', 273: '我酸了', 75: '月亮', 74: '太阳', 46: '猪头', 112: '菜刀', 56: '刀', 169: '手枪', 171: '茶', 59: '便便', 144: '喝彩', 147: '棒棒糖', 89: '西瓜', 61: '饭', 148: '喝奶', 274: '太南了', 113: '啤酒', 140: 'K歌', 53: '蛋糕', 188: '蛋', 55: '炸弹', 184: '河蟹', 158: '钞票', 54: '闪电', 69: '礼物', 190: '菊花', 151: '飞机', 145: '祈祷', 117: '瓢虫', 168: '药', 114: '篮球', 115: '乒乓', 57: '足球', 41: '发抖', 125: '转圈', 42: '爱情', 43: '跳跳', 86: '怄火', 129: '挥手', 85: '飞吻', 126: '磕头', 128: '跳绳', 130: '激动', 127: '回头', 132: '献吻', 134: '右太极', 133: '左太极', 131: '街舞', 276: '辣椒酱'}.get(faceID,"未知") + "]"

class Message():
    def __init__(self):
        self.MsgType = ""
        self.MsgTime = 0
        self.FromQQ = 0
        self.RecvQQ = 0
        self.FromGroup = 0
        self.MsgText = ""

    def Parse(self, src:bytes):
        unpack = utils.PackDecrypt()
        unpack.SetData(src)

        msgType = unpack.GetByte() # 消息类型
        dataLen = unpack.GetShort() # 数据长度
        pos = unpack.GetPosition()

        while pos+dataLen < len(unpack.GetAll()):
            unpack.GetByte()
            length = unpack.GetShort()

            if msgType == 1:    # 纯文本 && 艾特
                text = unpack.GetBin(length).decode()
                if text[0] == "@" and pos+dataLen-unpack.GetPosition() == 16:
                    unpack.GetBin(10)
                    self.MsgText += text
                    unpack.GetInt()
                else:
                    self.MsgText += text
            
            elif msgType == 2:  # Emoji(系统表情)
                self.MsgText += FaceToStr(unpack.GetByte())
                
            elif msgType == 3:  # 图片
                picStr = unpack.GetBin(length).decode()
                picStr = picStr[1:picStr.find("}")+1].replace("-","")
                self.MsgText += "[PQ:image,file=https://gchat.qpic.cn/gchatpic_new/0/0-0-"+picStr+"/0?term=3]"

            unpack.GetBin(pos + dataLen - unpack.GetPosition())
            msgType = unpack.GetByte()
            dataLen = unpack.GetShort()
            pos = unpack.GetPosition()

            