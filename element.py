class Element:
    def print(self):
        pass


class Paragraph(Element):
    def __init__(self, text):
        self.text = text

    def print(self):
        print(f"Paragraph: {self.text}")


class Image(Element):
    def __init__(self, image_name):
        self.image_name = image_name

    def print(self):
        print(f"Image: {self.image_name}")


class Table(Element):
    def __init__(self, title):
        self.title = title

    def print(self):
        print(f"Table: {self.title}")