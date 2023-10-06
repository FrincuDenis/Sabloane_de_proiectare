import subchapters

class chapters:
    def __init__(self,title):
        self.title=title
        self.subchapters=[]

    def add_subchp(self,subchapter):
        self.subchapters.append(subchapter)

    def print(self):
        print(f"Chapters: {self.title}")