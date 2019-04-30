from PIL import Image


class ClubFilter:

    # Class' attributes
    filter_name = "Club"
    filter_preview_url = ""

    # Filter method
    @staticmethod
    def filter(img):
        # Retrieve the width and height of the image
        width, height = img.size

        # Create a copy of the original image
        img_copy = img.copy()

        # Two for loops in order to change each pixel
        for x in range(width):
            for y in range(height):
                # Take the pixel at (x, y)
                r, g, b = img.getpixel((x,y))
                # Remove the Green values from that pixel and apply the change to the image
                img_copy.putpixel((x,y), (r, 0, b))

        return img_copy


class Grayscale:

    # Class attributes
    filter_name = "Grayscale"
    filter_preview_url = ""

    # Filter method
    @staticmethod
    def filter(img):
        # Retrieve the width and height of the image
        width, height = img.size

        # Create a copy of the original image
        img_copy = img.copy()

        # Two for loops in order to change each pixel
        for x in range(width):
            for y in range(height):
                # Take the pixel at (x, y)
                r, g, b = img.getpixel((x, y))
                average = round(((r + b + g)/3))
                # Change the RGB values to make the photo gray
                img_copy.putpixel((x, y), (average, average, average))

        return img_copy


class Negative:

    # Class' attributes
    filter_name = "Negative"
    filter_preview_url = ""

    # Filter method
    @staticmethod
    def filter(img):
        # Retrieve the width and height of the image
        width, height = img.size

        # Create a copy of the original image
        img_copy = img.copy()

        # Two for loops in order to change each pixel
        for x in range(width):
            for y in range(height):
                # Take the pixel at (x, y)
                r, g, b = img.getpixel((x,y))
                # Subtract the r g b values from 255 in order to get the inverted values
                img_copy.putpixel((x,y), (255-r, 255-g, 255-b))

        return img_copy


class Sepia:

    # Class' attributes
    filter_name = "Sepia"
    filter_preview_url = ""

    # Filter method
    @staticmethod
    def filter(img):
        # Retrieve the width and height of the image
        width, height = img.size

        # Create a copy of the original image
        img_copy = img.copy()

        # Two for loops in order to change each pixel
        for x in range(width):
            for y in range(height):
                # Take the pixel at (x, y)
                r, g, b = img.getpixel((x,y))
                # Subtract the r g b values from 255 in order to get the inverted values
                sepiaR = (r * 0.393 + g * 0.769 + b * 0.189)
                sepiaG = (r * 0.349 + g * 0.686 + b * 0.168)
                sepiaB = (r * 0.272 + g * 0.534 + b * 0.131)
                if sepiaR > 255:
                    sepiaR = 255
                if sepiaG > 255:
                    sepiaG = 255
                if sepiaB > 255:
                    sepiaB = 255
                img_copy.putpixel((x,y), (int(sepiaR), int(sepiaG), int(sepiaB)))

        return img_copy

class Flip:

    # Class' attributes
    filter_name = "Flip"
    filter_preview_url = ""

    # Filter method
    @staticmethod
    def filter(img):
        # Retrieve the width and height of the image
        width, height = img.size

        # Create a copy of the original image
        img_copy = img.copy()

        # Two for loops in order to change each pixel
        for x in range(width):
            for y in range(height):
                # Take the pixel at (x, y)
                r, g, b = img.getpixel((width-x-1, y))
                # Subtract the r g b values from 255 in order to get the inverted values
                img_copy.putpixel((x, y), (r, g, b))

        return img_copy

class Mirror:

    # Class' attributes
    filter_name = "Mirror"
    filter_preview_url = ""

    # Filter method
    @staticmethod
    def filter(img):
        # Retrieve the width and height of the image
        width, height = img.size

        # Create a copy of the original image
        img_copy = img.copy()

        # Two for loops in order to change each pixel
        for x in range(width//2):
            for y in range(height):
                # Take the pixel at (x, y)
                r, g, b = img.getpixel((width-x-1, y))
                # Subtract the r g b values from 255 in order to get the inverted values
                img_copy.putpixel((x, y), (r, g, b))

        return img_copy

# class Blur:
#
#     def filter(image):
#         img_copy = img.copy()
#         width, height = img.size
#         clear_radius = width / 4
#         img_copy = img_copy.filter(ImageFilter.BLUR)
#         return img_copy
#


if __name__ == '__main__':
    # Open the image file and read in its data so that we can access it
    img = Image.open('../fisher.jpeg')

    new_img_one = ClubFilter.filter(img)
    new_img_two = Grayscale.filter(img)
    new_img_three = Negative.filter(img)
    new_img_four = Sepia.filter(img)
    new_img_five = Mirror.filter(img)
    new_img_six = Flip.filter(img)
    new_img_seven = Blur.filter(img)

    new_img_one.save('club_filter.jpg')
    new_img_two.save('grayscale.jpg')
    new_img_three.save('negative.jpg')
    new_img_four.save('sepia.jpg')
    new_img_five.save('mirror.jpg')
    new_img_six.save('flip.jpg')
    new_img_seven.save('blur.jpg')