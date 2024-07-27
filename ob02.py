#Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников
# на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя
# из системы.

#Требования:
#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
#2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа, специфичный
# для администраторов ('admin'). Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и удалять
# пользователей из списка (представь, что это просто список экземпляров `User`).
#3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ
# к необходимым атрибутам через методы (например, get и set методы).

class User: #шаг1 создаём класса обычных сотрудников
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    def set_access_level(self, level):
        self.__access_level = level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__users_list = []

    def get_access_level(self):
        return self.__access_level

    def add_user(self, user):
        if isinstance(user, User):
            self.__users_list.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("Invalid user.")

    def remove_user(self, user_id):
        for user in self.__users_list:
            if user.get_user_id() == user_id:
                self.__users_list.remove(user)
                print(f"User {user.get_name()} removed.")
                return
        print("User not found.")

    def list_users(self):
        for user in self.__users_list:
            print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")


# Пример использования системы
if __name__ == "__main__":
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    admin = Admin(3, "Charlie")

    admin.add_user(user1)
    admin.add_user(user2)

    print("\nСписок пользователей:")
    admin.list_users()

    admin.remove_user(1)

    print("\nСписок пользователей после удаления:")
    admin.list_users()