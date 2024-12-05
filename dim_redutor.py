from PIL import Image
import os


def rgb_para_cinza(imagem_rgb):
    largura, altura = imagem_rgb.size
    pixels_rgb = imagem_rgb.convert('RGB').load()

    # Cria nova imagem em tons de cinza
    imagem_cinza = Image.new('L', (largura, altura))
    pixels_cinza = imagem_cinza.load()

    for i in range(largura):
        for j in range(altura):
            r, g, b = pixels_rgb[i, j]
            cinza = int(0.3 * r + 0.59 * g + 0.11 * b)
            pixels_cinza[i, j] = cinza

    return imagem_cinza


def cinza_para_binarizada(imagem_cinza, limiar=128):
    largura, altura = imagem_cinza.size
    pixels_cinza = imagem_cinza.load()

    imagem_binaria = Image.new('1', (largura, altura))
    pixels_binarios = imagem_binaria.load()

    for i in range(largura):
        for j in range(altura):
            if pixels_cinza[i, j] >= limiar:
                pixels_binarios[i, j] = 255  # Branco
            else:
                pixels_binarios[i, j] = 0    # Preto

    return imagem_binaria


# Carrega a imagem da pasta
entrada = "python_logo.png"
imagem_entrada = Image.open(entrada)

# Extrai o nome do arquivo sem a extensão
nome_base, extensao = os.path.splitext(entrada)

# Converte para cinza e binario
imagem_cinza = rgb_para_cinza(imagem_entrada)
imagem_binaria = cinza_para_binarizada(imagem_cinza)

# Salvar as imagens com nomes dinâmicos
imagem_cinza.save(f"{nome_base}_cinza.png")
imagem_binaria.save(f"{nome_base}_binaria.png")

# Mostrar as imagens
imagem_cinza.show()
imagem_binaria.show()
