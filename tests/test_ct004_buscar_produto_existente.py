from pages.HomePage import HomePage
from pages.SearchPage import  SearchPage


def test_ct004_buscar_produto_existente(driver):
    home = HomePage(driver)
    search = SearchPage(driver)

    home.open()
    home.search_product("Laptop")

    assert search.has_results()