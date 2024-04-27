## Youtube Video Downloader Python Project

---

**Project description**

The YouTube Video Downloader is a Python project developed to enable users to download videos from YouTube effortlessly. This project provides a convenient solution for users to access videos offline.

---

Import the library YouTube from pytube

```python
from pytube import YouTube
```
---

Create the function download_video, which represents the core of the software.

```python
def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print('Video downloaded successfully!')
    except Exception as e:
        print(e)
```
---

In this cell the software is executed, taking as input the url of the YouTube video.

```python
video_url = input('Enter a YouTube url: ')

folder = 'Downloads'

print('Started download...')
download_video(video_url, folder)
```

---

**Final considerations**

* While this project is straightforward in its current form, there is still ample opportunity for improvement to enhance its functionality and user experience.
* Despite its simplicity, the project has proven its practical value, as evidenced by personal usage experiences.
