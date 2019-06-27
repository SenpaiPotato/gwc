from PIL import Image
import filters

def main():
    filename = "michelle.jpg"
    img_object = Image.open("michelle.jpg")
    filters.obamicon(img_object)
    # img_object.show()







#don't touch
if __name__ == "__main__":
    main()