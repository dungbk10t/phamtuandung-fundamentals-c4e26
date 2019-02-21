from youtube_dl import YoutubeDL
#VD1: Tải xuống 1 video youtobe:
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=WHK5p7JL7g4"])
#VD2: Tải xuống nhiều videos youtobe:
dl = YoutubeDL()
# Đặt danh sách các url bài hát trong chức năng 
# tải xuống để tải xuống từng cái một
dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])

#VD3: Download audio
options = {
    "format":"bestaudio/audio" 
    # Nói với người tải xuống chỉ tải xuống chất lượng âm thanh tốt nhất
}
dl = YoutubeDL(options)
dl.download(["https://www.youtube.com/watch?v=3bJkVSMs4dw"])

#VD4: Tìm kiếm và sau đó tải xuống video đầu tiên.
options = {
    "default_search":"ytsearch",
    # bảo người tải xuống tìm kiếm thay vì tải xuống trực tiếp
    "max_downloads": 1,
    # Yêu cầu người tải xuống chỉ tải xuống mục đầu tiên (âm thanh)
    "format":"bestaudio/audio",
}
dl = YoutubeDL(options)
dl.download(["THẰNG ĐIÊN | JUSTATEE x PHƯƠNG LY | OFFICIAL MV"])
