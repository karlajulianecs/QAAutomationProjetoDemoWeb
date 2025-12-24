from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.BasePage import BasePage
from elements.SearchElements import SearchElements


class SearchPage(BasePage):

    def open_with_query(self, query: str):
        self.driver.get(
            f"https://demowebshop.tricentis.com/search?q={query}"
        )

    def sort_low_to_high(self):
        dropdown = Select(
            self.wait.until(
                EC.element_to_be_clickable(
                    SearchElements.SORT_DROPDOWN
                )
            )
        )
        dropdown.select_by_visible_text("Price: Low to High")

    def has_results(self) -> bool:
        return len(
            self.wait.until(
                EC.presence_of_all_elements_located(
                    SearchElements.PRODUCT_LIST
                )
            )
        ) > 0