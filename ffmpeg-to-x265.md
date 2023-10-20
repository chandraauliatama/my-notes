# My Script to Convert Video to x265 format for smaaller file size

## change to x265 codec(hemat size)

```
ffmpeg -i input.mp4 -vcodec libx265 -crf 28 output.mp4
```

## change all files in folder to x265

```
for i in *.mp4; do ffmpeg -i "$i" -vcodec libx265 -crf 28 "edited/${i%.*}.mp4"; done
```
