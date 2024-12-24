users = [
    {"login": "user", 
     "password": "user", 
     "role": "user", 
     "cart": [], 
     "purchases": []},

    {"login": "AdminDel", 
     "password": "chepuh", 
     "role": "admin"},
]

products = [
    {'product_name': 'Японская ручка', 'country': 'Япония', 'rating': 5.0, 'price': 119.59, 'clarity': 15},
    {'product_name': 'Чипсы Takis', 'country': 'США', 'rating': 4.5, 'price': 215.99, 'clarity': 20},
    {'product_name': 'Чипсы Doritos', 'country': 'США', 'rating': 4.6, 'price': 225.99, 'clarity': 10},
    {'product_name': 'Консервмированный туман', 'country': 'Калифорния', 'rating': 3.7, 'price': 97.99, 'clarity': 5},
    {'product_name': 'Раскрашенные черепа', 'country': 'Мексика', 'rating': 4.2, 'price': 110.59, 'clarity': 8},
    {'product_name': 'Матрёшка', 'country': 'Россия', 'rating': 4.9, 'price': 89.99, 'clarity': 12},
    {'product_name': 'Кукла "сарубобо"', 'country': 'Япония', 'rating': 5.0, 'price': 105.89, 'clarity': 12},
    {'product_name': 'Кленовый сироп', 'country': 'Drama', 'rating': 3.3, 'price': 159.99, 'clarity': 18},
    {'product_name': 'Камамбер', 'country': 'Франция', 'rating': 2.5, 'price': 359.99, 'clarity': 7},
    {'product_name': 'Веер', 'country': 'Япония', 'rating': 4.2, 'price': 59.9, 'clarity': 7},
]

# try:
#     with open('users.json', 'r') as file:
#         users = json.load(file)
#     with open('products.json', 'r') as file:
#         products = json.load(file)
# except FileNotFoundError:
#     print("Файлы с данными не найдены. Будут созданы новые.")


# def save_data():
#     with open('users.json', 'w', encoding='utf-8') as file:
#         json.dump(users, file, ensure_ascii=False, indent=4)
#     with open('products.json', 'w', encoding='utf-8') as file:
#         json.dump(products, file, ensure_ascii=False, indent=4)

def register():
    while True:
        login = input("\nВведите логин (не менее 6 символов, не более 25): ")
        if 6 <= len(login) <= 25:
            break
        else:
            print("Длина логина должна быть от 6 до 25 символов.")
    while True:
        password = input("\nВведите пароль (не менее 8 символов, не более 25): ")
        if 8 <= len(password) <= 25:
            break
        else:
            print("Длина пароля должна быть от 8 до 25 символов.")
    users.append(
        {
            "login": login,
            "password": password,
            "role": "user",
            "cart": [],
            "purchases": [],
        }
    )
    # save_data()
    print("Регистрация прошла успешно!")


def auth():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    for user in users:
        if user["login"] == login and user["password"] == password:
            print("Авторизация прошла успешно")
            return user
    return None

def print_product(products):
    if not products:
        print("Список пуст.")
        return
    for i, product in enumerate(products):
        print(f"\nТовар {i+1}:")
        for key, value in product.items():
            print(f"  {key}: {value}")

def pretty_print(elements):
    for element in elements:
        for key, value in element.items():
            print(f"{key}: {value}", end=" ")
            if key == 'price':
                print()

# Меню пользоваетеля
def user_menu(user):
    while True:
        print("\nМеню пользователя:")
        print("1. Просмотреть товары")
        print("2. Добавить товар в корзину")
        print("3. Просмотреть корзину")
        print("4. Оформить покупку")
        print("5. Просмотреть историю покупок")
        print("6. Отсортирвоать товары по цене")
        print("7. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == '1':            
                print(*list(map(lambda product: f"\n Товар: {product["product_name"]} ({product["country"]}), Цена: {product["price"]} рублей, Доступно сейчас: {product["clarity"]}", products)))
            elif choice == '2':
                print_product(products)
                product_index = int(input("Введите номер товара: ")) - 1
                if 0 <= product_index < len(products):
                    user["cart"].append(products[product_index])
                    print("Товар добавлен в корзину.")
                else:
                    print("Неверный номер товара.")
            elif choice == '3':
                print_product(user["cart"])
            elif choice == '4':
                if user["cart"]:
                    print_product(user["cart"])
                    confirm = input("Подтвердить покупку? (y/n): ")
                    if confirm.lower() == 'y':
                        user["purchases"].extend(user["cart"])
                        user["cart"] = []
                        # save_data()
                        print("Покупка оформлена.")
                    else:
                        print("Покупка отменена.")
                else:
                    print("Корзина пуста.")
            elif choice == '5':
                print_product(user["purchases"])
            elif choice == '6':
                pretty_print(elements = sorted(products, key=lambda product: product["price"], reverse=True))
            elif choice == '7':
                break
            else:
                print("Неверный выбор.")
        except ValueError:
            print("Некорректный ввод.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


def add_product():
    new_product = {}
    new_product["product_name"] = input("Введите название товара: ")
    new_product["country"] = input("Введите страну производителя: ")
    while True:
        try:
            new_product["price"] = float(input("Введите цену: "))
            break
        except ValueError:
            print("Неверный формат цены.")
    while True:
        try:
            new_product["clarity"] = int(input("Введите количество: "))
            break
        except ValueError:
            print("Неверный формат количества.")
    while True:
        try:
            new_product["rating"] = float(input("Введите рейтинг (0-5): "))
            if 0 <= new_product["rating"] <= 5:
                break
            else:
                print("Рейтинг должен быть от 0 до 5.")
        except ValueError:
            print("Неверный формат рейтинга.")

    products.append(new_product)
    # save_data()
    print("Товар добавлен.")

def delete_product():
    print_product(products)
    try:
        product_index = int(input("Введите номер товара для удаления: ")) - 1
        if 0 <= product_index < len(products):
            del products[product_index]
            # save_data()
            print("Товар удален.")
        else:
            print("Неверный номер товара.")
    except ValueError:
        print("Некорректный ввод.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def change_product():
    print_product(products)
    try:
        product_index = int(input("Введите номер товара для изменения: ")) - 1
        if 0 <= product_index < len(products):
            product = products[product_index]
            for key in product:
                new_value = input(f"Введите новое значение для {key} (или Enter для пропуска): ")
                if new_value:
                    try:
                        if key in ["price", "rating"]:
                            new_value = float(new_value)
                        elif key == "clarity":
                            new_value = int(new_value)
                        product[key] = new_value
                    except ValueError:
                        print("Неверный формат данных.")
                        return
            # save_data()
            print("Товар изменён.")
        else:
            print("Неверный номер товара.")
    except ValueError:
        print("Некорректный ввод.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def admin_menu():
    while True:
        print("\nМеню администратора:")
        print("1. Добавить товар")
        print("2. Удалить товар")
        print("3. Изменить товар")
        print("4. Просмотреть товары")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        try:
            if choice == '1':
                add_product()
            elif choice == '2':
                delete_product()
            elif choice == '3':
                change_product()
            elif choice == '4':
                print_product(products)
            elif choice == '5':
                break
            else:
                print("Неверный выбор.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

def main():
    while True:
        print("\nМеню:")
        print("1. Авторизация")
        print("2. Регистрация")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            user_auth = auth()
            if user_auth:
                if user_auth["role"] == "user":
                    user_menu(user_auth)
                elif user_auth["role"] == "admin":
                    admin_menu()
        elif choice == '2':
            register()
        elif choice == '3':
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()