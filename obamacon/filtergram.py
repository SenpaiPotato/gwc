from PIL import Image
import filters

def main():
    filename = "obama.jpg"
    img = filters.load_img(filename)
    filters.obamicon(img)
    img.show()







#don't touch
if __name__ == "__main__":
    main()