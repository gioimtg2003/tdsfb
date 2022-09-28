import json
import time
import os
import sys
import random
import base64
from datetime import datetime
white = '\033[1;97m'
red = '\033[1;91m'
pink = '\033[1;95m'
mautim = '\033[95m'
blue = '\033[1;94m'
xanhnhat = '\033[1;96m'
green = '\033[92m'
vang = '\033[93m'

try:
    import requests
    from pystyle import Anime, Colors, Colorate, Write, Add, Center, System, Write
except:
    os.system('python -m pip install requests')
    os.system('python -m pip pip install pystyle')
    import requests
    from pystyle import Anime, Colors, Colorate, Write, Add, Center, System, Write


def follow(uid, cookie):
    headers = {
        'authority': 'm.facebook.com',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-lsd': 'jbep7dZrR6bdEAIqWtv9g2',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'cookie': cookie
        } 
    get_data = requests.get('https://m.facebook.com/profile.php?id=' + str(uid), headers=headers).text
    fb_dtsg = get_data.split('dtsg:"')[1].split('"')[0]
    __a = get_data.split('"encrypted":"')[1].split('"')[0]
    data = {
    'subject_id': str(uid),
    'fb_dtsg': fb_dtsg,
    '__a': __a,
    }
    response = requests.post('https://m.facebook.com/a/subscriptions/add', headers=headers, data=data).text
    if 'cmd' in response:
        return True
    else:
        return False

def intro():
    in1 = '''
╔═════════════════════════════════════════════════════════╗
║                                   ║                     ║
║  █▀▀▀▀█╗░      ▀▀█▀▀╚█▀█╚█▀█╚█║   ║ By: Nguyễn Công Giới║
║ ░█░      ╚████╗ ░█   █░█ █░█ █║   ║ Sđt: 0367093723     ║
║ ░█░░ ███░       ░█░  █▄█ █▄█ █▄▄╗ ║ Fb:fb.com/bumbum26.4║
║ ░█▄▄▄▄█░░        ═   ╚═╝ ╚═╝ ╚══╝ ║ TOOL TRAODOISUB     ║
║  ╚════╝                           ║                     ║
╚═════════════════════════════════════════════════════════╝
'''
    clr()
    print(Colorate.Horizontal(Colors.rainbow, in1, 2))


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def hoan_thanh(dem, type, xu_tang, xu):
    list_color = ["\033[1;97m", "\033[1;91m", "\033[1;96m",
                  "\033[93m", "\033[92m", "\033[95m", "\033[1;95m"]
    color = random.choice(list_color)
    tgian = datetime.now().strftime('%H:%M:%S')
    x = f"[{dem}]  {tgian}  {type}  Đã Ẩn id  +{str(xu_tang)} Tổng: {str(xu)}"
    print(Colorate.Diagonal(Colors.yellow_to_green, f"[{dem}] ") + f"{red}● "+Colorate.Horizontal(Colors.white_to_green, tgian) +
          f" {red}● {color}{type} {red}● "+Colorate.DiagonalBackwards(Colors.white_to_black, "Ẩn ID") + f" {red}● {green}+{xu_tang} {red}● {white}Xu: {vang}{xu}")


def delay(delay1, delay2):
    delay_ = random.randint(delay1, delay2)
    for j in range(delay_, -1, -1):
        print(Colorate.Horizontal(Colors.blue_to_cyan,
              f"Vui Lòng Chờ {str(j)} giây > "), end=' \r')
        time.sleep(0.1)
        print(Colorate.Horizontal(Colors.white_to_blue,
              f"Vui Lòng Chờ {str(j)} giây   > "), end=' \r')
        time.sleep(0.1)
        print(Colorate.Horizontal(Colors.green_to_yellow,
              f"Vui Lòng Chờ {str(j)} giây     > "), end=' \r')
        time.sleep(0.1)
        print(Colorate.Horizontal(Colors.blue_to_purple,
              f"Vui Lòng Chờ {str(j)} giây      > "), end=' \r')
        time.sleep(0.1)
        print(Colorate.Horizontal(Colors.rainbow,
              f"Vui Lòng Chờ {str(j)} giây        > "), end=' \r')
        time.sleep(0.1)
        print(Colorate.Horizontal(Colors.green_to_white,
              f"Vui Lòng Chờ {str(j)} giây             "), end=' \r')
        time.sleep(0.5)


clr()
intro()
while True:
    if os.path.isfile('token_tds_conggioi.txt') == False:
        token_tds = str(Write.Input(">>> Nhập Token traodoisub: ",
                        Colors.white_to_green, interval=0.0025))
    else:
        print(Colorate.Horizontal(Colors.yellow_to_red,
              '[1] ')+f"{green}Để nhập token traodoisub mới")
        print(Colorate.Horizontal(Colors.yellow_to_red,
              '[2] ')+f"{green}Để nhập token traodoisub cũ")
        options_tds = str(Write.Input(
            ">>> Chọn: ", Colors.white_to_green, interval=0.0025))
        if options_tds == '1':
            token_tds = str(Write.Input(">>> Nhập Token traodoisub: ",
                                        Colors.white_to_green, interval=0.0025))
        elif options_tds == '2':
            with open('token_tds_conggioi.txt', 'r') as f:
                token_tds = f.read()

        else:
            exit(f"{red}>Chọn sai<")
        os.remove('token_tds_conggioi.txt')

    check_token_tds = requests.get(
        f"https://traodoisub.com/api/?fields=profile&access_token={token_tds}").json()
    if 'success' in check_token_tds:
        user_tds = check_token_tds['data']['user']
        xu_tds = check_token_tds['data']['xu']
        with open('token_tds_conggioi.txt', 'a') as f:
            f.write(token_tds)
        break
    else:
        Write.Print("Token traodoisub không hợp lệ!\n",
                    Colors.red_to_white, interval=0.0025)

Write.Print("="*50, Colors.yellow_to_red, interval=0.0025, end='\n')
list_cookie = []
dem = 1
while True:
    if len(list_cookie) == 0:
        dem_token = 1
        while True:
            cookie_fb = str(Write.Input(
                f">>> Nhập Cookie facebook {dem_token}: ", Colors.white_to_green, interval=0.0025))
            if cookie_fb == '':
                break
            head = {
                'authority': 'business.facebook.com',
                'cache-control': 'max-age=0',
                'sec-ch-ua-mobile': '?0',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'en,vi;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
                'cookie': cookie_fb
            }
            Write.Print("Đang Check Cookie Facebook",
                        Colors.blue_to_red, end=' \r', interval=0.001)
            token_fb_ = requests.get(
                'https://business.facebook.com/business_locations/?page_id=107478190916224', headers=head).text
            try:
                token_fb = token_fb_[token_fb_.find('EAAG'):].split('"')[0]
                check_token_fb = requests.get(
                    f"https://graph.facebook.com/me/?access_token={token_fb}").json()

                if 'id' in check_token_fb:
                    list_cookie.append(cookie_fb)
                    try:
                        person = requests.post(
                            f"https://graph.facebook.com/661977978284858/likes?access_token={token_fb}")
                    except:
                        pass
                    print(
                        f"{green}Tên: {vang}{check_token_fb['name']}   {green}UID: {vang}{check_token_fb['id']}    ")
                    dem_token += 1
                else:
                    print(
                        f"{white}[!]{red}Cookie die                              ")
            except:
                print(
                    f"{white}[!]{red}Cookie die                              ")
    clr()
    intro()
    if dem == 1:
        print(Colorate.Vertical(Colors.yellow_to_green, '-'*50))
        print(Colorate.Horizontal(Colors.yellow_to_green,
              "[1]") + f"{green} Nhiệm vụ Like")
        print(Colorate.Horizontal(Colors.yellow_to_green,
              "[2]") + f"{green} Nhiệm vụ Comment")
        print(Colorate.Horizontal(Colors.yellow_to_green,
              "[3]") + f"{green} Nhiệm vụ Share")
        print(Colorate.Horizontal(Colors.yellow_to_green,
              "[4]") + f"{green} Nhiệm vụ Follow")
        print(Colorate.Horizontal(Colors.yellow_to_green,
              "[5]") + f"{green} Nhiệm vụ Cảm Xúc")
        print(Colorate.Vertical(Colors.green_to_blue, '-'*50))
        option_job = str(Write.Input(
            ">>> Chọn nhiệm vụ (Nhiều nhiệm vụ thêm dấu +): ", Colors.white_to_green, interval=0.0025))
        if len(option_job) > 1:
            option_job = option_job.split('+')
            if '1' in option_job:
                option_job.append('1')
        try:
            block = int(Write.Input('>>> Bao nhiêu nhiệm vụ thì chống block: ',
                        Colors.yellow_to_green, interval=0.0025))
            delay_block = int(Write.Input(
                f'>>> Sau {block} nhiệm vụ chống block bao nhiêu giây: ', Colors.white_to_green, interval=0.0025))
            delay1 = int(Write.Input('>>> Delay từ: ',
                         Colors.blue_to_white, interval=0.0025))
            delay2 = int(Write.Input(
                '>>> Đến: : ', Colors.blue_to_white, interval=0.0025))
            convert_fb = int(Write.Input(
                '>>> Sau bao nhiêu nhiệm vụ thì đổi tài khoản: ', Colors.white_to_green, interval=0.0025))
            stop_tool = int(Write.Input(
                '>>> Sau bao nhiêu nhiệm vụ thì dừng tool: ', Colors.yellow_to_green, interval=0.0025))
        except:
            exit(f"\n{red}[!]{white} Nhập Sai")
    cookie_error = 0
    for cookie in list_cookie:
        if cookie_error == 1:
            break
        head = {
            'authority': 'business.facebook.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en,vi;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
            'cookie': cookie
        }
        try:
            token_ = requests.get(
                'https://business.facebook.com/business_locations/?page_id=107478190916224', headers=head).text
            token_fb = token_[token_.find('EAAG'):].split('"')[0]
            data_fb = requests.get(
                f"https://graph.facebook.com/me/?access_token={token_fb}").json()
        except:
            list_cookie.remove(cookie)
            print(f"{red}[!]{white} Cookie die")
            continue
        run_tds = requests.get(
            f"https://traodoisub.com/api/?fields=run&id={str(data_fb['id'])}&access_token={token_tds}").json()
        if 'success' in run_tds:
            print(Colorate.Horizontal(Colors.white_to_red, '-'*50), end='\n')
            print(
                f"{green}Cấu hình uid: {vang}{data_fb['id']} {green}Name: {vang}{data_fb['name']}")
            print(Colorate.Horizontal(Colors.white_to_red, '-'*50), end='\n')
            time.sleep(1.5)
        else:
            exit(
                f"{red}[!]{white} Vào lại tds cấu hình uid{green} {data_fb['id']}")
        error_like = 0
        error_cmt = 0
        error_share = 0
        error_follow = 0
        error_cxuc = 0
        while True:
            if dem % stop_tool == 0:
                exit(f"{green}Đã dừng tool")
            if cookie_error == 1:
                break
            job_ = random.choice(option_job)
            if (job_ == '1') and (error_like == 0):
                uid_like = requests.get(
                    f"https://traodoisub.com/api/?fields=like&access_token={token_tds}").json()
                if len(uid_like) > 0:
                    if 'countdown' in uid_like:
                        for _ in range(int(uid_like['countdown']), 0, -1):
                            print(Colorate.DiagonalBackwards(
                                Colors.yellow_to_red, f"Lấy nhiệm vụ quá nhanh, thử lại sau: {str(_)}"), end=' \r')
                            time.sleep(1)
                    elif 'error' in uid_like:
                        if len(uid_like) == 1:
                            print(f"{white} {uid_like['error']}")
                            break
                    else:
                        print(
                            f"{vang}Tìm Thấy {str(len(uid_like))} Nhiệm Vụ Like                     ", end=' \r')
                        time.sleep(1)
                        for i in range(len(uid_like)):
                            like = requests.post(
                                f"https://graph.facebook.com/{str(uid_like[int(i)]['id'])}/likes?access_token={token_fb}").json()
                            get_like = requests.get(
                                f"https://traodoisub.com/api/coin/?type=LIKE&id={str(uid_like[int(i)]['id'])}&access_token={token_tds}").json()
                            if 'success' in get_like:
                                hoan_thanh(dem, "LIKE", "300",
                                           get_like['data']['xu'])
                                if dem % block == 0:
                                    delay(delay_block, delay_block)
                                else:
                                    delay(delay1, delay2)
                                dem += 1
                            elif 'thao tác chậm lại' in get_like['error']:
                                time.sleep(2)
                            else:
                                if like == True:
                                    time.sleep(2)
                                elif 'error' in like:
                                    if like['error']['code'] == 368:
                                        if 'spam' in like['error']['message']:
                                            print(Colorate.Horizontal(
                                                Colors.red_to_yellow, like['error']['message']))
                                            delay(5, 8)
                                        else:
                                            print(Colorate.Horizontal(
                                                Colors.red_to_yellow, "Đã bị block like"))
                                            if len(option_job) == 1:
                                                cookie_error = 1
                                                list_cookie.remove(cookie)
                                                break
                                            elif len(option_job) > 1:
                                                error_like = 1
                                    elif like['error']['code'] == 190:
                                        try:
                                            token_ = requests.get(
                                                'https://business.facebook.com/business_locations/?page_id=107478190916224', headers=head).text
                                            token_fb = token_[token_.find('EAAG'):].split('"')[
                                                0]
                                            data_fb = requests.get(
                                                f"https://graph.facebook.com/me/?access_token={token_fb}").json()
                                        except:
                                            list_cookie.remove(cookie)
                                            cookie_error = 1
                                            print(
                                                f"{red}[!]{white} Cookie die")
                                            break
                                else:
                                    time.sleep(2)
                            if dem % stop_tool == 0:
                                exit(f"{green}Đã dừng tool")
                            if dem % convert_fb == 0:
                                break
                        time.sleep(5)
                elif len(uid_like) == 0:
                    print(Colorate.Horizontal(
                        Colors.red_to_blue, 'Tạm Thời Hết Nhiệm Vụ'), end=' \r')
                    time.sleep(5)
            elif (job_ == '2') and (error_cmt == 0):
                uid_cmt = requests.get(
                    f"https://traodoisub.com/api/?fields=comment&access_token={token_tds}").json()
                if len(uid_cmt) > 0:
                    if 'countdown' in uid_cmt:
                        for _ in range(int(uid_cmt['countdown']), 0, -1):
                            print(Colorate.DiagonalBackwards(
                                Colors.yellow_to_red, f"Lấy nhiệm vụ quá nhanh, thử lại sau: {str(_)}"), end=' \r')
                            time.sleep(1)
                    elif 'error' in uid_cmt:
                        if len(uid_cmt) == 1:
                            print(f"{white} {uid_cmt['error']}")
                            break
                    else:
                        print(
                            f"{vang}Tìm Thấy {str(len(uid_cmt))} Nhiệm Vụ Comment                           ", end=' \r')
                        time.sleep(1)
                        for i in range(len(uid_cmt)):
                            cmt = requests.post(
                                f"https://graph.facebook.com/{str(uid_cmt[int(i)]['id'])}/comments", data={'access_token': token_fb, 'message': str(uid_cmt[int(i)]['msg'])}).json()
                            get_cmt = requests.get(
                                f"https://traodoisub.com/api/coin/?type=COMMENT&id={str(uid_cmt[int(i)]['id'])}&access_token={token_tds}").json()
                            if 'success' in get_cmt:
                                hoan_thanh(dem, "COMMENT", "600",
                                           get_cmt['data']['xu'])
                                print(
                                    f"{xanhnhat}{str(uid_cmt[int(i)]['msg'])}")
                                if dem % block == 0:
                                    delay(delay_block, delay_block)
                                else:
                                    delay(delay1, delay2)
                                dem += 1
                            elif 'thao tác chậm lại' in get_cmt['error']:
                                time.sleep(2)
                            else:
                                if 'id' in cmt:
                                    time.sleep(2)
                                elif 'error' in cmt:
                                    if cmt['error']['code'] == 368:
                                        if 'spam' in cmt['error']['message']:
                                            print(Colorate.Horizontal(
                                                Colors.red_to_yellow, cmt['error']['message']))
                                            delay(5, 8)
                                        else:
                                            print(Colorate.Horizontal(
                                                Colors.red_to_yellow, "Đã bị block comment"))
                                            if len(option_job) == 1:
                                                cookie_error = 1
                                                list_cookie.remove(cookie)
                                                break
                                            elif len(option_job) > 1:
                                                error_cmt = 1
                                    elif cmt['error']['code'] == 190:
                                        try:
                                            token_ = requests.get(
                                                'https://business.facebook.com/business_locations/', headers=head).text
                                            token_fb = token_[token_.find('EAAG'):].split('"')[
                                                0]
                                            data_fb = requests.get(
                                                f"https://graph.facebook.com/me/?access_token={token_fb}").json()
                                        except:
                                            list_cookie.remove(cookie)
                                            cookie_error = 1
                                            print(
                                                f"{red}[!]{white} Cookie die")
                                            break
                                else:
                                    time.sleep(2)
                            if dem % stop_tool == 0:
                                exit(f"{green}Đã dừng tool")
                            if dem % convert_fb == 0:
                                break
                        time.sleep(5)
                elif len(uid_like) == 0:
                    print(Colorate.Horizontal(
                        Colors.red_to_blue, 'Tạm Thời Hết Nhiệm Vụ'), end=' \r')
                    time.sleep(5)
            elif (job_ == '3') and (error_share == 0):
                uid_share = requests.get(
                    f"https://traodoisub.com/api/?fields=share&access_token={token_tds}").json()
                if len(uid_share) > 0:
                    if 'countdown' in uid_share:
                        for _ in range(int(uid_share['countdown']), 0, -1):
                            print(Colorate.DiagonalBackwards(
                                Colors.yellow_to_red, f"Lấy nhiệm vụ quá nhanh, thử lại sau: {str(_)}"), end=' \r')
                            time.sleep(1)
                    elif 'error' in uid_share:
                        if len(uid_share) == 1:
                            print(f"{white} {uid_share['error']}")
                            break
                    else:
                        print(
                            f"{vang}Tìm Thấy {str(len(uid_share))} Nhiệm Vụ Share                           ", end=' \r')
                        time.sleep(1)
                        for i in range(len(uid_share)):
                            share = requests.post(f"https://graph.facebook.com/v2.0/me/feed", data={
                                                  'privacy': '{"value":"EVERYONE"}', 'link': 'https://mbasic.facebook.com/' + str(uid_share[int(i)]['id']), 'access_token': token_fb}).json()
                            get_share = requests.get(
                                f"https://traodoisub.com/api/coin/?type=SHARE&id={str(uid_share[int(i)]['id'])}&access_token={token_tds}").json()
                            print(get_share)
                            if 'success' in get_share:
                                hoan_thanh(dem, "SHARE", "800",
                                           get_share['data']['xu'])
                                if dem % block == 0:
                                    delay(delay_block, delay_block)
                                else:
                                    delay(delay1, delay2)
                                dem += 1
                            elif 'thao tác chậm lại' in get_share['error']:
                                time.sleep(2)
                            else:
                                if 'id' in share:
                                    time.sleep(2)
                                elif 'error' in share:
                                    if share['error']['code'] == 368:
                                        if 'spam' in share['error']['message']:
                                            print(Colorate.Horizontal(
                                                Colors.red_to_yellow, share['error']['message']))
                                            delay(5, 8)
                                        else:
                                            print(Colorate.Horizontal(
                                                Colors.red_to_yellow, "Đã bị block share"))
                                            if len(option_job) == 1:
                                                cookie_error = 1
                                                list_cookie.remove(cookie)
                                                break
                                            elif len(option_job) > 1:
                                                error_share = 1
                                    elif share['error']['code'] == 190:
                                        try:
                                            token_ = requests.get(
                                                'https://business.facebook.com/business_locations/', headers=head).text
                                            token_fb = token_[token_.find('EAAG'):].split('"')[
                                                0]
                                            data_fb = requests.get(
                                                f"https://graph.facebook.com/me/?access_token={token_fb}").json()
                                        except:
                                            list_cookie.remove(cookie)
                                            cookie_error = 1
                                            print(
                                                f"{red}[!]{white} Cookie die")
                                            break
                                else:
                                    time.sleep(2)
                            if dem % stop_tool == 0:
                                exit(f"{green}Đã dừng tool")
                            if dem % convert_fb == 0:
                                break
                        time.sleep(5)
                elif len(uid_like) == 0:
                    print(Colorate.Horizontal(
                        Colors.red_to_blue, 'Tạm Thời Hết Nhiệm Vụ'), end=' \r')
                    time.sleep(5)
            elif (job_ == '4') and (error_follow == 0):
                uid_follow = requests.get(
                    f"https://traodoisub.com/api/?fields=follow&access_token={token_tds}").json()
                if len(uid_follow) > 0:
                    if 'countdown' in uid_follow:
                        for _ in range(int(uid_follow['countdown']), 0, -1):
                            print(Colorate.DiagonalBackwards(
                                Colors.yellow_to_red, f"Lấy nhiệm vụ quá nhanh, thử lại sau: {str(_)}"), end=' \r')
                            time.sleep(1)
                    elif 'error' in uid_follow:
                        if len(uid_follow) == 1:
                            print(f"{white} {uid_follow['error']}")
                            break
                    else:
                        print(
                            f"{vang}Tìm Thấy {str(len(uid_follow))} Nhiệm Vụ Follow                           ", end=' \r')
                        time.sleep(1)
                        for i in range(len(uid_follow)):
                            share = requests.post(f"https://graph.facebook.com/v2.0/me/feed", data={
                                                  'privacy': '{"value":"EVERYONE"}', 'link': 'https://mbasic.facebook.com/' + str(uid_share[int(i)]['id']), 'access_token': token_fb}).json()
                            get_share = requests.get(
                                f"https://traodoisub.com/api/coin/?type=SHARE&id={str(uid_follow[int(i)]['id'])}&access_token={token_tds}").json()
                            print(get_share)
                            if 'success' in get_share:
                                hoan_thanh(dem, "SHARE", "800",
                                           get_share['data']['xu'])
                                if dem % block == 0:
                                    delay(delay_block, delay_block)
                                else:
                                    delay(delay1, delay2)
                                dem += 1
                            elif 'thao tác chậm lại' in get_share['error']:
                                time.sleep(2)
                            else:
                                if 'id' in share:
                                    time.sleep(2)
                                elif 'error' in share:
                                    if share['error']['code'] == 368:
                                        if 'spam' in share['error']['message']:
                                            print(Colorate.Horizontal(
                                                Colors.red_to_yellow, share['error']['message']))
                                            delay(5, 8)
                                        else:
                                            print(Colorate.Horizontal(
                                                Colors.red_to_yellow, "Đã bị block share"))
                                            if len(option_job) == 1:
                                                cookie_error = 1
                                                list_cookie.remove(cookie)
                                                break
                                            elif len(option_job) > 1:
                                                error_share = 1
                                    elif share['error']['code'] == 190:
                                        try:
                                            token_ = requests.get(
                                                'https://business.facebook.com/business_locations/', headers=head).text
                                            token_fb = token_[token_.find('EAAG'):].split('"')[
                                                0]
                                            data_fb = requests.get(
                                                f"https://graph.facebook.com/me/?access_token={token_fb}").json()
                                        except:
                                            list_cookie.remove(cookie)
                                            cookie_error = 1
                                            print(
                                                f"{red}[!]{white} Cookie die")
                                            break
                                else:
                                    time.sleep(2)
                            if dem % stop_tool == 0:
                                exit(f"{green}Đã dừng tool")
                            if dem % convert_fb == 0:
                                break
                        time.sleep(5)
                elif len(uid_like) == 0:
                    print(Colorate.Horizontal(
                        Colors.red_to_blue, 'Tạm Thời Hết Nhiệm Vụ'), end=' \r')
                    time.sleep(5)
            if dem % convert_fb == 0:
                break
