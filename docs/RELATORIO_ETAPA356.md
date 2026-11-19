# Etapa 356 — logotipo CAPTAIN TSUBASA III

Atendendo ao pedido de substituir os caracteres japoneses na tela de título, os 136 pixels superiores do painel dourado foram redesenhados com CAPTAIN / TSUBASA em letras latinas verticais. O III original, de 48 pixels de altura, foi preservado byte a byte. As letras usam uma matriz de pixels, preenchimento dourado, brilho e sombra com a paleta original. Não houve geração ou substituição da captura de tela: a alteração foi reinserida nos tiles da própria ROM e capturada no Mesen 2.

A camada BG1 usa mapa VRAM byte 8000 e gráficos em A000. Foram alterados 68 tiles de 4bpp: colunas 4–7, linhas 2–18 do mapa de título, com uma ocorrência por índice nesse mapa. As linhas 19–24, que contêm III, permanecem intactas. Os dados provêm do recurso nativo 053C00–0547FF; cada offset alterado está em CT3_356_PTBR_LOGOTIPO.json. Não usar a primeira ocorrência global de um tile em branco como endereço de origem: havia coincidências binárias em outros bancos. O construtor verifica a igualdade do offset do recurso com o tile efetivamente carregado em VRAM.

A ROM de produção CT3_356_PTBR_LOGOTIPO.sfc contém 1.983 bytes diferentes em relação à RC1, somente nos bitmaps e checksum. SHA-256 b302f1f3268da2ed2887b3eff5b532f8794fc678b9af42dc1110a04d16213a8c. Código, mapas, paletas, fonte compartilhada e todos os bancos expandidos são idênticos à RC1. Original e RC1 foram preservadas.

validate356.py aprovou 32 capturas pareadas de inicializações reais com os mesmos controles. Quatro capturas mostram o logotipo novo; em uma captura estável foi confirmada a presença dos 68 tiles novos completos. Em todos os pares, os pixels fora de x32..63/y15..150 são idênticos; a VRAM só difere nos tiles previstos e seus valores correspondem exatamente aos bitmaps reinseridos. Os estados PPU são iguais. Os seis blocos de linha que formam o numeral III foram conferidos separadamente. O IPS cumulativo reaplicado à original produz exatamente a nova ROM.

Reprodução: python ct3/build356.py; executar run343.py com CT3_HARNESS=studiopath354.lua, LABEL=logo356, casos none e a ROM 356; python ct3/validate356.py. O baseline preservado é graphics354_ptbr. package356.py monta o pacote e valida o aplicador. A construção precisa do mapa de título preservado em evidence/title354_5520_vram.bin, incluído no checkpoint.

Esta etapa é uma alteração visual delimitada, não uma nova certificação de campanha ou dos significados dos diálogos. A candidata anterior permanece recuperável.
