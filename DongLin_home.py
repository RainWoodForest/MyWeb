"""我的主页"""
# 导入需要的库
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image, ImageFilter, ImageOps, ImageDraw, ImageFont
import webbrowser

# 设置页面配置
st.set_page_config(
    page_title='雨木森林',
    page_icon='DongLin_Pic1.png',
)

# 使用streamlit库中所有功能几乎都以组件的形式调用
page = st.sidebar.radio("我的首页", ["我的个人资料", "我的图片换色工具", "我的图片尺寸调整工具", "我的图片滤镜工具", "我的智慧词典", "我的留言区", "春节解锁此页", "关于此网站"])  # 使用sidebar()组件创建侧边栏结构
# 音乐播放
st.subheader(":green[:musical_note: Relaxing Light Background - AudioCoffee]")
with open("./DongLin_BGM1.mp3", "rb") as f:
    myMp3 = f.read()
st.audio(myMp3, format="audio/mp3", start_time=1)
st.divider()  # 添加一条分割线
# 定义每一页的函数
def page1():  # 我的个人资料
    st.balloons()
    st.subheader(":green[:frame_with_picture: 我的头像]")
    st.image("DongLin_Pic1.png", width=300)
    st.subheader(":green[:link: 我其他平台的个人主页]")
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1.5, 1.8, 2, 2, 1.5, 1.5, 1.5])
    with col1:
        st.link_button('Github', 'https://github.com/RainWoodForest')
    with col2:
        st.link_button('哔哩哔哩', 'https://space.bilibili.com/672508011')
    with col3:
        st.link_button('编程猫社区', 'https://shequ.codemao.cn/user/939345')
    with col4:
        st.link_button('神奇代码岛', 'https://box3.codemao.cn/u/12753431')
        
def page2():  # 网站代码展示
    with open("DongLin_Code.txt", encoding="utf-8") as c:
        code = c.read()
    st.code(code, language='python')
    
def page3():  # 我的图片换色工具
    st.subheader(":green[:sparkles:图片换色小程序:sparkles:]")
    st.text("交换图片的RGB值")
    uploaded_file = st.file_uploader("上传图片", type=["png","jpeg","jpg","bmp"])
    if(uploaded_file):
        # 获取图片文件的名称.类型.大小
        file_name = uploaded_file.name  # 文件名字
        file_type = uploaded_file.type  # 文件格式
        file_size = uploaded_file.size  # 文件大小
        img = Image.open(uploaded_file)
        st.image(img)
        tab1,tab2,tab3,tab4 = st.tabs(["原图RGB","改色RBG","改色GBR","改色GRB"])
        with(tab1):
            st.write("处理结果：")
            st.image(img)
        with(tab2):
            st.write("处理结果：")
            st.image(img_change(img, 0, 2, 1))
        with(tab3):
            st.write("处理结果：")
            st.image(img_change(img, 1, 2, 0))
        with(tab4):
            st.write("处理结果：")
            st.image(img_change(img, 1, 0, 2))
        st.info("处理好后的图片可以直接右击并选择【将图像另存为】将其保存到本地")

def page4():  # 我的图片尺寸调整工具
    st.subheader(":green[:sparkles:图片尺寸调整工具:sparkles:]")
    st.text("自定义调整图片尺寸")
    uploaded_file = st.file_uploader("上传图片", type=["png","jpeg","jpg","bmp"])
    if(uploaded_file):
        img = Image.open(uploaded_file)
        st.image(img)
        old_width, old_height = img.size
        st.write(f"原图尺寸: {old_width}×{old_height}")
        cab_1, cab_2 = st.columns([1,1])
        with cab_1:
            new_width = st.number_input(label="请输入新图片的宽", min_value=1, value=old_width, step=1)
        with cab_2:
            new_height = st.number_input(label="请输入新图片的高", min_value=1, value=old_height, step=1)
        if(st.button("确定")):
            st.write(f"处理结果({new_width}×{new_height})：")
            img1 = img.resize(( int(new_width), int(new_height) ))
            st.image(img1)
            st.info("处理好后的图片可以直接右击并选择【将图像另存为】将其保存到本地")

# 滤镜
filters = {
    "模糊滤镜": ImageFilter.BLUR,
    "轮廓滤镜": ImageFilter.CONTOUR,
    "边缘增强滤镜": ImageFilter.EDGE_ENHANCE,
    "浮雕滤镜": ImageFilter.EMBOSS,
    "锐化滤镜": ImageFilter.SHARPEN,
    "平滑滤镜": ImageFilter.SMOOTH,
}

def page5():  # 我的图片滤镜工具
    global filters
    st.subheader(":green[:sparkles:图片滤镜调整工具:sparkles:]")
    st.text("自定义调整图片滤镜")
    type_list = ["png","jpeg","jpg","bmp"]
    uploaded_file = st.file_uploader("上传图片", type=type_list)
    if(uploaded_file):
        # 获取图片文件的名称.类型.大小
        file_name = uploaded_file.name  # 文件名字
        file_type = uploaded_file.type  # 文件格式
        file_size = uploaded_file.size  # 文件大小
        img = Image.open(uploaded_file)
        st.image(img)
        # 定义选项列表
        filter_options = ['请选择...', '模糊滤镜', '轮廓滤镜', '边缘增强滤镜', '浮雕滤镜', '锐化滤镜', '平滑滤镜', '素描风格转化', '字符画风格转化(实验性功能)']
        # 使用selectbox方法显示下拉选择框
        selected_filter = st.selectbox('请选择一个滤镜', filter_options)
        # 处理图片
        if("滤镜" in selected_filter):
            st.write("处理结果：")
            img_temp = img.filter(filters[selected_filter]).convert("RGBA")
            st.image(img_temp)
            st.info("处理好后的图片可以直接右击并选择【将图像另存为】将其保存到本地")
        elif(selected_filter == "素描风格转化"):
            st.write("处理结果：")
            img_temp = to_sketch(img)
            st.image(img_temp)
            st.info("处理好后的图片可以直接右击并选择【将图像另存为】将其保存到本地")
        elif(selected_filter == "字符画风格转化(实验性功能)"):
            st.info("字符画风格转化为实验性功能, 可能会出现转换有误的问题")
            st.write("处理结果：")
            img_temp = to_char(img)
            st.image(img_temp)
            st.info("处理好后的图片可以直接右击并选择【将图像另存为】将其保存到本地")
        

def page6():  # 我的智慧词典
    st.subheader(":orange[:ledger:智慧词典:ledger:]")
    # 从本地文件中将词典信息读取出来, 并存储在列表中
    with open("DongLin_words_space.txt", "r", encoding="utf-8") as f:
        words_list = f.read().split("\n")
    # print(words_list)
    # 将列表中的每一项内容再进行分割, 分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    # 将列表中的内容导入字典, 方便查询, 格式为“单词:[编号,解释]”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # print(words_dict)
    # 从本地文件中将单词的查询次数读取出来, 并存储在列表中
    with open("DongLin_check_out_times.txt","r",encoding="utf-8") as f:
        times_list = f.read().split("\n")
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input("请输入要查询的单词(按Enter键确认):", value="")
    # 显示查询内容
    if(word):
        if (word in words_dict):
            st.write(words_dict[word][1])
            n = words_dict[word][0]
            if(n in times_dict):
                times_dict[n] += 1
            else:
                times_dict[n] = 1

            with open("DongLin_check_out_times.txt", "w", encoding="utf-8") as f:
                message = ""
                for k,v in times_dict.items():  # k是编号, v是次数
                    message += str(k) + "#" + str(v) + "\n"
                message = message[:-1]
                f.write(message)
            st.write("查询次数:", times_dict[n])
            
            if (word == "birthday") or (word == "holiday") or (word == "vacation") or (word == "balloon"):
                st.success("成功触发彩蛋")
                st.balloons()
            if (word == "winter") or (word == "snow"):
                st.success("恭喜你发现彩蛋")
                st.snow()
            if (word == "error"):
                st.error("Error: This Just a JOKE. :)")
        if (word in ["Python","python"]):
            st.success("成功触发彩蛋")
            st.code('''# 恭喜你发现彩蛋, 这里是一行Python代码
print("This is a line of Python code. ")''', language="python")
        elif (word in ["JS","js","JavaScript","javascript"]):
            st.success("成功触发彩蛋")
            st.code('''// 恭喜你发现彩蛋, 这里是一行JavaScript代码
console.log("This is a line of JavaScript code. ")''', language="javascript")
        elif (word == "bilibili"):
            if(st.button("跳转")):
                webbrowser.open("https://www.bilibili.com")
        elif (word == "baidu"):
            if(st.button("跳转")):
                webbrowser.open("https://baidu.com")
        elif (word == "GitHub"):
            if(st.button("跳转")):
                webbrowser.open("https://github.com")
        elif (word == "codemao"):
            if(st.button("跳转")):
                webbrowser.open("https://www.codemao.cn")
        elif not (word in words_dict):
            st.warning("未找到结果！")
    

def page7():  # 我的留言区
    st.subheader("我的留言区")
    # 从文件中加载内容, 并处理成列表
    with open("DongLin_leave_messages.txt", "r", encoding="utf-8") as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if(i[1] == "雨木森林") or (i[1] == "董霖"):
            with st.chat_message("🌲"):
                st.write(i[1] + ": " + i[2])
        else:
            with st.chat_message("👨‍💻"):
                st.text(i[1] + ": " + i[2])
    name = st.text_input("我是……", value="匿名用户")
    password = ""
    new_message = st.text_input(label="请在此键入想要说的话…")
    if(name == "雨木森林")or(name == "董霖"):
        password = st.text_input("请输入6位数密码:")
    if(st.button("完成")):
        if(password == "100428") and ((name == "雨木森林")or(name == "董霖")):
            messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
            st.info("留言成功, 请手动刷新网页以查看最新留言")
            with open("DongLin_leave_messages.txt", "w", encoding="utf-8") as f:
                message = ""
                for i in messages_list:
                    message += i[0]+"#"+i[1]+"#"+i[2]+"\n"
                message = message[:-1]
                f.write(message)
        elif((name == "雨木森林")or(name == "董霖")) and (password != "100428"):
            st.warning("请勿冒充作者！")
        else:
            messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
            st.info("留言成功, 请手动刷新网页以查看最新留言")
            with open("DongLin_leave_messages.txt", "w", encoding="utf-8") as f:
                message = ""
                for i in messages_list:
                    message += i[0]+"#"+i[1]+"#"+i[2]+"\n"
                message = message[:-1]
                f.write(message)

def page_test():
    pass

def page_about():
    components.iframe("//player.bilibili.com/player.html?aid=1100320038&bvid=BV1gA4m157HX&cid=1432932265&p=1", height=520)

def page_happy2024():
    st.title("新年快乐, 春节解锁此页, 敬请期待")

def img_change(img, rc, gc, bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            R = img_array[x,y][rc]
            G = img_array[x,y][gc]
            B = img_array[x,y][bc]
            img_array[x,y] = (R,G,B)
    return img

def to_sketch(img):
    width,height = img.size
    # 转灰度图
    img_gray = img.convert("L")
    # 反色
    img_invert = ImageOps.invert(img_gray)
    # 高斯模糊
    img_gaussian = img_invert.filter(ImageFilter.GaussianBlur(5))
    # 颜色减淡
    for x in range(width):
        for y in range(height):
            pos = (x,y)
            # 获取灰度图与高斯图的像素值
            A = img_gray.getpixel(pos)
            B = img_gaussian.getpixel(pos)
            # 颜色减淡公式
            img_gray.putpixel(pos,min(int(A+A*B/(255-B+1)),255))  # 手动防止除以零
    return img_gray

def to_char(img):
    # 图片宽高
    width, height = (70, 70)
    # 灰度图
    img = img.convert("L").resize((width, height))
    # 70 level 字符串
    ASCII_HIGH = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. """
    # 灰度转字符串
    txt = ""
    for y in range(width):
        for x in range(height):
            pos = (x,y)
            gray = img.getpixel(pos)  # 0-255
            index = int(gray/256*70)
            txt += ASCII_HIGH[index] + " "
        txt += "\n"
    # 字符串转图片
    img_new = Image.new("RGB",(width*12,height*15),'white')
    draw = ImageDraw.Draw(img_new)
    draw.text((0,0), txt, fill='black', font=ImageFont.truetype("DongLin_Font_BD.ttf",10))
    return img_new.resize((width*12,width*12)).convert("RGBA")

# 判断用户点击的是哪个页, 并进行跳转
if(page == "我的个人资料"):
    page1()
elif(page == "网站代码展示"):
    page2()
elif(page == "我的图片换色工具"):
    page3()
elif(page == "我的图片尺寸调整工具"):
    page4()
elif(page == "我的图片滤镜工具"):
    page5()
elif(page == "我的智慧词典"):
    page6()
elif(page == "我的留言区"):
    page7()
elif(page == "测试"):
    page_test()
elif(page == "关于此网站"):
    page_about()
elif(page == "春节解锁此页"):
    page_happy2024()
