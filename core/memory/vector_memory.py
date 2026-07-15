class VectorMemory:
    def __init__(self):
        self.documents = []

    def add(self, text):
        self.documents.append(text)

    def search(self, query):
        matches = []
        for doc in self.documents:
            if query.lower() in doc.lower():
                matches.append(doc)
        return matches