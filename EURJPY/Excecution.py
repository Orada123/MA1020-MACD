from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import json
import EURJPY as EJ
import schedule
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from urllib3.exceptions import MaxRetryError
from selenium.common.exceptions import TimeoutException

def buy_order_1():
    global driver
    Stop_1 = True
    while Stop_1:
        try:
            PATH = r"C:\Users\Nicholas Lim\Downloads\chromedriver.exe"
            driver = webdriver.Chrome(PATH)

            t = time.time()
            driver.set_page_load_timeout(10)

            try:
                driver.get("https://webtrader.icmarkets.com/")

            except TimeoutException:
                driver.execute_script("window.stop();")
                print('Time consuming:', time.time() - t)

            # options.add_argument('window-size=1200,1100');

            time.sleep(2)

            # Access elements that are within an iframe
            driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

            time.sleep(2)

            # Closing demo account application
            actions = ActionChains(driver)
            actions.send_keys(Keys.ESCAPE)
            actions.perform()

            # Login credentials
            Login = driver.find_element_by_id('login')
            Login.send_keys("1900063596")

            Passsword = driver.find_element_by_id('password')
            Passsword.send_keys("Adeline1")

            Server = driver.find_element_by_class_name('input-combobox')
            Server.click()

            Server = driver.find_element_by_xpath('//*[@id="server"]/option[22]')
            Server.click()

            OK_button = driver.find_element_by_xpath('/html/body/div[14]/div/div[3]/button[2]')
            OK_button.click()

            time.sleep(5)

            Buy_px = driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div[1]/div/table/tbody/tr[16]/td[3]/div/span')
            try:
                while True:
                    try:
                        # Creating a new buy order
                        New_order = driver.find_element_by_xpath('/html/body/div[3]/div[1]/a[1]')
                        New_order.click()

                        time.sleep(3)

                        # Selecting the symbol
                        Symbol = driver.find_element_by_id('symbol')
                        Symbol.click()

                        Symbol = driver.find_element_by_xpath('// *[ @ id = "symbol"] / option[16]')
                        Symbol.click()

                        # Number of lots
                        Volume = driver.find_element_by_id('volume')
                        Volume.click()
                        Volume.send_keys('0.01')

                        # Stop loss level is 100 points
                        Stop_Loss = driver.find_element_by_id('sl')
                        Stop_Loss.click()
                        """Need to change to int"""
                        SL = str(float(Buy_px.text) - 0.15)
                        Stop_Loss.send_keys(SL)  # Max 100 points loss 300 points profit

                        Comment = driver.find_element_by_id('comment')
                        Comment.click()
                        Comment.send_keys("Buy (MA50200) EURJPY")

                        Take_Profit = driver.find_element_by_id('tp')
                        Take_Profit.click()
                        TP = str(float(Buy_px.text) + 0.3)
                        Take_Profit.send_keys(TP)

                        Buy_btn = driver.find_element_by_xpath('/html/body/div[17]/div/div[3]/button[3]')
                        Buy_btn.click()

                        Stop_1 = False

                        time. sleep(2)

                        driver.quit()

                    except (ElementClickInterceptedException, ElementNotInteractableException) as e:
                        print(e)
                        Order_close = driver.find_element_by_xpath('/html/body/div[16]/div/div[2]')
                        Order_close.click()
                        pass

            except MaxRetryError as e:
                break

        except (NoSuchElementException, ElementNotInteractableException) as e:
            print(e)
            driver.quit()
            pass


"""Creates a sell order when requirements are met with tp and sl"""
def sell_order_1():
    global driver
    Stop_1 = True
    while Stop_1:
        try:
            PATH = r"C:\Users\Nicholas Lim\Downloads\chromedriver.exe"
            driver = webdriver.Chrome(PATH)

            t = time.time()
            driver.set_page_load_timeout(10)

            try:
                driver.get("https://webtrader.icmarkets.com/")

            except TimeoutException:
                driver.execute_script("window.stop();")
                print('Time consuming:', time.time() - t)

            # options.add_argument('window-size=1200,1100');

            time.sleep(2)

            # Access elements that are within an iframe
            driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

            # Closing demo account application
            actions = ActionChains(driver)
            actions.send_keys(Keys.ESCAPE)
            actions.perform()

            Login = driver.find_element_by_id('login')
            Login.send_keys("1900063596")

            Passsword = driver.find_element_by_id('password')
            Passsword.send_keys("Adeline1")

            Server = driver.find_element_by_class_name('input-combobox')
            Server.click()

            Server = driver.find_element_by_xpath('//*[@id="server"]/option[22]')
            Server.click()

            OK_button = driver.find_element_by_xpath('/html/body/div[14]/div/div[3]/button[2]')
            OK_button.click()

            time.sleep(5)

            Sell_px = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[3]/div[1]/div/table/tbody/tr[16]/td[2]/div/span')

            try:
                while True:
                    try:
                        # Creating a new buy order
                        New_order = driver.find_element_by_xpath('/html/body/div[3]/div[1]/a[1]')
                        New_order.click()

                        time.sleep(3)

                        # Selecting the symbol
                        Symbol = driver.find_element_by_id('symbol')
                        Symbol.click()

                        Symbol = driver.find_element_by_xpath('// *[ @ id = "symbol"] / option[16]')
                        Symbol.click()

                        # Number of lots
                        Volume = driver.find_element_by_id('volume')
                        Volume.click()
                        Volume.send_keys('0.01')

                        # Stop loss level is 100 points
                        Stop_Loss = driver.find_element_by_id('sl')
                        Stop_Loss.click()
                        """Need to change to int"""
                        SL = str(float(Sell_px.text) + 0.15)
                        Stop_Loss.send_keys(SL)  # Max 100 points loss 300 points profit

                        Comment = driver.find_element_by_id('comment')
                        Comment.click()
                        Comment.send_keys("Sell (MA50200) EURJPY")

                        Take_Profit = driver.find_element_by_id('tp')
                        Take_Profit.click()
                        TP = str(float(Sell_px.text) - 0.3)
                        Take_Profit.send_keys(TP)

                        Sell_btn = driver.find_element_by_xpath('/html/body/div[17]/div/div[3]/button[2]')
                        Sell_btn.click()

                        Stop_1 = False

                        time.sleep(2)

                        driver.quit()

                    except (ElementClickInterceptedException, ElementNotInteractableException) as e:
                        print(e)
                        Order_close = driver.find_element_by_xpath('/html/body/div[16]/div/div[2]')
                        Order_close.click()
                        pass

            except MaxRetryError as e:
                break

        except (NoSuchElementException, ElementNotInteractableException) as e:
            print(e)
            driver.quit()
            pass

def main_job_1():
    # Activates Data_Receiver.py
    Trigger_Flags_1 = {}
    Crossing_Flags_1 = {}

    now_1 = datetime.now()
    current_time_1 = now_1.strftime("%H:%M:%S")
    print("Current Time = ", current_time_1)

    EJ.retrieve_json()

    file_name = "Trigger_Flags.json"

    with open(file_name) as f_obj:
        data = f_obj.read()
        retrieve = json.loads(data)

    Buy_flag = retrieve["Buy_flag"]
    Sell_flag = retrieve["Sell_flag"]

    """When a purchase is made the flags are reverted back to false and an email is sent out or maybe a whatsapp notification"""
    # Constantly checks the

    if Buy_flag:
        buy_order_1()

        print('A buy order has been made! (MA50200) EURJPY')

        Trigger_Flags_1["Buy_flag"] = False
        Trigger_Flags_1["Sell_flag"] = False

        file_name = "Trigger_Flags.json"
        with open(file_name, "w") as f_obj:
            json.dump(Trigger_Flags_1, f_obj)

        Crossing_Flags_EMA = {}

        Crossing_Flags_EMA['Cross_Up'] = False
        Crossing_Flags_EMA['Cross_Down'] = False

        file_name = "Crossing_Flags_EMA.json"

        with open(file_name, "w") as f_obj:
            json.dump(Crossing_Flags_EMA, f_obj)

        Crossing_Flags_MACD = {}

        Crossing_Flags_MACD['Cross_Up'] = False
        Crossing_Flags_MACD['Cross_Down'] = False

        file_name = "Crossing_Flags_MACD.json"

        with open(file_name, "w") as f_obj:
            json.dump(Crossing_Flags_MACD, f_obj)
    elif Sell_flag:
        sell_order_1()

        print('A sell order has been made! (MA50200) EURJPY')

        Trigger_Flags_1["Buy_flag"] = False
        Trigger_Flags_1["Sell_flag"] = False

        file_name = "Trigger_Flags.json"
        with open(file_name, "w") as f_obj:
            json.dump(Trigger_Flags_1, f_obj)

        Crossing_Flags_EMA = {}

        Crossing_Flags_EMA['Cross_Up'] = False
        Crossing_Flags_EMA['Cross_Down'] = False

        file_name = "Crossing_Flags_EMA.json"

        with open(file_name, "w") as f_obj:
            json.dump(Crossing_Flags_EMA, f_obj)

        Crossing_Flags_MACD = {}

        Crossing_Flags_MACD['Cross_Up'] = False
        Crossing_Flags_MACD['Cross_Down'] = False

        file_name = "Crossing_Flags_MACD.json"

        with open(file_name, "w") as f_obj:
            json.dump(Crossing_Flags_MACD, f_obj)
    else:
        pass



now = datetime.now()
current_time = now.strftime("%H:%M")

# Need to push demo login credential before passing live credentials to test
def consolidated():
    main_job_1()

print("Program started")
schedule.every().day.at("00:00").do(consolidated)
schedule.every().day.at("01:00").do(consolidated)
schedule.every().day.at("02:00").do(consolidated)
schedule.every().day.at("03:00").do(consolidated)
schedule.every().day.at("04:00").do(consolidated)
schedule.every().day.at("05:00").do(consolidated)
schedule.every().day.at("06:00").do(consolidated)
schedule.every().day.at("07:00").do(consolidated)
schedule.every().day.at("08:00").do(consolidated)
schedule.every().day.at("09:00").do(consolidated)
schedule.every().day.at("10:00").do(consolidated)
schedule.every().day.at("11:00").do(consolidated)
schedule.every().day.at("12:00").do(consolidated)
schedule.every().day.at("13:00").do(consolidated)
schedule.every().day.at("14:00").do(consolidated)
schedule.every().day.at("15:00").do(consolidated)
schedule.every().day.at("16:00").do(consolidated)
schedule.every().day.at("17:00").do(consolidated)
schedule.every().day.at("18:00").do(consolidated)
schedule.every().day.at("19:00").do(consolidated)
schedule.every().day.at("20:00").do(consolidated)
schedule.every().day.at("21:00").do(consolidated)
schedule.every().day.at("22:00").do(consolidated)
schedule.every().day.at("23:00").do(consolidated)

schedule.every().day.at("00:05").do(consolidated)
schedule.every().day.at("01:05").do(consolidated)
schedule.every().day.at("02:05").do(consolidated)
schedule.every().day.at("03:05").do(consolidated)
schedule.every().day.at("04:05").do(consolidated)
schedule.every().day.at("05:05").do(consolidated)
schedule.every().day.at("06:05").do(consolidated)
schedule.every().day.at("07:05").do(consolidated)
schedule.every().day.at("08:05").do(consolidated)
schedule.every().day.at("09:05").do(consolidated)
schedule.every().day.at("10:05").do(consolidated)
schedule.every().day.at("11:05").do(consolidated)
schedule.every().day.at("12:05").do(consolidated)
schedule.every().day.at("13:05").do(consolidated)
schedule.every().day.at("14:05").do(consolidated)
schedule.every().day.at("15:05").do(consolidated)
schedule.every().day.at("16:05").do(consolidated)
schedule.every().day.at("17:05").do(consolidated)
schedule.every().day.at("18:05").do(consolidated)
schedule.every().day.at("19:05").do(consolidated)
schedule.every().day.at("20:05").do(consolidated)
schedule.every().day.at("21:05").do(consolidated)
schedule.every().day.at("22:05").do(consolidated)
schedule.every().day.at("23:05").do(consolidated)

schedule.every().day.at("00:10").do(consolidated)
schedule.every().day.at("01:10").do(consolidated)
schedule.every().day.at("02:10").do(consolidated)
schedule.every().day.at("03:10").do(consolidated)
schedule.every().day.at("04:10").do(consolidated)
schedule.every().day.at("05:10").do(consolidated)
schedule.every().day.at("06:10").do(consolidated)
schedule.every().day.at("07:10").do(consolidated)
schedule.every().day.at("08:10").do(consolidated)
schedule.every().day.at("09:10").do(consolidated)
schedule.every().day.at("10:10").do(consolidated)
schedule.every().day.at("11:10").do(consolidated)
schedule.every().day.at("12:10").do(consolidated)
schedule.every().day.at("13:10").do(consolidated)
schedule.every().day.at("14:10").do(consolidated)
schedule.every().day.at("15:10").do(consolidated)
schedule.every().day.at("16:10").do(consolidated)
schedule.every().day.at("17:10").do(consolidated)
schedule.every().day.at("18:10").do(consolidated)
schedule.every().day.at("19:10").do(consolidated)
schedule.every().day.at("20:10").do(consolidated)
schedule.every().day.at("21:10").do(consolidated)
schedule.every().day.at("22:10").do(consolidated)
schedule.every().day.at("23:10").do(consolidated)

schedule.every().day.at("00:15").do(consolidated)
schedule.every().day.at("01:15").do(consolidated)
schedule.every().day.at("02:15").do(consolidated)
schedule.every().day.at("03:15").do(consolidated)
schedule.every().day.at("04:15").do(consolidated)
schedule.every().day.at("05:15").do(consolidated)
schedule.every().day.at("06:15").do(consolidated)
schedule.every().day.at("07:15").do(consolidated)
schedule.every().day.at("08:15").do(consolidated)
schedule.every().day.at("09:15").do(consolidated)
schedule.every().day.at("10:15").do(consolidated)
schedule.every().day.at("11:15").do(consolidated)
schedule.every().day.at("12:15").do(consolidated)
schedule.every().day.at("13:15").do(consolidated)
schedule.every().day.at("14:15").do(consolidated)
schedule.every().day.at("15:15").do(consolidated)
schedule.every().day.at("16:15").do(consolidated)
schedule.every().day.at("17:15").do(consolidated)
schedule.every().day.at("18:15").do(consolidated)
schedule.every().day.at("19:15").do(consolidated)
schedule.every().day.at("20:15").do(consolidated)
schedule.every().day.at("21:15").do(consolidated)
schedule.every().day.at("22:15").do(consolidated)
schedule.every().day.at("23:15").do(consolidated)

schedule.every().day.at("00:20").do(consolidated)
schedule.every().day.at("01:20").do(consolidated)
schedule.every().day.at("02:20").do(consolidated)
schedule.every().day.at("03:20").do(consolidated)
schedule.every().day.at("04:20").do(consolidated)
schedule.every().day.at("05:20").do(consolidated)
schedule.every().day.at("06:20").do(consolidated)
schedule.every().day.at("07:20").do(consolidated)
schedule.every().day.at("08:20").do(consolidated)
schedule.every().day.at("09:20").do(consolidated)
schedule.every().day.at("10:20").do(consolidated)
schedule.every().day.at("11:20").do(consolidated)
schedule.every().day.at("12:20").do(consolidated)
schedule.every().day.at("13:20").do(consolidated)
schedule.every().day.at("14:20").do(consolidated)
schedule.every().day.at("15:20").do(consolidated)
schedule.every().day.at("16:20").do(consolidated)
schedule.every().day.at("17:20").do(consolidated)
schedule.every().day.at("18:20").do(consolidated)
schedule.every().day.at("19:20").do(consolidated)
schedule.every().day.at("20:20").do(consolidated)
schedule.every().day.at("21:20").do(consolidated)
schedule.every().day.at("22:20").do(consolidated)
schedule.every().day.at("23:20").do(consolidated)

schedule.every().day.at("00:25").do(consolidated)
schedule.every().day.at("01:25").do(consolidated)
schedule.every().day.at("02:25").do(consolidated)
schedule.every().day.at("03:25").do(consolidated)
schedule.every().day.at("04:25").do(consolidated)
schedule.every().day.at("05:25").do(consolidated)
schedule.every().day.at("06:25").do(consolidated)
schedule.every().day.at("07:25").do(consolidated)
schedule.every().day.at("08:25").do(consolidated)
schedule.every().day.at("09:25").do(consolidated)
schedule.every().day.at("10:25").do(consolidated)
schedule.every().day.at("11:25").do(consolidated)
schedule.every().day.at("12:25").do(consolidated)
schedule.every().day.at("13:25").do(consolidated)
schedule.every().day.at("14:25").do(consolidated)
schedule.every().day.at("15:25").do(consolidated)
schedule.every().day.at("16:25").do(consolidated)
schedule.every().day.at("17:25").do(consolidated)
schedule.every().day.at("18:25").do(consolidated)
schedule.every().day.at("19:25").do(consolidated)
schedule.every().day.at("20:25").do(consolidated)
schedule.every().day.at("21:25").do(consolidated)
schedule.every().day.at("22:25").do(consolidated)
schedule.every().day.at("23:25").do(consolidated)

schedule.every().day.at("00:30").do(consolidated)
schedule.every().day.at("01:30").do(consolidated)
schedule.every().day.at("02:30").do(consolidated)
schedule.every().day.at("03:30").do(consolidated)
schedule.every().day.at("04:30").do(consolidated)
schedule.every().day.at("05:30").do(consolidated)
schedule.every().day.at("06:30").do(consolidated)
schedule.every().day.at("07:30").do(consolidated)
schedule.every().day.at("08:30").do(consolidated)
schedule.every().day.at("09:30").do(consolidated)
schedule.every().day.at("10:30").do(consolidated)
schedule.every().day.at("11:30").do(consolidated)
schedule.every().day.at("12:30").do(consolidated)
schedule.every().day.at("13:30").do(consolidated)
schedule.every().day.at("14:30").do(consolidated)
schedule.every().day.at("15:30").do(consolidated)
schedule.every().day.at("16:30").do(consolidated)
schedule.every().day.at("17:30").do(consolidated)
schedule.every().day.at("18:30").do(consolidated)
schedule.every().day.at("19:30").do(consolidated)
schedule.every().day.at("20:30").do(consolidated)
schedule.every().day.at("21:30").do(consolidated)
schedule.every().day.at("22:30").do(consolidated)
schedule.every().day.at("23:30").do(consolidated)

schedule.every().day.at("00:35").do(consolidated)
schedule.every().day.at("01:35").do(consolidated)
schedule.every().day.at("02:35").do(consolidated)
schedule.every().day.at("03:35").do(consolidated)
schedule.every().day.at("04:35").do(consolidated)
schedule.every().day.at("05:35").do(consolidated)
schedule.every().day.at("06:35").do(consolidated)
schedule.every().day.at("07:35").do(consolidated)
schedule.every().day.at("08:35").do(consolidated)
schedule.every().day.at("09:35").do(consolidated)
schedule.every().day.at("10:35").do(consolidated)
schedule.every().day.at("11:35").do(consolidated)
schedule.every().day.at("12:35").do(consolidated)
schedule.every().day.at("13:35").do(consolidated)
schedule.every().day.at("14:35").do(consolidated)
schedule.every().day.at("15:35").do(consolidated)
schedule.every().day.at("16:35").do(consolidated)
schedule.every().day.at("17:35").do(consolidated)
schedule.every().day.at("18:35").do(consolidated)
schedule.every().day.at("19:35").do(consolidated)
schedule.every().day.at("20:35").do(consolidated)
schedule.every().day.at("21:35").do(consolidated)
schedule.every().day.at("22:35").do(consolidated)
schedule.every().day.at("23:35").do(consolidated)

schedule.every().day.at("00:40").do(consolidated)
schedule.every().day.at("01:40").do(consolidated)
schedule.every().day.at("02:40").do(consolidated)
schedule.every().day.at("03:40").do(consolidated)
schedule.every().day.at("04:40").do(consolidated)
schedule.every().day.at("05:40").do(consolidated)
schedule.every().day.at("06:40").do(consolidated)
schedule.every().day.at("07:40").do(consolidated)
schedule.every().day.at("08:40").do(consolidated)
schedule.every().day.at("09:40").do(consolidated)
schedule.every().day.at("10:40").do(consolidated)
schedule.every().day.at("11:40").do(consolidated)
schedule.every().day.at("12:40").do(consolidated)
schedule.every().day.at("13:40").do(consolidated)
schedule.every().day.at("14:40").do(consolidated)
schedule.every().day.at("15:40").do(consolidated)
schedule.every().day.at("16:40").do(consolidated)
schedule.every().day.at("17:40").do(consolidated)
schedule.every().day.at("18:40").do(consolidated)
schedule.every().day.at("19:40").do(consolidated)
schedule.every().day.at("20:40").do(consolidated)
schedule.every().day.at("21:40").do(consolidated)
schedule.every().day.at("22:40").do(consolidated)
schedule.every().day.at("23:40").do(consolidated)

schedule.every().day.at("00:45").do(consolidated)
schedule.every().day.at("01:45").do(consolidated)
schedule.every().day.at("02:45").do(consolidated)
schedule.every().day.at("03:45").do(consolidated)
schedule.every().day.at("04:45").do(consolidated)
schedule.every().day.at("05:45").do(consolidated)
schedule.every().day.at("06:45").do(consolidated)
schedule.every().day.at("07:45").do(consolidated)
schedule.every().day.at("08:45").do(consolidated)
schedule.every().day.at("09:45").do(consolidated)
schedule.every().day.at("10:45").do(consolidated)
schedule.every().day.at("11:45").do(consolidated)
schedule.every().day.at("12:45").do(consolidated)
schedule.every().day.at("13:45").do(consolidated)
schedule.every().day.at("14:45").do(consolidated)
schedule.every().day.at("15:45").do(consolidated)
schedule.every().day.at("16:45").do(consolidated)
schedule.every().day.at("17:45").do(consolidated)
schedule.every().day.at("18:45").do(consolidated)
schedule.every().day.at("19:45").do(consolidated)
schedule.every().day.at("20:45").do(consolidated)
schedule.every().day.at("21:45").do(consolidated)
schedule.every().day.at("22:45").do(consolidated)
schedule.every().day.at("23:45").do(consolidated)

schedule.every().day.at("00:50").do(consolidated)
schedule.every().day.at("01:50").do(consolidated)
schedule.every().day.at("02:50").do(consolidated)
schedule.every().day.at("03:50").do(consolidated)
schedule.every().day.at("04:50").do(consolidated)
schedule.every().day.at("05:50").do(consolidated)
schedule.every().day.at("06:50").do(consolidated)
schedule.every().day.at("07:50").do(consolidated)
schedule.every().day.at("08:50").do(consolidated)
schedule.every().day.at("09:50").do(consolidated)
schedule.every().day.at("10:50").do(consolidated)
schedule.every().day.at("11:50").do(consolidated)
schedule.every().day.at("12:50").do(consolidated)
schedule.every().day.at("13:50").do(consolidated)
schedule.every().day.at("14:50").do(consolidated)
schedule.every().day.at("15:50").do(consolidated)
schedule.every().day.at("16:50").do(consolidated)
schedule.every().day.at("17:50").do(consolidated)
schedule.every().day.at("18:50").do(consolidated)
schedule.every().day.at("19:50").do(consolidated)
schedule.every().day.at("20:50").do(consolidated)
schedule.every().day.at("21:50").do(consolidated)
schedule.every().day.at("22:50").do(consolidated)
schedule.every().day.at("23:50").do(consolidated)

schedule.every().day.at("00:55").do(consolidated)
schedule.every().day.at("01:55").do(consolidated)
schedule.every().day.at("02:55").do(consolidated)
schedule.every().day.at("03:55").do(consolidated)
schedule.every().day.at("04:55").do(consolidated)
schedule.every().day.at("05:55").do(consolidated)
schedule.every().day.at("06:55").do(consolidated)
schedule.every().day.at("07:55").do(consolidated)
schedule.every().day.at("08:55").do(consolidated)
schedule.every().day.at("09:55").do(consolidated)
schedule.every().day.at("10:55").do(consolidated)
schedule.every().day.at("11:55").do(consolidated)
schedule.every().day.at("12:55").do(consolidated)
schedule.every().day.at("13:55").do(consolidated)
schedule.every().day.at("14:55").do(consolidated)
schedule.every().day.at("15:55").do(consolidated)
schedule.every().day.at("16:55").do(consolidated)
schedule.every().day.at("17:55").do(consolidated)
schedule.every().day.at("18:55").do(consolidated)
schedule.every().day.at("19:55").do(consolidated)
schedule.every().day.at("20:55").do(consolidated)
schedule.every().day.at("21:55").do(consolidated)
schedule.every().day.at("22:55").do(consolidated)
schedule.every().day.at("23:55").do(consolidated)

while True:
    schedule.run_pending()
    time.sleep(1)
