# cashier.py

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, price, quantity):
        if product in self.items:
            self.items[product]['quantity'] += quantity
        else:
            self.items[product] = {'price': price, 'quantity': quantity}

    def calculate_total(self):
        total = 0
        for product, item_info in self.items.items():
            total += item_info['price'] * item_info['quantity']
        return total

    def apply_discount(self, discount_percent):
        total = self.calculate_total()
        discount_amount = (discount_percent / 100) * total
        return total - discount_amount

    def checkout(self):
        # Proses pembayaran (belum diimplementasikan dalam contoh ini)
        return "Transaksi selesai."

    def check_stock(self, product, quantity):
        # Manajemen stok (belum diimplementasikan dalam contoh ini)
        return True

