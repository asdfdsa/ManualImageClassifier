import sys
import numpy as np
import matplotlib.pyplot as plt
import shutil
import datetime
from PIL import Image
from pathlib import Path
from matplotlib.widgets import Button

class manual_classifier(object):

    """The class uses only matplotlib functions to realize a convenient manual classification for images
    that sit in the specified folder. It will copy the images to the desired image class folder (e.g.
    class_1 and class_2)

    Input:
    The path of images that are mixed and that need to be classified into two classes.

    Usage:
    manualLabeler (str)/path/to/your/images

    author: Bin Wang
    email: alexwang911217@gmail.com"""

    def __init__(self, path, name="*", folder="*", iformat="tiff"):
        self.classified_path = Path(path)
        self.particularName = name
        self.particularFolder = folder
        self.img_format = iformat

        self.now = datetime.datetime.now().strftime("%H:%M:%S")
        self.now = self.now.replace(":","_")
        self.ind = 0

        self.img_enumerator = self.image_enumerator(path=self.classified_path)

        self.class_1_path = path.parent / "class_1"
        self.class_1_path.mkdir(parents=True, exist_ok=True)
        self.class_2_path = path.parent / "class_2"
        self.class_2_path.mkdir(parents=True, exist_ok=True)

        self.fig = plt.figure()

        self.b1 = Button(self.fig.add_axes([0, 0.75, 0.1, 0.04]), 'Class_1')
        self.b1.on_clicked(self.Classify_to_1)

        self.b2 = Button(self.fig.add_axes([0, 0.50, 0.1, 0.04]), 'Class_2')
        self.b2.on_clicked(self.Classify_to_2)

        self.b3 = Button(self.fig.add_axes([0, 0.25, 0.1, 0.04]), 'Skip')
        self.b3.on_clicked(self.next_img)

        self.canvas = self.fig.add_axes([0, 0, 1, 1])
        self.canvas.get_xaxis().set_visible(False)
        self.canvas.get_yaxis().set_visible(False)

        self.current_img_path = next(self.img_enumerator)[1]

        img0 = self.read_img(self.current_img_path)
        self.img_to_update = self.plot_img(ax = self.canvas, imgarray=img0)

        plt.show()

    def next_img(self, event=None):
        try:
            self.current_img_path = next(self.img_enumerator)[1]
            imgnew = self.read_img(self.current_img_path)
            self.img_to_update.set_data(imgnew)
            plt.draw()
        except StopIteration:
            print("Images have been exhausted!")
            pass

    def read_img(self, img_path):
        return np.array(Image.open(img_path))

    def Classify_to_1(self, path):
        path = self.class_1_path / f"{self.now}_{self.ind}.{self.img_format}"
        self.ind += 1
        print(f"copying file to {path}...")
        try:
            shutil.copy(self.current_img_path, path)
        except shutil.SameFileError:
            print(f"Image {self.current_img_path} has already been copied!")
            pass
        finally:
            self.next_img()

    def Classify_to_2(self, path):
        path = self.class_2_path / f"{self.now}_{self.ind}.{self.img_format}"
        self.ind += 1
        print(f"copying file to {path}...")
        try:
            shutil.copy(self.current_img_path, path)
        except shutil.SameFileError:
            print(f"Image {self.current_img_path} has already been copied!")
            pass
        finally:
            self.next_img()

    def plot_img(self, ax, imgarray):
        return ax.imshow(imgarray, vmin=imgarray.min(), vmax=imgarray.max())

    def image_enumerator(self, path, particularFolder = None, particularName="*", iformat = "tiff"):
        particularFolder = self.particularFolder
        particularName = self.particularName
        if particularFolder == "*":
            print(f"{particularName}.{iformat}")
            imagefiles = path.rglob(f"{particularName}.{iformat}")
        else:
            print(f"{particularFolder}\\{particularName}.{iformat}")
            imagefiles = path.rglob(f"{particularFolder}\\{particularName}.{iformat}")
        return enumerate(imagefiles)

def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        path = Path(r".\tiff_image")
    try:
        pn = sys.argv[2]
    except IndexError:
        pn = "*"
    try:
        pf = sys.argv[3]
    except IndexError:
        pf = "*"

    manual_classifier(path, pn, pf)

if __name__ == "__main__":
    main()
