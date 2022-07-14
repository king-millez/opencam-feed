import os
import re
import atexit
import shutil
import requests
import subprocess
from time import sleep
from datetime import datetime
from urllib.parse import urlsplit


with open("root.js", "r") as f:
    ip = re.search(r"const ip = '(.+)'", f.read()).group(1)

index = 0
out_dir = (
    "".join(f"{i.split(':')[0]}_" for i in urlsplit(ip).netloc.split("."))
    + "seq_"
    + str(int(datetime.now().timestamp()))
)
os.mkdir(out_dir)


def create_video():
    print("Writing MP4")
    if os.name == "nt":
        ffmpeg = "ffmpeg.exe"
    else:
        ffmpeg = "ffmpeg"
    subprocess.run(
        [
            ffmpeg,
            "-r",
            "1",
            "-i",
            f"{out_dir}/img%05d.jpg",
            "-c:v",
            "libx264",
            "-vf",
            "fps=25",
            "-pix_fmt",
            "yuv420p",
            f"{out_dir}.mp4",
        ]
    )
    shutil.rmtree(out_dir)


atexit.register(create_video)

while True:
    data = requests.get(
        f"{ip}cgi-bin/CGIProxy.fcgi?cmd=snapPicture2&usr=admin&pwd=&{int(datetime.now().timestamp() * 10**3)}"
    ).content
    fname = os.path.join(out_dir, f"img{str(index).zfill(5)}.jpg")
    with open(fname, "wb") as f:
        f.write(data)
    print(f"Wrote {fname}")
    index += 1
    sleep(1)
