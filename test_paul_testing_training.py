import pytest
from paul_testing_training import GoogleChecker

def test___init__():
    googlechecker1 = GoogleChecker("https://www.google.com")
    print(googlechecker1.record.status_code)
    assert googlechecker1.record.status_code == 200

def test_check_for_submit_button():
    googlechecker2 = GoogleChecker("https://www.google.com")
    actual_response = googlechecker2.check_for_submit_button()
    assert actual_response == True

def test_show_html():
    googlechecker3 = GoogleChecker("https://www.google.com")
    html_string = googlechecker3.show_html()
    # with open("html_text.txt", "w+") as writefile:
      #   writefile.write(html_string)
    with open("html_text.txt", "w+") as readfile:
        html_string_from_file = readfile.read()
    assert html_string == html_string_from_file

    

