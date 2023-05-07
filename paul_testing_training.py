import requests

class GoogleChecker:
    """This class checks a URL to see if the word "submit" is in its HTML code."""

    def __init__(self,url):
        """Gets the file at the designated url.
        inputs: url(string)
        outputs: None """
        self.record = requests.get(url)

    def check_for_submit_button(self):
        """Checks the downloaded file to see if it contains the string 'submit' 
        inputs: None
        outputs: String"""
        if "submit" in self.record.text:
            print("******submit button found!")
            return True

    def show_html(self):
        """Shows the full text of the downloaded file
        inputs: None
        outputs: String"""
        print(self.record.text)
        return self.record.text
