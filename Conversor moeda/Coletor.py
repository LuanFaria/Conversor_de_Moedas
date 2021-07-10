# Lembrar de instalar o selenium e o geckodriver (pasta bin)


def coletar_dollar():
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    firefox_options = Options()
    firefox_options.headless = True
    navegador = webdriver.Firefox(options=firefox_options)
    navegador.get('https://www.melhorcambio.com/dolar-hoje')
    cot_dolar = navegador.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value')
    cot_dolar = cot_dolar.replace(',', '.')
    return (cot_dolar)


def coletar_euro():
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    fire_op = Options()
    fire_op.headless = True
    navegador = webdriver.Firefox(options=fire_op)
    navegador.get('https://www.remessaonline.com.br/cotacao/cotacao-euro')
    cot_euro = navegador.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div/div[1]/div/div[3]/div[2]/form/div[2]/input').get_attribute('value')
    cot_euro = cot_euro.replace(',', '.')
    return cot_euro


# def coletar_bitcoins():
#     from selenium import webdriver
#     from selenium.webdriver.firefox.options import Options
#     fire_opt = Options()
#     fire_opt.headless = True
#     navegador = webdriver.Firefox(options=fire_opt)
#     # navegador = webdriver.Firefox()
#     navegador.get('https://www.google.com/search?channel=fs&client=ubuntu&q=pre%C3%A7o+do+bitcoin')
#     cot_bit = navegador.find_element_by_xpath(
#         '/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div[3]/table/tbody/tr[3]/td[1]/input').get_attribute(
#         'value')
#     cot_bit = cot_bit.replace('.', '')
#     cot_bit = cot_bit.replace(',', '.')
#     return cot_bit


def coletar_real():
    cot_real = 1
    return cot_real


def coletar_iene():
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    fire_opt = Options()
    fire_opt.headless = True
    navegador = webdriver.Firefox(options=fire_opt)
    navegador.get('https://www.google.com/search?channel=fs&client=ubuntu&q=pre%C3%A7o+iene')
    cot_iene = navegador.find_element_by_xpath(
        '/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/span[1]').get_attribute(
        'data-value')
    cot_iene = cot_iene.replace(',', '.')
    return cot_iene

# # Para Testar
if __name__ == '__main__':
    print(coletar_dollar())
    print(coletar_euro())
    print(coletar_real())
    print(coletar_iene())

