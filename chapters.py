import subchapters as SubChapter
class Chapters:
    def __init__(self, title):
        self.title = title
        self.subchapters = []

    def add_subchapter(self, subchapter: SubChapter):
        self.subchapters.append(subchapter)

    def print_chapter(self):
        print(f"Chapter name: {self.title}")
        for subchapter in self.subchapters:
            subchapter.print_subchapter()