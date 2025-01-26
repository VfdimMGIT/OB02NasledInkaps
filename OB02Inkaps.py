# Класс User: инкапсулирует данные о пользователе
class User:
    def __init__(self, user_id, name, access_level='user'):
        # Приватные атрибуты (инкапсуляция)
        self._user_id = user_id  # Уникальный идентификатор пользователя
        self._name = name  # Имя пользователя
        self._access_level = access_level  # Уровень доступа (по умолчанию 'user')

    # Геттеры для доступа к приватным атрибутам
    def get_user_id(self):
        return self._user_id  # Возвращает ID пользователя

    def get_name(self):
        return self._name  # Возвращает имя пользователя

    def get_access_level(self):
        return self._access_level  # Возвращает уровень доступа

    # Сеттеры для изменения приватных атрибутов
    def set_name(self, name):
        self._name = name  # Устанавливает новое имя пользователя

    def set_access_level(self, access_level):
        self._access_level = access_level  # Устанавливает новый уровень доступа

    # Метод для строкового представления объекта
    def __str__(self):
        return f"ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level}"


# Класс Admin: наследует от User и добавляет функциональность администратора
class Admin(User):
    def __init__(self, user_id, name):
        # Вызов конструктора родительского класса с уровнем доступа 'admin'
        super().__init__(user_id, name, access_level='admin')
        # Приватный список для хранения пользователей
        self._users = []

    # Метод для добавления пользователя в список
    def add_user(self, user):
        if user not in self._users:  # Проверка, что пользователь еще не добавлен
            self._users.append(user)  # Добавление пользователя в список
            print(f"User {user.get_name()} added successfully.")
        else:
            print(f"User {user.get_name()} already exists.")

    # Метод для удаления пользователя из списка
    def remove_user(self, user):
        if user in self._users:  # Проверка, что пользователь существует в списке
            self._users.remove(user)  # Удаление пользователя из списка
            print(f"User {user.get_name()} removed successfully.")
        else:
            print(f"User {user.get_name()} not found.")

    # Метод для вывода списка всех пользователей
    def list_users(self):
        if not self._users:  # Проверка, что список не пуст
            print("No users in the system.")
        else:
            for user in self._users:  # Перебор всех пользователей в списке
                print(user)  # Вывод информации о пользователе


# Пример использования программы
if __name__ == "__main__":
    # Создаем обычных пользователей
    user1 = User(1, "Alice")  # Создаем пользователя с ID 1 и именем Alice
    user2 = User(2, "Bob")  # Создаем пользователя с ID 2 и именем Bob

    # Создаем администратора
    admin = Admin(100, "Admin")  # Создаем администратора с ID 100 и именем Admin

    # Администратор добавляет пользователей
    admin.add_user(user1)  # Добавляем пользователя Alice
    admin.add_user(user2)  # Добавляем пользователя Bob

    # Выводим список пользователей
    print("\nList of users after adding:")
    admin.list_users()  # Выводим список всех пользователей

    # Администратор удаляет пользователя
    admin.remove_user(user1)  # Удаляем пользователя Alice

    # Выводим список пользователей после удаления
    print("\nList of users after removal:")
    admin.list_users()  # Выводим обновленный список пользователей