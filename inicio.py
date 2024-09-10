from flask import Flask, render_template

app = Flask(__name__)

@app.route('/cadastro_produto')
def mostrar_cadastro_produto():
    return render_template ('cadastroProduto.html')

@app.route('/cadastro_fornecedor')
def mostrar_cadastro_fornecedor():
    return render_template ('cadastroFornecedor.html')

@app.route('/cadastro_cliente')
def mostrar_cadastro_cliente():
    return render_template ('cadastroCliente.html')

@app.route('/cadastro_categoria')
def mostrar_cadastro_categoria():
    return render_template ('cadastroCategoria.html')




@app.route('/lista_produtos')
def lista_produtos():
    return render_template ('listaProdutos.html')




@app.route('/carrinho')
def mostrar_carrinho():
    return render_template ('carrinho.html')

@app.route('/pagamento')
def mostrar_pagamento():
    return render_template ('pagamento.html')




@app.route('/detalhe_pedido')
def detalhe_pedido():
    return render_template ('detalhePedido.html')


app.run(debug=True)