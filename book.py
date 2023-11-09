from author import Author
from chapters import Chapters
from subchapters import SubChapter
from element import Paragraph
from sectiune import Section
from image_proxy import ImageProxy,Image
from paragraph_proxy import ParagraphProxy
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

author = Author("John Doe")

# Create a book
book = Book("My Book")

# Create a section
section = Section("Section 1")

# Create a chapter
chapter = Chapters("Chapter 1")

# Create a subchapter
subchapter = SubChapter("Subchapter 1")

# Create a paragraph
paragraph = Paragraph("This is a paragraph")

# Add the paragraph to the subchapter
subchapter.add_element(paragraph)

# Add the subchapter to the chapter
chapter.add_subchapter(subchapter)

# Add the chapter to the section
section.add_chapter(chapter)

# Add the section to the book
book.add_section(section)

# Add an author to the book
book.add_author(author)

image_proxy = ImageProxy("Proxy Image", "https://en.m.wikipedia.org/wiki/File:Sunflower_from_Silesia2.jpg")

# Add the ImageProxy to the subchapter
subchapter.add_element(image_proxy)

# Create a ParagraphProxy and add it to the existing structure
paragraph_proxy = ParagraphProxy("This is a proxy paragraph.")
subchapter.add_element(paragraph_proxy)
book.print()