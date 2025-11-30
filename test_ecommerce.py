import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains




def test_correct_page():
 
 option = webdriver.ChromeOptions()
 driver = webdriver.Chrome(options = option)
 wait = WebDriverWait(driver, timeout=20)

 print("Opening website...")
 driver.get("https://tutorialsninja.com/demo/")
 driver.maximize_window()
 print("Waiting 10 seconds for page to load - take screenshot now!")
 time.sleep(10)

 title_page= driver.title
 assert title_page == "Your Store"
 print(f"Page title verified: {title_page}")


 print("Clicking on Cameras link...")
 cameras_locator=(By.XPATH, '//a[text()="Cameras"]')
 wait_cameras= wait.until(EC.presence_of_element_located(cameras_locator))

 wait_cameras.click()

 print("Waiting 10 seconds after clicking Cameras - take screenshot now!")
 time.sleep(10)
    

 print("Clicking on Nikon D300 camera...")
 camera = (By.XPATH, '//a[text()="Nikon D300"]')
 wait_camera= wait.until(EC.element_to_be_clickable(camera))
 wait_camera.click()
 print("Waiting 8 seconds after selecting camera - take screenshot now!")
 time.sleep(8)


 print("Clicking on first product picture...")
 first_pic_locator = (By.XPATH, '//a[@class="thumbnail"]')
 first_pic = wait.until(EC.element_to_be_clickable(first_pic_locator))
 first_pic.click()
 print("Waiting 8 seconds after opening image gallery - take screenshot now!")
 time.sleep(8)


 print("Clicking next picture 5 times...")
 next_picture_locator = (By.XPATH,'//button[@title="Next (Right arrow key)"]')
 next_picture = wait.until(EC.element_to_be_clickable(next_picture_locator))
 for i in range(0,5):
        print(f"  Clicking next picture {i+1}/5...")
        next_picture.click()
        time.sleep(3)  # 3 seconds between each picture
 print("Waiting 5 seconds after viewing pictures - take screenshot now!")
 time.sleep(5)

 print("Closing image gallery...")
 c_button_locator = (By.XPATH,'//button[@title="Close (Esc)"]')
 c_button = wait.until(EC.element_to_be_clickable(c_button_locator))
 c_button.click()
 print("Waiting 5 seconds after closing gallery - take screenshot now!")
 time.sleep(5)



 print("Setting quantity to 3...")
 quantity=driver.find_element(By.ID,'input-quantity')
 quantity.click()
 time.sleep(2)
 

 quantity.clear()
 time.sleep(2)
 quantity.send_keys('3')
 print("Waiting 5 seconds after setting quantity - take screenshot now!")
 time.sleep(5)


 print("Adding first item to cart...")
 add_button=driver.find_element(By.ID,'button-cart')
 add_button.click()
 print("Waiting 8 seconds after adding to cart - take screenshot now!")
 time.sleep(8)


 print("Navigating back to home page...")
 try:

     logo = driver.find_element(By.XPATH, '//img[@title="Your Store"]')
     logo.click()
 except:

     driver.get("https://tutorialsninja.com/demo/")
 print("Waiting 5 seconds after navigating to home - take screenshot now!")
 time.sleep(5)


 print("Navigating to Desktops page...")

 try:
     driver.get("https://tutorialsninja.com/demo/index.php?route=product/category&path=20")
     print("Waiting 8 seconds after navigating to Desktops page - take screenshot now!")
     time.sleep(8)
 except:
     
     print("Direct navigation failed, trying hover method...")
     desktops_locator = (By.XPATH, '//a[text()="Desktops"]')
     desktops = wait.until(EC.presence_of_element_located(desktops_locator))
     action = ActionChains(driver)
     action.move_to_element(desktops).perform()
     print("Waiting 8 seconds after hovering - take screenshot now!")
     time.sleep(8)
     
     
     desktop = None
     locators_to_try = [
         (By.XPATH, "//a[contains(text(), 'Show All Desktops')]"),
         (By.XPATH, "//a[contains(text(), 'Show All')]"),
         (By.XPATH, "//a[@class='see-all']"),
         (By.XPATH, "//ul[@class='dropdown-menu']//a[contains(@href, 'desktop')]"),
     ]
     
     for locator in locators_to_try:
         try:
             print(f"  Trying locator: {locator[1]}")
             
             short_wait = WebDriverWait(driver, timeout=3)
             desktop = short_wait.until(EC.element_to_be_clickable(locator))
             print(f"  Found element with locator: {locator[1]}")
             break
         except:
             continue
     
     if desktop:
         driver.execute_script("arguments[0].click();", desktop)
         print("Waiting 8 seconds after clicking Show All Desktops - take screenshot now!")
         time.sleep(8)
     else:
         print("Could not find dropdown link, page should already be on desktops")



 print("Clicking on Apple Cinema product...")
 AC= driver.find_element(By.XPATH, "//a[contains(@href, 'product_id=42')]")
 AC.click()

 print("Waiting 8 seconds after selecting Apple Cinema - take screenshot now!")
 time.sleep(8)



 print("Scrolling to Add to Cart button...")
 add_button_2=driver.find_element(By.XPATH, '//button[@id="button-cart"]')
 driver.execute_script("arguments[0].scrollIntoView(true);", add_button_2)
 print("Waiting 5 seconds after scrolling - take screenshot now!")
 time.sleep(5)



 print("Opening calendar...")
 calendar=driver.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
 calendar.click()
 print("Waiting 5 seconds after opening calendar - take screenshot now!")
 time.sleep(5)

 next_click=driver.find_element(By.XPATH, '//th[@class="next"]')
 month_year=driver.find_element(By.XPATH, '//th[@class="picker-switch"]')



 print("Navigating calendar to June 2011...")
 click_count = 0
 while month_year.text != 'June 2011' and click_count < 100:
  next_click.click()
  click_count += 1
  print(f"  Calendar navigation: {month_year.text} (click {click_count})")
  time.sleep(3) 

 print("Waiting 5 seconds after calendar navigation - take screenshot now!")
 time.sleep(5)


 print("Selecting day 31...")
 calendar_date = driver.find_element(By.XPATH, '//td[text()="31"]')
 calendar_date.click()
 print("Waiting 5 seconds after selecting date - take screenshot now!")
 time.sleep(5)


 print("Adding second item to cart...")
 add_button_2.click()
 print("Waiting 8 seconds after adding to cart - take screenshot now!")
 time.sleep(8)


 print("Clicking on cart total...")
 cart = driver.find_element(By.ID, 'cart-total')

 cart.click()
 print("Waiting 10 seconds after clicking cart - take screenshot now!")
 time.sleep(10)
 
 print("Test completed! Closing browser in 5 seconds...")
 time.sleep(5)
 driver.quit()
 print("Browser closed. All done!")


if __name__ == "__main__":
    test_correct_page()
