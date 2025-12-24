
from pages.HeaderComponent import HeaderComponent

from pages.HomePage import HomePage
from pages.ProductPage import ProductPage

def test_ct001_adicionar_produto_ao_carrinho(driver):

        home = HomePage(driver)
        product = ProductPage(driver)
        header = HeaderComponent(driver)

        home.open()
        home.open_laptop()
        product.add_to_cart()

        assert "(1)" in header.get_cart_quantity()
        assert "14.1-inch Laptop" in header.get_flyout_text()