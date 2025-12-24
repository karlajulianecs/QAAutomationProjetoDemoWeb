from pages.HeaderComponent import HeaderComponent
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.ProductPage import ProductPage
from pages.CartPage import CartPage

def test_ct006_adicionar_produto_a_wishlist(driver):
    login = LoginPage(driver)
    home = HomePage(driver)
    product = ProductPage(driver)
    header = HeaderComponent(driver)
    cart = CartPage(driver)

    login.open()
    login.login("test@demo.com", "123456")

    home.open()
    home.open_laptop()
    product.add_to_cart()

    #assert "(1)" in product.get_text(ProductElements.WISHLIST_QTY)

    assert "(1)" in header.get_cart_quantity()

    cart.open()
    assert cart.has_products()