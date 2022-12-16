import datetime


class Task:
    def __init__(self, content):
        self.content = content
        current_datetime = datetime.datetime.now()
        self.datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return f'{self.content} (создано {self.datetime})'

    def __str__(self):
        return f'{self.content} (создано {self.datetime})'

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.content == other.content
        return NotImplemented

    def __hash__(self):
        return hash(self.content)

    def __bool__(self):
        return bool(self.content)


if __name__ == '__main__':
    # JOB 1
    todo_list = set()

    todo_list.add(Task('Сделать домашку'))
    todo_list.add(Task('Выпить кофе'))
    todo_list.add(Task('Выйти на пробежку'))
    todo_list.add(Task('Сделать домашку'))

    for item in todo_list:
        print(item)

    # JOB 2

    todo_list = []

    todo_list.append(Task('Сделать домашку'))
    todo_list.append(Task(''))
    todo_list.append(Task('Сделать домашку'))
    todo_list.append(Task(''))
    
    non_empty_tasks = [item for item in todo_list if item]
    print(non_empty_tasks)
    print(len([item for item in todo_list if not item]))