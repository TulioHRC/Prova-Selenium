## Prova-Tecnica-Coimbra

Projeto básico para teste de conhecimentos em Python e sua biblioteca Selenium (https://selenium-python.readthedocs.io/).

O maior desáfio deste projeto foi a inserção dos dados na página web da receita, já que parece haver uma renderização dinâmica dos componentes, necessitando de um clique para os inputs (como o de CPF) aparecerem no HTML. 
Como solução, adotei utilizar cliques para acessar os blocos do formulário, em uma janela padrão do browser em 1080x800, como se fosse um usuário mesmo.

### Funcionamento
Execução padrão -> python main.py
Execução com melhor visualização -> python main.py -v

Obs.: Na execução padrão, você pode interagir normalmente com o computador durante a execução do programa.

### Requisitos
- Google Chrome 120.0.6099.109 (link alternativo para download: https://googlechromelabs.github.io/chrome-for-testing/#stable)
- Selenium Version 4.9.1 (python -m pip install --upgrade pip; pip install selenium;)
- Python3