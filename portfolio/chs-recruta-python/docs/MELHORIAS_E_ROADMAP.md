# Melhorias e roadmap — CHS Recruta

Este arquivo separa o que **já está implementado** do que vale evoluir para tornar o produto tecnicamente mais robusto e mais útil para RH. A prioridade é melhorar o sistema sem criar automações opacas que tomem decisões de contratação no lugar de pessoas.

## Backend — prioridades

### P0 — qualidade de produção

1. **Alembic para migrations** — substituir `create_all` como mecanismo de evolução do schema e versionar mudanças de banco.
2. **PostgreSQL no CI** — executar testes de integração contra o mesmo banco usado em deploy, além dos testes rápidos com SQLite.
3. **Paginação, filtros e ordenação server-side** — candidatos, vagas e auditoria não devem carregar toda a tabela em memória.
4. **Soft delete + restauração** — candidatos/vagas importantes devem ser arquivados, não apagados fisicamente por padrão.
5. **Constraints e índices** — revisar unicidade, FKs, índices compostos e regras de integridade no banco.
6. **Hardening de autenticação/RBAC** — rotação/revogação de sessões, política de senha, bloqueio progressivo de login, recuperação segura de conta e testes de autorização por endpoint.
7. **Logs estruturados + request ID** — permitir correlacionar erro, usuário, endpoint e operação sem armazenar dados pessoais desnecessários.
8. **Backups PostgreSQL** — política automática de backup, retenção e teste periódico de restauração.

### P1 — produtividade e integração

- importação CSV/XLSX com preview e erro por linha;
- bulk actions com transação;
- filas/jobs para importações e relatórios pesados;
- webhooks para integrações;
- OpenTelemetry/Sentry para tracing e erros;
- cache apenas para consultas realmente custosas;
- idempotency keys em operações externas;
- API versionada quando houver consumidores externos;
- testes de carga básicos para listagem/busca.

## Frontend — melhorias

### Organização

A interface atual é propositalmente simples e sem framework. Em uma evolução maior, vale usar **React + TypeScript + Vite** ou manter Vanilla JS modular com build, desde que a complexidade justifique.

### Experiência de RH

- filtros persistentes por período, recrutador, vaga, cidade, origem e status;
- tabela paginada server-side;
- seleção em lote com ações seguras;
- Kanban do funil com drag-and-drop e histórico da movimentação;
- página completa do candidato com abas `Dados`, `Processos`, `Entrevistas`, `Comunicações` e `Histórico`;
- validação inline, máscaras e mensagens de erro específicas;
- busca global com atalhos de teclado;
- comandos rápidos para triagem;
- skeleton/loading e empty states;
- design tokens, tema claro/escuro e acessibilidade WCAG 2.2 AA;
- responsividade para notebook, tablet e celular;
- impressão e exportação orientadas a relatórios, não à tela inteira.

## Funcionalidades de RH sugeridas

### Pipeline configurável

Permitir que cada operação defina etapas como:

`Novo → Contato → Triagem → Entrevista RH → Entrevista Técnica → Proposta → Contratado`

Cada transição deve registrar usuário, data/hora e motivo.

### Entrevistas e scorecards

- kits de entrevista por vaga;
- competências e perguntas estruturadas;
- notas por critério com justificativa textual;
- feedback independente de cada entrevistador;
- prazo para feedback;
- histórico imutável após encerramento do processo, salvo correção auditada.

### Agenda e comunicação

- integração com Google/Microsoft Calendar;
- templates de convite, follow-up e retorno;
- histórico de comunicação;
- lembrete de entrevista;
- controle de consentimento e canal preferido;
- aprovação humana antes de envios em lote.

### Talent pools

- pools por profissão/especialidade;
- tags e skills;
- disponibilidade;
- preferência geográfica/remoto;
- certificações com validade;
- data do último contato;
- lembrete para reengajamento.

### Matching explicável

Evoluir o matching atual para combinar:

- profissão;
- skills obrigatórias e desejáveis;
- cidade/remoto;
- disponibilidade;
- certificações;
- senioridade;
- requisitos eliminatórios definidos pela vaga.

O resultado deve mostrar **por que** houve correspondência, permitir override humano e nunca usar atributo sensível ou inferido para ranquear candidatos.

### Gestão de vagas

- templates de vaga;
- headcount e quantidade de posições;
- prioridade;
- data alvo;
- aging da vaga;
- aprovadores;
- centro de custo;
- faixa salarial quando aplicável;
- motivo de fechamento/cancelamento;
- SLA por etapa.

### Analytics úteis

- time-to-hire;
- time-to-fill;
- source of hire;
- taxa de resposta;
- no-show de entrevista;
- conversão por etapa;
- aging de candidatos e vagas;
- carga por recrutador;
- motivos de rejeição;
- eficiência de fontes;
- qualidade de contratação somente quando houver métrica posterior legítima e governada.

Evitar métricas de vaidade e rankings sem contexto.

## LGPD, privacidade e governança

Para uma versão real multiusuário, adicionar:

- política de retenção por tipo de dado;
- anonimização após prazo definido;
- exportação dos dados de um titular;
- trilha de acessos a dados sensíveis;
- minimização de campos coletados;
- segregação por organização/tenant se virar SaaS;
- criptografia de backups;
- controle de acesso por campo para informações sensíveis;
- auditoria append-only para eventos críticos;
- documentação de base legal/processo organizacional fora do código.

## O que não implementar

- IA tomando decisão final de contratação;
- ranking opaco de candidatos;
- inferência de raça, saúde, religião, orientação sexual, personalidade ou outros atributos sensíveis;
- biometria para triagem;
- coleta de dados sem necessidade clara;
- dados reais de candidatos em demos públicas;
- autenticação de produção baseada em `localStorage`;
- regras de negócio duplicadas no frontend;
- automações de comunicação externa sem controles de aprovação e auditoria.

## Sequência recomendada

### Fase 1 — backend profissional

Alembic → PostgreSQL CI → paginação → soft delete → autorização completa → logs estruturados → backups.

### Fase 2 — operação de RH

Pipeline configurável → página de candidato → scorecards → agenda/comunicação → talent pools.

### Fase 3 — analytics e escala

SLA → métricas de recrutamento → importações em lote → jobs assíncronos → observabilidade.

### Fase 4 — inteligência assistiva

Matching explicável → sugestões de busca → sumarização de histórico com fonte → auxílio na redação de comunicações, sempre mantendo decisão e envio sob controle humano.
