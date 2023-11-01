from element import Element

class ImageProxy(Element):
    def __init__(self, image_name, image_url):
        self.image_name = image_name
        self.image_url = image_url
        self.image = None

    def load_image(self):
        # Simulate image loading from the URL
        # In a real scenario, you would fetch the image from the URL
        # For simplicity, we use a print statement here
        print(f"Image loaded: {self.image_name} from {self.image_url}")
        self.image = Image(self.image_name)  # Load the image

    def print(self):
        if self.image is None:
            self.load_image()  # Load the image if not already loaded
        self.image.print()

# Update the existing Image class
class Image(Element):
    def __init__(self, image_name):
        self.image_name = image_name

    def print(self):
        print(f"Image: {self.image_name}")