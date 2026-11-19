# Captain Tsubasa III — Tradução PT-BR

Tradução independente de **Captain Tsubasa III: Koutei no Chousen** (Super Famicom) para português brasileiro.

## Versão para testes: etapa 356
Esta versão acrescenta o logotipo **CAPTAIN TSUBASA** em letras latinas na tela de título, preservando o numeral III, o subtítulo **O DESAFIO DO IMPERADOR** e a tradução acumulada da RC1.

**Estado:** experimental, para revisão jogando. A campanha completa e a revisão semântica dos diálogos ainda não foram concluídas.

## Instalação
1. Utilize sua própria cópia da ROM japonesa original **sem cabeçalho**, com SHA-256:
   `6a299b99e0a55aec6669930dc622037d82d297e875630273c6cd6f05438aa3e6`
2. Faça backup da ROM.
3. Aplique `patches/CT3_356_PTBR_LOGOTIPO.ips` **diretamente na ROM japonesa original**. Não aplique sobre a RC1 ou outra ROM modificada.
4. Alternativamente, utilize `scripts/aplicar_ct3_356.py`, que verifica os hashes.
5. Inicie um jogo novo para revisar. Estados antigos podem conservar gráficos anteriores.

SHA-256 esperado da ROM modificada:
`b302f1f3268da2ed2887b3eff5b532f8794fc678b9af42dc1110a04d16213a8c`

## Documentação
- `docs/LEIA_ME_ETAPA356.md`: detalhes da versão e instalação.
- `docs/RELATORIO_ETAPA356.md`: investigação gráfica.
- `docs/VALIDACAO356.json`: resultados de testes automatizados relatados pelo checkpoint.
- `docs/PREVIA.png` e `docs/COMPARACAO.png`: imagens de referência.

## Direitos autorais
Não distribuímos ROMs comerciais. Captain Tsubasa e os recursos originais pertencem aos respectivos titulares. Projeto independente e não oficial.
