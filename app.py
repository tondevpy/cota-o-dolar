import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from time import sleep

def driver():
    

    while True:  
        app = uc.Chrome()
        app.get('https://wise.com/br/currency-converter/dolar-hoje')

        # aguardar pagina carregar 
        try:
            elemento = WebDriverWait(app, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'text-success'))
            )
            if elemento:
                dolar_real = app.find_element(By.CLASS_NAME, 'text-success').text
                data = datetime.now().strftime('%H:%M')
                
                with open('cotação.txt', 'a', encoding='utf-8') as arq:
                    arq.write(f'Cotação: R$ {dolar_real} - {data}\n')
            else:
                print('Elemento não localizado...')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
        finally:
            print('Finalizado com sucesso...')
            app.quit()
        # obter valor do dolar
        sleep(10)

driver()