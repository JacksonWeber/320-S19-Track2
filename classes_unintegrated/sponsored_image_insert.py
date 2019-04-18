from PIL import Image
from PIL import ImageFilter

class sponsoredImageInsertion:

    def scale(self, height, widht, factor):
       #TODO: write code for scaling, aka return scaled height and width
        return False

    def insert(mg, sponsored_item):
        # retrieve the width and height of the image for the scale


        # create a scale for insert to be resized to


        # create a copy of the original image
        img_copy = img.copy()

        # retrieve the proper sponsored item insert
        insert = Image.open('sponsored_items/' + sponsored_item + '.jpg')
        width, height = insert.size
        width_scale = round(width * .2)
        height_scale = round(height * .2)
        print(width_scale)
        print(height_scale)
        # resize the sponsored item
        insert = insert.resize((width_scale,height_scale))

        for x in range(width_scale):
            for y in range(height_scale):
                pixel = insert.getpixel((x, y))
                img_copy.putpixel((x, y), pixel)

        # return the image with the sponsored content inserted
        return img_copy

    def insertPNG(mg, sponsored_item):
        # retrieve the width and height of the image for the scale


        # create a copy of the original image
        img_copy = img.copy()

        # retrieve the proper sponsored item insert
        insert = Image.open('sponsored_items/' + sponsored_item + '.png')
        width, height = insert.size
        width_scale = round(width * .2)
        height_scale = round(height * .2)
        print(width_scale)
        print(height_scale)
        # resize the sponsored item
        insert = insert.resize((width_scale, height_scale))
        data = insert.convert("RGBA")
        data = data.load()
        for x in range(width_scale):
            for y in range(height_scale):
                if data[x, y][3] != 0:
                    pixel = insert.getpixel((x, y))
                    img_copy.putpixel((x, y), pixel)

        # return the image with the sponsored content inserted
        return img_copy
# Main which is just here for testing
if __name__ == '__main__':
    # Open the image file and read in its data so that we can access it
    img = Image.open('../fisher.jpeg')

   # new_img_one = sponsoredImageInsertion.insert(img, "pepsi")
    new_img_one = sponsoredImageInsertion.insert(img, "amazon")
    new_img_two = sponsoredImageInsertion.insert(img, "coca cola")
    new_img_three = sponsoredImageInsertion.insertPNG(img, 'cokecan')


    # Save the image file so that we can view it
    new_img_one.save('amazon pic.jpg')
    new_img_two.save('coca cola pic.jpg')
    new_img_three.save('coke can.jpg')