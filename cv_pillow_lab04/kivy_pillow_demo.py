from io import BytesIO
from kivy.app import App
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image
from PIL import Image as PilImage

class MyApp(App):
    def build(self):
        image = Image(source="")
        pil_image = PilImage.open("hummingbird.jpg")

        img_data = BytesIO()
        pil_image.save(img_data,format='png')
        img_data.seek(0)

        image.texture = CoreImage(img_data, ext='png').texture
        image.reload()

        return image

MyApp().run()
