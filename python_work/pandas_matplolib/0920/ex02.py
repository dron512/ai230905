import urllib.request

url = 'https://files.juvis.co.kr/upload/star/pc/images/sbs_ing/star_w_detail_top.png'

# 로컬에 저장될 파일 경로 및 이름
local_file_path = 'c.png'

# URL로부터 파일을 다운로드하고 로컬에 저장
urllib.request.urlretrieve(url, local_file_path)

print('다운로드가 완료되었습니다.')