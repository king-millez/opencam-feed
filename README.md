# opencam-feed

**This project is for fun and education (what's the difference right?)**

This is a hacky little thing for viewing and downloading openly accessible webcam feeds.

If you know how to use the network tab in your browser's 'inspect' menu that'll help you.

This only has foscam code in it at the moment (and another brand but I forgot what it was, it's commented out in [root.js](/root.js))

## Setup

1. You'll need a camera IP. You can view open ones (no password required) on [Insecam](http://www.insecam.org/en/):
![cameras](/.github/img/1.PNG)
2. Select a camera. By default this application only supports foscam branded webcams - mainly because I don't want to get in trouble - but this will work with any camera that sends its streams as image sequences with a little tweaking.
3. Open [root.js](/root.js). replace `ipgohere` with the IP _and port_ of the cam. (like `const ip = 'http://106.70.45.58:89/'`)

#### Non-foscam

1. If you want to be really l33t, you can hack in a different type of camera. Take an open Vivotek camera on Insecam for example. Upon analysis of the camera's client, we can see how it requests the images:
![camera network activity](/.github/img/2.PNG)

The application requests the feed with this simple URL:

`http://{ip:port}/cgi-bin/viewer/video.jpg?r={timestamp}`

The format is a simple JPG image, so all you have to do is replace the format string(s) in [root.js](/root.js) _and_ [write_img_seq.py](/write_img_seq.py) (if you plan on downloading the stream) with that URL.

## Usage

### Viewing

For simple viewing, open `index.html` in your browser. If there's multiple cameras being used in the feed, the CSS and JS will handle this for you (if you set it up correctly).

### Downloading

You'll need [ffmpeg](https://ffmpeg.org/) for the application to automatically convert the downloaded image sequences to a playable MP4 file.

To download the camera feed, simply run
```sh
python3 write_img_seq.py
```
It will download for as long as you run it. When you're satisfied with the length of the feed download, hit **Ctrl + C** and `ffmpeg` will merge the sequence into a video file, then the script will terminate.

## Issues

If you have a problem with this "application":
1. I wouldn't be surprised
2. I can be reached on [Twitter](https://twitter.com/king_millez) if you want something fixed but don't know what you're doing, or
3. Feel free to submit a pull request.