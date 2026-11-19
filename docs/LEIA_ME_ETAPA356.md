# Captain Tsubasa III PT-BR — logotipo em letras latinas

Versão 356, baseada na RC1. O painel japonês da tela de título agora mostra CAPTAIN TSUBASA na vertical, mantendo o III original e a paleta dourada. O nome do jogo foi preservado; não foi substituído por outro nome de personagem ou franquia. A tradução acumulada, os menus, o subtítulo O DESAFIO DO IMPERADOR e a placa NO AR permanecem.

## Usar esta versão

CT3_356_PTBR_LOGOTIPO.sfc é a ROM pronta. CT3_356_PTBR_LOGOTIPO.ips é o patch cumulativo para a japonesa original sem cabeçalho; não aplicar por cima da RC1 nem de outra tradução.

Origem: 1.048.576 bytes; SHA-256:
6a299b99e0a55aec6669930dc622037d82d297e875630273c6cd6f05438aa3e6

Resultado: 2.097.152 bytes; SHA-256:
b302f1f3268da2ed2887b3eff5b532f8794fc678b9af42dc1110a04d16213a8c

Aplicador opcional, Python 3, sem dependências:

python aplicar_ct3_356.py "sua_ROM_japonesa.sfc"

O script confere a origem, o patch e a saída; aceita também a mesma origem com 512 bytes de cabeçalho de copiador, removidos somente na saída. A origem e destinos diferentes já existentes são preservados.

Reinicie o jogo para conferir o título. Um estado de emulador salvo antes da alteração pode conservar o logotipo antigo na memória gráfica.

## Verificação

No Mesen 2, 32 capturas pareadas com a RC1, com quatro capturas de exibição do logotipo alterado: somente os 68 tiles previstos e os pixels do painel superior mudaram. O III, personagem, menus, subtítulo, créditos e todos os outros pixels dessas capturas permanecem iguais. Estado PPU, mapas, paletas, código, fonte e bancos de tradução não foram alterados.

Esta alteração não acrescenta cobertura da campanha nem revisão semântica dos diálogos. Permanecem os limites documentados na RC1. O checkpoint completo conserva a RC1, os scripts e os relatórios.
