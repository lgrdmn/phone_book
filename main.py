action = input('Введите A, если хотите добавить абонента \n'
               'Введите D, если хотите удалить абонента \n'
               'Введите F, если хотите найти абонента \n')
if action == 'A':
      add_sub = input('Введите данные абонента в формате: имя, номер, адрес \n')
      phonebook = open('pb.txt', 'a')
      phonebook.write(add_sub + '\n')
      phonebook.close()
      print('Абонент добавлен в телефонный справочник ')
elif action == 'D':
      del_sub = input('Введите имя, номер или адрес абонента которого хотите УДАЛИТЬ \n')
      file = open('pb.txt', 'r+')
      file = file.readlines()
      for i in range(0, len(file)):
          if del_sub in file[i]:
              del file[i]
              file = ''.join(file)
              print('Абонент удалён из телефонного справочника')
              phonebook = open('pb.txt', 'w')
              phonebook.write(file)
              phonebook.close()
elif action == 'F':
      find_sub = input('Введите имя, номер или адрес абонента которого хотите НАЙТИ \n')
      file = open('pb.txt', 'r')
      file = file.readlines()
      for i in range(0, len(file)):
          if find_sub in file[i]: print('Абонент есть в телефонном справочнике:', file[i])
else:
      print('Вы ввели неверную команду ')

