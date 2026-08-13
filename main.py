from catalogo import (
    filmes,
    cadastrar_filme,
    cadastrar_personagem,
    cadastrar_figurinha,
    listar_filmes
)

vingadores = cadastrar_filme(titulo="Vingadores", preco_album=15, preco_pacote=5)
hulk = cadastrar_filme(titulo="Hulk", preco_album=10, preco_pacote=4)

homem_ferro = cadastrar_personagem(filme=vingadores, nome="Homem de ferro")
xenoman = cadastrar_personagem(filme=vingadores, nome="Xenoman")

fig1=cadastrar_figurinha(filme=vingadores, numero=1, personagem=homem_ferro)
fig2=cadastrar_figurinha(filme=vingadores, numero=2, personagem=xenoman)

listar_filmes()
