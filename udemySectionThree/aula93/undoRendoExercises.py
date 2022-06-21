# listaDeTarefas = ['Acordar', 'Tomar café', 'Fazer almoço', 'Almoçar', 'Lavar a louça']
#
#
# def addTarefa(tarefa=None):
#     listaDeTarefas.append(tarefa)
#     return ''
#
#
# def desfazerTarefa():
#     return listaDeTarefas.pop()
#
#
# def refazerTarefa():
#     listaDeTarefas.append(addTarefa(tarefa))
#     desfazerTarefa()
#
#
# def showTarefa():
#     print(f'A lista atual de tarefas é: {listaDeTarefas}')
#
#
# while True:
#
#     option = input(
#         'Tarefas.\nAdicionar Tarefa(1)\nDesfazer Tarefa(2)\nRefazer Tarefa(3)\nMostrar Lista de Tarefas(4): \n')
#
#     if option == '1':
#         tarefa = input('Digite uma tarefa: ')
#         addTarefa(tarefa)
#         showTarefa()
#         print()
#
#     if option == '2':
#         desfazerTarefa()
#         showTarefa()
#         print()
#
#     if option == '3':
#         refazerTarefa()
#         showTarefa()
#         print()
#
#     if option == '4':
#         showTarefa()
#         print()


# coach luiz otávio resolution:

def show_todo_list(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return
    last_todo = redo_list.pop()
    todo_list.append(last_todo)


def todo_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls: ')

        if todo == 'ls':
            show_todo_list(todo_list)

        elif todo == 'undo':
            do_undo(todo_list, redo_list)

        elif todo == 'redo':
            do_redo(todo_list, redo_list)

        else:
            todo_add(todo, todo_list)
