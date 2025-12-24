from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.ProductPage import ProductPage


def test_ct007_estimar_frete(driver):
    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    home.open()
    home.open_laptop()
    product.add_to_cart()

    cart.open()
    cart.estimate_shipping("Brazil", "01001-000")

    assert cart.has_shipping_result()