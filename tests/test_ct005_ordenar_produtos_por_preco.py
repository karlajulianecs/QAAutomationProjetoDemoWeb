from pages.SearchPage import SearchPage

def test_ct005_ordenar_produtos_por_preco(driver):
    search = SearchPage(driver)

    search.open_with_query("Laptop")
    search.sort_low_to_high()

    assert search.has_results()