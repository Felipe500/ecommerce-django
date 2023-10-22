from model_utils import Choices


ORDER_STATUS = Choices(
    ('created', 'Criado'),
    ('pending', 'Pendente'),
    ('paid', 'Aprovado'),
    ('sent', 'Enviado'),
    ('completed', 'Completo'),
    ('failed', 'Reprovado'),
)

ORDER_PAYMENT_METHOD = Choices(
    ('card', '1 cartão'),
    ('two_card', '2 cartões'),
    ('billet', 'Boleto'),
    ('pix', 'Pix'),
    ('smart_card', 'Parcelamento Inteligente (1 Cartão)'),
)

STATES_BR = Choices(
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)
