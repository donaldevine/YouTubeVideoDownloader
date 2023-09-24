import pytube # pip install pytube

# "https://www.youtube.com/watch?v=VIDEO_ID"
video_url = input("What is the Video URL?")

destination = input("Where do you want to save the video (path to folder) ?")

youtube = pytube.YouTube(video_url)

stream = youtube.streams.get_highest_resolution()

stream.download(output_path=destination)

print("Video downloaded successfully!")
