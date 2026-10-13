from PIL import Image

im = Image.open('scratch/screenshot_375.png')
crop = im.crop((0, 30, 375, 200))
crop.save('scratch/nav_crop_real.png')
print("Saved scratch/nav_crop_real.png, size:", crop.size)
