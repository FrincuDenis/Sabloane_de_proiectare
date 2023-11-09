from element import Element ,Paragraph
from subchapters import SubChapter as sub
class ParagraphProxy(Element):
    def __init__(self, text):
        self.text = text
        self.loaded = False
        self.paragraph = None

    def load_paragraph(self):
        # Simulate loading the paragraph content
        # In a real scenario, you might fetch the content from a database or an external source
        # For simplicity, we use a print statement here
        print(f"Paragraph loaded: {self.text}")
        self.paragraph = Paragraph(self.text)
        self.loaded = True

    def print(self):
        if not self.loaded:
            self.load_paragraph()  # Load the paragraph if not already loaded
        self.paragraph.print()



