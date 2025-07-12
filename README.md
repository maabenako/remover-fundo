# Remoção de Fundo com Python 🖼️✨

Este é um script super simples que usa a biblioteca `rembg` para remover o fundo de uma imagem automaticamente. Ideal pra quem quer deixar uma imagem com fundo transparente em poucos segundos e sem precisar abrir o Photoshop 😎

## Como funciona

O script faz o seguinte:

1. Abre a imagem original (com fundo)
2. Remove o fundo usando o `rembg`
3. Salva uma nova imagem com fundo transparente (.png)

## Requisitos

Instale as dependências com:

```bash
pip install rembg pillow
```

## Como usar

Coloque sua imagem no mesmo diretório com o nome `cl.jpg`, depois execute o script:

```bash
python remove_bg.py
```

⚠️ Não esqueça de renomear os arquivos conforme os nomes das imagens e resultados que deseja utilizar e receber! O resultado será salvo como `output2.png`.

## Exemplo de código

```python
from rembg import remove
from PIL import Image

input_path = 'input.jpg'
output_path = 'output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
```

## Créditos

Feito com muito carinho por Marcela Nako 💖
