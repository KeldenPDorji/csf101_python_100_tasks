from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = './editedimgs'

os.makedirs(pathOut, exist_ok=True)

for filename in os.listdir(path):
    try:
        img = Image.open(f"{path}/{filename}")
    except IOError:
        print(f"Unable to open {filename}. Skipping.")
        continue
    
    """Photo Manipulation Tools.Remove the comment to apply the filters"""
   
    """Apply sharpening filter to the opened image"""
    img = img.filter(ImageFilter.SHARPEN)
    # img = img.filter(ImageFilter.SHARPEN)
    # img = img.filter(ImageFilter.SHARPEN)


    """Apply blur filter"""
    # img_blur = img.filter(ImageFilter.BLUR)
    # img_blur = img.filter(ImageFilter.BLUR)
    # img_blur = img.filter(ImageFilter.BLUR)
    # img_blur = img.filter(ImageFilter.BLUR)
    # img_blur = img.filter(ImageFilter.BLUR)
    # img_blur = img.filter(ImageFilter.BLUR)
    
    """Apply detail filter"""
    # img_detail = img.filter(ImageFilter.DETAIL)
    # img_detail = img.filter(ImageFilter.DETAIL)
    # img_detail = img.filter(ImageFilter.DETAIL)
    # img_detail = img.filter(ImageFilter.DETAIL)
    # img_detail = img.filter(ImageFilter.DETAIL)

    """Apply edge finding filter"""
    # img = img.filter(ImageFilter.FIND_EDGES)

    """Apply emboss filter"""
    # img = img.filter(ImageFilter.EMBOSS)
    
    """Apply smooth more filter"""
    # img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE)
    # img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE)
    # img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE)
    # img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE)
    # img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE)
    
    """Convert the image to RGB"""
    img = img.convert('RGB')
    
    """Convert the image to grayscale"""
    img = img.convert('L')

    """ Enhance contrast"""
    factor = 1.5
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    """Save the image at its highest quality"""
    img.save(f'{pathOut}/{clean_name}_edited.jpg', quality=100)
