
import yt_dlp
url = "https://www.youtube.com/watch?v=s5OIP-EjMe8"
options = {
    "format": "bestaudio/best",
    "extractaudio": True,  # Extracts only audio
    "audioformat": "mp3",  # Converts to MP3
    "outtmpl": "%(title)s.mp3",  # Saves as title.mp3
}
with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])





#with yt_dlp.YoutubeDL(options) as ydl:
 #   ydl.download([url])
