

def test_Home_page_title(driver):
    print(driver.title)
    assert "Your Store" in driver.title


def test_Home_page_url(driver):
    print(driver.current_url)
    assert "http://localhost/opencart/" in driver.current_url

