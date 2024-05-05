from selenium import webdriver

class TestHome():
    def __init__(self):
        # Create driver
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("window-size=1200x600")
        self.driver = webdriver.Chrome(options=options)