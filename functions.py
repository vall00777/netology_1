documents = [
	{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
	{'type': 'invoce', 'number': '11-2', 'name': 'Геннадий Покемонов'},
	{'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}

]

def information():
 n = input('''Нужно ввести букву,которая подразумевает под собой выполнение команды:
p - спросит номер документа и выведет имя человека, которому он принадлежит;
l - выводит список всех документов;
s - спросит номер документа и выведет № полки, на которой он находится;
a - добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя
владельца и номер полки, на котором он будет храниться.
b - выведет имена всех владельцев документов
Введите букву: ''')
 return n

def all_name(documents):
    l = []
    for i in documents:
         try:
              l.append(i['name'])
         except KeyError:
               print('Error')
    print(', '.join(l))

def input_doc_number():
    n = input('Ведите номер документа: ')
    return n

def input_document():
    n = input_doc_number()
    type_doc = input('Тип документа: ')
    fio_name = input('Введите имя: ')
    shelf_number = input('Номер полки: ')
    return n, type_doc, fio_name, shelf_number

def command_people (documents):
    n = input_doc_number()
    for i in documents:
        for values in i.values():
            if values == n:
                print(i["name"])

def command_list (documents): 
    print('Cписок всех документов')
    for i in documents:
        print(*i.values())

def command_shelf (directories):
    n = input_doc_number()
    for key, items in directories.items():
        if n in items:
                print('Документ лежит на полке c № {}!'.format(key))

		
def command_add(documents,directories):
    n, type_doc, fio_name, shelf_number = input_document()
    documents.append({"type": type_doc, "number": n, "name": fio_name})
    if shelf_number not in directories:
        print('Такой полки нет,создадим')
        directories[shelf_number] = []	
        directories[shelf_number].append(n)
    else:
        directories[shelf_number].append(n)
    print(documents, '\n', directories)

def choice_leter(n):
    if n == 'p':
        command_people(documents)
    elif n == 'l':
        command_list(documents)
    elif n == 's':
        command_shelf(directories)
    elif n == 'a':
        command_add(documents, directories)
    elif n == 'b':
        all_name(documents)

def main():
  while True:
    n = information()
    if n not in 'plsadb':
      print('Ошибка!Нет такой команды!!!')
    else:
      choice_leter(n)

main()
