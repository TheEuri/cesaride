from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)


## create a random username
username = ''.join(random.choices(string.ascii_lowercase, k=8))
username2= ''.join(random.choices(string.ascii_lowercase, k=8))
username3 = ''.join(random.choices(string.ascii_lowercase, k=8))
## create a random password
password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

class TestSignupLogin(TestCase):
    def test_a_register_driver(self):
        browser.get("http://127.0.0.1:8000/signup/") 
        time.sleep(0.5)
        browser.find_element(By.ID, "username").send_keys(username)
        time.sleep(0.5)
        browser.find_element(By.ID, "email").send_keys(username + "@gmail.com")
        time.sleep(0.5)
        browser.find_element(By.ID, "password1").send_keys(password)
        time.sleep(0.5)
        browser.find_element(By.ID, "password2").send_keys(password)
        time.sleep(0.5)
        browser.find_element(By.ID, "phone_number").send_keys("123456789")
        time.sleep(0.5)
        browser.find_element(By.ID, "is_student").click()
        time.sleep(0.5)
        browser.find_element(By.ID, "submit").click()
        time.sleep(1)
        assert browser.current_url == "http://127.0.0.1:8000/"

    def test_b_login_driver(self):
       
        time.sleep(1)
        browser.find_element(By.ID, "username").send_keys(username)
        time.sleep(0.5)
        browser.find_element(By.ID, "password").send_keys(password)
        time.sleep(0.5)
        browser.find_element(By.ID, "submit").click()
        assert browser.current_url == "http://127.0.0.1:8000/choose_role/"

    def test_c_choose_role_driver(self):
       
        time.sleep(1)
        browser.find_element(By.ID, "submit").click()
        time.sleep(0.5)
        assert browser.current_url == "http://127.0.0.1:8000/driver_home"

    def test_d_create_vehicle(self):
      time.sleep(1)
      browser.find_element(By.ID, "menu-toggle").click()
      time.sleep(0.5)
      sidebar_nav = browser.find_element(By.CLASS_NAME, "sidebar-nav")
      sidebar_nav.find_element(By.XPATH, '//a[@href="/driver/cars/create/"]').click()
      time.sleep(1)
      browser.find_element(By.ID, "id_brand").send_keys("Minha marca")
      time.sleep(0.5)
      browser.find_element(By.ID, "id_model").send_keys("Meu modelo")
      time.sleep(0.5)
      browser.find_element(By.ID, "id_plate").send_keys("ABC1234")
      time.sleep(0.5)
      browser.find_element(By.ID, "id_observations")
      time.sleep(0.5)
      browser.find_element(By.ID, "id_observations").send_keys("Minhas observações")
      time.sleep(0.5)
      browser.find_element(By.XPATH, "//button[@type='submit']").click()
      time.sleep(1)
      assert browser.current_url == "http://127.0.0.1:8000/driver_home"

    def test_e_create_rice(self):
        time.sleep(1)
        browser.find_element(By.ID, "btn-create-ride").click()
        time.sleep(0.5)
        
        select_element = browser.find_element(By.ID, 'car')
        select = Select(select_element)
        select.select_by_index(0)

        browser.find_element(By.ID, 'origin').send_keys("rua 1")
        time.sleep(0.5)
        browser.find_element(By.ID, 'destination').send_keys("rua 2")
        time.sleep(0.5)
        browser.find_element(By.ID, 'price').send_keys("10")
        time.sleep(0.5)
        browser.find_element(By.ID, 'passengers').send_keys("1")
        time.sleep(0.5)
        browser.find_element(By.ID, 'time').send_keys("10:30")
        time.sleep(0.5)
        browser.find_element(By.ID, 'observations').send_keys("Observação")
        time.sleep(0.5)
        browser.find_element(By.ID, 'submit').click()
        time.sleep(5)

        assert browser.current_url == "http://127.0.0.1:8000/driver_home"
       
    
    def test_f_create_rice_2(self):
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[2]/div[1]/a[1]").click()
        time.sleep(0.5)
        
        select_element = browser.find_element(By.XPATH, '/html/body/div/div/form/div[1]/select')
        select = Select(select_element)
        select.select_by_index(0)

        browser.find_element(By.XPATH, '/html/body/div/div/form/div[2]/input').send_keys("rua 11")
        time.sleep(0.5)
        browser.find_element(By.XPATH, '/html/body/div/div/form/div[3]/input').send_keys("rua 12")
        time.sleep(0.5)
        browser.find_element(By.XPATH, '/html/body/div/div/form/div[4]/div/input').send_keys("12")
        time.sleep(0.5)
        browser.find_element(By.XPATH, '/html/body/div/div/form/div[5]/input').send_keys("4")
        time.sleep(0.5)
        browser.find_element(By.XPATH, '/html/body/div/div/form/div[6]/input').send_keys("10:30")
        time.sleep(0.5)
        browser.find_element(By.XPATH, '/html/body/div/div/form/div[7]/textarea').send_keys("Observação")
        time.sleep(0.5)
        browser.find_element(By.XPATH, '/html/body/div/div/form/button').click()
        time.sleep(2)

        assert browser.current_url == "http://127.0.0.1:8000/driver_home"
        
    def test_g_cancel_ride(self): 
        browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[2]/div/div/strong/div[2]/a").click()
        time.sleep(1)
        browser.find_element(By.ID, "menu-toggle").click()
        time.sleep(0.5)
        sidebar_nav = browser.find_element(By.CLASS_NAME, "sidebar-nav")
        sidebar_nav.find_element(By.XPATH, '/html/body/div[1]/a/button').click()
        time.sleep(0.5)

        assert browser.current_url == "http://127.0.0.1:8000/"
        
    # # #entrando como passageiro para solicitar a corrida
    # def test_h_register_driver(self):
    #     browser.get("http://127.0.0.1:8000/signup/") 
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "username").send_keys(username2)
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "email").send_keys(username2 + "@gmail.com")
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "password1").send_keys(password)
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "password2").send_keys(password)
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "phone_number").send_keys("123456789")
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "is_student").click()
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "submit").click()
    #     time.sleep(1)
    #     assert browser.current_url == "http://127.0.0.1:8000/"
    

    # def test_i_login_passenger(self): 
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "username").send_keys(username2)
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "password").send_keys(password)
    #     time.sleep(1)
    #     browser.find_element(By.ID, "submit").click()
    #     assert browser.current_url == "http://127.0.0.1:8000/choose_role/"
    
    # def test_j_choose_role_passenger(self):
    #     time.sleep(1)
    #     select_element = browser.find_element(By.ID, 'role')
    #     select = Select(select_element)
    #     select.select_by_index(1)
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "submit").click()
    #     time.sleep(0.75)
    #     assert browser.current_url == "http://127.0.0.1:8000/passanger_home/"
    
    # def test_k_request_travel(self):
    #     time.sleep(0.75)
    #    # browser.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/a')
    #     browser.get('http://127.0.0.1:8000/passenger/request_ride/1/')
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "origin").send_keys("rua 3")
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "destination").send_keys("rua 4")
    #     time.sleep(1.5)
    #     browser.find_element(By.ID, "submit").click()
    #     time.sleep(2)
    #     browser.find_element(By.ID, "back").click()
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "menu-toggle").click()
    #     time.sleep(0.5)
    #     sidebar_nav = browser.find_element(By.CLASS_NAME, "sidebar-nav")
    #     sidebar_nav.find_element(By.XPATH, '/html/body/div[1]/a/button').click()
    #     time.sleep(0.75)
       
    # #entrando com a 2a conta para solicitar corrida 
    
    # def test_l_register_driver(self):
    #     browser.get("http://127.0.0.1:8000/signup/") 
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "username").send_keys(username3)
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "email").send_keys(username3 + "@gmail.com")
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "password1").send_keys(password)
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "password2").send_keys(password)
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "phone_number").send_keys("123456789")
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "is_student").click()
    #     time.sleep(0.5)
    #     browser.find_element(By.ID, "submit").click()
    #     time.sleep(1)
    #     assert browser.current_url == "http://127.0.0.1:8000/"
    
    # def test_m_login_passenger2(self):
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "username").send_keys(username3)
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "password").send_keys(password)
    #     time.sleep(1)
    #     browser.find_element(By.ID, "submit").click()
    #     assert browser.current_url == "http://127.0.0.1:8000/choose_role/"
    
    # def test_n_choose_role_passenger2(self):
    #     time.sleep(1)
    #     select_element = browser.find_element(By.ID, 'role')
    #     select = Select(select_element)
    #     select.select_by_index(1)
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "submit").click()
    #     time.sleep(0.75)
    #     assert browser.current_url == "http://127.0.0.1:8000/passanger_home/"
    
    # def test_o_request_travel2(self):
    #     time.sleep(0.75)
    #     browser.get('http://127.0.0.1:8000/passenger/request_ride/1/')
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "origin").send_keys("rua 3")
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "destination").send_keys("rua 4")
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "submit").click()
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "back").click()
    #     browser.find_element(By.ID, "menu-toggle").click()
    #     time.sleep(0.5)
    #     sidebar_nav = browser.find_element(By.CLASS_NAME, "sidebar-nav")
    #     sidebar_nav.find_element(By.XPATH, '/html/body/div[1]/a/button').click()
    #     time.sleep(0.75)
        

    # #entrando na conta do motorista para aceitar a solicitação

    # def test_p_login_driver(self):
    #     browser.get('http://127.0.0.1:8000/')
    #     time.sleep(1)
    #     browser.find_element(By.ID, "username").send_keys(username)
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "password").send_keys(password)
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "submit").click()
    #     assert browser.current_url == "http://127.0.0.1:8000/choose_role/"
    
    # def test_q_choose_role_driver(self):
       
    #     time.sleep(1)
    #     browser.find_element(By.ID, "submit").click()
    #     time.sleep(0.75)
    #     assert browser.current_url == "http://127.0.0.1:8000/driver_home"
    
    
    # def test_r_accepting_race(self):
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "details").click()
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "btn-refuse").click()
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "btn-acecept").click()
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "btn-ending").click()
    #     assert browser.current_url == "http://127.0.0.1:8000/driver_home"
    
    # #historico do motorista 

    # def test_s_ride_history(self):
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "menu-toggle").click()
    #     time.sleep(0.5)
    #     sidebar_nav = browser.find_element(By.CLASS_NAME, "sidebar-nav")
    #     sidebar_nav.find_element(By.XPATH, '/html/body/div[1]/ul/li[3]/a').click()
    #     time.sleep(0.75)
    #     browser.find_element(By.XPATH, "/html/body/div/button").click()
    #    # browser.find_element(By.ID, "menu-toggle").click()
    #     time.sleep(1)
    #     sidebar_nav = browser.find_element(By.CLASS_NAME, "sidebar-nav")
    #     sidebar_nav.find_element(By.XPATH, '/html/body/div[1]/a/button').click()
        
    #     #entrando como passageiro para ver o historico
    
    # def test_t_login_passenger3(self):
    #     time.sleep(0.75)
    #     browser.get('http://127.0.0.1:8000/')
    #     time.sleep(1)
    #     browser.find_element(By.ID, "username").send_keys(username3)
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "password").send_keys(password)
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "submit").click()
    #     assert browser.current_url == "http://127.0.0.1:8000/choose_role/"
    
    # def test_u_choose_role_passenger3(self):
    #     time.sleep(1)
    #     select_element = browser.find_element(By.ID, 'role')
    #     select = Select(select_element)
    #     select.select_by_index(1)
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "submit").click()
    #     time.sleep(0.75)
    #     assert browser.current_url == "http://127.0.0.1:8000/passanger_home/"
    
    # def test_v_history_passenger(self):
    #     browser.find_element(By.ID, "menu-toggle").click()
    #     time.sleep(0.5)
    #     sidebar_nav = browser.find_element(By.CLASS_NAME, "sidebar-nav")
    #     sidebar_nav.find_element(By.XPATH, '/html/body/div[1]/ul/li[3]/a').click()
    #     time.sleep(3)
    
    # def test_w_forgotten_item(self):
    #     browser.find_element(By.XPATH, "/html/body/div/div/div/a[1]").click()
    #     time.sleep(1)
    #     browser.find_element(By.XPATH, "/html/body/div/div/div/form/div[1]/input").send_keys("computador")
    #     time.sleep(1)
    #     browser.find_element(By.XPATH, "/html/body/div/div/div/form/div[2]/textarea").send_keys("esqueci no banco de trás")
    #     time.sleep(1)
    #     browser.find_element(By.XPATH, "/html/body/div/div/div/form/button").click()

    # def test_x_rating(self):
    #     browser.find_element(By.ID, "menu-toggle").click()
    #     time.sleep(1)
    #     sidebar_nav = browser.find_element(By.CLASS_NAME, "sidebar-nav")
    #     sidebar_nav.find_element(By.XPATH, '/html/body/div[1]/ul/li[3]/a').click()
    #     time.sleep(3)
    #     browser.find_element(By.XPATH, "/html/body/div/div/div/a[2]").click()
    #     time.sleep(1)
    #     browser.find_element(By.XPATH, "/html/body/div/div/div/form/div[1]/input").send_keys("5")
    #     time.sleep(1)
    #     browser.find_element(By.XPATH, "/html/body/div/div/div/form/div[2]/textarea").send_keys("muito bom")
    #     time.sleep(1)
    #     browser.find_element(By.XPATH, "/html/body/div/div/div/form/button").click()
    #     time.sleep(1)
    #     browser.find_element(By.ID, "menu-toggle").click()
    #     time.sleep(0.5)
    #     sidebar_nav = browser.find_element(By.CLASS_NAME, "sidebar-nav")
    #     sidebar_nav.find_element(By.XPATH, '/html/body/div[1]/a/button').click()
    #     time.sleep(0.5)
    
    # def test_y_selling_forgotten_item(self):
    #     browser.get('http://127.0.0.1:8000/')
    #     time.sleep(1)
    #     browser.find_element(By.ID, "username").send_keys(username)
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "password").send_keys(password)
    #     time.sleep(0.75)
    #     browser.find_element(By.ID, "submit").click()
    #     time.sleep(1)
    #     browser.find_element(By.ID, "submit").click()
    #     time.sleep(0.75)
    #     browser.find_element(By.XPATH, "/html/body/div[2]/div[1]/a[2]").click()
    #     time.sleep(1)
    #     browser.find_element(By.XPATH, "/html/body/div/button").click()
    
    # def test_z_selling_rating(self):
    #     browser.find_element(By.XPATH, "/html/body/div[2]/div[1]/a[3]").click()
    #     time.sleep(1)
    #     browser.find_element(By.XPATH, "/html/body/div/button").click()
    #     time.sleep(5)











    


    

