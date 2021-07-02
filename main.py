from tkinter import *


class GUI(Tk):
    def __init__(self, title="Window", icon=None, width=200, height=200, bg="white",
                 resizableX=0, resizableY=0):
        super().__init__()
        self.title(title)
        self.iconbitmap(icon)
        self.geometry(f"{width}x{height}")
        self.config(bg=bg)
        self.resizable(resizableX, resizableY)

    def start(self):
        self.mainloop()

    def stop(self):
        self.destroy()


class TopWindow(Toplevel):
    def __init__(self, title, msg):
        super(TopWindow, self).__init__()
        self.title(title)
        self.geometry("270x100")
        self.resizable(0, 0)
        msg = Label(self, text=msg)
        msg.pack()


def formatName(name):
    if len(name) > 20:
        return name[:8] + "...." + name[-8:]
    return name


def open_img():
    import os
    from PIL import Image
    from tkinter import filedialog
    global img

    root.img_dir = filedialog.askopenfilename(initialdir="D:", title="Select image to make icon",
                                              filetypes=(
                                                  ("PNG Images", "*.png"),
                                                  ("JPG Images", "*.jpg"),
                                                  ("ALL Files", "*.*")
                                              ))
    try:
        img = Image.open(root.img_dir)
        fileName.config(text=formatName(os.path.basename(root.img_dir)))
        convB.config(state=ACTIVE)
    except:
        fileName.config(text="Invalid")
        convB.config(state=DISABLED)
        prevB.config(state=DISABLED)
    outputName.config(text="None")


def convert_image():
    from tkinter import filedialog
    import os
    global output_path

    output_path = filedialog.asksaveasfilename(initialfile='icon.ico', defaultextension=".ico",
                                               filetypes=[("Icon Files", "*.ico")])
    img.save(output_path, format="ICO", sizes=[(ico_size.get(), ico_size.get())])
    prevB.config(state=ACTIVE)
    outputName.config(text=formatName(os.path.basename(output_path)))


def preview():
    prev = TopWindow("Preview", "This is your preview")
    prev.iconbitmap(output_path)


if __name__ == '__main__':
    bg = "white"
    # Making Window
    root = GUI(title="Icon Maker", width=350, height=120, icon="icon.ico")

    chooseL = Label(root, text="Choose Image", bg=bg)
    chooseL.grid(row=0, column=0, pady=5, padx=5)

    chooseB = Button(root, text="Choose", command=open_img, width=10)
    chooseB.grid(row=0, column=1, pady=5, padx=10)

    fileName = Label(root, text="None", bg=bg, anchor=W, width=20)
    fileName.grid(row=0, column=2, pady=5, padx=5)

    sizeL = Label(root, text="Select size", bg=bg)
    sizeL.grid(row=1, column=0, pady=5, padx=5)

    ico_size = IntVar()
    sizes = [16, 24, 32, 48, 64, 128, 255]
    ico_size.set(32)
    size_menu = OptionMenu(root, ico_size, *sizes)
    size_menu.config(width=6)
    size_menu.grid(row=1, column=1, pady=5, padx=10)

    convB = Button(root, text="Convert", width=10, state=DISABLED, command=convert_image)
    convB.grid(row=2, column=0, pady=5, padx=5)

    prevB = Button(root, text="Preview", width=10, state=DISABLED, command=preview)
    prevB.grid(row=2, column=1, pady=5, padx=10)

    outputName = Label(root, text="None", bg=bg, anchor=W, width=20)
    outputName.grid(row=2, column=2, pady=5, padx=5)

    # Starting Window
    root.start()
