from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def extract_usp_current_lot_number(catalog_number):
    url = f"https://store.usp.org/product/{catalog_number}"

    # ChromeDriver 경로 설정
    chrome_service = Service(executable_path='C:\\Users\\4CE147B4DC\\test\\chromedriver.exe')

    # Chrome 옵션 설정
    chrome_options = Options()
    # SSL 오류 무시
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')
    # 창 없는 모드 (필요한 경우 주석 해제)
    # chrome_options.add_argument('--headless')

    # WebDriver 객체 생성
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    try:
        driver.get(url)
        
        # JavaScript가 로드될 때까지 최대 7초 대기
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-bind='text: $data.usp_current_lot_number']"))
        )
        
        # usp_current_lot_number 추출
        element = driver.find_element(By.CSS_SELECTOR, "[data-bind='text: $data.usp_current_lot_number']")
        usp_current_lot_number = element.text
        
        return usp_current_lot_number
    finally:
        driver.quit()

# 예제 사용
catalog_number = "1479009"
print(extract_usp_current_lot_number(catalog_number))
