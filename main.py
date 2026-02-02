import os
import time
from colorist import bg_rgb
import sys

COLOR_BLACK = "\033[0;30m"
COLOR_RED = "\033[0;31m"
COLOR_GREEN = "\033[0;32m"
COLOR_BROWN = "\033[0;33m"
COLOR_BLUE = "\033[0;34m"
COLOR_PURPLE = "\033[0;35m"
COLOR_CYAN = "\033[0;36m"
COLOR_LIGHT_GRAY = "\033[0;37m"
COLOR_DARK_GRAY = "\033[1;30m"
COLOR_LIGHT_RED = "\033[1;31m"
COLOR_LIGHT_GREEN = "\033[1;32m"
COLOR_YELLOW = "\033[1;33m"
COLOR_LIGHT_BLUE = "\033[1;34m"
COLOR_LIGHT_PURPLE = "\033[1;35m"
COLOR_LIGHT_CYAN = "\033[1;36m"
COLOR_LIGHT_WHITE = "\033[1;37m"
B = "\033[1m"
W = "\033[0m"

vnlogo = """
#447294 #447294█#447294█#457394▓#457395█#457395█#457395█#457395 #457395▓#467495█#467496█#467496 #467496 #467496 #467496█#477596█#477597▓#477597 #477597 #477597 #477597 #487697█#487698█#487698▒#487698 #487698 #497698 #497798█#497799▓#497799 #497799█#497799 #4a7899 #4a7899 #4a789a #4a789a█#4a789a█#4a789a #4b799a #4b799a█#4b799b█#4b799b█#4b799b▄#4c799b #4c7a9b #4c7a9b #4c7a9c #4c7a9c█#4c7a9c #4d7a9c #4d7b9c█#4d7b9c #4d7b9d #4d7b9d #4d7b9d #4e7b9d█#4e7c9d█#4e7c9d #4e7c9e #4e7c9e▒#4e7c9e█#4f7c9e█#4f7d9e█#4f7d9e█#4f7d9f█#4f7d9f #507d9f #507e9f #507e9f█#507e9f█#507ea0█#507ea0▄#517ea0 #517fa0 #517fa0 #517fa0 #517fa1█#517fa1 #527fa1 #5280a1 #5280a1▄#5280a1█#5280a2█#5280a2█#5380a2█#5381a2 
#5381a2▓#5381a2█#5381a3█#5481a3░#5481a3 #5482a3 #5482a3█#5482a3█#5482a4▒#5582a4▒#5583a4█#5583a4█#5583a4 #5583a4 #5583a5█#5683a5█#5684a5▒#5684a5 #5684a5 #5684a5 #5684a6▓#5784a6█#5785a6█#5785a6░#5785a6 #5785a6 #5885a6 #5885a7█#5886a7▒#5886a7 #5886a7█#5886a7█#5986a7 #5986a8 #5987a8▓#5987a8█#5987a8█#5987a8▒#5a87a8 #5a88a9█#5a88a9█#5a88a9 #5a88a9▀#5b88a9█#5b88a9 #5b89aa #5b89aa #5b89aa█#5b89aa #5c89aa #5c89aa█#5c8aab█#5c8aab #5c8aab #5c8aab▓#5d8aab█#5d8aab█#5d8bac▒#5d8bac▒#5d8bac█#5d8bac█#5e8bac▒#5e8bac #5e8cad #5e8cad█#5e8cad█#5f8cad▒#5f8cad #5f8dad█#5f8dae█#5f8dae #5f8dae▀#608dae█#608dae #608eae #608eaf #608eaf█#608eaf #618eaf #618eaf█#618faf█#618fb0▒#618fb0 #618fb0▀#628fb0█#628fb0▒
#6290b0▓#6290b1█#6290b1█#6390b1░#6390b1 #6390b1█#6391b1█#6391b2▓#6391b2▒#6491b2 #6491b2▒#6491b2█#6492b2█#6492b3 #6492b3█#6592b3█#6592b3░#6593b3 #6593b3 #6593b4 #6593b4 #6693b4▓#6693b4█#6694b4█#6694b4 #6694b5 #6794b5█#6794b5▒#6794b5░#6795b5▓#6795b5█#6795b6█#6895b6 #6895b6 #6895b6▒#6896b6█#6896b6█#6896b7░#6996b7▓#6996b7█#6996b7█#6997b7 #6997b7 #6a97b7▀#6a97b8█#6a97b8 #6a98b8█#6a98b8█#6a98b8▒#6b98b8▓#6b98b9█#6b98b9█#6b99b9 #6b99b9 #6b99b9▒#6c99b9█#6c99ba█#6c99ba░#6c9aba▒#6c9aba█#6c9aba█#6d9aba░#6d9abb #6d9abb #6d9bbb█#6d9bbb█#6e9bbb▒#6e9bbb▓#6e9bbc█#6e9bbc█#6e9cbc #6e9cbc #6f9cbc▀#6f9cbc█#6f9cbd #6f9dbd█#6f9dbd█#6f9dbd▒#709dbd▒#709dbd█#709dbe█#709ebe░#709ebe▄#709ebe▄#719ebe▄#719ebe░
#719ebf▒#719fbf█#719fbf█#729fbf▄#729fbf█#729fbf▓#729fc0▒#72a0c0 #72a0c0▒#73a0c0 #73a0c0░#73a0c0 #73a0c1▐#73a1c1█#73a1c1█#74a1c1▓#74a1c1░#74a1c1 #74a1c2 #74a2c2 #74a2c2 #75a2c2 #75a2c2▒#75a2c2█#75a3c3█#75a3c3 #76a3c3█#76a3c3░#76a3c3░#76a3c3▓#76a4c4▓#76a4c4█#77a4c4 #77a4c4 #77a4c4░#77a4c4█#77a5c5█#77a5c5░#78a5c5▓#78a5c5█#78a5c5█#78a5c5▒#78a6c6 #79a6c6 #79a6c6▐#79a6c6▌#79a6c6█#79a6c6█#79a7c7▒#7aa7c7▓#7aa7c7▓#7aa7c7█#7aa7c7 #7aa8c7 #7aa8c8░#7ba8c8█#7ba8c8█#7ba8c8░#7ba8c8▒#7ba9c8█#7ba9c9█#7ca9c9 #7ca9c9 #7ca9c9 #7ca9c9█#7caac9█#7daac9░#7daaca▓#7daaca█#7daaca█#7daaca▒#7dabca #7eabca #7eabcb▐#7eabcb▌#7eabcb█#7eabcb█#7eaccb▒#7faccb░#7faccc▓#7faccc█#7faccc #7fadcc #7fadcc█#80adcc█#80adcd▓
#80adcd▒#80adcd█#80aecd█#81aecd▒#81aecd #81aece░#81aece #81aece #81afce░#82afce #82afce░#82afcf #82afcf█#82afcf█#82b0cf▒#83b0cf▓#83b0cf░#83b0d0 #83b0d0 #83b0d0 #83b1d0 #84b1d0 #84b1d0 #84b1d1▒#84b1d1▀#84b2d1█#85b2d1░#85b2d1 #85b2d1 #85b2d2▒#85b2d2▒#85b3d2█#86b3d2█#86b3d2█#86b3d2█#86b3d3█#86b3d3▓#86b4d3 #87b4d3▒#87b4d3█#87b4d3█#87b4d4░#87b4d4 #88b5d4 #88b5d4 #88b5d4▓#88b5d4█#88b5d5█#88b5d5░#89b6d5▒#89b6d5▒#89b6d5█#89b6d5█#89b6d6█#89b6d6█#8ab7d6█#8ab7d6▓#8ab7d6 #8ab7d6░#8ab7d7 #8ab8d7█#8bb8d7█#8bb8d7█#8bb8d7█#8bb8d7▓#8bb8d8▒#8cb9d8░#8cb9d8▒#8cb9d8█#8cb9d8█#8cb9d8░#8cb9d9 #8dbad9 #8dbad9 #8dbad9▓#8dbad9█#8dbad9█#8dbada░#8ebbda░#8ebbda▒#8ebbda▓#8ebbda█#8ebbda█#8ebbdb█#8fbcdb▀#8fbcdb▒
#8fbcdb▒#8fbcdb▓#8fbcdb▒#90bcdb░#90bcdb #90bcdb░#90bcdb #91bcda #91bcda░#91bdda #91bdda #92bdda█#92bdda█#92bdda▒#92bdda▒#93bdda▒#93bdda #93bdda #93bdda #93bdda #94bdda #94bdd9 #94bdd9 #94bdd9░#95bdd9 #95bed9▐#95bed9░#95bed9 #96bed9 #96bed9░#96bed9▒#96bed9▓#97bed9▒#97bed9 #97bed9▒#97bed8 #97bed8▒#98bed8 #98bed8░#98bed8 #98bed8▒#99bed8░#99bfd8 #99bfd8 #99bfd8 #9abfd8▒#9abfd8 #9abfd8▒#9abfd8 #9bbfd7░#9bbfd7▒#9bbfd7▓#9bbfd7▒#9bbfd7 #9cbfd7▒#9cbfd7 #9cbfd7▒#9cbfd7 #9dc0d7░#9dc0d7 #9dc0d7▒#9dc0d7░#9ec0d7▒#9ec0d6░#9ec0d6▒#9ec0d6░#9fc0d6 #9fc0d6░#9fc0d6 #9fc0d6▒#9fc0d6░#a0c0d6 #a0c0d6 #a0c0d6 #a0c0d6▒#a1c1d6 #a1c1d6▒#a1c1d5 #a1c1d5 #a2c1d5░#a2c1d5▒#a2c1d5 #a2c1d5 #a3c1d5 #a3c1d5▒#a3c1d5 
#a3c1d5░#a3c1d5▒#a4c1d5 #a4c1d5░#a4c1d4 #a4c2d4 #a5c2d4 #a5c2d4 #a5c2d4 #a5c2d4▓#a6c2d4█#a6c2d4█#a6c2d4 #a6c2d4░#a7c2d4▒#a7c2d4░#a7c2d4 #a7c2d4 #a7c2d3 #a8c2d3 #a8c2d3 #a8c2d3 #a8c3d3 #a9c3d3░#a9c3d3 #a9c3d3░#a9c3d3░#aac3d3 #aac3d3 #aac3d3░#aac3d3░#abc3d3▒#abc3d2░#abc3d2 #abc3d2░#abc3d2 #acc3d2░#acc3d2 #acc4d2░#acc4d2 #adc4d2░#adc4d2░#adc4d2 #adc4d2 #aec4d2 #aec4d2░#aec4d1 #aec4d1▒#afc4d1░#afc4d1░#afc4d1░#afc4d1▒#afc4d1░#b0c4d1 #b0c4d1░#b0c5d1 #b0c5d1░#b1c5d1 #b1c5d1 #b1c5d1 #b1c5d0░#b2c5d0 #b2c5d0▒#b2c5d0 #b2c5d0▒#b3c5d0░#b3c5d0 #b3c5d0░#b3c5d0 #b3c5d0░#b4c5d0░#b4c6d0 #b4c6d0 #b4c6d0 #b5c6cf░#b5c6cf #b5c6cf▒#b5c6cf░#b6c6cf #b6c6cf #b6c6cf░#b6c6cf #b7c6cf #b7c6cf #b7c6cf░#b7c6cf 
#b7c6cf░#b8c6ce░#b8c7ce #b8c7ce #b8c7ce #b9c7ce #b9c7ce #b9c7ce #b9c7ce #bac7ce▒#bac7ce #bac7ce▒#bac7ce #bbc7ce░#bbc7ce░#bbc7cd #bbc7cd #bbc7cd #bcc8cd #bcc8cd #bcc8cd #bcc8cd #bdc8cd #bdc8cd #bdc8cd #bdc8cd░#bec8cd░#bec8cd #bec8cd #bec8cc #bfc8cc░#bfc8cc░#bfc8cc░#bfc8cc #bfc8cc░#c0c9cc #c0c9cc░#c0c9cc #c0c9cc #c1c9cc #c1c9cc #c1c9cc░#c1c9cc #c2c9cb #c2c9cb #c2c9cb░#c2c9cb #c3c9cb░#c3c9cb #c3c9cb #c3c9cb░#c4cacb░#c4cacb░#c4cacb #c4cacb░#c4cacb #c5cacb░#c5caca #c5caca░#c5caca #c6caca░#c6caca #c6caca░#c6caca #c7caca▒#c7caca #c7caca #c7caca #c8cbca #c8cbca #c8cbca░#c8cbc9 #c8cbc9 #c9cbc9 #c9cbc9░#c9cbc9 #c9cbc9░#cacbc9 #cacbc9░#cacbc9 #cacbc9░#cbcbc9 #cbcbc9 #cbcbc9 #cbccc9░#ccccc8 
#ccccc8 #ccccc8 #ccccc8 #ccccc8 #cdccc8 #cdccc8 #cdccc8 #cdccc8 #ceccc8 #ceccc8░#ceccc8 #ceccc8░#cfccc7 #cfccc7 #cfccc7 #cfcdc7 #d0cdc7 #d0cdc7 #d0cdc7 #d0cdc7 #d0cdc7 #d1cdc7 #d1cdc7 #d1cdc7 #d1cdc7 #d2cdc7 #d2cdc6░#d2cdc6 #d2cdc6 #d3cdc6 #d3cdc6 #d3cec6 #d3cec6░#d4cec6 #d4cec6 #d4cec6 #d4cec6 #d4cec6 #d5cec6 #d5cec6 #d5cec5 #d5cec5 #d6cec5 #d6cec5 #d6cec5 #d6cec5 #d7cec5 #d7cec5░#d7cfc5 #d7cfc5 #d8cfc5 #d8cfc5 #d8cfc5░#d8cfc5 #d8cfc4 #d9cfc4 #d9cfc4 #d9cfc4 #d9cfc4 #dacfc4 #dacfc4 #dacfc4 #dacfc4░#dbcfc4 #dbd0c4░#dbd0c4 #dbd0c4 #dcd0c4 #dcd0c3 #dcd0c3 #dcd0c3 #dcd0c3 #ddd0c3 #ddd0c3 #ddd0c3 #ddd0c3 #ded0c3░#ded0c3 #ded0c3 #ded0c3 #dfd0c3 #dfd1c3 #dfd1c2 #dfd1c2 #e0d1c2░#e0d1c2 
#e0d1c2 #e0d1c2 #e0d1c2 #e1d1c2 #e1d1c2 #e1d1c2 #e1d1c2 #e2d1c2 #e2d1c2 #e2d1c1░#e2d1c1 #e3d2c1░#e3d2c1 #e3d2c1 #e3d2c1 #e4d2c1 #e4d2c1 #e4d2c1 #e4d2c1 #e4d2c1 #e5d2c1 #e5d2c1 #e5d2c1 #e5d2c0 #e6d2c0 #e6d2c0░#e6d2c0 #e6d2c0 #e7d3c0 #e7d3c0 #e7d3c0 #e7d3c0 #e8d3c0 #e8d3c0 #e8d3c0 #e8d3c0 #e8d3c0 #e9d3bf #e9d3bf #e9d3bf #e9d3bf #ead3bf #ead3bf #ead3bf #ead4bf #ebd4bf #ebd4bf #ebd4bf #ebd4bf #ecd4bf #ecd4bf #ecd4be #ecd4be #ecd4be #edd4be #edd4be #edd4be #edd4be #eed4be #eed4be #eed4be #eed5be #efd5be #efd5be #efd5be #efd5bd #f0d5bd #f0d5bd #f0d5bd #f0d5bd #f0d5bd #f1d5bd #f1d5bd #f1d5bd #f1d5bd #f2d5bd #f2d5bd #f2d6bd #f2d6bd #f3d6bc #f3d6bc #f3d6bc #f3d6bc #f4d6bc #f4d6bc #f4d6bc 

"""

def logo():
    vnlg = vnlogo
    for line in vnlg.strip().split('\n'):
        bo = line.split('#')
        for part in bo:
            if not part: continue
            a = part[:6]
            b = part[6:]
            do = int(a[0:2], 16)
            xanh = int(a[2:4], 16)
            xanh_bien = int(a[4:6], 16)
            sys.stdout.write(f'\033[38;2;{do};{xanh};{xanh_bien}m{b}')
        sys.stdout.write('\n')

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def yt():
    def ytvideo():
        clear()
        logo()
        from rich.console import Console
        console = Console()
        console.print("[bold blue]PyVuNuong 1.0![/bold blue]")
        from pytubefix import YouTube
        from pytubefix.cli import on_progress
        print("Nhập link video:")
        url = input("> ")
        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)
        ys = yt.streams.get_highest_resolution()
        ys.download()
    def ytamthanh():
        clear()
        logo()
        from rich.console import Console
        console = Console()
        console.print("[bold blue]PyVuNuong 1.0![/bold blue]")
        from pytubefix import YouTube
        from pytubefix.cli import on_progress
        url = input("Nhập link video: ")
        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)
        ys = yt.streams.get_audio_only()
        ys.download()
    clear()
    logo()
    from rich.console import Console
    console = Console()
    console.print("[bold blue]PyVuNuong 1.0![/bold blue]")
    print("""
1. Tải video
2. Tải âm thanh
    """)
    try:
        yt = int(input("> "))
    except ValueError:
        clear()
        print("Vui lòng lựa chọn 1-2!")
        return
        exit()
    if yt == 1:
        ytvideo()
    elif yt == 2:
        ytamthanh()
    else:
        clear()
        print("Lựa chọn không hợp lệ")

def sp():
    import speedtest
    clear()
    logo()
    from rich.console import Console
    console = Console()
    console.print("[bold blue]PyVuNuong 1.0![/bold blue]")
    print("🚀 Đang kiểm tra tốc độ internet, vui lòng chờ...")
    st = speedtest.Speedtest()
    st.get_best_server()
    down_speed = st.download() / 1_000_000
    up_speed = st.upload() / 1_000_000
    ping = st.results.ping
    clear()
    logo()
    from rich.console import Console
    console = Console()
    console.print("[bold blue]PyVuNuong 1.0![/bold blue]")
    print("\n" + "="*30)
    print("📊 KẾT QUẢ KIỂM TRA TỐC ĐỘ")
    print("="*30)
    print(f"⬇️ Tải xuống: {down_speed:.2f} Mbps")
    print(f"⬆️ Tải lên:   {up_speed:.2f} Mbps")
    print(f"🏓 Ping:      {ping:.1f} ms")
    print("="*30)

def qrcode():
    import qrcode
    clear()
    logo()
    from rich.console import Console
    console = Console()
    console.print("[bold blue]PyVuNuong 1.0![/bold blue]")
    print("Gửi link cần tạo thành mã QR:")
    qr1 = input("> ")
    if qr1 == "":
        clear()
        print("Vui lòng gửi link!")
        exit()
    clear()
    logo()
    console.print("[bold blue]PyVuNuong 1.0![/bold blue]")
    print("Tên của file ảnh:")
    qr2 = input("> ")
    if qr2 == "":
        clear()
        print("Vui lòng gửi file!")
        exit()
    try:
        os.mkdir("QR")
    except FileExistsError:
        time.sleep(0.1)
    qr = qrcode.make(f"{qr1}")
    qr3 = str(f"{qr2}.png")
    qr4 = os.path.join("QR", f"{qr2}.png")
    qr.save(f'QR/{qr2}.png')
    print('✅ Đã tạo xong!')
    print("📍 > " + os.path.abspath(qr4))

def danhsachchucnang():
    from rich.console import Console
    console = Console()
    console.print("[bold blue]PyVuNuong 1.0![/bold blue]")
    print(f"""
1. Tạo QR
2. Speed Test
3. Tải video/âm thanh Youtube

By IdlerHa
    """)
    try:
        lc = int(input("> "))
    except ValueError:
        clear()
        print("Vui lòng lựa chọn 1-3!")
        return
        exit()
    if lc == 1:
        qrcode()
    elif lc == 2:
        sp()
    elif lc == 3:
        yt()
    else:
        clear()
        print("Vui lòng lựa chọn 1-3!")
        return
        exit()
clear()
logo()
danhsachchucnang()
