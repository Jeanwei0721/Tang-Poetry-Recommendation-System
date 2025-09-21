from tkinter import *
import os
from PIL import Image, ImageTk
import customtkinter
import pywinstyles
from math import ceil
from Poetry_Recommendation import PoetryRecommender,User


global csv_path, model_path, author, title, text, tags, main_poetry
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(THIS_FOLDER, 'all-MiniLM-L6-v2-Q8_0.gguf')
csv_path = os.path.join(THIS_FOLDER, 'Tang Poetry Dataset.csv')
recommender = PoetryRecommender(model_path, csv_path)
user = User(recommender)

author = [""] * 5
title = [""] * 5
text = [""] * 5
p_n = [0, 1, 2, 3, 4]
main_poetry = 0 # 顯示在正中央的詩編號
tags = []
# author = ["白居易", "李世民", "李白", "李白"]
# title = ["宮詞", "自河南經亂，關內阻饑，兄弟離散，各在一處。因望月有感，聊書所懷，寄上浮梁大兄，於潛七兄，烏江十五兄，兼示符離及下邽弟妹。", 
#          "帝京篇十首", "奉和聖制從蓬萊向興慶閣道中留春雨中春望之作應制",
#          "樂府雜曲。鼓吹曲辭。有所思", "獨不見（古意呈補闕喬知之）",
#          "關山月", "至德二載甫自金光門出，間道歸鳳翔。乾元初從左拾遺移華州掾，與親故別，因出此門，有悲往事。"
#          ]
# text = ["淚盡羅巾夢不成，夜深前殿按歌聲。紅顏未老恩先斷，斜倚薰籠坐到明。", 
#         "鄉心新歲切，天畔獨潸然。老至居人下，春歸在客先。嶺猿同旦暮，江柳共風煙。已似長沙傅，從今又幾年？",
#         "三年謫宦此棲遲，萬古惟留楚客悲。秋草獨尋人去後，寒林空見日斜時。漢文有道恩猶薄，湘水無情弔豈知。寂寂江山搖落處，憐君何事到天涯。",
#         "明月出天山，蒼茫雲海間。長風幾萬里，吹度玉門關。漢下白登道，胡窺青海灣。由來征戰地，不見有人還。戍客望邊色，思歸多苦顏。高樓當此夜，歎息未應閒。", 
#         "絕頂一茅茨，直上三十里。叩關無僮僕，窺室惟案几。若非巾柴車，應是釣秋水。差池不相見，黽勉空仰止。草色新雨中，松聲晚窗裡。及茲契幽絕，自足蕩心耳。雖無賓主意，頗得清淨理。興盡方下山，何必待之子。",
#         "永日方慼慼，出門復悠悠。女子今有行，大江泝輕舟。爾輩苦無恃，撫念益慈柔。幼為長所育，兩別泣不休。對此結中腸，義往難復留。自小闕內訓，事姑貽我憂。賴茲託令門，仁卹庶無尤。貧儉誠所尚，資從豈待周。孝恭遵婦道，容止順其猷。別離在今晨，見爾當何秋？居閑始自遣，臨感忽難收。歸來視幼女，零淚緣纓流。",
#         "國初已來畫鞍馬，神妙獨數江都王。將軍得名三十載，人間又見真乘黃。曾貌先帝照夜白，龍池十日飛霹靂。內府殷紅瑪瑙盤，婕妤傳詔才人索。盤賜將軍拜舞歸，輕紈細綺相追飛。貴戚權門得筆跡，始覺屏障生光輝。昔日太宗拳毛騧，近時郭家獅子花。今之新圖有二馬，復令識者久歎嗟。此皆騎戰一敵萬，縞素漠漠開風沙。其餘七匹亦殊絕，迥若寒空動煙雪。霜蹄蹴踏長楸間，馬官廝養森成列。可憐九馬爭神駿，顧視清高氣深穩。借問苦心愛者誰，後有韋諷前支遁。憶昔巡幸新豐宮，翠華拂天來向東。騰驤磊落三萬匹，皆與此圖筋骨同。自從獻寶朝河宗，無復射蛟江水中。君不見金粟堆前松柏裡，龍媒去盡鳥呼風。",
#         "張生手持石鼓文，勸我試作石鼓歌。少陵無人謫仙死，才薄將奈石鼓何。周綱陵夷四海沸，宣王憤起揮天戈。大開明堂受朝賀，諸侯劍佩鳴相磨。蒐於岐陽騁雄俊，萬里禽獸皆遮羅。鐫功勒成告萬世，鑿石作鼓隳嵯峨。從臣才藝咸第一，揀選撰刻留山阿。雨淋日炙野火燎，鬼物守護煩撝呵。公從何處得紙本，毫髮盡備無差訛。辭嚴義密讀難曉，字體不類隸與蝌。年深豈免有缺畫，快劍斫斷生蛟鼉。鸞翔鳳翥眾仙下，珊瑚碧樹交枝柯。金繩鐵索鎖鈕壯，古鼎躍水龍騰梭。陋儒編詩不收入，二雅褊迫無委蛇。孔子西行不到秦，掎摭星宿遺羲娥。嗟予好古生苦晚，對此涕淚雙滂沱。憶昔初蒙博士徵，其年始改稱元和。故人從軍在右輔，為我度量掘臼科。濯冠沐浴告祭酒，如此至寶存豈多？氈包席裹可立致，十鼓祇載數駱駝。薦諸太廟比郜鼎，光價豈止百倍過？聖恩若許留太學，諸生講解得切磋。觀經鴻都尚填咽，坐見舉國來奔波。剜苔剔蘚露節角，安置妥帖平不頗。大廈深簷與蓋覆，經歷久遠期無佗。中朝大官老於事，詎肯感激徒媕婀。牧童敲火牛礪角，誰復著手為摩挲。日銷月鑠就埋沒，六年西顧空吟哦。羲之俗書趁姿媚，數紙尚可博白鵝。繼周八代爭戰罷，無人收拾理則那？方今太平日無事，柄任儒術崇丘軻。安能以此上論列，願借辨口如懸河。石鼓之歌止於此，嗚呼吾意其蹉跎。", "二月黃鸝飛上林，春城紫禁曉陰陰。長樂鐘聲花外盡，龍池柳色雨中深。陽和不散窮途恨，霄漢長懸捧日心。獻賦十年猶未遇，羞將白髮對華簪。"
#         ]

# 載入圖片
def relative_to_assets(asset):
    return os.path.join(THIS_FOLDER, asset)

class Controller(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.current_frame = None  # 用來追蹤當前的 Frame

        # 背景圖片1
        self.bg_file = relative_to_assets("bg.png")
        # 使用 Pillow 加載並調整圖片大小
        img = Image.open(self.bg_file)
        target_width = img.width  # 寬度不變
        target_height = int(img.height * ((self.winfo_screenheight() - 80) / img.height))        
        # 調整圖片大小
        img_resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        self.bg_file = ImageTk.PhotoImage(img_resized)
        # 顯示圖片
        self.bg_photo = Label(self, image = self.bg_file, borderwidth = 0) 
        self.bg_photo.place(x = 0,y = 0) 

        # 標題
        self.title_file = relative_to_assets("title_text.png")
        img3 = Image.open(self.title_file)
        self.title_image = ImageTk.PhotoImage(img3)
        self.title_photo = customtkinter.CTkLabel(self, image = self.title_image, text = "", bg_color = "#FBF8EF")
        self.title_photo.place(x = 33, y = 20)
        pywinstyles.set_opacity(self.title_photo, color = "#FBF8EF")


        # 預設顯示 FrameA
        self.show_frame(FrameA)

    def show_frame(self, frame_class):
        """顯示新 Frame 並清除舊 Frame"""
        if self.current_frame is not None:
            # 清理當前 Frame 的所有元件
            self.current_frame.destroy()
        # 創建並顯示新的 Frame
        self.current_frame = frame_class(self)
        self.current_frame.pack(fill=BOTH, expand=True)

    def switch_frame(self):
        """切換 Frame"""
        # 切換到另一個 Frame
        if isinstance(self.current_frame, FrameA):
            self.show_frame(FrameB)
        else:
            self.show_frame(FrameA)

class FrameA(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        # 背景圖片1
        self.bg_file = relative_to_assets("bg.png")
        # 使用 Pillow 加載並調整圖片大小
        img = Image.open(self.bg_file)
        target_width = img.width  # 寬度不變
        target_height = int(img.height * ((self.winfo_screenheight() - 80) / img.height))        
        # 調整圖片大小
        img_resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        self.bg_file = ImageTk.PhotoImage(img_resized)
        # 顯示圖片
        self.bg_photo = Label(self, image = self.bg_file, borderwidth = 0) 
        self.bg_photo.place(x = 0,y = 0) 

        # 標題
        self.title_file = relative_to_assets("title_text.png")
        img3 = Image.open(self.title_file)
        self.title_image = ImageTk.PhotoImage(img3)
        self.title_photo = customtkinter.CTkLabel(self, image = self.title_image, text = "", bg_color = "#FBF8EF")
        self.title_photo.place(x = 33, y = 20)
        pywinstyles.set_opacity(self.title_photo, color = "#FBF8EF")


        # 背景圖片2
        self.choose_bg_file = relative_to_assets("choose_bg.png")
        img2 = Image.open(self.choose_bg_file)
        self.choose_bg_image = ImageTk.PhotoImage(img2)
        self.choose_bg_photo = customtkinter.CTkLabel(self, image = self.choose_bg_image, text = "", bg_color = "#FBF8EE")
        self.choose_bg_photo.place(x = (self.winfo_screenwidth() - img2.width)/2, y = (self.winfo_screenheight() - 708))
        # 紀錄背景圖片2座標，當作選項的初始座標
        self.bg2_x = (self.winfo_screenwidth() - img2.width)/2
        self.bg2_y = (self.winfo_screenheight() - 708)
        print("x: ", self.bg2_x, " y: ", self.bg2_y)

        # 標題
        self.choose_title_file = relative_to_assets("title_text.png")
        img3 = Image.open(self.choose_title_file)
        self.choose_title_image = ImageTk.PhotoImage(img3)
        self.choose_title_photo = customtkinter.CTkLabel(self, image = self.choose_title_image, text = "", bg_color = "#FBF8EF")
        self.choose_title_photo.place(x = 33, y = 20)
        pywinstyles.set_opacity(self.choose_title_photo, color = "#FBF8EF")

        self.show_tags()


    def tag_clicked(self, num, option):
        global tags
        if option not in tags:  # 檢查 tag 是否已存在 tags
            if num < 4:         # 換不同 bttn 顏色
                self.tag[num].configure(fg_color = "#C7B57E")#, hover_color = "#ECE9D1"
            elif num < 10:
                self.tag[num].configure(fg_color = "#C3BC80")
            elif num < 14:
                self.tag[num].configure(fg_color = "#B1BF83")
            else:
                self.tag[num].configure(fg_color = "#BBB972")
            tags.append(option)  
            user.select_tag(option)   # 加入標籤
        else:
            if num < 4:
                self.tag[num].configure(fg_color = "#EADFBF")#, hover_color = "#ECE9D1"
            elif num < 10:
                self.tag[num].configure(fg_color = "#E7E3C0")
            elif num < 14:
                self.tag[num].configure(fg_color = "#D5DEB6")
            else:
                self.tag[num].configure(fg_color = "#E9E7B9")
            tags.remove(option)
            user. remove_tag(option)     # 刪除標籤
        print(tags)

    def recommend(self):
        # global tags
        # results = " ".join(tags) + " " + self.search_textbox.get("0.0", "end")
        global author, title, text
        author,title,text = user.recommend_poetry(self.search_textbox.get("0.0", "end"))
        
        # print("推薦結果", results)
        self.master.switch_frame()
        


    # 顯示選項
    def show_tags(self):
        self.ment = customtkinter.CTkLabel(self, text = "請選擇您感興趣的唐詩標籤 ( 可複選 )", text_color = "black", font = ("Noto Sans TC", 20), bg_color = "#FBF8EE")
        self.ment.place(x = self.bg2_x + 317, y = self.bg2_y + 88)
        pywinstyles.set_opacity(self.ment, color="#FBF8EE")

        self.tag = {}
        self.tag[0] = customtkinter.CTkButton(self, text = "春季", text_color= "#362A22", width = 55, fg_color = "#EADFBF", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#C7B57E", command = lambda: self.tag_clicked(0, "春季"))
        self.tag[0].place(x = self.bg2_x + 317, y = self.bg2_y + 145)        
        pywinstyles.set_opacity(self.tag[0], color="#FBF8EE")
        self.tag[1] = customtkinter.CTkButton(self, text = "夏季", text_color= "#362A22", width = 55, fg_color = "#EADFBF", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#C7B57E", command = lambda: self.tag_clicked(1, "夏季"))
        self.tag[1].place(x = self.bg2_x + 392, y = self.bg2_y + 145)        
        pywinstyles.set_opacity(self.tag[1], color="#FBF8EE")
        self.tag[2] = customtkinter.CTkButton(self, text = "秋季", text_color= "#362A22", width = 55, fg_color = "#EADFBF", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#C7B57E", command = lambda: self.tag_clicked(2, "秋季"))
        self.tag[2].place(x = self.bg2_x + 467, y = self.bg2_y + 145)        
        pywinstyles.set_opacity(self.tag[2], color="#FBF8EE")
        self.tag[3] = customtkinter.CTkButton(self, text = "冬季", text_color= "#362A22", width = 55, fg_color = "#EADFBF", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#C7B57E", command = lambda: self.tag_clicked(3, "冬季"))
        self.tag[3].place(x = self.bg2_x + 542, y = self.bg2_y + 145)        
        pywinstyles.set_opacity(self.tag[3], color="#FBF8EE")

        self.tag[4] = customtkinter.CTkButton(self, text = "喜", text_color= "#362A22", width = 39, fg_color = "#E7E3C0", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#C3BC80", command = lambda: self.tag_clicked(4, "喜"))
        self.tag[4].place(x = self.bg2_x + 317, y = self.bg2_y + 208)        
        pywinstyles.set_opacity(self.tag[4], color="#FBF8EE")
        self.tag[5] = customtkinter.CTkButton(self, text = "怒", text_color= "#362A22", width = 39, fg_color = "#E7E3C0", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#C3BC80", command = lambda: self.tag_clicked(5, "怒"))
        self.tag[5].place(x = self.bg2_x + 376, y = self.bg2_y + 208)        
        pywinstyles.set_opacity(self.tag[5], color="#FBF8EE")
        self.tag[6] = customtkinter.CTkButton(self, text = "哀", text_color= "#362A22", width = 39, fg_color = "#E7E3C0", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#C3BC80", command = lambda: self.tag_clicked(6, "哀"))
        self.tag[6].place(x = self.bg2_x + 435, y = self.bg2_y + 208)        
        pywinstyles.set_opacity(self.tag[6], color="#FBF8EE")
        self.tag[7] = customtkinter.CTkButton(self, text = "樂", text_color= "#362A22", width = 39, fg_color = "#E7E3C0", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#C3BC80", command = lambda: self.tag_clicked(7, "樂"))
        self.tag[7].place(x = self.bg2_x + 494, y = self.bg2_y + 208)        
        pywinstyles.set_opacity(self.tag[7], color="#FBF8EE")
        self.tag[8] = customtkinter.CTkButton(self, text = "愉悅", text_color= "#362A22", width = 55, fg_color = "#E7E3C0", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#C3BC80", command = lambda: self.tag_clicked(8, "愉悅"))
        self.tag[8].place(x = self.bg2_x + 553, y = self.bg2_y + 208)        
        pywinstyles.set_opacity(self.tag[8], color="#FBF8EE")
        self.tag[9] = customtkinter.CTkButton(self, text = "惆悵", text_color= "#362A22", width = 55, fg_color = "#E7E3C0", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#C3BC80", command = lambda: self.tag_clicked(9, "惆悵"))
        self.tag[9].place(x = self.bg2_x + 628, y = self.bg2_y + 208)        
        pywinstyles.set_opacity(self.tag[9], color="#FBF8EE")

        self.tag[10] = customtkinter.CTkButton(self, text = "抒情", text_color= "#362A22", width = 55, fg_color = "#D5DEB6", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#B1BF83", command = lambda: self.tag_clicked(10, "抒情"))
        self.tag[10].place(x = self.bg2_x + 317, y = self.bg2_y + 271)        
        pywinstyles.set_opacity(self.tag[10], color="#FBF8EE")
        self.tag[11] = customtkinter.CTkButton(self, text = "歷史", text_color= "#362A22", width = 55, fg_color = "#D5DEB6", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#B1BF83", command = lambda: self.tag_clicked(11, "歷史"))
        self.tag[11].place(x = self.bg2_x + 392, y = self.bg2_y + 271)        
        pywinstyles.set_opacity(self.tag[11], color="#FBF8EE")
        self.tag[12] = customtkinter.CTkButton(self, text = "戰爭", text_color= "#362A22", width = 55, fg_color = "#D5DEB6", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#B1BF83", command = lambda: self.tag_clicked(12, "戰爭"))
        self.tag[12].place(x = self.bg2_x + 467, y = self.bg2_y + 271)        
        pywinstyles.set_opacity(self.tag[12], color="#FBF8EE")
        self.tag[13] = customtkinter.CTkButton(self, text = "山水", text_color= "#362A22", width = 55, fg_color = "#D5DEB6", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#B1BF83", command = lambda: self.tag_clicked(13, "山水"))
        self.tag[13].place(x = self.bg2_x + 542, y = self.bg2_y + 271)        
        pywinstyles.set_opacity(self.tag[13], color="#FBF8EE")

        self.tag[14] = customtkinter.CTkButton(self, text = "官場", text_color= "#362A22", width = 55, fg_color = "#E9E7B9", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#BBB972", command = lambda: self.tag_clicked(14, "官場"))
        self.tag[14].place(x = self.bg2_x + 317, y = self.bg2_y + 332)        
        pywinstyles.set_opacity(self.tag[14], color="#FBF8EE")
        self.tag[15] = customtkinter.CTkButton(self, text = "酒", text_color= "#362A22", width = 39, fg_color = "#E9E7B9", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#BBB972", command = lambda: self.tag_clicked(15, "酒"))
        self.tag[15].place(x = self.bg2_x + 392, y = self.bg2_y + 332)        
        pywinstyles.set_opacity(self.tag[15], color="#FBF8EE")
        self.tag[16] = customtkinter.CTkButton(self, text = "光陰", text_color= "#362A22", width = 55, fg_color = "#E9E7B9", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#BBB972", command = lambda: self.tag_clicked(16, "光陰"))
        self.tag[16].place(x = self.bg2_x + 451, y = self.bg2_y + 332)        
        pywinstyles.set_opacity(self.tag[16], color="#FBF8EE")
        self.tag[17] = customtkinter.CTkButton(self, text = "英雄", text_color= "#362A22", width = 55, fg_color = "#E9E7B9", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#BBB972", command = lambda: self.tag_clicked(17, "英雄"))
        self.tag[17].place(x = self.bg2_x + 526, y = self.bg2_y + 332)        
        pywinstyles.set_opacity(self.tag[17], color="#FBF8EE")
        self.tag[18] = customtkinter.CTkButton(self, text = "花鳥", text_color= "#362A22", width = 55, fg_color = "#E9E7B9", font = ("Noto Sans TC", 16), corner_radius = 100, bg_color = "#FBF8EE", hover_color = "#BBB972", command = lambda: self.tag_clicked(18, "花鳥"))
        self.tag[18].place(x = self.bg2_x + 601, y = self.bg2_y + 332)        
        pywinstyles.set_opacity(self.tag[18], color="#FBF8EE")

        self.ment = customtkinter.CTkLabel(self, text = "或輸入您喜歡的唐詩標籤 ( 可留空 )", text_color = "black", font = ("Noto Sans TC", 20), bg_color = "#FBF8EE")
        self.ment.place(x = self.bg2_x + 317, y = self.bg2_y + 400)
        pywinstyles.set_opacity(self.ment, color="#FBF8EE")

        self.search_textbox = customtkinter.CTkTextbox(self, width = 301, height = 20, text_color = "black", font = ("Noto Sans TC", 16), corner_radius = 5, fg_color = "white", bg_color = "#FBF8EE", border_width = 2, border_color = "#978C6F")
        self.search_textbox.place(x = self.bg2_x + 317, y = self.bg2_y + 456)
        pywinstyles.set_opacity(self.search_textbox, color="#FBF8EE")

        self.recommend_button = customtkinter.CTkButton(self, text = "推薦", text_color= "white", width = 196, fg_color = "#97896F", font = ("Noto Sans TC", 16), corner_radius = 50, bg_color = "#FBF8EE", hover_color = "#7A6F5A", command = lambda: self.recommend())
        self.recommend_button.place(x = self.bg2_x + 317, y = self.bg2_y + 545)        
        pywinstyles.set_opacity(self.recommend_button, color="#FBF8EE")
        print("show option")

class FrameB(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        # 背景圖片1
        self.bg_file = relative_to_assets("bg.png")
        # 使用 Pillow 加載並調整圖片大小
        img = Image.open(self.bg_file)
        target_width = img.width  # 寬度不變
        target_height = int(img.height * ((self.winfo_screenheight() - 80) / img.height))        
        # 調整圖片大小
        img_resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        self.bg_file = ImageTk.PhotoImage(img_resized)
        # 顯示圖片
        self.bg_photo = Label(self, image = self.bg_file, borderwidth = 0) 
        self.bg_photo.place(x = 0,y = 0) 

        # 標題
        self.title_file = relative_to_assets("title_text.png")
        img3 = Image.open(self.title_file)
        self.title_image = ImageTk.PhotoImage(img3)
        self.title_photo = customtkinter.CTkLabel(self, image = self.title_image, text = "", bg_color = "#FBF8EF")
        self.title_photo.place(x = 33, y = 20)
        pywinstyles.set_opacity(self.title_photo, color = "#FBF8EF")

        # 返回按鈕
        self.back_btn_file = relative_to_assets("back_btn.png")
        img4 = Image.open(self.back_btn_file)
        self.back_btn_image = ImageTk.PhotoImage(img4)
        self.back_btn_hover_file = relative_to_assets("back_btn2.png")
        img5 = Image.open(self.back_btn_hover_file)
        self.back_btn_hover_image = ImageTk.PhotoImage(img5)
        self.back_btn_photo = customtkinter.CTkLabel(self, image = self.back_btn_image, text = "", bg_color = "#FBF8EF")
        self.back_btn_photo.place(x = 33, y = 85)
        pywinstyles.set_opacity(self.back_btn_photo, color = "#FBF8EF")
        # 綁定滑鼠事件
        self.back_btn_photo.bind("<Enter>", self.on_hover)
        self.back_btn_photo.bind("<Leave>", self.off_hover)
        self.back_btn_photo.bind("<Button-1>", self.on_back_click)


        """ 唐詩的畫面背景設置 """
        # 唐詩 1
        # 背景
        self.main_poetry_frame = customtkinter.CTkFrame(self, width = 453, height = 323, border_width = 1, fg_color = "#FBF8EE", bg_color = "#FBF8EF", border_color = "#97896F", corner_radius = 20)
        self.main_poetry_frame.place(x = 541, y = 252)        
        pywinstyles.set_opacity(self.main_poetry_frame, color = "#FBF8EF")
        # 文字 frame
        self.in_main_frame = customtkinter.CTkFrame(self.main_poetry_frame, width = 366, border_width = 0, fg_color = "#FBF8EE", bg_color = "#FBF8EF", corner_radius = 0)
        self.in_main_frame.place(x = 44, y = 25)
        # grid frame
        self.in_main_poetry_title_frame = customtkinter.CTkFrame(self.in_main_frame, border_width = 0, fg_color = "#FBF8EE", bg_color = "#FBF8EF", corner_radius = 0)
        self.in_main_poetry_title_frame.grid(row = 0, column = 0, sticky = W, padx = 0)
        

        # 排版用 - 計算座標
        self.h = ((self.winfo_screenheight() - 80 - 166*4)*0.3)/3
        self.h2 = ((self.winfo_screenheight() - 80 - 166*4)*0.7)/2

        self.poetry_text_frame = {}
        for i in range(4):
            self.poetry_text_frame[i] = customtkinter.CTkFrame(self, width=289, height=166, border_width=0, fg_color="#EDE7D6", bg_color="#EDE7D8", corner_radius=20)
            self.poetry_text_frame[i].place(x=1237, y=self.h2 + 166 * i + self.h * i)
            pywinstyles.set_opacity(self.poetry_text_frame[i], color="#EDE7D8")
            self.poetry_text_frame[i].bind("<Enter>", lambda event, idx=i: self.on_hover_side_poetry(idx))
            self.poetry_text_frame[i].bind("<Leave>", lambda event, idx=i: self.off_hover_side_poetry(idx))
            self.poetry_text_frame[i].bind("<Button-1>", lambda event, idx=i: self.change_main_poetry(idx))


        """ 唐詩的文字內容顯示 """
        global title, author, text, main_poetry
        # 第一推薦的唐詩 frame 內文字
        self.poetry1_title = customtkinter.CTkLabel(self.in_main_poetry_title_frame, text = title[0], text_color = "black", fg_color = "#FBF8EE", font = ("微軟正黑體", 20, "bold"), wraplength = 370, justify = "left")
        self.poetry1_title.grid(row = 0, column = 0, sticky = W)
        self.poetry1_author = customtkinter.CTkLabel(self.in_main_poetry_title_frame, text = author[0], text_color = "black", fg_color = "#FBF8EE", font = ("微軟正黑體", 16))
        self.poetry1_author.grid(row = 1, column = 0, sticky = W, ipady = 10)
        # 詩長度剛好
        self.main_poetry_text = Label(self.in_main_poetry_title_frame, text = "", font = ("微軟正黑體", 14), bg = "#FBF8EE", fg = "black", wraplength = 650, justify = "left")
        # 詩過長
        self.main_poetry_long_frame = customtkinter.CTkScrollableFrame(self.in_main_poetry_title_frame, height = 550, border_width = 0, fg_color = "#FBF8EE", bg_color = "#F5F5F5", corner_radius = 0, scrollbar_fg_color = "#F1EDD7", scrollbar_button_color = "#D1C08E", scrollbar_button_hover_color = "#9C8A54")
        self.main_poetry_long_text = Label(self.main_poetry_long_frame, text = "", font = ("微軟正黑體", 14), bg = "#FBF8EE", fg = "black", wraplength = 650, justify = "left")
        
        # 判斷詩的長度
        self.poetry_short = self.is_poetry_length_too_long(main_poetry)
        
        self.poetry_title = {}
        self.poetry_author = {}
        self.poetry_text = {}

        for i in range(4):
            self.poetry_title[i] = customtkinter.CTkLabel(self.poetry_text_frame[i], text=title[i+1], text_color="#97896F", fg_color="#EDE7D6", font=("微軟正黑體", 18))
            self.poetry_title[i].place(x=20, y=26)
            self.poetry_title[i].bind("<Enter>", lambda event, idx=i: self.on_hover_side_poetry_title(idx))
            self.poetry_title[i].bind("<Leave>", lambda event, idx=i: self.off_hover_side_poetry_title(idx))
            self.poetry_title[i].bind("<Button-1>", lambda event, idx=i: self.change_main_poetry(idx))

            self.poetry_author[i] = customtkinter.CTkLabel(self.poetry_text_frame[i], text=author[i+1], text_color="#97896F", fg_color="#EDE7D6", font=("微軟正黑體", 14))
            self.poetry_author[i].place(x=175, y=25)
            self.poetry_author[i].bind("<Enter>", lambda event, idx=i: self.on_hover_side_poetry_author(idx))
            self.poetry_author[i].bind("<Leave>", lambda event, idx=i: self.off_hover_side_poetry_author(idx))
            self.poetry_author[i].bind("<Button-1>", lambda event, idx=i: self.change_main_poetry(idx))
             
            self.poetry_text[i] = customtkinter.CTkLabel(self.poetry_text_frame[i], text=text[i+1], text_color="#97896F", fg_color="#EDE7D6", font=("微軟正黑體", 16), wraplength=268, justify="left")
            self.poetry_text[i].place(x=20, y=63)
            self.poetry_text[i].bind("<Enter>", lambda event, idx=i: self.on_hover_side_poetry_text(idx))
            self.poetry_text[i].bind("<Leave>", lambda event, idx=i: self.off_hover_side_poetry_text(idx))
            self.poetry_text[i].bind("<Button-1>", lambda event, idx=i: self.change_main_poetry(idx))



    def change_main_poetry(self, to_main):
        global p_n

        temp = p_n[0]
        p_n[0] = p_n[to_main+1]
        p_n[to_main+1] = temp
        print("to_main: ", p_n[0], " to_side: ", p_n[to_main+1])

        # 刪掉上一篇唐詩的物件設定
        self.main_poetry_long_frame.grid_forget()
        self.main_poetry_text.grid_forget()
        self.main_poetry_long_text.pack_forget()

        # 更新右側被點選的唐詩 換成原本的 main_poetry
        self.poetry_title[to_main].configure(text = title[p_n[to_main+1]])
        self.poetry_author[to_main].configure(text = author[p_n[to_main+1]])
        self.poetry_text[to_main].configure(text = text[p_n[to_main+1]])

        # 更新主要唐詩顯示
        self.poetry1_title.configure(text = title[p_n[0]])
        self.poetry1_author.configure(text = author[p_n[0]])

        self.is_poetry_length_too_long(p_n[0])
        



    # 滑鼠進入返回按鈕時切換圖片
    def on_hover(self, event):
        self.back_btn_photo.configure(image=self.back_btn_hover_image)

    # 滑鼠離開返回按鈕時恢復圖片
    def off_hover(self, event):
        self.back_btn_photo.configure(image=self.back_btn_image)

    def on_back_click(self, event):
        # 執行切換頁面的功能
        self.master.switch_frame()

    # 右側唐詩被滑鼠停留時 背景換色
    def on_hover_side_poetry(self, n):
        self.poetry_text_frame[n].configure(fg_color = "#DFD3B2")
        self.poetry_title[n].configure(fg_color = "#DFD3B2")
        self.poetry_author[n].configure(fg_color = "#DFD3B2")
        self.poetry_text[n].configure(fg_color = "#DFD3B2")

    def off_hover_side_poetry(self, n):
        self.poetry_text_frame[n].configure(fg_color = "#EDE7D6")
        self.poetry_title[n].configure(fg_color = "#EDE7D6")
        self.poetry_author[n].configure(fg_color = "#EDE7D6")
        self.poetry_text[n].configure(fg_color = "#EDE7D6")

    def on_hover_side_poetry_author(self, n):
        self.poetry_text_frame[n].configure(fg_color = "#DFD3B2")
        self.poetry_title[n].configure(fg_color = "#DFD3B2")
        self.poetry_author[n].configure(fg_color = "#DFD3B2")
        self.poetry_text[n].configure(fg_color = "#DFD3B2")

    def off_hover_side_poetry_author(self, n):
        self.poetry_text_frame[n].configure(fg_color = "#EDE7D6")
        self.poetry_title[n].configure(fg_color = "#EDE7D6")
        self.poetry_author[n].configure(fg_color = "#EDE7D6")
        self.poetry_text[n].configure(fg_color = "#EDE7D6")

    def on_hover_side_poetry_title(self, n):
        self.poetry_text_frame[n].configure(fg_color = "#DFD3B2")
        self.poetry_title[n].configure(fg_color = "#DFD3B2")
        self.poetry_author[n].configure(fg_color = "#DFD3B2")
        self.poetry_text[n].configure(fg_color = "#DFD3B2")

    def off_hover_side_poetry_title(self, n):
        self.poetry_text_frame[n].configure(fg_color = "#EDE7D6")
        self.poetry_title[n].configure(fg_color = "#EDE7D6")
        self.poetry_author[n].configure(fg_color = "#EDE7D6")
        self.poetry_text[n].configure(fg_color = "#EDE7D6")

    def on_hover_side_poetry_text(self, n):
        self.poetry_text_frame[n].configure(fg_color = "#DFD3B2")
        self.poetry_title[n].configure(fg_color = "#DFD3B2")
        self.poetry_author[n].configure(fg_color = "#DFD3B2")
        self.poetry_text[n].configure(fg_color = "#DFD3B2")

    def off_hover_side_poetry_text(self, n):
        self.poetry_text_frame[n].configure(fg_color = "#EDE7D6")
        self.poetry_title[n].configure(fg_color = "#EDE7D6")
        self.poetry_author[n].configure(fg_color = "#EDE7D6")
        self.poetry_text[n].configure(fg_color = "#EDE7D6")


    # 計算唐詩長度是否需要 Frame
    def is_poetry_length_too_long(self, n: int, limit=20):
        global text
        
        original_text = text[n].replace("\n", "").strip()
        # 計算句中句號（。）、問號（？）和驚嘆號（！）的總數
        total_count = sum(original_text.count(char) for char in "。？！")
        print("total_count: ", total_count)

        # 清除修正換行後 最後多餘的 \n
        def clean_text(new_text):
            if new_text.endswith("\n"):
                new_text = new_text[:-1]
            
            return new_text

        # 修正唐詩換行並顯示在畫面
        if total_count <= 18:
            print("don't need frame1")
            # 唐詩換行處理
            new_text = original_text.replace("。", "。\n").replace("？", "？\n").replace("！", "！\n")

            new_text = clean_text(new_text)
            print(new_text)

            new_height = 180 + 21 * total_count
            print("new height: ", new_height)            

            n_height = (self.winfo_screenheight() - 80 - new_height)/2
            # 更新物件上的唐詩文字
            self.main_poetry_text.config(text = new_text)
            self.main_poetry_text.grid(row = 2, column = 0, columnspan = 2, sticky = W, ipady = 10)

            self.main_poetry_frame.place_forget()
            # 更新物件大小並顯示
            if new_height > 323:                
                self.main_poetry_frame.configure(width = 453, height = new_height)                
                self.main_poetry_frame.place(x = 541, y = n_height)
            else:
                self.main_poetry_frame.configure(width = 453, height = 323)                
                self.main_poetry_frame.place(x = 541, y = 252)

        elif total_count <= 50:
            print("don't need frame2")
            period_count = 0
            new_text = ""

            # 換行處理
            for char in original_text:
                new_text += char
                if char in "。？！":                    
                    period_count += 1
                    if period_count % 2 == 0:
                        new_text += "\n"
                
            new_text = clean_text(new_text)
            print(new_text)


            new_height = 180 + 21 * ceil(total_count / 2)
            print("new height: ", new_height)            

            count_char = 0
            for char in new_text:
                if char == "\n":
                    break
                count_char += 1

            new_width = count_char * 21 + 30
            print("new_width: ", new_width)


            self.main_poetry_text.config(text = new_text)
            self.main_poetry_text.grid(row = 2, column = 0, columnspan = 2, sticky = W, ipady = 10)

            self.main_poetry_frame.place_forget()

            n_x = (self.winfo_screenwidth() - 80 - new_width)/2   
            if new_height < 700: 
                n_y = (self.winfo_screenheight() - 80 - new_height)/2                           
                self.main_poetry_frame.configure(width = new_width, height = new_height)                
                self.main_poetry_frame.place(x = n_x, y = n_y)
            else:
                n_y = (self.winfo_screenheight() - 80 - 700)/2
                self.main_poetry_frame.configure(width = new_width, height = 700)                
                self.main_poetry_frame.place(x = n_x, y = n_y)
           
        else:
            print("need frame")
            period_count = 0
            new_text = ""

            # 換行處理
            for char in original_text:
                new_text += char
                if char in "。？！":                    
                    period_count += 1
                    if period_count % 2 == 0:
                        new_text += "\n"
                
            new_text = clean_text(new_text)
            print(new_text)         


            count_char = 0
            for char in new_text:
                if char == "\n":
                    break
                count_char += 1

            new_width = count_char * 21 + 30
            print("new_width: ", new_width)

            # 更新物件上的唐詩文字
            self.main_poetry_long_text.configure(text = new_text)
            self.main_poetry_frame.place_forget()

            # 計算物件新座標
            n_x = (self.winfo_screenwidth() - 80 - new_width)/2
            n_y = (self.winfo_screenheight() - 80 - 700)/2      

            # 更新物件內容 大小 並顯示
            self.main_poetry_long_frame.configure(width = new_width - 70)  
            self.main_poetry_frame.configure(width = new_width, height = 700)
            self.main_poetry_frame.place(x = n_x, y = n_y)

            self.main_poetry_long_text.grid(row = 0, column = 0, sticky = W, ipady = 20)
            self.main_poetry_long_frame.grid(row = 2, column = 0, sticky = W, ipady = 20)




def main():
    root = Tk()
    root.title("Dynamic Frame Management")
    root.geometry(f"{root.winfo_screenwidth()-10}x{root.winfo_screenheight()-80}+0+0")
    app = Controller(root)
    app.pack(fill=BOTH, expand=True)
    root.mainloop()

if __name__ == '__main__':
    main()
