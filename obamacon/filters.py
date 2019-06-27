from PIL import Image

def load_img(filename):
    img = Image.open(filename)
    return img

def show_img(img_object):
    img_object.show()

def save_img(img_object, save_name):
    img_object.save(save_name)
#should return a new image object with filter applied
def obamicon(img_object):
    #create new empty list where you will put new pixel values into (use Append)
    original_pixels = img_object.getdata()
    intensities = []
    for i in range(0,len(original_pixels)):

        intensity = int(sum(original_pixels[i]))
        intensities.append(intensity)
    for i in intensities:
        if i < 182:
            original_pixels.append(0, 51, 76)
        elif 182 < i < 364:
            original_pixels.append(207, 26, 33)
        elif 364 < i < 546:
            original_pixels.append(112, 150, 158)
        elif i > 546:
            original_pixels.append(252, 227, 166)
    img_object.putdata(original_pixels)
    print(original_pixels)
    #use for loop to go through each pixel
    #at every pixel sum up the rgb values

    #use conditionals and boolean checks to determine which new color to change to

 