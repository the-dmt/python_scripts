#!/usr/bin/env python3

import os
from rembg import remove
from PIL import Image

file_path = os.path.join(os.environ['HOME'], os.getcwd())

files = os.listdir()

images = [ 
	image for image in files
	if image.endswith('jpg')
	or image.endswith('jpeg')
	or image.endswith('png')
]

if len(images) > 0:

	images = dict(enumerate(images, 1))

	for index, image in images.items():
		print(f"{index}) {image}")

	choice = int(input('enter index of your image: '))

	if choice in images:
		input_img = images[choice]
		clean = input_img.split('.')[:-1]
		input_img_clean = ' '.join(clean)
		output_img = f"{input_img_clean}_rmbg.png"
		inp = image.open(input_img)
		output = remove(inp)
		output.save(output_img)
	else:
		print(f"{choice} is out of range.")

else:
	print('There are no images in the current directory.')
