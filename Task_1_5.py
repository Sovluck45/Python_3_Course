import chardet
import subprocess

args = ['ping', 'yandex.ru']
yandex_process = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in yandex_process.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

args = ['ping', 'youtube.com']
youtube_process = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in youtube_process.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
