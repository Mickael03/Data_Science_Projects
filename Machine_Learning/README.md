Contém os códigos do livro:

>[![Machine Learning – Guia de Referência Rápida](https://d229kd5ey79jzj.cloudfront.net/2469/images/2469_1_H.png)](https://novatec.com.br/livros/machine-learning-guia-referencia/)

Editora: Novatec, São Paulo.  
Escrito: Matt Harrison

# Pyenv

Módulo para controle de múltiplas versos do python no computador  

[![pyenv](https://avatars.githubusercontent.com/u/46895318?s=200&v=4)](https://github.com/pyenv-win/pyenv-win)  

Guia de instalação: [Pyenv for Windows](https://github.com/pyenv-win/pyenv-win)  

> Instalação de uma versão: 
`pyenv install <versao>`

> Versão do pyenv   
`pyenv --version`

> Mostrar versão local  
`pyenv local --version`

> Mostrar versão global     
`pyenv global --version`

> Mostrar versões disponíveis   
`pyenv versions`

# Venv

Módulo para criar ambientes virtuais [Documentação do venv](https://docs.python.org/3/library/venv.html)  

> criar um ambiente:  
`python -m venv meu_ambiente`  

> Ativa o ambiente:  
``meu_ambiente\Scripts\activate``  

> Instação dos pacotes:  
``pip install pacotes``  

> Criar arquivo com versões de pacotes  
`pip freeze > requirements.txt`  

> Instalações de pacotes a partir de uma arquivo  
`pip install -r requirements.txt`  

> Desativa o ambiente:  
`deactivate`