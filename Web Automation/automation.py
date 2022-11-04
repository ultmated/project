import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType, os_name, OSType
from webdriver_manager.core.logger import log

binary_location = {
    OSType.LINUX: "/usr/bin/brave-browser",
    OSType.MAC: "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    OSType.WIN: "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
}[os_name()]
log(binary_location)
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
