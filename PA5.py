from matplotlib import pyplot
from matplotlib import image
import numpy as np

def main():
    word = input("which buttons do you want to press")
    
    while word != "Q":
        if word == "M":
            menu()
        elif word == "L":
            name = input("Which file you want to execute")
            img = image.imread(name)
            img2 = np.asarray(img)
        elif word == "V":
            pyplot.imshow(img)
        elif word == "I":
            print(img2.shape)
        elif word == "F":
            factor = int(input("which factor you want to give"))
            img3 =  img2[::factor,::factor,::]
            pyplot.imshow(img3)
        elif word == "Z":
            scale = int(input("Which scale you want to give"))
            img4 = img2[160 - scale:160 + scale,118 - scale:118 + scale,:]
            pyplot.imshow(img4)
        elif word == "B":
            val = int(input("What is the value that you want"))
            b1 = brighten(img2,val)
            pyplot.imshow(b1)
        elif word == "E":
            val = int(input("What value that you want"))
            e1 = edge_detect(img2,val)
            pyplot.imshow(e1)
        elif word == "C":
            alpha = float(input("What value that you want"))
            c1 = colorize(img2,alpha)
            pyplot.imshow(c1)
        elif word == "R":
            rg_blind = red_green_colorblindness(img2)
            pyplot.imshow(rg_blind)
        elif word == "S":
        
            pyplot.imsave('image3.jpg',img2)
            pyplot.imsave('image3.jpg',img3)
            pyplot.imsave('image4.jpg',img4)
            pyplot.imsave('image5.jpg',b1)
            pyplot.imsave("image6.jpg", e1)
            pyplot.imsave("image7.jpg", c1)
            pyplot.imsave("image8.jpg", rg_blind)
        word = input("which buttons do you want to press")
    print("goodbye")



def menu():
    print("M - print this menu")
    print("L - ask for a name of an image file and load it into the system")
    print("V  - view the current image (use pyplot.imshow)")
    print("I  - print Info about the image including its size")
    print("F - scale down the image by an integer factor k (and ask the user for that factor)")
    print("Z - zoom in on a range of the image (ask the user for the bounds)")
    print("B - brighten the image by a specified value (ask the user for the value)")
    print("E - run edge detection on the image with a specified difference value")
    print("C - colorize the image with the factor alpha (ask the user for alpha)'")
    print("R - run the red-green-color blindness filter on the image")
    print("S - save the image in a file (ask the user for the file name)")
    print("Q - quit the program")
    


def brighten(img, val):
    img2 = img.copy()
    for i in range(len(img2)):
        for j in range(len(img2[0])):
            x = img2[i][j]
            for k in range(3):
                x[k] += val
                if x[k] < 0:
                    x[k] = 0
    return img2
        
def colorize(img,alpha):
    img2 = img.copy()
    for i in range(len(img2)):
        for j in range(len(img2[0])):
            x = img2[i][j]
            m = (int(x[0]) + int(x[1]) + int(x[2])) / 3
            for i in range(3):
                if x[i] > m:
                    x[i] = x[i] * (1 - alpha) + 255 * alpha
                else:
                    x[i] = x[i] *(1 - alpha)
    return img2
           
def red_green_colorblindness(img):
    img2 = img.copy()
    for i in range(len(img2)):
        for j in range(len(img2[0])):
            x = img2[i][j]
            x[0] = x[0] // 2 + x[1] // 2
            x[1] = x[0] // 2 + x[1] // 2
    return img2

def edge_detect(img,val):
    img2 = img.copy()
    for i in range(len(img2)):
        for j in range(len(img2[0])):
            x = img2[i][j]
            if i != len(img2) - 1:
                r = img2[i + 1][j]
                if (abs(x[0]-r[0])+abs(x[1]-r[1]) + abs(x[2]-r[2])> val):
                    x[0] = 255
                    x[1] = 255
                    x[2] = 255
                else:
                    x[0] = 0
                    x[1] = 0
                    x[2] = 0
            if j != len(img2[0]) - 1:
                b = img2[i][j + 1]
                if (abs(x[0]-b[0])+abs(x[1]-b[1]) + abs(x[2]-b[2])> val):
                    x[0] = 255
                    x[1] = 255
                    x[2] = 255
                else:
                    x[0] = 0
                    x[1] = 0
                    x[2] = 0
    return img2
                          
main()