from ..shared.exceptions import AuthenticationError

class Store():
    def __init__(self):
        self.userManager = UserManager()
        self.productManager = ProductManager()

    def add_user(self, user_data):
        return self.userManager.add_user(user_data)

    def find_user(self, credentials):
        return self.userManager.find_user(credentials)

    def add_product(self, product_data):
        return self.productManager.add_product(product_data)

    def get_all_products(self):
        return self.productManager.get_all_products()


class UserManager ():
    def __init__(self):
        self.users = {
            'admin': {
            'username': 'admin',
            'password': 'admin_pass',
            'role': 'admin'
            }
        }
    def add_user(self, user_data):
        username = user_data['username']
        self.users[username] = user_data
        return self.users[username]

    def find_user(self, credentials):
        username = credentials['username']
        password = credentials['password']
        authError = AuthenticationError('Invalid login credentials')

        try:
            user = self.users[username]
        except KeyError as e:
            raise authError

        if not password == user['password']:
            raise authError
        return user



class ProductManager ():
    def add_product(self, product_data):
        product_name = product_data['name'];
        self.products[product_name] = product_data
        return self.products[product_name]

    def get_all_products(self):
        return list(self.products.values())



store = Store()
