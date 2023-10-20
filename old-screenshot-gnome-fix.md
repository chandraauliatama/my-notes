# Return Old Screenshots Feature in Gnome

## Requirement

- Install Gnome Screenshot

```
sudo apt install gnome-screenshot -y
```

- Disable shortcut screenshot default

## Add New Shortcut

### Screenshot(PrtScr)

```
sh -c 'gnome-screenshot && xclip "/home/chandraat/Pictures/Screenshots/Screenshot from $(date +\%Y-\%m-\%d) $(date +\%H-\%M-\%S).png" -selection clipboard -target image/png'
```

### Screenshot to clipboard only(Ctrl + PrtScr)

```
sh -c 'gnome-screenshot -cf /tmp/test.png && xclip /tmp/test.png -selection clipboard -target image/png; rm /tmp/test.png || echo ""'
```

### Screenshot selected area (Shift + PrtScr)

```
sh -c 'gnome-screenshot -a && xclip "/home/chandraat/Pictures/Screenshots/Screenshot from $(date +\%Y-\%m-\%d) $(date +\%H-\%M-\%S).png" -selection clipboard -target image/png'
```

### Screnshot selected area to clipboard only(Shift + Ctrl + PrtScr)

```
sh -c 'gnome-screenshot -af /tmp/test.png && xclip /tmp/test.png -selection clipboard -target image/png; rm /tmp/test.png || echo ""'
```

### Screnshot active window(Alt + PrtScr)

```
sh -c 'gnome-screenshot -w && xclip "/home/chandraat/Pictures/Screenshots/Screenshot from $(date +\%Y-\%m-\%d) $(date +\%H-\%M-\%S).png" -selection clipboard -target image/png'
```

### Screnshot active window to clipboard only(Alt + Ctrl + PrtScr)

```
sh -c 'gnome-screenshot -wf /tmp/test.png && xclip /tmp/test.png -selection clipboard -target image/png; rm /tmp/test.png || echo ""'
```

## How To Remember The Shortcuts

- PrtScr = Do Screenshot
- Ctrl = Clipboard Only
- Shift = Select Area
- Alt = Active Window
