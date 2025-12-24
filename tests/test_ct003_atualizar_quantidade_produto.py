from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.ProductPage import ProductPage


def test_ct003_atualizar_quantidade_produto(driver):
        home = HomePage(driver)
        product = ProductPage(driver)
        cart = CartPage(driver)

        home.open()
        home.open_laptop()
        product.add_to_cart()

        cart.open()
        cart.update_quantity("3")

        assert cart.has_products()