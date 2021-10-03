from PIL import Image

img1 = Image.open("./images/img1.jpeg")
img2 = Image.open("./images/img2.jpeg")
img3 = Image.open("./images/img3.jpeg")
img4 = Image.open("./images/img4.jpeg")

im_list = [img2, img3, img4]

pdf1_filename = "./output/output.pdf"

img1.save(pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=im_list)
