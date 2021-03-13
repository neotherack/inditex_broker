from bs4 import BeautifulSoup
import requests

class Website:
    replacements = ["«","»","_","%","-","&","“","”",".",":","\n","\r","\t","\'","|","/",'"',",","º","ª","(",")"]
    useless_words = ["a", "ante", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "so", "sobre", "tras", "versus", "vía"]
    BLANKS = 50
    OFFSET = 1000
    LIMIT = 10000
    url = ""
    noisy_text = ""
    clear_text = ""
    encoded_data = []

    def __init__(self, url):
        if not url.startswith("www."):
            url = "www."+url
        if not url.startswith("https://"):
            url = "https://"+url
        self.url = url
        self.noisy_text = self.dump_website()
        self.clear_text = self.get_text()
        self.encoded_data = self.encode()

    def dump_website(self):
        result = requests.get(self.url)
        soup = BeautifulSoup(result.text, 'html.parser')
        text = soup.get_text().lower().strip()
        return text

    def get_text(self):
        text = self.noisy_text
        for useless_word in self.useless_words:
            text = text.replace(f" {useless_word} ", " ")

        for rep in self.replacements:
            text = text.replace(rep, " ")

        for i in range(self.BLANKS, 1, -1):
            text = text.replace(" "*i, " ")

        return text

    def encode(self):
        text = self.clear_text[self.OFFSET:self.LIMIT+self.OFFSET].ljust(self.LIMIT, chr(0))
        values = list(map(ord, text))
        return values
