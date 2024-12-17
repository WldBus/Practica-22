users = [
    {"login": "user", "password": "user", "role": "user", "purchases": []},
    {"login": "HochuPelmeni227", "password": "YaAdmin120", "role": "admin", "purchases": []},
]

products = [
    {'product_name': 'Японская ручка', 'country': 'Япония', 'rating': 5.0, 'price': 119.59, 'available_now': 15},
    {'product_name': 'Чипсы Takis', 'country': 'США', 'rating': 4.5, 'price': 215.99, 'available_now': 20},
    {'product_name': 'Чипсы Doritos', 'country': 'США', 'rating': 4.6, 'price': 225.99, 'available_now': 10},
    {'product_name': 'Консервмированный туман', 'country': 'Калифорния', 'rating': 3.7, 'price': 97.99, 'available_now': 5},
    {'product_name': 'Раскрашенные черепа', 'country': 'Мексика', 'rating': 4.2, 'price': 110.59, 'available_now': 8},
    {'product_name': 'Матрёшка', 'country': 'Россия', 'rating': 4.9, 'price': 89.99, 'available_now': 12},
    {'product_name': 'Кукла "сарубобо"', 'country': 'Япония', 'rating': 5.0, 'price': 105.89, 'available_now': 12},
    {'product_name': 'Кленовый сироп', 'country': 'Drama', 'rating': 3.3, 'price': 159.99, 'available_now': 18},
    {'product_name': 'Камамбер', 'country': 'Франция', 'rating': 2.5, 'price': 359.99, 'available_now': 7},
    {'product_name': 'Веер', 'country': 'Япония', 'rating': 4.2, 'price': 59.9, 'available_now': 7},
]

cart = {}

def product_print(elements):
    for element in elements:
        for key, value in element.items():
            print(f"{key}: {value}", end=" ")
            if key == 'available_now':
                print()

def print_product(elements):
    for i, element in enumerate(elements):
        print(f"\nТовар {i+1}:")
        for key, value in element.items():
            print(f" {key}: {value}")

def register():
    while True:
        login = input("\nВведите логин (не менее 6 символов, не более 25): ")
        if 6 <= len(login) <= 25:
            print("Логин введён.")
            break
        else:
            print("Длина логина должна быть от 6 до 25 символов.")
    while True:
        password = input("\nВведите пароль (не менее 8 символов, не более 25): ")
        if 8 <= len(password) <= 25:
            print("Пароль введён.")
            break
        else:
            print("Длина пароля должна быть от 8 до 25 символов.")
    users.append(
        {
            "login": login,
            "password": password, # Хеширование пароля
            "role": "user",
            "purchases": [],
        }
    )


def auth():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    for user in users:
        if user["login"] == login and user["password"] == password:
            print("Авторизация прошла успешно")
            return (user)
    return None


def view_products():
    print(*list(map(lambda product: f"\n Товар: {product['product_name']} ({product['country']}), Цена: {product['price']} рублей, Доступно сейчас: {product['available_now']}", products)))


def view_purchases(user):
    if user["purchases"]:
        print("Ваши покупки:")
        for purchase in user["purchases"]:
            print(f"- {purchase['product_name']}") # Пока не храним количество и цену
    else:
        print("История покупок пуста.")

def add_to_cart(user, product_id):
    global cart
    if 0 <= product_id < len(products):
        cart[product_id] = cart.get(product_id, 0) + 1
        print(f"Товар добавлен в корзину.")
    else:
        print("Товар не найден.")

def main():
    print("\nДобро пожаловать в онлайн-магазин!")
    while True:
        try:
            action = int(input("Выберите:\n1. Авторизация\n2. Регистрация\nВведите операцию: "))
            match action:
                case 1:
                    user = auth()
                    if user:
                        if user["role"] == "admin":
                            # Администраторский режим (добавьте функциональность для администратора)
                            print("\nВы зашли под админом")
                            while True:
                                try:
                                    action = int(input("Выберите:\n1. Просмотреть товары\n2. Выйти из админ-панели: "))
                                    match action:
                                        case 1:
                                            view_products()
                                        case 2:
                                            break
                                except ValueError:
                                    print("Неверный ввод")
                            break
                        else:
                            # Пользовательский режим
                            print("\nВы зашли под пользователем")
                            while True:
                                try:
                                    action = int(input("Операции:\n1. Просмотреть товары\n2. Посмотреть свою историю покупок\n3. Выйти из магазина\nВыберите операцию: "))
                                    match action:
                                        case 1:
                                            view_products()
                                            choice = int(input("Операции:\n1. Отсортировать товары по цене (от дешевого к дорогому)\n2. Добавить товар в корзину\n3. Оплатить покупку\nВыберите операцию: "))
                                            if choice == 1:
                                                product_print(elements = sorted(products, key=lambda product: product["price"], reverse=True))
                                            elif choice == "2":
                                                 print_product(products)
                                                 product_id = int(input("\nВведите номер товара для добавления в корзину: ")) -1 # -1 чтобы получить корректный индекс
                                                 add_to_cart(user, product_id)
                                        case 2:
                                            view_purchases(user)
                                        case 3:
                                            break
                                except ValueError:
                                    print("Неверный ввод")
                            break
                    else:
                        print("Хз")
                case 2:
                    register()
        except ValueError:
            print("Неверный ввод")
    print("До свидания!")


if __name__ == "__main__":
    main()