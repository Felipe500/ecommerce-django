(function () {
    select_variacao = document.getElementById('select-variations');
    variation_preco = document.getElementById('variation-price');
    variation_preco_promocional = document.getElementById('variation-price-promotional');

    if (!select_variacao) {
        return;
    }

    if (!variation_preco) {
        return;
    }

    select_variacao.addEventListener('change', function () {
        preco = this.options[this.selectedIndex].getAttribute('data-price');
        preco_promocional = this.options[this.selectedIndex].getAttribute('data-price-promotional');


        if (preco && variation_preco) {
            variation_preco.innerHTML = preco;
        }
        
        if (variation_preco_promocional && preco_promocional) {
            variation_preco_promocional.innerHTML = preco_promocional;
        } else {
            variation_preco_promocional.innerHTML = preco;
            variation_preco.innerHTML = ''
        }

    })
    
})();

