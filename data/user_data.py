# Handles user-entered recycling dat# data/user_data.py
class UserData:
    def __init__(self):
        self.recycling_guide = {}
        self.history = []

    def add_instruction(self, item, instruction):
        self.recycling_guide[item.lower()] = instruction
        self.history.append(f"{item}: {instruction}")

    def get_instruction(self, item):
        return self.recycling_guide.get(item.lower(), None)

    def get_history(self):
        return self.history