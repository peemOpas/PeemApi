from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "/Users/peem/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("http://localhost:3000/")

waittime = 1000

#click filter  button
driver.implicitly_wait(waittime)
link = driver.find_element_by_css_selector("#root > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-3 > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-md-4 > a > span.MuiFab-label")
link.click()

#click Category button
driver.implicitly_wait(waittime)
element = driver.find_element_by_css_selector("#search_input")
action = ActionChains(driver)
action.drag_and_drop_by_offset(element,500,0)
action.perform()





#Selected one of Category
driver.implicitly_wait(waittime)
element2 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(1) > input")
# action = ActionChains(driver)
action.drag_and_drop_by_offset(element2,500,0)
action.perform()


driver.implicitly_wait(waittime)
element4 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(2) > input")
# action4 = ActionChains(driver)
action.drag_and_drop_by_offset(element4,500,0)
action.perform()

#Unselected one of Category
driver.implicitly_wait(waittime)
element3 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li.option.selected.highlightOption.highlight > input")
# action3 = ActionChains(driver)
action.drag_and_drop_by_offset(element3,500,0)
action.perform()


driver.implicitly_wait(waittime)
element5 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(2) > input")
# action5 = ActionChains(driver)
action.drag_and_drop_by_offset(element5,100,0)
action.perform()

driver.implicitly_wait(waittime)
element6 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(3) > input")
# action5 = ActionChains(driver)
action.drag_and_drop_by_offset(element6,100,0)
action.perform()

driver.implicitly_wait(waittime)
element7 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(4) > input")
# action5 = ActionChains(driver)
action.drag_and_drop_by_offset(element7,100,0)
action.perform()

driver.implicitly_wait(waittime)
element8 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(5) > input")
# action5 = ActionChains(driver)
action.drag_and_drop_by_offset(element8,100,0)
action.perform()

driver.implicitly_wait(waittime)
element9 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(6) > input")
# action5 = ActionChains(driver)
action.drag_and_drop_by_offset(element9,100,0)
action.perform()

driver.implicitly_wait(waittime)
element10 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(7) > input")
# action5 = ActionChains(driver)
action.drag_and_drop_by_offset(element10,100,0)
action.perform()

driver.implicitly_wait(waittime)
element11 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(3) > input")
# action5 = ActionChains(driver)
action.drag_and_drop_by_offset(element11,100,0)
action.perform()

driver.implicitly_wait(waittime)
element12 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(4) > input")
# action5 = ActionChains(driver)
action.drag_and_drop_by_offset(element12,100,0)
action.perform()

driver.implicitly_wait(waittime)
element13 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(5) > input")
# action5 = ActionChains(driver)
action.drag_and_drop_by_offset(element13,100,0)
action.perform()

driver.implicitly_wait(waittime)
element14 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(6) > input")
# action5 = ActionChains(driver)
action.drag_and_drop_by_offset(element14,100,0)
action.perform()

driver.implicitly_wait(waittime)
element15 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(7) > input")
# action5 = ActionChains(driver)
action.drag_and_drop_by_offset(element15,100,0)
action.perform()











driver.implicitly_wait(waittime)
action.drag_and_drop_by_offset(element,200,0)
action.perform()