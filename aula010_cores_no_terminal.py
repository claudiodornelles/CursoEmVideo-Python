"""

para implementar cores no terminal podemos utilizar os códigos de escape sequence ANSI

 ->  \033[style;text;backgroundm
 Exemplo:
 ->  \033[0;33;44m

style
0 - None
1 - Bold
4 - Underline
7 - Negative - Inverte configurações - O que setar para fundo vai para letra e vice-versa

Text
30 - Branco
31 - Vermelho
32 - Verde
33 - Amarelo
34 - Azul
35 - Magenta
36 - Ciano
37 - Cinza

Background
40 - Branco
41 - Vermelho
42 - Verde
43 - Amarelo
44 - Azul
45 - Magenta
46 - Ciano
47 - Cinza

"""

#  Exemplo
print('\033[1;30;41mOlá, Mundo!')
print('\033[1;30;41mOlá, Mundo!\033[m')
print('\033[1;30;41m Olá, Mundo! \033[m')
nome = "Claudio"
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m'}
print(f"Olá {cores['amarelo']}{nome}{cores['limpa']}")
