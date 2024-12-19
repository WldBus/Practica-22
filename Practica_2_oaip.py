users = [
    {"login": "user", "password": "user", "role": "user", "cart": [], "purchases": []},
    {"login": "HochuPelmeni227", "password": "YaAdmin120", "role": "admin"},
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

cart = {}

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

def product_print(elements):
    for element in elements:
        for key, value in element.items():
            print(f"{key}: {value}", end=" ")
            if key == 'clarity':
                print()

def print_product(elements):
    for i, element in enumerate(elements):
        print(f"\nТовар {i+1}:")
        for key, value in element.items():
            print(f" {key}: {value}")

def view_products():
    print(*list(map(lambda product: f"\n Товар: {product['product_name']} ({product['country']}), Цена: {product['price']} рублей, Доступно сейчас: {product['clarity']}", products)))