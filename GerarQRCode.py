#pip install qrcode

import qrcode

links_sites = {
    "google":"https://www.google.com.br",
    "Olhar digital":"https://www.olhardigital.com.br"
}

for link in links_sites:
    site = links_sites[link]
    imagem_qrcode = qrcode.make(site)
    imagem_qrcode.save(f"qrcode_{link}.png")