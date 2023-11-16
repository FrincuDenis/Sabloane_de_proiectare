class Element:
    def print(self):
        pass
    def acceptp(self, visitor):
        visitor.visit_concrete_element_paragraph(self)
    def accepti(self, visitor):
        visitor.visit_concrete_element_image(self)
    def acceptt(self, visitor):
        visitor.visit_concrete_element_table(self)

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