from django.shortcuts import render, redirect
from django.http import  HttpResponse, HttpResponseRedirect
from . import models
from django.http import HttpResponse, HttpResponseRedirect
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import random
from django.shortcuts import render, redirect
from django.template import loader, Context
# Create your views here.
from . import models
def mainpage(request):     #个人主页
    return render(request, 'mainpage.html')

def software_mainpage(request):
    return render(request, 'software_templates/software_mainpage.html')

def login(request):     #登录界面
    return render(request, 'login.html')

def login_action(request):       #登录事务
    user_account = request.POST.get('user_account', 'USER_ACCOUNT')
    user_password = request.POST.get('user_password', 'USER_PASSWORD')
    i=0
    for users in models.user.objects.all():
        if user_account == users.user_account and user_password == users.user_password:
           i=1
    if i==1:
        response = HttpResponseRedirect('/mainpage/')
        response.set_cookie('user_account', user_account, 604800)
        response.set_cookie('user_password', user_password, 604800)
        return response
    if i==0:
        for software_man in models.software_man.objects.all():
            if user_account == software_man.software_man_account and user_password == software_man.software_man_password:
                i = 2
        if i == 2:
            response = HttpResponseRedirect('/softwareMainpage/')
            response.set_cookie('user_account', user_account, 604800)
            response.set_cookie('user_password', user_password, 604800)
            return response
        else:
            return render(request, 'login.html', {'msg':'用户名或密码错误!'})

def register(request):       #注册界面
    return render(request, 'register.html')

def register_action(request):        #注册事务
    user_account = request.POST.get('user_account', 'USER_ACCOUNT')
    if models.user.objects.filter(user_account=user_account):
        return render(request, 'register.html', {'msg': '用户名已经存在!'})
    user_password = request.POST.get('user_password', 'USER_PASSWORD')
    user_name = request.POST.get('user_name', 'USER_NAME')
    user_introduction = request.POST.get('user_introduction', 'USER_INTRODUCTION')
    user_email = request.POST.get('user_email', 'USER_EMAIL')
    if user_password =="" or user_account =="" or user_email=="" or user_name== "":
        return render(request, 'register.html', {'msg': '信息不全!'})
    models.user.objects.create(user_account=user_account, user_password=user_password, user_name=user_name,
                               user_introduction=user_introduction, user_email=user_email)
    return render(request, 'login.html')

def personalInformation(request):      #查看个人信息事务
    if "user_account" in request.COOKIES:
        user_account = request.COOKIES.get("user_account")
        user = models.user.objects.get(user_account=user_account)
        return render(request, "personal_information.html", {'user': user})
    else:
        return render(request, 'login.html')

def informationModification(request):
    if "user_account" in request.COOKIES:
        user_account = request.COOKIES.get("user_account")
        user = models.user.objects.get(user_account=user_account)
        return render(request, 'information_modification.html', {'user': user})

def informationModification_action(request):     #个人信息修改事务
    if "user_account" in request.COOKIES:
        user_account = request.COOKIES.get("user_account")
        user_name = request.POST.get('user_name', 'USER_NAME')
        user_introduction = request.POST.get('user_introduction', 'USER_INTRODUCTION')
        user_email = request.POST.get('user_email', 'USER_EMAIL')
        if user_email == "" or user_name == "":
            return render(request, 'information_modification.html', {'msg': '信息不全!'})
        models.user.objects.filter(user_account=user_account).update(user_name=user_name, user_introduction=user_introduction, user_email=user_email)
        if "user_account" in request.COOKIES:
            user_account = request.COOKIES.get("user_account")
            user = models.user.objects.get(user_account=user_account)
            return render(request, "personal_information.html", {'user': user})

def STOP(request):      #榜单界面
    songs = models.STOP.objects.all().order_by("-search_number")[:100]
    return render(request, 'STOP.html', {'songs': songs})

def CTOP(request):    #ctop榜单界面
    songs= []
    ctops = models.song_information.objects.all().order_by("-click_number")[:100]
    for ctop in ctops:
        songs.append(ctop)
    return render(request, 'CTOP.html', {'songs': songs})

def Best_singer(request):  # 最佳歌手榜单
    singers = models.musician.objects.filter(musician_kind="歌手").order_by("-click_number")[:100]
    return render(request, 'Best_singer.html', {'singers': singers})

def Best_composer(request):  # 最佳作曲人榜单
    composers = models.musician.objects.filter(musician_kind="作曲人").order_by("-click_number")[:100]
    return render(request, 'Best_composer.html', {'composers': composers})

def Best_lyrics_maker(request):  # 最佳作词人榜单
    lyrics_makers = models.musician.objects.filter(musician_kind="作词人").order_by("-click_number")[:100]
    return render(request, 'Best_lyrics_maker.html', {'lyrics_makers': lyrics_makers})

def Best_software(request):      #最佳软件榜单
    soft_wares = models.software.objects.order_by("-click_number")[:100]
    return render(request, 'Best_software.html', {'soft_wares': soft_wares})

def query(request):            #歌名查询事务
        kind = request.POST.get('kind')
        if '1' == kind:
            song_name = request.POST.get('text', 'SONG_NAME')
            songs = models.song_information.objects.filter(song_name=song_name)
            stop = models.STOP.objects.get(song_name=song_name)
            models.STOP.objects.filter(song_name=song_name).update(search_number=stop.search_number + 1)
            return render(request, 'query.html', {'songs': songs})
        elif kind == '3':
            composer = request.POST.get('text', 'COMPOSER')
            songs = models.song_information.objects.filter(composer=composer)
            return render(request, 'query.html', {'songs': songs})
        elif kind == '2':
            singer = request.POST.get('text', 'SINGER')
            songs = models.song_information.objects.filter(singer=singer)
            return render(request, 'query.html', {'songs': songs})
        elif kind == '4':
            lyrics_maker = request.POST.get('text', 'LYRICS_MAKER')
            songs = models.song_information.objects.filter(lyrics_maker=lyrics_maker)
            return render(request, 'query.html', {'songs': songs})

def interlinkage(request):      #点击链接事务
    if request.method == "POST":
      if "查看链接" in request.POST:
        song_ID = request.POST.get('查看链接')
        song = models.song_information.objects.get(song_ID=song_ID)
        models.song_information.objects.filter(song_ID=song_ID).update(click_number=song.click_number + 1)
        if models.musician.objects.get(musician_name=song.singer, musician_kind="歌手"):
           singer = models.musician.objects.get(musician_name=song.singer, musician_kind="歌手")
           models.musician.objects.filter(musician_name=singer.musician_name, musician_kind="歌手").update(click_number=singer.click_number + 1)
        composer = models.song_information.objects.get(song_ID=song_ID).composer
        if models.musician.objects.get(musician_name=composer, musician_kind="作曲人"):
           composer = models.musician.objects.get(musician_name=composer, musician_kind="作曲人")
           models.musician.objects.filter(musician_name=composer.musician_name, musician_kind="作曲人").update(click_number=composer.click_number + 1)
        lyrics_maker = models.song_information.objects.get(song_ID=song_ID).lyrics_maker
        if models.musician.objects.get(musician_name=lyrics_maker, musician_kind="作词人"):
           lyrics_maker = models.musician.objects.get(musician_name=lyrics_maker, musician_kind="作词人")
           models.musician.objects.filter(musician_name=lyrics_maker.musician_name, musician_kind="作词人").update(click_number=lyrics_maker.click_number + 1)
        software = models.song_information.objects.get(song_ID=song_ID).software
        if models.software.objects.get(software_name=software):
           software = models.software.objects.get(software_name=software)
           models.software.objects.filter(software_name=song.software).update(click_number=software.click_number + 1)
        return render(request, 'interlinkage.html',  {'song': song})
      if "收藏" in request.POST:
          song_ID = request.POST.get('收藏')
          if "user_account" in request.COOKIES:
              user_account = request.COOKIES.get("user_account")
              user = models.user.objects.get(user_account=user_account)
              song = models.song_information.objects.get(song_ID=song_ID)
              if models.collection.objects.filter(song_ID_id=song_ID, user_ID_id=user.user_ID):
                  return render(request, 'collection.html', {'msg': '歌曲已经存在!'})
              models.collection.objects.create(song_ID=song, user_ID=user)
              return render(request, 'mainpage.html')

def retrieve_password(request):   #找回密码界面业务
    if "user_account" in request.COOKIES:
        user_account = request.COOKIES.get("user_account")
        user = models.user.objects.get(user_account=user_account)

        # 第三方 SMTP 服务
        mail_host = "smtp.163.com"
        mail_user = "music_selection"
        mail_pass = "qiyihao666"

        sender = 'music_selection@163.com'
        receivers = [user.user_email]  # 接收邮件地址

        salt = ''.join(random.sample('0123456789', 4))
        models.user.objects.filter(user_account=user.user_account).update(user_verification=salt)
        content = '验证码如上'
        title = salt  # 邮件主题

        message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
        message['From'] = "{}".format(sender)
        message['To'] = ",".join(receivers)
        message['Subject'] = title
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        return render(request, 'input_verification.html')

def input_double_password(request): #输入两次密码确认
    if "user_account" in request.COOKIES:
        user_account = request.COOKIES.get("user_account")
        user = models.user.objects.get(user_account=user_account)

    user_verification = request.POST.get('user_verification', 'USER_VERIFICATION')
    if user_verification == user.user_verification:
        return render(request, 'reset_password.html')
    else:
        return render(request, 'input_verification.html', {'msg': '验证码错误，请重新确认!'})
def forget_password_action(request):  # 忘记密码事务
    if "user_account" in request.COOKIES:
        user_account = request.COOKIES.get("user_account")
        user = models.user.objects.get(user_account=user_account)

        user_passwords = request.POST.get('user_passwords', 'USER_PASSWORDS')
        user_passwords2 = request.POST.get('user_passwords2', 'USER_PASSWORDS2')
        if user_passwords == user_passwords2:
            models.user.objects.filter(user_account=user.user_account).update(user_password=user_passwords)
            return render(request, 'login.html')
        else:
            return render(request, 'input_verification.html', {'msg': '两次输入的密码不一致！'})

def input_useraccount(request):    #输入用户名界面业务
    return render(request, 'input_user_account.html')

def input_useraccount_action(request):  #检测
    user_account = request.POST.get('user_account', 'USER_ACCOUNT')
    i=0
    for users in models.user.objects.all():
        if user_account == users.user_account:
           i=1
    if i==1:
        response = HttpResponseRedirect('/inputUserAccount/retrievePassword')
        response.set_cookie('user_account', user_account, 604800)
        return response
    if i==0:
        return render(request, 'login.html', {'msg': '用户名不存在!'})


def collection(request): #收藏界面
    if "user_account" in request.COOKIES:
        songs = []
        user_account = request.COOKIES.get("user_account")
        user = models.user.objects.get(user_account=user_account)
        collections = models.collection.objects.filter(user_ID_id=user.user_ID)
        for collection in collections:
            song = models.song_information.objects.get(song_ID=collection.song_ID_id)
            songs.append(song)
        return render(request, 'collection.html', {'songs': songs})

def delete_my_collection(request):    #删除收藏歌曲
    if "删除" in request.POST:
        song_ID = request.POST.get('删除')
        if "user_account" in request.COOKIES:
           user_account = request.COOKIES.get("user_account")
           user = models.user.objects.get(user_account=user_account)
           models.collection.objects.get(song_ID_id=song_ID, user_ID_id=user.user_ID).delete()
           songs = []
           user_account = request.COOKIES.get("user_account")
           user = models.user.objects.get(user_account=user_account)
           collections = models.collection.objects.filter(user_ID_id=user.user_ID)
           for collection in collections:
               song = models.song_information.objects.get(song_ID=collection.song_ID_id)
               songs.append(song)
           return render(request, 'collection.html', {'songs': songs})
    if"生成歌单" in request.POST:
        song_IDs = request.POST.getlist('歌单歌曲')
        list_name = request.POST.get('list_name', 'LIST_NAME')
        if list_name == "":
            return render(request, 'collection.html',  {'msg': '歌单名为空'})
        if models.Song_list.objects.filter(songlist_name=list_name):
            return render(request, 'collection.html',  {'msg': '歌单名已经存在!'})
        if len(song_IDs)==0:
            return render(request, 'collection.html',  {'msg': '未勾选歌曲!'})
        for song_ID in song_IDs:
            song = models.song_information.objects.get(song_ID=song_ID)
            models.Song_list.objects.create(songlist_name=list_name, song_ID=song)
        songs = []
        user_account = request.COOKIES.get("user_account")
        user = models.user.objects.get(user_account=user_account)
        collections = models.collection.objects.filter(user_ID_id=user.user_ID)
        for collection in collections:
            song = models.song_information.objects.get(song_ID=collection.song_ID_id)
            songs.append(song)
        return render(request, 'collection.html', {'songs': songs})

def change_password(request):
    return render(request, 'password_modification.html')

def change_password_actiom(request):     #修改密码
    if "user_account" in request.COOKIES:
        user_account = request.COOKIES.get("user_account")
        user = models.user.objects.get(user_account=user_account)
    user_password = request.POST.get('user_password', 'USER_PASSWORD')
    if user_password == user.user_password:
        user_passwords = request.POST.get('user_passwords', 'USER_PASSWORDS')
        user_passwords2 = request.POST.get('user_passwords2', 'USER_PASSWORDS2')
        if user_passwords == user_passwords2:
            models.user.objects.filter(user_account=user.user_account).update(user_password=user_passwords)
            return render(request, 'mainpage.html')
        else:
            return render(request, 'password_modification.html', {'msg': '两次输入的密码不一致！'})
    else:
        return render(request, 'password_modification.html', {'msg': '原密码错误！'})

def software_songs(request):
    if "user_account" in request.COOKIES:
        user_account = request.COOKIES.get("user_account")
        user = models.software_man.objects.get(software_man_account=user_account)
        software = models.software.objects.get(software_ID=user.software_ID_id)
        songs = models.song_information.objects.filter(software=software.software_name)
        return render(request, 'software_templates/software_songs.html', {'songs': songs})

def software_personal_information(request):
    if "user_account" in request.COOKIES:
        user_account = request.COOKIES.get("user_account")
        user = models.software_man.objects.get(software_man_account=user_account)
        return render(request, 'software_templates/softwareman_personal_information.html', {'user': user})

def add_songs(request):
    return render(request, 'software_templates/add_song.html')

def add_songs_action(request):
    if "user_account" in request.COOKIES:
        user_account = request.COOKIES.get("user_account")
        user = models.software_man.objects.get(software_man_account=user_account)
    song_name = request.POST.get('song_name', 'SONG_NAME')
    singer = request.POST.get('singer', 'SINGER')
    composer = request.POST.get('composer', 'COMPOSER')
    lyrics_maker = request.POST.get('lyrics_maker', 'LYRICS_MAKER')
    software = models.software.objects.get(software_ID=user.software_ID_id).software_name
    time = request.POST.get('time', 'TIME')
    need_vip = request.POST.get('need_VIP', 'NEED_VIP')
    need_pay = request.POST.get('need_pay', 'NEED_PAY')
    payment = request.POST.get('payment', 'PAYMENT')
    tone_quality = request.POST.get('tone_quality', 'TONE_QUALITY')
    interlinkage = request.POST.get('interlinkage', 'INTERLINKAGE')
    if song_name == "" or singer == "" or composer == "" or lyrics_maker == "" or  time == "" or need_pay == "" or need_vip=="" or payment=="" or tone_quality == "" or interlinkage == "":
        return render(request, 'software_templates/add_song.html', {'msg': '信息不全!'})

    if models.song_information.objects.filter(song_name=song_name, singer=singer, lyrics_maker=lyrics_maker,
                                           composer=composer, time=time, software=software,
                                           need_VIP=need_vip, need_pay=need_pay,
                                           payment=payment, tone_quality=tone_quality, interlinkage=interlinkage):
        return render(request, 'software_templates/add_song.html', {'msg': '该歌曲已经存在!'})
    models.song_information.objects.create(song_name=song_name, singer=singer, lyrics_maker=lyrics_maker,
                                           composer=composer, time=time, software=software,
                                           need_VIP=need_vip, need_pay=need_pay,
                                           payment=payment, tone_quality=tone_quality, interlinkage=interlinkage,
                                           click_number=0, search_number=0)
    if not models.STOP.objects.filter(song_name=song_name):
        models.STOP.objects.create(song_name=song_name, search_number=0)
    software = models.software.objects.get(software_ID=user.software_ID_id)
    models.software.objects.filter(software_ID=user.software_ID_id).update(song_numbers=software.song_numbers + 1)

    if "user_account" in request.COOKIES:
        user_account = request.COOKIES.get("user_account")
        user = models.software_man.objects.get(software_man_account=user_account)
        software = models.software.objects.get(software_ID=user.software_ID_id)
        songs = models.song_information.objects.filter(software=software.software_name)
        return render(request, 'software_templates/software_songs.html', {'songs': songs})

def song_change(request):
    return render(request, 'software_templates/song_change.html')

def button(request):
    if "删除" in request.POST:
        song_ID = request.POST.get('删除')
        models.song_information.objects.get(song_ID=song_ID).delete()
        if "user_account" in request.COOKIES:
            user_account = request.COOKIES.get("user_account")
            user = models.software_man.objects.get(software_man_account=user_account)
            software = models.software.objects.get(software_ID=user.software_ID_id)
            songs = models.song_information.objects.filter(software=software.software_name)
            return render(request, 'software_templates/software_songs.html', {'songs': songs})
    if "修改" in request.POST:
        song_ID = request.POST.get('修改')
        response = HttpResponseRedirect('/softwareMainpage/softwareSongs/change')
        response.set_cookie('song_ID', song_ID, 604800)
        return response

def song_change_action(request):
    if "song_ID" in request.COOKIES:
         song_ID = request.COOKIES.get("song_ID")
         song_name = request.POST.get('song_name', 'SONG_NAME')
         singer = request.POST.get('singer', 'SINGER')
         composer = request.POST.get('composer', 'COMPOSER')
         lyrics_maker = request.POST.get('lyrics_maker', 'LYRICS_MAKER')
         time = request.POST.get('time', 'TIME')
         need_vip = request.POST.get('need_vip', 'NEED_VIP')
         need_pay = request.POST.get('need_pay', 'NEED_PAY')
         payment = request.POST.get('payment', 'PAYMENT')
         tone_quality = request.POST.get('tone_quality', 'TONE_QUALITY')
         interlinkage = request.POST.get('interlinkage', 'INTERLINKAGE')
         models.song_information.objects.filter(song_ID=song_ID).update(song_name=song_name, singer=singer,
                                                lyrics_maker=lyrics_maker, composer=composer,
                                                time=time, need_VIP=need_vip, need_pay=need_pay,
                                                payment=payment, tone_quality=tone_quality, interlinkage=interlinkage)
    if "user_account" in request.COOKIES:
        user_account = request.COOKIES.get("user_account")
        user = models.software_man.objects.get(software_man_account=user_account)
        software = models.software.objects.get(software_ID=user.software_ID_id)
        songs = models.song_information.objects.filter(software=software.software_name)
        return render(request, 'software_templates/software_songs.html', {'songs': songs})

def song_list_view(request):
    song_lists = []
    for song_list in models.Song_list.objects.all():
        if song_list.songlist_name not in song_lists:
            song_lists.append(song_list.songlist_name)
    return render(request, 'song_list.html', {'song_lists': song_lists})

def song_list(request):
    list_name = request.POST.get('查看歌单')
    songs = []
    for list in models.Song_list.objects.all():
        if list.songlist_name == list_name:
            song = models.song_information.objects.get(song_ID=list.song_ID_id)
            songs.append(song)
    return render(request, 'list.html', {'songs': songs})

def add_musician(request):
    return render(request, 'software_templates/add_musician.html')

def add_musician_action(request):
    musician_name = request.POST.get('musician_name', 'NAME')
    if models.musician.objects.filter(musician_name=musician_name):
        return render(request, 'software_templates/add_musician.html', {'msg': '音乐人已经存在!'})
    musician_sex = request.POST.get('musician_sex', 'SEX')
    musician_age = request.POST.get('musician_age', 'AGE')
    musician_kind = request.POST.get('musician_kind', 'KIND')
    if musician_age == "" or musician_age == "" or musician_name=="" or musician_kind=="":
        return render(request, 'software_templates/add_musician.html', {'msg': '信息不全!'})
    models.musician.objects.create(musician_name=musician_name, musician_sex=musician_sex,
                                   musician_age=musician_age, musician_kind=musician_kind, click_number=0)
    if "user_account" in request.COOKIES:
        user_account = request.COOKIES.get("user_account")
        user = models.software_man.objects.get(software_man_account=user_account)
        software = models.software.objects.get(software_ID=user.software_ID_id)
        songs = models.song_information.objects.filter(software=software.software_name)
        return render(request, 'software_templates/software_songs.html', {'songs': songs})
