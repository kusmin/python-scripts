from datetime import datetime

import instaloader

# carrega a lib e faz login na conta
L = instaloader.Instaloader()
L.login('usuario', 'senha')

# carrega todos os posts do perfil escolhido
posts = instaloader.Profile.from_username(L.context, "pycodebr").get_posts()

# Periodo que deseja baixar os post
SINCE = datetime(2021, 1, 16)
UNTIL = datetime(2021, 1, 18)

# Percorre os posts e baixa apenas os que estao dentro do periodo desejado
for post in posts:
    if(post.date >= SINCE) and (post.date <= UNTIL):
        print(post.date)
        L.download_post(post, "insta-posts-downloads")
