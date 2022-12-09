class TodoList():
    tasks = ["список строк"]

    def __init__(self):
        self.tasks = []

    def add_tasks(self, *args):
        for i in args:
            self.tasks.append(i)

todo_list = TodoList()
todo_list.add_tasks("купить лампочку", "поменять лампочку", "выкинуть лампочку")

print("\n".join(todo_list.tasks))