from chapters import Chapters
class Section:
    def __init__(self, title):
        self.title = title
        self.chapters = []

    def add_chapter(self, chapter: Chapters):
        self.chapters.append(chapter)

    def print_section(self):
        print(f"Section name: {self.title}")
        for chapter in self.chapters:
            chapter.print_chapter()