# test_cashier.py

import unittest
from cashier import Cart

class TestCashier(unittest.TestCase):

    # ...

    def test_check_stock_insufficient(self):
        # Menguji manajemen stok ketika stok tidak mencukupi
        cart = Cart()

        # Menambahkan barang ke keranjang dengan jumlah yang melebihi stok
        cart.add_item("Produk D", 20.0, 100)

        # Mengecek stok
        result = cart.check_stock("Produk D", 101)

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
