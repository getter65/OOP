from tasks_1_2 import Task


class TodoList:
    def __init__(self):
        self.tasks = ['None'] * 2
        self.counter = -1

    def __setitem__(self, key, value):
        self.tasks[key] = str(value)

    def __str__(self):
        task_list = ', '.join(self.tasks)
        return task_list

    def __getitem__(self, item):
        return self.tasks[item]

    def __delitem__(self, key):
        del self.tasks[key]

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter >= len(self.tasks):
            raise StopIteration
        return self.tasks[self.counter]


if __name__ == '__main__':
    # JOB 3
    todo_list = TodoList()
    todo_list[0] = Task('Сдать домашку')
    todo_list[1] = Task('Выпить кофе')
    print(todo_list)
    print(todo_list[0])

    # JOB 4
    print(next(todo_list))
    print(next(todo_list))

    # JOB 5
    for item in todo_list:
        print(item)
