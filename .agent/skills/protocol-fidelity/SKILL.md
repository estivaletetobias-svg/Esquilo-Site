---
name: protocol-fidelity-rule
trigger: always_on
---

# REGRA INTERNA: FIDELIDADE TOTAL EM PROTOCOLOS DE CLIENTES

## ⛔ PROIBIDO — NUNCA FAÇA ISSO

1. **NUNCA resuma, condense ou mescle seções** do material original do protocolo.
2. **NUNCA adicione conteúdo não fornecido** pelo usuário (ingredientes, alimentos, observações, etc).
3. **NUNCA presuma que uma seção "já está lá"** — verifique com grep antes de confirmar.
4. **NUNCA construa o HTML de memória** — leia o `.md` completo antes de escrever uma linha de HTML.

---

## ✅ PROCESSO OBRIGATÓRIO PARA CADA PROTOCOLO HTML

### PASSO 1 — LEIA O .MD COMPLETO
Antes de escrever qualquer HTML, leia o arquivo `.md` do protocolo **na íntegra** usando `view_file`.

### PASSO 2 — CRIE UM ÍNDICE DE SEÇÕES
Liste mentalmente (ou em comentário) TODAS as seções encontradas no `.md`:

```
Exemplo para protocolo Retatrutide:
[ ] Apresentação
[ ] Análise da Caneta
[ ] Conversão Estratégica (tabela de cliques)
[ ] Princípio Fundamental — Menor Dose Eficaz
[ ] Regra de Ouro (2,5mg / 3mg / critérios de subida)
[ ] Estrutura do Protocolo (tabela master)
[ ] Fase 1 — objetivos + benefícios da adaptação lenta
[ ] Fase 2 — objetivos
[ ] Fase 3 — objetivos + OBSERVAÇÃO para progressão a 4mg
[ ] Ajuste Final da Caneta (tabela Sem 9-12 / Sem 13-16)
[ ] Tabela Utilização Final Ajustada + Obs + desmame
[ ] Local de Aplicação
[ ] Rodízio (tabela por semana)
[ ] Estratégia Nutricional — Proteína (com objetivos)
[ ] Carboidratos (lista priorizar + quando ingerir)
[ ] Gorduras (lista priorizar)
[ ] Hidratação (ml/kg + exemplo)
[ ] Vitaminas e Minerais (tabela completa)
[ ] Sugestão Alimentar — 4 refeições com 3 opções cada
[ ] Sono e Recuperação (objetivo + lista de benefícios)
[ ] Consideração Final (frase + lista de 6 benefícios)
```

### PASSO 3 — MAPEIE CADA SEÇÃO PARA UM CARD HTML
Cada seção do `.md` = pelo menos um card ou bloco no HTML. Nenhuma seção pode ser "absorvida" por outra.

### PASSO 4 — VERIFIQUE ANTES DE FAZER COMMIT
Execute grep para confirmar que palavras-chave únicas de cada seção principal existem no HTML:
```bash
grep -n "NÃO HÁ NECESSIDADE" protocolo-*.html
grep -n "AJUSTE FINAL" protocolo-*.html
grep -n "SOMENTE se" protocolo-*.html
```

### PASSO 5 — SÓ ENTÃO FAÇA O COMMIT

---

## REGRA DE FIDELIDADE DE CONTEÚDO

> **O HTML deve ser um espelho fiel do `.md`. Se está no `.md`, ESTÁ no HTML. Se não está no `.md`, NÃO COLOQUE no HTML.**

### Proibições específicas:
- Não trocar "patinho" por "patinho moído" (não está no original)
- Não adicionar "nozes" e "sementes" se não estão na lista original
- Não criar lista "EVITAR" se o original não tem
- Não resumir lista de objetivos de 5 items em 1 frase
- Não mesclar a observação da Fase 3 (progressão) com a observação do desmame (Fase 4)

---

## CHECKLIST FINAL (ANTES DE CADA COMMIT DE PROTOCOLO)

- [ ] Cada seção do `.md` tem correspondência no HTML?
- [ ] Nenhum conteúdo foi inventado ou adicionado?
- [ ] As tabelas estão completas (todas as colunas e linhas)?
- [ ] As listas de objetivos por fase estão completas (sem resumo)?
- [ ] As 3 opções de cada refeição estão presentes?
- [ ] O Princípio Fundamental tem as Regras de Ouro?
- [ ] A seção AJUSTE FINAL está presente?
- [ ] O rodízio tem a tabela Semana x Local?
- [ ] A Consideração Final tem os 6 bullets?
