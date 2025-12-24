from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.ProductPage import ProductPage
from pages.ComparePage import ComparePage

def test_ct009_limpar_carrinho(driver):
    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    home.open()
    home.open_laptop()
    product.add_to_cart()

    cart.open()
    cart.remove_product()

    assert cart.is_empty()
