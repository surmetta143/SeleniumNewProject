def test_google_search(driver):
    search_page = GoogleSearchPage(driver)
    search_page.load()
    driver.maximize_window()
    time.sleep(5)
    search_page.setEmail("suresh@gmail.com")
    time.sleep(5)
    search_page.setPhone("8985256492")
    time.sleep(5)