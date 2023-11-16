from author import Author
from chapters import Chapters
from subchapters import SubChapter
from element import Paragraph
from sectiune import Section
from image_proxy import ImageProxy,Image
from paragraph_proxy import ParagraphProxy
from visitor import ConcreteVisitorStats
class Book:
    def __init__(self, title):
        self.title = title
        self.author = None
        self.sections = []

    def add_author(self, author: Author):
        self.author = author

    def add_section(self, section: Section):
        self.sections.append(section)

    def print(self):
        print(f"Book Title: {self.title}")
        if self.author:
            self.author.print()
        else:
            print("None")
        for section in self.sections:
            section.print_section()


element_list=[Paragraph("This is a paragraph"),
              ImageProxy("Proxy Image", "https://en.m.wikipedia.org/wiki/File:Sunflower_from_Silesia2.jpg"),
              ImageProxy("Proxy Image1", "https://en.m.wikipedia.org/wiki/File:Sunflower_from_Silesia2.jpg"),
              ImageProxy("Proxy Image2", "https://en.m.wikipedia.org/wiki/File:Sunflower_from_Silesia2.jpg"),
              Paragraph("This is a paragraph2")]
section=[Section("Section 1")]
chapter=[Chapters("Chapter 1")]
subchapter=[SubChapter("Subchapter 1")]
author = Author("John Doe")
visitor= ConcreteVisitorStats()
# Create a book
book = Book("My Book")
for sec in section:
    for chap in chapter:
        for subc in subchapter:
            for element in element_list:
                if isinstance(element, Paragraph):
                    element.acceptp(visitor)
                    visitor.nrp += 1
                elif isinstance(element, ImageProxy):
                    element.accepti(visitor)
                    visitor.nri += 1
                subc.add_element(element)
            chap.add_subchapter(subc)
        sec.add_chapter(chap)
    book.add_section(sec)

book.add_author(author)

#paragraph_proxy = ParagraphProxy("This is a proxy paragraph.")
#subchapter.add_element(paragraph_proxy)
print("Paragraph: ",visitor.nrp)
print("Image: " ,visitor.nri)
print("Table: ", visitor.nrt)
book.print()
