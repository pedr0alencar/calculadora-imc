# Calculadora de IMC

Atividade em Python 3 com interface gráfica em Tkinter. O programa calcula o IMC a partir da altura em centímetros e do peso em quilogramas e mostra a classificação para adultos.

## Como executar

Abra um terminal na pasta do projeto e rode:

```sh
python imc.py
```

No Windows, se necessário, use `py imc.py`. Para conferir se o Tkinter está disponível, rode `python -m tkinter`. Não há pacotes de terceiros para instalar.

## Como usar

- Preencha a altura em centímetros e o peso em quilogramas. A interface aceita vírgula ou ponto decimal.
- Clique em **Calcular**. Por exemplo, 175 cm e 70 kg resultam em **22,86 kg/m² — Peso normal**.
- **Reiniciar** limpa os campos e o resultado. **Sair** fecha a janela.

O nome e o endereço são campos da interface e não são gravados. Para testar, use dados fictícios.

Fórmula: peso em kg dividido pela altura em metros ao quadrado. A classificação usa o valor antes do arredondamento. [Referência do enunciado](https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal).
