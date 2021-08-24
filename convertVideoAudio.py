import moviepy.editor

# Carrega arquivo de video
video = moviepy.editor.VideoFileClip(
    "/home/renan/Vídeos/O Esquadrão Suicida 2021 1080p WEB-DL DUAL 5.1/O Esquadrão Suicida 2021 1080p WEB-DL DUAL 5.1.mkv")

audio_data = video.audio

audio_data.write_audiofile("audio.mp3")
