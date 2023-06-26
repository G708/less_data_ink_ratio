# data_ink_ratio.py

## ---------------- ##
## plot全体の色の濃さ ##
## ---------------- ##

# 参考：　https://rightcode.co.jp/blog/information-technology/python-image-analysis-hsv-tapioca
# 軸、タイトルやラベルを含めた文字、plotの色の濃さを見つけたいので、このブログの最初の例（タピオカ＋ストロー）によって、
# 色の濃さを定量する

# Pillowで白い余白をクロップした方法を紹介した記事（https://nouka-it.hatenablog.com/entry/2022/09/01/211600）を
# 参考に、余白をクロップするかどうかを引数で指定できるようにした。
# Cropすると比較したい全plotとdata ink plotで画像のサイズが異なるため、除いた

import cv2
import io
import numpy as np
from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import argparse

# 引数の設定
parser = argparse.ArgumentParser(description='plot全体の色の濃さを定量する')
parser.add_argument('--plot', type=str, default='plot.py', help='plotを作成するpythonファイル名')
parser.add_argument('--threshold', type=int, default=255, help='plot全体の色の濃さの閾値')
parser.add_argument('-m','--method', choices=['bgr2gray','hsv'], default='hsv', help='plot全体の色の濃さを定量する方法')
# parser.add_argument('--crop', action='store_true', help='画像の余白が白い場合に、余白を削除するかどうか')
parser.add_argument('-o', '--output', type=str, default='output.png', help='plot全体の色の濃さを定量した画像ファイル名')
args = parser.parse_args()

# plot image from input python file
def get_img_from_py(input, png_name):
	"""
	Read plot image from input python file

	Args:
		input: input python file name

	Returns:
		img: plot image
	"""
	# run python file
	exec(open(input).read(), globals())

	# read plot image
	img = cv2.imread(png_name)

	return img

# get the plot which is only plotting data ink
def get_data_ink_py(input):
	"""
	Insert `plt.gca().axis('off')` befor `plt.savefig('plot.png')` in input python file,
	Also, change the name of output plot image to 'data_ink.png'
	then run script.
	"""
	# open input python file and Insert `plt.gca().axis('off')` befor `plt.savefig('plot.png')`
	# changethe name of output plot image of `plt.savefig('plot.png')` to 'data_ink.png'
	# delete legend line if it exists
	with open(input, 'r') as f:
		lines = f.readlines()
		lines.insert(-1, "plt.gca().axis('off')\n")
		lines[-1] = lines[-1].replace('plot.png', 'data_ink.png')
		line_num = -1
		for line in lines:
				if "legend" in line:
						line_num += 1
		if line_num != -1:
				lines.insert(-1, "legend.remove()\n")
		f.close()

	# write new python file
	with open('data_ink.py', 'w') as f:
		f.writelines(lines)
		f.close()
	return




# read plot image inside jupyter notebook
def get_img_from_fig(fig, dpi=180):
	buf = io.BytesIO()
	fig.savefig(buf, format="png", dpi=dpi)
	buf.seek(0)
	img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
	buf.close()
	img = cv2.imdecode(img_arr, 1)

	return img


# Quantify the darkness of the plot
class img_di_ratio(object):
	"""
	Read plot image and quantify the darkness of the plot
	Args:
		img: plot image
		threshold: threshold of darkness
		method: method to quantify the darkness of the plot		
	"""

	def __init__(self, img, threshold, method):
		self.img = img
		self.threshold = threshold
		self.method = method
		# self.crop = crop

	def convert_gray(self):
		if self.method == 'bgr2gray':
			# convert to gray scale
			gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

		elif self.method == 'hsv':
			# first convert to hsv
			hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
			# back to bgr, then convert to gray scale
			bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
			gray  = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
		return gray	

	# def crop_img(self,gray):
	# 	# convert to PIL image
	# 	pil_image = Image.fromarray(gray)

	# 	BG_COLOR = (255)  # white
	# 	bg_img = Image.new('L', pil_image.size, BG_COLOR)

	# 	# compare the two images
	# 	diff_img = ImageChops.difference(pil_image, bg_img)

	# 	# clop the image
	# 	crop_range = diff_img.convert('RGB').getbbox()
	# 	crop_img = pil_image.crop(crop_range)

	# 	# convert to numpy array
	# 	crop_gray = np.array(crop_img)

	# 	return crop_gray


	def total_ink(self):
		"""
		Convert color of the plot in to gray scale and quantify the darkness of the plot

		Returns:
			img_mod: plot image with only data ink
		"""

		gray = self.convert_gray()

		# if self.crop == True:
		# 	gray = self.crop_img(gray)

		if self.method == 'bgr2gray':
			img_mod = np.where(gray > self.threshold , 0, gray)
		
		elif self.method == 'hsv':
			img_mod = np.where(gray < self.threshold, 255, 0)

		return img_mod

	def save_total_ink(self, output):
		"""
		Save plot image with highlighting total ink region
		
		Args:
			output: output file name
		"""

		# save image
		cv2.imwrite(output, img_mod)
		return None

	
if __name__ == '__main__':
	# get plot image from input python file
	img = get_img_from_py(args.plot, 'plot.png')

	get_data_ink_py(args.plot)

	# get the plot which is only plotting data ink
	data_ink = get_img_from_py('data_ink.py', 'data_ink.png')

	# Quantify the ink of the all plot
	img_di = img_di_ratio(img, args.threshold, args.method)
	img_mod = img_di.total_ink()
	plt.imsave("All_ink_img.png", img_mod)

	# Quantify the data ink
	data_ink_di = img_di_ratio(data_ink, args.threshold, args.method)
	data_ink_mod = data_ink_di.total_ink()
	plt.imsave("data_ink_img.png", data_ink_mod)

	# culculate the ratio of data ink
	ratio = np.sum(data_ink_mod)/np.sum(img_mod)
	# print(data_ink_mod)

	print('The data ink ratio is {:.2f}'.format(ratio))