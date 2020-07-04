from PIL import Image
import os
import sys

def main(dir):
    saved_GIF_count = 0

    png_files = [fn for fn in os.listdir(dir) if fn.endswith('.png')]
    try:
        os.mkdir(os.path.join(dir, 'gifs'))
        print('Saving to ./gifs directory')
    except:
        print('gifs directory already exists. Saving there...')

    for f in png_files:
        try:
            im = Image.open(os.path.join(dir, f))
            # Create a new image with a solid color
            background = Image.new('RGBA', im.size, (255, 255, 255))

            # Paste the image on top of the background
            background.paste(im, im)
            im = background.convert('RGB').convert('P', palette=Image.ADAPTIVE)
            
            im.save(dir + '/gifs/' + f[:-3] + 'gif')
            saved_GIF_count = saved_GIF_count + 1
        except:
            pass

    print('Saved {} GIFs'.format(saved_GIF_count))
        

if __name__ == '__main__':
    main(sys.argv[1])