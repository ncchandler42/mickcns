import subprocess
import functools
import json
import tkinter as tk
from PIL import Image, ImageTk

def get_dosxid():
    xid = subprocess.run(
        ["xdotool", "search", "--name", "DOSBox"],
        capture_output=True
    ).stdout

    return str(xid, encoding="utf-8").strip()

def sendkey(xid, key):
    subprocess.run(
        ["xdotool", "key", "--window", xid, key]
    )

with open("mapping.json", "r") as mapping:
    keymap = json.load(mapping)

xid = get_dosxid()
if xid == "":
    print("Unable to find DOSBox window. Is DOSBox running?")
    exit()

mainscreen = tk.Tk()
mainscreen.title("Mickey's Colors and Shapes")

icons = {}
cmds = {}
for buttid in keymap.keys():
    icons[buttid] = ImageTk.PhotoImage(Image.open(f"icons/{buttid}.png"))
    cmds[buttid] = functools.partial(sendkey, xid, keymap[buttid])
    tk.Button(
        mainscreen,
        image=icons[buttid],
        command=cmds[buttid]
    ).pack(side="left")

mainscreen.mainloop()
