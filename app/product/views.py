from django.http import HttpResponse

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View

from .models import Product, VariationProduct
from django.contrib import messages


class ListProductView(ListView):
    model = Product
    template_name = 'product/list_product.html'
    context_object_name = 'products'
    paginate_by = 10


class DetailsProductView(DetailView):
    model = Product
    template_name = 'product/detail_product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class AddToCarProductView(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('product:list')
        )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(
                self.request,
                'Produto não existe'
            )
            return redirect(http_referer)

        variacao = get_object_or_404(VariationProduct, id=variacao_id)
        variacao_estoque = variacao.stock
        produto = variacao.product

        produto_id = produto.id
        produto_nome = produto.name
        variacao_nome = variacao.name or ''
        preco_unitario = variacao.price
        preco_unitario_promocional = variacao.price_promotional
        quantidade = 1
        slug = produto.slug
        imagem = produto.image

        if imagem:
            imagem = imagem.name
        else:
            imagem = ''

        if variacao.stock < 1:
            messages.error(
                self.request,
                'Estoque insuficiente'
            )
            return redirect(http_referer)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
            quantidade_carrinho = carrinho[variacao_id]['quantidade']
            quantidade_carrinho += 1

            if variacao_estoque < quantidade_carrinho:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {quantidade_carrinho}x no '
                    f'produto "{produto_nome}". Adicionamos {variacao_estoque}x '
                    f'no seu carrinho.'
                )
                quantidade_carrinho = variacao_estoque

            carrinho[variacao_id]['quantidade'] = quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo'] = preco_unitario * \
                quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * \
                quantidade_carrinho
        else:
            carrinho[variacao_id] = {
                'produto_id': produto_id,
                'produto_nome': produto_nome,
                'variacao_nome': variacao_nome,
                'variacao_id': variacao_id,
                'preco_unitario': preco_unitario,
                'preco_unitario_promocional': preco_unitario_promocional,
                'preco_quantitativo': preco_unitario,
                'preco_quantitativo_promocional': preco_unitario_promocional,
                'quantidade': 1,
                'slug': slug,
                'imagem': imagem,
            }
        self.request.session['my_car'] = 'mini'
        self.request.session.save()

        messages.success(
            self.request,
            f'Produto {produto_nome} {variacao_nome} adicionado ao seu '
            f'carrinho {carrinho[variacao_id]["quantidade"]}x.'
        )

        return redirect(http_referer)


class RemoveToCarProductView(View):
    pass


class ShoppingCartView(View):
    pass


class FinishShoppingCartView(View):
    pass



