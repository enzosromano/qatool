from selenium import webdriver

class TestExample():

    def test_example(self): #Pytest will only run your functions if their names begin with "test"
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("window-size=1200x600")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://enzosromano.github.io/portfolio/")
        assert "Enzo Romano" in self.driver.title

        self.driver.close()
        self.driver.quit()
