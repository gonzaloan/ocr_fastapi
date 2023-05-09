import asyncio

import pytesseract

async def read_image(img_path, lang='eng'):
    try:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\gonzalo.munoz\AppData\Local\Programs\Tesseract-OCR' \
                                                r'\tesseract.exe '
        text = pytesseract.image_to_string(img_path, lang=lang)
        await asyncio.sleep(2)
        return text
    except Exception as e:
        print(e)
        return "[ERROR] Unable to process file: {0}".format(img_path)