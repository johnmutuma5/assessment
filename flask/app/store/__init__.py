class Store():
    def __init__(self):
        self.users = {}
        self.products = {}
        self.tokens = {}

    def add_user(self, user_data):
        self.users[user_data['username']] = user_data
        return self.users

    def add_product(self, product_data):
        self.products[product_data['name']] = product_data
        return self.products

    def add_token(self, token, user_data):
        self.tokens[token] = user_data
        return self.tokens

store = Store()
