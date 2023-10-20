# Script My Experiment for Converting Video to x264 Format

## x265 to x264

```
ffmpeg -i input.mp4 -map 0 -c:v libx264 -crf 20 -c:a copy output.mp4
```

## autoencode all in folder to x264

```
for i in *.mkv; do ffmpeg -i "$i" -map 0 -c:v libx264 -crf 20 -c:a copy "x264/${i%.*}.mkv"; done
```

## x265 to x264(HighProfile)

```
ffmpeg -i input.mkv -map 0 -c:v libx264 -profile:v high -pix_fmt yuv420p -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -crf 20 -c:a copy output.mkv
```

## if error subtitle(add -s:a copy)

```
ffmpeg -i input.mkv -map 0 -c:v libx264 -profile:v high -pix_fmt yuv420p -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -crf 20 -c:a copy -s:a copy output.mkv
```

## auto all in folder to x264(HighProfile)

```
for i in *.mkv; do ffmpeg -i "$i" -map 0 -c:v libx264 -profile:v high -pix_fmt yuv420p -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -crf 20 -c:a copy "FolderBaru/${i%.*}.mkv"; done
```

## speed video

```
ffmpeg -i input.mkv -filter_complex "[0:v]setpts=0.5*PTS[v]" -map "[v]" output.mkv
```

## automatic

```
for i in *.mkv; do ffmpeg -i "$i" -filter_complex "[0:v]setpts=0.5*PTS[v]" -map "[v]" "render/${i%.*} - UAS.mkv"; done
```
