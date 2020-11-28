# 💻 GetFollowed 💻
Script feito com o intuito de ganhar seguidores por meio de receber follows mútuos.

## Redes Sociais suportadas (até então):
- 🐦 Twitter (somente tema padrão);<sup id="a1">[1](#f1)</sup>
- 📷 Instagram

## Como usar?
Antes de começar, você deve ter o [Python3](https://www.python.org/downloads/) instalado.<sup id="a2">[2](#f2)</sup>
Após a instalação, clone ou baixe esse repositório, e na pasta principal, use `cd src`
e depois `pip install -r requirements.txt`, e você está pronto para continuar.

Antes de iniciar o script, veja se a rede social que você deseja usar está na lista acima, 
se estiver, abra a rede social que gostaria de usar, e procure uma aba de
"pessoas recomendadas para você seguir" ou algo relacionado/parecido à isso.

Após isso, inicie o script, ou clicando diretamente nele, ou usando `python main.py` estando na pasta `src`. 
Quando o script for iniciado, ele perguntará qual rede social você irá usar,
você deve escolher uma das opções disponíveis usando o número correto para a opção desejada, 
e em seguida, um timer de 5 segundos irá começar, nesse tempo, você deve voltar para a página
da rede social, e esperar. O script deve começar automaticamente à clicar no botão de seguir,
e se ele não achar, ele irá scrollar para baixo automaticamente. (Muito fácil, não?)

### To-Do:
- [ ] Adicionar suporte à mais redes sociais;
- [ ] Adicionar suporte à outros temas do Twitter;
- [X] Documentar melhor o código;
- [ ] Adicionar suporte à inglês;

#### Footnotes
<b id="f1">1.</b> [Outros temas geram incompatibilidade no script, solução em andamento;](#a1)

<b id="f2">2.</b> [Python3 recomendado;](#a2)