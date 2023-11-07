import re
import uuid
import posixpath

from pathlib import Path
from PIL import Image
from io import BytesIO
from datetime import datetime

from django.core.files import File
from django.core.files.utils import validate_file_name
from django.db import models


def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return False

    novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
    reverso = 10                        # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0                   # Zera o total
            novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False



image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}


def image_resize(image, width, height):
    with Image.open(image) as img:
        if img.width > width or img.height > height:
            output_size = (width, height)
            img.thumbnail(output_size, Image.LANCZOS)
            img_filename = Path(image.file.name).name
            img_suffix = Path(image.file.name).name.split(".")[-1]
            img_format = image_types[img_suffix]
            buffer = BytesIO()
            img.save(buffer, format=img_format)
            file_object = File(buffer)
            image.save(img_filename, file_object)


def _generate_filename(inst_upload_to, filename) -> str:
    ext = filename.split('.')[-1]
    hash_name = str(uuid.uuid4())
    filename = f"{hash_name}.{ext}"
    upload_to = f"{inst_upload_to}/%Y/%m/%d/"
    dirname = datetime.now().strftime(upload_to)
    filename = posixpath.join(dirname, filename)
    filename = validate_file_name(filename, allow_relative_path=True)
    return filename


class FileField(models.FileField):
    def generate_filename(self, instance, filename):
        return self.storage.generate_filename(_generate_filename(self.upload_to, filename))


class ImageField(models.ImageField):
    def generate_filename(self, instance, filename):
        return self.storage.generate_filename(_generate_filename(self.upload_to, filename))


def format_price_(val):
    return f'R$ {val:.2f}'.replace('.', ',')


def cart_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])


def cart_totals(carrinho):
    return sum(
        [
            item.get('preco_quantitativo_promocional')
            if item.get('preco_quantitativo_promocional')
            else item.get('preco_quantitativo')
            for item
            in carrinho.values()
        ]
    )
