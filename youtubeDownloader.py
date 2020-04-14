from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=YXal3Q-L-WI').streams.first().download()
