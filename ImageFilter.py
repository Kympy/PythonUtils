import cv2


def load_image(img_name):
    loaded_image = cv2.imread("Images\\" + img_name)

    if loaded_image is None:
        print("Loaded Image " + img_name + " is None")
        return

    return loaded_image

def save_image(save_name, pixel_array):
    save_name += ".jpg"
    print("Saved Image : " + save_name)
    cv2.imwrite("Images\\" + save_name, pixel_array)

def negative(img_name):

    loaded_image = load_image(img_name)
    if loaded_image is None:
        return

    height = loaded_image.shape[0]
    width = loaded_image.shape[1]
    #print("Image size : " + str(width) + " * " + str(height))

    for col in range(height):
        for row in range(width):
            # Subtract 255, 255, 255 from pixel
            new_pixel = abs(loaded_image[col, row] - [255, 255, 255])
            #print(str(loaded_image[col, row]) + " - 255, 255, 255 = " + str(new_pixel))
            loaded_image[col, row] = new_pixel

    save_name = img_name.split('.')[0] + "_reversed"
    save_image(save_name, loaded_image)

def custom_gray_scale(img_name):
    loaded_image = load_image(img_name)
    if loaded_image is None:
        return

    height = loaded_image.shape[0]
    width = loaded_image.shape[1]

    for col in range(height):
        for row in range(width):
            # Get average value of pixels
            added = int(loaded_image[col, row][0]) + loaded_image[col, row][1] + loaded_image[col, row][2]
            if added != 0:
                average = (added) / 3
            else:
                average = 0

            new_pixel = [average, average, average]
            loaded_image[col, row] = new_pixel

    save_name = img_name.split('.')[0] + "_grayscale"
    save_image(save_name, loaded_image)