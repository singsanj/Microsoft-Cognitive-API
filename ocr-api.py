import pyoxford

api = pyoxford.vision("33b6b29738f340a298a376556fe77a4b")
#result = api.ocr("https://oxfordportal.blob.core.windows.net/vision/OpticalCharacterRecognition/1.jpg")
#result =api.ocr("https://www.realpython.com/images/blog_images/ocr/ocr.jpg")
#result = api.ocr("https://www.realpython.com/images/blog_images/ocr/sample1.jpg")
#result = api.ocr("https://www.realpython.com/images/blog_images/ocr/sample2.jpg")
#result = api.ocr("https://www.realpython.com/images/blog_images/ocr/sample3.jpg")
#result = api.ocr("https://www.realpython.com/images/blog_images/ocr/sample4.jpg")
result = api.ocr("https://www.realpython.com/images/blog_images/ocr/sample5.jpg")
doc = result.to_document()
for par in doc:
    print("\n".join(par))