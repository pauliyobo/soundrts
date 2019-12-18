Manual do jogo
==============

.. language: pt_BR
.. contents::

1. Introdu��o
-------------

Bem-vindo ao SoundRTS!

SoundRTS � um jogo de estrat�gia em tempo real inspirado por Warcraft e Starcraft, mas um �udio-jogo, portanto adaptado para cegos.
Nesse jogo, voc� explorar� os arredores, explorar� minas de ouro e bosques,
construir�, recrutar� oper�rios e soldados, e lutar� contra o inimigo!

Por padr�o o jogo est� no modo mapa: voc� est� virado para norte pode
selecionar todos os objetos sem a necessidade de se virar.
Voc� pode, todavia, jogar no modo em primeira pessoa, �til para
explora��o e ataque.

No Windows, voc� precisar� de um leitor de tela ou de uma voz SAPI 5.
No Linux o jogo usa o Speech Dispatcher.
Mac OS X usa NS Speech Synthesis.
A fala gravada foi totalmente removida no SoundRTS 1.2-alpha9.

2. Tutorial
-----------

Esse tutorial ir� ajud�-lo a aprender os principais controles do jogo.

2.1 Tutorial do cap�tulo 1
^^^^^^^^^^^^^^^^^^^^^^^^^^

Se voc� usa o Jaws ou alguma revis�o de tela, talvez voc� precise
desativ�-la para ter acesso completo ao teclado.

Quando o jogo come�ar, voc� ouvir� o nome do quadrado onde voc� est�: "A1".
A presen�a de uma mina de ouro em A1 � tamb�m anunciada. Para examinar
esse quadrado, pressione Tab algumas vezes.
Voc� vai notar que esse quadrado tem apenas uma sa�da (um caminho), uma
mina de ouro, um bosque, prefeitura 1 (� a sua base), e o oper�rio 1.

Ent�o pressione "Page Down" para saber se outro quadrado pode ser
examinado. Voc� ouvir� "C1", que cont�m (pressione Tab para saber) uma
fazenda, um caminho, um bosque e o soldado 1.

Se voc� pressionar "Page Down" novamente, estar� de novo em "A1". Isso
significa que apenas dois quadrados podem ser examinados no momento.

Uma forma alternativa de se mover pelo mapa � usar as setas. Assim voc� pode
passar pelos quadrados desconhecidos para selecionar um deles como alvo de uma ordem.

O objetivo desse mapa � construir uma fazenda e um quartel. Apenas o
oper�rio pode fazer isso. Mas ele precisa de ouro e madeira, e um
espa�o livre (um terreno). Para saber quanto de ouro, madeira e comida
voc� tem, pressione z, x e c, respectivamente.

Vamos mandar o oper�rio recolher ouro. Primeiro, para control�-lo, pressione Q
at� que voc� ou�a "oper�rio 1, esperando ordens!". Ent�o, pressione A
at� selecionar "explorar"; ent�o pressione Tab algumas vezes para selecionar a mina de ouro, e d�
Enter para confirmar. O oper�rio vai come�ar a extrair o ouro.

Para ir mais r�pido voc� precisar� de mais oper�rios. Pressione Q para
controlar a prefeitura, pressione A at� Recrutar Oper�rio e pressione Enter para confirmar.
Ap�s alguns segundos, um novo oper�rio, oper�rio 2, aparecer�.

Para mandar o oper�rio 2 recolher madeira, fa�a como o primeiro ou, para ir mais r�pido, pressione Q at� controlar o oper�rio 2, ent�o
pressione Tab para selecionar a mina de ouro, e finalmente pressione "Backspace".
Essa tecla faz a a��o padr�o no alvo selecionado: aqui, a a��o padr�o �
"explorar a mina de ouro".

Antes de recrutar um terceiro oper�rio, vamos dizer para a prefeitura 1
que todos os novos oper�rios dever�o explorar a mina de ouro. Para fazer
isso, pressione Q at� controlar a prefeitura 1. Ent�o pressione Tab at� selecionar a mina de
ouro. Finalmente, pressione "Backspace" para dar a ordem padr�o para a
prefeitura : "reuni�o � mina de ouro".
Agora voc� pode recrutar o terceiro oper�rio. Pressione A at� recrutar
oper�rio e pressione "Enter" para confirmar.

Quando voc� tiver ouro suficiente ou quando a mina se esgotar,
pressione D para controlar todos os oper�rios, Tab at� selecionar o
bosque e "Backspace" para confirmar.

O resto n�o � dif�cil.

2.2 Tutorial do cap�tulo 2
^^^^^^^^^^^^^^^^^^^^^^^^^^

Dica: agrupe suas unidades de combate. Para fazer isso, controle-as
(com a letra S) e fa�a-as patrulhar entre os quadrados que voc� quer
proteger.

2.3 Dicas e truques
^^^^^^^^^^^^^^^^^^^

- Mantenha suas for�as focadas.
- Fa�a seus soldados patrulharem. Soldados que patrulham podem proteger uma zona maior enquanto mant�m as for�as focadas.
- Use pontos de encontro nas constru��es. As constru��es que tem a possibilidade de recrutar unidades podem definir um ponto de encontro. As novas unidades v�o ter
  esse ponto de encontro como alvo. Por exemplo um novo oper�rio explorar� a mina de ouro.

- Use o modo defensivo para espiar. Uma unidade no modo defensivo vai fugir se ela encontrar inimigos mais fortes. Com isso voc� pode saber quantos inimigos tem
  num quadrado sem sacrificar a espia. Os oper�rios
  ficam no modo defensivo por padr�o mas os soldados podem ser configurados para ficarem nesse modo tamb�m.

- Uma unidade que fugir esquece suas ordens. Um oper�rio que fugir n�o vai voltar a recolher ouro, enquanto que se ele lutasse e sobrevivesse, ele iria voltar e
  exploraria novamente a mina.


3. Lista de comandos
--------------------

O jogo consiste em dar ordens �s suas unidades e constru��es. Para dar
uma ordem � uma unidade, voc� deve control�-la primeiro.
Se voc� pressionar F10 durante o jogo, voc� ir� para o menu da partida.

Movendo-se pelo mapa
^^^^^^^^^^^^^^^^^^^^

As setas fazem voc� se mover de um quadrado a outro pelo mapa. Se um
caminho direto existir entre o quadrado que voc� estiver e o novo, voc�
ouvir� um som
dependendo do tipo do caminho (caminho ou ponte). Se n�o existir um
caminho direto, voc� ouvir� um som de colis�o e permanecer� no mesmo
quadrado (pressione control + setas para passar por cima do obst�culo).
Se voc� n�o conhecer ainda se um caminho existe (quadrado desconhecido)
ent�o nenhum som ser� ouvido.

Outra forma de se mover pelo mapa � pressionar Page Up, que levar� voc� ao
pr�ximo quadrado interessante sem passar por quadrados vazios. Desde o SoundRTS 1.1 alpha
3, algumas variantes est�o dispon�veis:

- pressione Alt + PageUp/PageDown para selecionar o quadrado desconhecido anterior / seguinte.
- pressione Shift + PageUp/PageDown para selecionar o quadrado anterior / seguinte que contenha recursos.

Quando voc� controlar uma unidade e pressionar a Barra de espa�o, voc� a
seguir� quando ela mover de um quadrado a outro.

Escolhendo uma unidade para controlar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para controlar a pr�xima unidade local, pressione Q.

Para controlar a pr�xima constru��o, pressione W.
Para controlar o pr�ximo oper�rio, pressione E. Para controlar todos os oper�rios locais, pressione D.
Para controlar o pr�ximo oper�rio desocupado, pressione Alt + E. Para controlar todos os oper�rios desocupados locais, pressione Alt + D.
Para controlar o pr�ximo soldado, pressione R. Para controlar todos os soldados locais, pressione F.
Para controlar o pr�ximo arqueiro, pressione T. Para controlar todos os arqueiros locais, pressione G.
Para controlar o pr�ximo cavaleiro, pressione Y. Para controlar todos os cavaleiros locais, pressione H.
Para controlar a pr�xima catapulta, pressione U. Para controlar todas as catapultas locais, pressione J.
Para controlar o pr�ximo drag�o, pressione I. Para controlar todos os drag�es locais, pressione K.
Para controlar o pr�ximo mago, pressione O. Para controlar todos os magos locais, pressione L.

Quando uma tecla faz voc� controlar a pr�xima unidade, a mesma tecla
combinada com Shift faz voc� controlar a unidade anterior. Por exemplo,
para controlar o oper�rio anterior, pressione Shift + E.

Para controlar todas as unidades do mesmo tipo e no mesmo quadrado que a unidade atual, pressione 1.
Para controlar apenas a metade ou ter�o, pressione 2 ou 3.
Para parar de controlar um grupo, pressione 0.

Para controlar todas as unidades de combate locais, pressione S.
Para controlar todas as unidades de combate e oper�rios, pressione Alt + S.

Quando uma tecla fazer voc� controlar um grupo de unidades locais, a
mesma tecla combinada com o Control faz voc� controlar um grupo de todo
o mapa. Por exemplo, para controlar todos os soldados, pressione Control R ou Control F.

Dando uma ordem (m�todo principal)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para dar uma ordem � unidade controlada, o m�todo principal consiste em
escolher a ordem numa lista e selecionar o alvo se a ordem pedir.

Para selecionar a ordem na lista, pressione A (e Shift A para a anterior).

Se voc� precisar escolher um alvo, pressione Tab (ou Shift Tab). Para
selecionar um quadrado remoto como alvo, use as setas.

Pressione Enter para confirmar sua escolha.

Dando uma ordem: m�todo alternativo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Um segundo m�todo de dar uma ordem consiste em selecionar um alvo com
Tab (ou as setas) e ent�o apertar Backspace. A ordem padr�o ser� dada.
Por exemplo, um oper�rio com alvo numa mina de ouro ir� explor�-la se
voc� apertar Backspace.

Dando uma ordem: usando atalhos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para dar uma ordem com um atalho, pressione Alt + A. Uma mensagem vai
falar a lista de atalhos dispon�veis para a unidade controlada.
Pressione o atalho e a ordem ser� executada imediatamente, a menos que
um alvo necessite ser selecionado.

Examinando a situa��o
^^^^^^^^^^^^^^^^^^^^^^^^^

Para saber que unidade (ou grupo) voc� controla, pressione Espa�o.
Ademais, voc� se mover� ao quadrado ocupado pela unidade (ou pelo l�der do grupo).

Para saber quanto de ouro voc� tem, pressione Z. Pressione X para a madeira e C para a comida.

Para saber a vida da unidade selecionada, pressione V.

Para examinar novamente um objeto selecionado com Tab, pressione Control.

Dando uma ordem sem cancelar as anteriores (enfileirando comandos)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Segure Shift antes de apertar enter para confirmar a ordem.

Tamb�m funciona para ordens padr�es, use Shift antes de apertar
Backspace.

Pressione Espa�o para verificar se a unidade tem v�rias ordens para executar.

Aqui est� uma lista de situa��es que enfileirar ordens pode ajudar:

- Exemplo 1: voc� quer mandar um oper�ri ir em todos os quadrados iniciais (para saber onde o inimigo est�). Mova o cursor para um dos quadrados iniciais e pressione
  Shift Backspace. Repita para cada quadrado inicial
  e o oper�rio ir� se mover para um quadrado e em seguida ir� para outro.

- Exemplo 2: voc� quer que um oper�rio explore v�rios recursos. Selecione um recurso como alvo, pressione Shift + Backspace. Repita para cada recurso. Quando um
  recurso se esgotar, o oper�rio ir� explorar os pr�ximos de sua lista de ordens.


Dando uma ordem imperativa
^^^^^^^^^^^^^^^^^^^^^^^^^^

Se voc� segurar o Control antes de pressionar Enter ou Backspace, a
ordem vai ser imperativa.

Unidades com uma ordem imperativa tendem a ignorar tudo que n�o �
relacionado � ordem. Se elas tiverem que ir em algum lugar e encontrarem
unidades inimigas, elas v�o simplesmente ignor�-las.
Isso � arriscado na maioria das vezes mas em alguns casos pode ser �til,
por exemplo para focar-se num alvo muito importante.

Aqui est�o algumas situa��es em que um comando imperativo pode ser �til:

- Exemplo 1: voc� quer que suas unidades ataquem uma constru��o ou unidade inimiga espec�fica e ignorarem o resto. Selecione o alvo e aperte Control Backspace.
- Exemplo 2: voc� quer que suas unidades saiam de um quadrado e ignorem o inimigo. Selecione outro quadrado e pressione Control Backspace.

Voc� pode enfileirar ordens imperativas tamb�m. Segure Control + Shift
ao inv�s de Shift.

Atacando uma unidade amiga
^^^^^^^^^^^^^^^^^^^^^^^^^^

Selecione a unidade e pressione Shift Backspace: as unidades v�o atacar
o alvo.

Exce��o: se o alvo for uma constru��o danificada (ou uma unidade
repar�vel como a catapulta) e voc� controlar oper�rios, eles v�o reparar o alvo.

Bloqueando uma sa�da
^^^^^^^^^^^^^^^^^^^^

Introduzido na vers�o 1.2 alpha 10.

Para bloquear uma sa�da (caminho, ponte), voc� pode fazer qualquer uma dessas alternativas:
- ordenar uma unidade (ou v�rias) a bloquear a sa�da (dando a ordem "bloquear" ou usando back space com a sa�da como alvo);
- construir uma muralha nela;
- construir qualquer outra constru��o nela.

Uma unidade ou um port�o deixar� unidades amigas passarem.

Modo zoom (experimental)
^^^^^^^^^^^^^^^^^^^^^^^^

Novo na vers�o 1.2 alpha 10.

F8: entrar ou sair do modo zoom. Escape tamb�m sai.

O quadrado � dividido em 3 quadrados menores de 3 x 3. Um quadrado
com zoom pode ser usado como um alvo de uma ordem (ir a, essencialmente).

Grupos de controle
^^^^^^^^^^^^^^^^^^^^^^^^^

Novo em 1.2 alpha 10.

Control + 6, 7, 8 ou 9: configura o grupo 6, 7, 8 ou 9 com as unidades
controladas atualmente

Shift + 6, 7, 8 ou 9: adiciona as unidades controladas atualmente ao grupo 6, 7, 8 ou 9

6, 7, 8 ou 9: recupera o grupo 6, 7, 8 ou 9

Nos menus
^^^^^^^^^^^^

As setas funcionam tamb�m: Cima e Baixo para selecionar, Direita confirma, Esquerda cancela.

Pressione qualquer letra para selecionar o pr�ximo item come�ando com essa letra.
Pressione Shift + qualquer letra para selecionar o item anterior come�ando com essa letra.

Outros comandos
^^^^^^^^^^^^^^^

F5 e F6: mensagem anterior / pr�xima no hist�rico.
Alt: interrompe a frase atual.

Para sair de uma partida ou acessar o menu, pressione F10. Alt F4 e Control C fazem o mesmo.

Control + Espa�o: faz o jogo entrar no modo em primeira pessoa. Escape: volta para o modo mapa.

Home / End, + / - do teclado num�rico: aumenta / diminui o volume geral do som.
Control Home / End, control + / - do teclado num�rico: aumenta / diminui o volume relativo da voz.

F3: fala o tempo de jogo.
Control F3: sino em minuto ligado / desligado (desligado por padr�o)

Control + Tab seleciona apenas bosques, minas de ouro, terrenos, e
alvos repar�veis ou constru�veis (constru��es danificadas, terrenos de constru��o, catapultas danificadas...).

Alt + R resseleciona a ordem dada anteriormente. �til para recrutar a mesma unidade ou construir o mesmo tipo de constru��o v�rias vezes.
Alt + G resseleciona a ordem dada anteriormente e a valida se n�o
precisar de alvo. Por exemplo, para recrutar 5 arqueiros adicionais,
pressione Alt + G 5 vezes.
Desde o SoundRTS 1.1 alpha 3, Alt + A faz a mesma coisa que Alt + G.

Ap�strofo (a tecla a baixo do Escape): comandos de console (apenas no modo offline).
No momento os comandos �teis s�o apenas add_units (para obter unidades
ou constru��es instantaneamente)
e victory (para ganhar, por exemplo para passar um cap�tulo). Exemplo
do comando "add_units": "add_units a1 100 archer". Novo no SoundRTS 1.2 alpha 9.

4. Jogos multijogador
---------------------

4.1 Iniciando um jogo multijogador
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Selecione multijogador e depois escolher o servidor numa lista.

Num servidor p�blico, voc� poder� organizar um jogo.

Dica: enquanto voc� estiver esperando por jogadores, voc� pode executar
SoundRTS uma segunda vez para jogar offline. Quando algu�m aparecer,
pressione F10 para pausar seu jogo e poder come�ar a jogar online.

4.2 Conversando
^^^^^^^^^^^^^^^

Voc� pode conversar na entrada do servidor, na sala de pr�-jogo e
durante a partida. Todavia, o organizador est� temporariamente indispon�vel
durante a sele��o do mapa e da velocidade da partida.

Para conversar com todos da mesma sala, pressione F7, digite a mensagem
e pressione Enter.

Outra op��o seria usar o Skype (ou algum programa similar) se voc� conhece os outros jogadores.

4.3 Jogo em equipe
^^^^^^^^^^^^^^^^^^

As equipes devem ser criadas antes que o jogo inicie. Elas n�o podem ser mudadas durante o jogo.

Jogadores aliados compartilham o conhecimento do mapa, a vit�ria, os
investimentos (novo no SoundRTS 1.2 alpha 9), e suas unidades podem se
ajudar. Um trabalhador pode usar um dep�sito do aliado (o recurso vai
ser adicionado � tropa do trabalhador).

Num jogo de servidor, os computadores n�o s�o aliados por padr�o.

Nota: num jogo offline, os computadores s�o aliados.

Dica: para jogar com um computador como aliado, crie um servidor privado.

4.4 Como fazer com que seu servidor fique acess�vel a outros jogadores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para verificar se seu servidor pode ser acessado fora de sua rede
local, espere algu�m conectar, ou idealmente pergunte a um amigo se ele
pode se conectar de fora. Como uma �ltima tentativa,
voc� pode tentar usar um servi�o de teste de portas ( pesquise "port forwarding tester"
por exemplo). Tenha cuidado: eu n�o garanto que esse tipo de site n�o
seja malicioso!
O site n�o deve solicitar que voc� instale alguma ferramenta, por exemplo.

Em muitos casos voc� ter� que configurar seu roteador para que ele envie
as conex�es que entram no seu servidor na porta 2500 para seu computador da rede local.

Voc� poder� tamb�m ter que configurar o DHCP para que seu servidor tenha
sempre o
mesmo endere�o IP na rede local.

Se voc� est� usando um firewall, voc� tamb�m ter� que liberar a porta 2500 nele.

Sobre os servidores padr�o (o que n�o � executado pelo menu do
jogo):mesmo que seu servidor seja acess�vel de fora, em alguns casos
voc� n�o conseguir� conectar nele de sua rede local usando a lista de
servidores. A op��o "Digite o endere�o IP do servidor" funciona em
muitos casos, mas ela n�o significa que o servidor � acess�vel de fora.

4.5 Como baixar um mapa de um servidor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Jogue uma partida com o mapa que voc� quer baixar. Antes que o jogo
inicie, o mapa aparecer� na `pasta tempor�ria`_ e ficar� l� at� que
outro mapa o sobrescreva. Dependendo do formato do mapa, pode ser um
arquivo de texto chamado recent_map.txt ou uma pasta chamada recent_map.

5. Elementos do jogo
--------------------

Comida
^^^^^^

O recrutamento de uma nova unidade s� pode acontecer se o jogador tiver
comida suficiente. Se algumas fazendas forem destru�das ou novas
unidades forem obtidas sem recrutar, e
a comida vir a ser insuficiente, as unidades v�o ser mantidas sem
nenhum problema. Entretanto, nenhum recrutamento vai ser permitido at�
que o jogador consiga mais comida.

Investimento de tecnologia
^^^^^^^^^^^^^^^^^^^^^^^^^^

Os investimentos se aplicam � todas as unidades do jogador (atuais e futuras).

Unidades voadoras
^^^^^^^^^^^^^^^^^

Desde o SoundRTS 1.1, as unidades a�reas voam em linha reta at� o
objetivo, ignorando o caminho terrestre.

Unidades invis�veis e detectoras
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para se defender de unidades invis�veis, existem pelo menos 3 maneiras.

- consiga uma unidade detectora (ou lance uma magia de detec��o) e ataque a unidade invis�vel;
- Use uma magia de destrui��o de �rea no quadrado que cont�m a unidade;
- ignore a unidade invis�vel e destrua as constru��es rapidamente o suficiente.

6. Mais detalhes para personaliza��o
------------------------------------

SoundRTS.ini
^^^^^^^^^^^^

Esse arquivo se localiza na `Pasta do usu�rio`_ . Ele cont�m v�rios
par�metros sobre como o jogo trabalha. Quando SoundRTS inicia, se esse
arquivo contiver um erro, um novo ser� gerado tentando se recuperar a maior
quantidade de par�metros do arquivo original.

Op��es da linha de comando
^^^^^^^^^^^^^^^^^^^^^^^^^^

Pela linha de comando, a op��o -h d� a lista de op��es dispon�veis.

A op��o --mods sobrescreve a linha "mods =" do SoundRTS.ini_ . Por
exemplo, para iniciar SoundRTS com o soundpack e o mod orc: soundrts.exe --mods=soundpack,orc

Pacote de sons
^^^^^^^^^^^^^^

SoundRTS vem com um mod chamado "soundpack" contendo sons alternativos.
Para ativar esse mod, no SoundRTS.ini_ substitua a linha "mods =" com "mods = soundpack".
Ent�o, reinicie o jogo para que as altera��es tenham efeito.

SAPI 5 (Windows)
^^^^^^^^^^^^^^^^

No `Soundrts.ini`_, se "srapi = 0", a voz padr�o SAPI 5 ser� usada diretamente.

Par�metro srapi para Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No `Soundrts.ini`_, coloque "srapi = 1" para usar um leitor de tela (atrav�s de ScreenReaderAPI).

Par�metro srapi_wait para Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Como eu n�o consegui achar uma maneira de saber quando um leitor de
tela para de falar no Windows, eu tive que calcular a dura��o de cada mensagem.
Um par�metro adicional chamado "srapi_wait" determina quanto tempo SoundRTS vai esperar at� que ele envie outra mensagem ao leitor.
Com "srapi_wait = .1" e uma mensagem de 10 caracteres, SoundRTS vai esperar por .1 * 10 = 1 segundo.

Aumente o valor de "srapi_wait" se algumas mensagens est�o sendo interrompidas pela pr�xima.
Diminua o valor de "srapi_wait" se o jogo est� silenciando muito entre uma mensagem e outra.

Pasta tempor�ria
^^^^^^^^^^^^^^^^

A pasta tempor�ria cont�m os logs e o mapa jogado pela �ltima vez.

A pasta tempor�ria est� localizada na `pasta do usu�rio`_ com o nome de "tmp".

Pasta do usu�rio
^^^^^^^^^^^^^^^^

A pasta do usu�rio cont�m as configura��es do jogo, os mapas
personalizados e mods, e a pasta tempor�ria.
Uma forma f�cil de achar a pasta do usu�rio � abr�-la pelo menu de
op��es.

Se a pasta principal do jogo tiver uma pasta denominada "user", ent�o essa pasta vai ser a pasta do usu�rio.
Se a pasta "user" n�o existir, a pasta do usu�rio vai ser localizada dependendo do sistema operacional:

- Windows XP: "C:\\Documents and settings\\seu_nome_de_usuario\\Dados de aplicativos\\SoundRTS unstable"
- Linux: "home/seu_nome_de_usuario/.SoundRTS unstable"

Como criar uma vers�o port�til do SoundRTS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Desde o SoundRTS 1.0 beta 10 p, � poss�vel ter todos os arquivos do jogo (log,
configura��o, mapas personalizados...) dentro da pasta do jogo. Seguem
as instru��es de como proceder para fazer isso:

- installe o SoundRTS
- Windows: copie a `pasta do jogo` de "Arquivos de programas" para
  uma pasta que voc� pode escrever (a �rea de trabalho, um drive USB, etc)

- na nova pasta do SoundRTS, crie uma pasta chamada "user". "user" pode
  ser uma c�pia de uma `pasta do usu�rio`_ existente (por�m a vers�o tem que ser a mesma).

- Windows: para jogar, execute "soundrts.exe".


Como mudar a velocidade padr�o de jogos offline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encontre SoundRTS.ini_ na `pasta do usu�rio`_ e modifique a linha "speed = ...". Use um n�mero inteiro.

Mudando algumas teclas do jogo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Desde o SoundRTS 1.1, o layout de teclado est� definido num arquivo
chamado "bindings.txt" na `pasta do jogo`.

Criando um app para Mac
^^^^^^^^^^^^^^^^^^^^^^^

Se voc� conseguiu instalar a vers�o multiplataforma para o Mac, talvez
voc� possa criar um app para facilitar a instala��o para outros jogadores.
Seguem algumas dicas. Use py2app.
Voc� n�o precisa do c�digo. Por exemplo, crie um arquivo chamado soundrts_launcher.py
contendo essa linha: "import soundrts".
Voc� tamb�m pode criar um arquivo chamado server_launcher.py com a linha: "import server".
Verifique se executar "soundrts_launcher.py" funciona.

Usando o instalador do Windows com uma conta limitada (Windows XP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Voc� pode usar uma conta limitada para instalar SoundRTS. Escolha uma
pasta diferente da "Arquivos de programas".

Ainda que voc� instale SoundRTS com uma conta administradora, voc� pode jogar usando uma conta limitada.

O que faz um mapa multijogador ser oficial?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mapas oficiais n�o tocam nenhum som antes de seu t�tulo. Os mapas
multijogador oficiais s�o listados em cfg/official_maps.txt com
checksums para ter a certeza de que eles n�o foram modificados.

Como selecionar um idioma diferente?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Se cfg/language.txt estar vazio, o programa selecionar� automaticamente o idioma do sistema.
Para selecionar um idioma espec�fico, digite o c�digo do idioma em cfg/language.txt,
por exemplo "en", "fr-ca", "pt" ou "pt-BR".
Verifique a pasta res para saber que c�digos de idioma est�o inclu�dos.

7. Cr�ditos
-----------

Nota: essa lista n�o � exaustiva. Obrigado a todos que ajudaram!

O jogo foi escrito por SoundMUD (soundmud@gmail.com).

Descoberta da comunidade franca de jogos acess�veis de �udio, e ideias iniciais: Sabine Gorecki.
In�meros testes e encourajamentos durante o primeiro per�odo do SoundMUD: Alex.
Primeiro teste do SoundMUD no Linux: Miguel.
Relan�amento do projeto do SoundMUD, encorajamentos durante o segundo
per�odo do SoundMUD para completar o jogo de estrat�gia, e in�meros
testes: Louis-Rock Lampron et Martin Morin.

Tradu��o em Ingl�s: SoundMUD.
Tradu��o em Alem�o: Alexander Westphal from Gameport.
Tradu��o em Italiano: Gabriel Battaglia.
Tradu��o em Espanhol: Alan.

Melhoras da voz em ingl�s e sons: Bryan Smart.

Mapa multijogador 101 - fronteira: Bryan Smart.

Notas finais do tradutor

Gostaria de agradecer a todo o pessoal da BGB Blind Games Brasil, que
traduziu o jogo at� 2013, que foi quando eu comecei a traduzir. Voc�s
merecem. Sem voc�s eu nunca teria conhecido esse jogo, nem o teria
traduzido como fiz agora. Obrigado!
