from rembg import remove  # Importo a função mágica que remove o fundo da imagem
from PIL import Image     # Biblioteca para manipular imagens no Python (amo o poder do Pillow 💅)

input_path = 'cl.jpg'     # Caminho da imagem original (com fundo)
output_path = 'output2.png'  # Nome da imagem que vai sair sem fundo

input = Image.open(input_path)  # Abro a imagem que quero editar
output = remove(input)          # Removo o fundo com uma única função (muito chique)
output.save(output_path)        # Salvo a nova imagem com fundo transparente
