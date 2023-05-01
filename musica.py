from pytube import YouTube
from moviepy.editor import *

# URL do vídeo a ser baixado
url = "https://www.youtube.com/watch?v=t050lriI0_w"

# Baixa o vídeo usando a biblioteca pytube
yt = YouTube(url)
stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
stream.download()

# Converte o vídeo para MP3 usando a biblioteca moviepy
video = VideoFileClip(stream.default_filename)
audio = video.audio
audio.write_audiofile("audio.mp3")

# Remove o arquivo de vídeo original
os.remove(stream.default_filename)
