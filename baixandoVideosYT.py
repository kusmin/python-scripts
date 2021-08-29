from pytube import YouTube

# Digite o link do video e o local que deseja salvar o video
link = input("Digite o link do video que deseja baixar: ")
path = input("Digite o directorio que deseja salvar o video: ")
yt = YouTube(link)

# Mostra os detalhes do video
print("titulo: ", yt.title)
print("numero de views", yt.views)
print("tamanho do video: {} segundos".format(yt.length))
print("Avaliação do video: ", yt.rating)

# Usa a maior resolução
ys = yt.streams.get_highest_resolution()

# Começa o Download do video
print("Baixando....")
ys.download(path)
print("Download Completo!")
