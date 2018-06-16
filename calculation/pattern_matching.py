class Levenshtein:
    def __init__(self,string1,string2):
        self.string1 = string1
        self.string2 = string2

    def levenshtein(self):
        if len(self.string1) < len(self.string2):
            return Levenshtein(self.string2, self.string1).levenshtein()
    # len(self.self.string1) >= len(self.self.string2)
        if len(self.string2) == 0:
            return len(self.string1)
        previous_row = range(len(self.string2) + 1)
        for i, c1 in enumerate(self.string1):
            current_row = [i + 1]
            for j, c2 in enumerate(self.string2):
                insertions = previous_row[j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
                deletions = current_row[j] + 1  # than self.self.string2
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]
