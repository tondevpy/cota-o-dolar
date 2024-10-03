# Monitor de Cotação do Dólar

Este projeto é um **monitorador de cotações** que verifica o valor do dólar em relação ao real em intervalos regulares e salva os resultados em um arquivo de texto (`cotação.txt`). Ele utiliza o **Selenium** com **undetected_chromedriver** para acessar a página de cotações e obter o valor atual.

## Funcionalidades

- Acessa automaticamente a página de conversão de moedas do site [Wise](https://wise.com/br/currency-converter/dolar-hoje).
- Extrai o valor do dólar em relação ao real (R$).
- Salva a cotação e o horário em que foi verificada no arquivo `cotação.txt`.
- Repete o processo automaticamente em intervalos de tempo (configurável via `sleep()`).

## Requisitos

Antes de executar o projeto, você precisará instalar algumas dependências. Use o seguinte comando para instalar as bibliotecas necessárias:

```bash
pip install undetected-chromedriver selenium
```

##  Requisitos do Sistema

Python 3.x
Google Chrome instalado
ChromeDriver compatível com a versão do seu Google Chrome (gerenciado pelo undetected_chromedriver).