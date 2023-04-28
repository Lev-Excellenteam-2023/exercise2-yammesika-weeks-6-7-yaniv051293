
import imageio as iio

def main():
    # read an image
    img = iio.v3.imread('code.png')
    list_of_numbers = []
    print(img.shape)
    for y in range(0,img.shape[1]):
        for x in range(0, img.shape[0]):
            pixel_value = img[x, y]
            if pixel_value != 255:
                list_of_numbers.append(x)

    for number in list_of_numbers:
        print(chr(number), end="")

if __name__ == '__main__':
    main()