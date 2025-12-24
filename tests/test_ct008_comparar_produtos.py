from pages.HomePage import HomePage
from pages.ProductPage import ProductPage
from pages.ComparePage import ComparePage

def test_ct008_comparar_produtos(driver):
    home = HomePage(driver)
    product = ProductPage(driver)
    compare = ComparePage(driver)

    home.open()
    home.open_laptop()

    product.add_to_compare()

    compare.open()

    assert compare.has_products()