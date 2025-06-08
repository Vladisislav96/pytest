class Base:
    def __init__(self, driver):
        self.driver=driver





    """Метод для получения нынешней URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Нынешняя url - " + get_url)

    """метод для проверки слов"""
    def assert_word(self, word, result):
        value_word=word.text
        assert value_word == result
        print("значения совпадают")
