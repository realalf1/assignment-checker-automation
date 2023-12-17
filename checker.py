from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def pertemuan():
    pertemuan = int(input(
    """
            Pertemuan
    ---------------------------
    Pertemuan 1  | Pertemuan 10
    Pertemuan 2  | Pertemuan 11
    Pertemuan 3  | Pertemuan 12
    Pertemuan 4  | Pertemuan 13
    Pertemuan 5  | Pertemuan 14
    Pertemuan 6  | Pertemuan 15
    Pertemuan 7  | Pertemuan 16
    Pertemuan 8  | Pertemuan 17
    Pertemuan 9  | Pertemuan 18
    ---------------------------
    Pilih: """))

    if pertemuan == 1: sid = 1
    if pertemuan == 2: sid = 2
    if pertemuan == 3: sid = 3
    if pertemuan == 4: sid = 4
    if pertemuan == 5: sid = 5
    if pertemuan == 6: sid = 6
    if pertemuan == 7: sid = 7
    if pertemuan == 8: sid = 8
    if pertemuan == 9: sid = 9
    if pertemuan == 10: sid = 10
    if pertemuan == 11: sid = 11
    if pertemuan == 12: sid = 12
    if pertemuan == 13: sid = 13
    if pertemuan == 14: sid = 14
    if pertemuan == 15: sid = 15
    if pertemuan == 16: sid = 16
    if pertemuan == 17: sid = 17
    if pertemuan == 18: sid = 18

    matkul = int(input('''
    Mata Kuliah:
        1. Teori Bahasa dan Otomata
        2. Logika Komputasional
        3. Aljabar Linear
        4. Organisasi dan Arsitektur Komputer
        5. Praktikum Algoritma dan Struktur Data
        6. Algoritma dan Struktur Data
    ----------------------------------------------
    Pilih: '''))

    if matkul == 1: cid = 15553
    elif matkul == 2: cid = 15554
    elif matkul == 3: cid = 15555
    elif matkul == 4: cid = 15556
    elif matkul == 5: cid = 15557
    elif matkul == 6: cid = 15558
    
    return sid, cid

def assignment(url, username, password, cid, sid):

    driver = webdriver.Firefox()
    prefix = "https://"
    login_path = "/login"
    login_url = f"{prefix}{url}{login_path}"
    driver.get(login_url)

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginbtn").click()

    course_path = "/course/view.php"
    course_url = f"{prefix}{url}{course_path}?id={cid}"

    driver.get(course_url)
    course_sid = f"{course_url}#section-{sid}"
    driver.get(course_sid)

    sleep(2)
    driver.quit()

sid,cid = pertemuan()
assignment("login.url.com", "username", "passwd", cid, sid)
