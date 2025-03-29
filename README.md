# PaddleOCR Demo on Apple Silicon M1 (KTP Indonesia OCR)

This repository demonstrates a simple PaddleOCR setup and execution on an Apple Silicon M1 Mac, specifically for performing OCR on Indonesian ID cards (KTP).

## Prerequisites

* macOS with Apple Silicon (M1 or later)
* Python 3.11.x installed
* An image of an Indonesian KTP (named `image.jpg`)
* A font file (e.g., `simfang.ttf`) for drawing the OCR results.

## Setup and Execution

Follow these steps to run the demo:

1.  **Create and activate a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    This creates a virtual environment named `.venv` in the current directory and activates it. Using a virtual environment helps isolate project dependencies.

2.  **Install PaddlePaddle and PaddleOCR:**

    ```bash
    pip install -r requirements.txt
    ```

    Ensure that `requirements.txt` is in the same directory as your commands. It should contain the necessary packages, including PaddlePaddle and PaddleOCR.


3.  **Run the demo script:**

    ```bash
    python sample_ocr.py
    ```

    This will execute the `sample_ocr.py` script, which performs OCR on the KTP image and saves the result to `result.jpg`.

## Example `sample_ocr.py`

Here's the full code for `sample_ocr.py`:

```python
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

```