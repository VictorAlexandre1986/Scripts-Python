#pip install speedtest-cli

import speedtest

objeto = speedtest.Speedtest()

download = objeto.download()

upload = objeto.upload()

conf = objeto.get_servers()

print(f'Download: {round((download)/(1024*1024))}GB')
print(f'Upload: {round((upload)/(1024*1024))}GB')
print('Informações sobre o servidor speedtest: {conf}')