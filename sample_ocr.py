from PIL import Image
from paddleocr import PaddleOCR, draw_ocr
# Import time module
import time
start = time.time()
# need to run only once to download and load model into memory
ocr = PaddleOCR(lang='id')
img_path = 'image.jpg'
result = ocr.ocr(img_path, cls=False)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)


# draw result
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')


end = time.time()

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
