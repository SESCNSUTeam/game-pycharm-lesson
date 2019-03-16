from classes.activities.Stack import Stack


class GameStateManager:
    def __init__(self, activity):
        self.stack = Stack()
        self.stack.push(activity)

