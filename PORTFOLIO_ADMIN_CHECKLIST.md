# Portfolio — reta final

Este arquivo registra apenas o que ainda depende de configuração administrativa externa. O código e a organização dos projetos principais já foram migrados para seus repositórios definitivos.

## Concluído

- `berger33/chs-recruta` criado e preenchido com o backend Python/FastAPI;
- CI do CHS executando no repositório próprio;
- staging `portfolio/chs-recruta-python/` removido do repositório de perfil;
- workflow antiga do staging removida;
- perfil aponta diretamente para `berger33/chs-recruta`;
- `berger33/Projeto` renomeado para `berger33/aurora-document-rag` e links do perfil/README atualizados;
- badge de CI da Aurora atualizado para o slug definitivo;
- LeadFlow evidence-first mesclado na `main`, com Behavior Evals e Docker smoke de primeira instalação validados;
- healthcheck WAHA alinhado à configuração atual e importação n8n compatível com PostgreSQL;
- Indoor Grow com updates de `@types/react-dom` e `@types/react` incorporados, lockfile e SBOM determinístico sincronizados;
- configuração do Dependabot do Indoor Grow corrigida para não solicitar labels inexistentes;
- Quality Gate do Indoor Grow verde na `main` após as correções;
- roadmap do CHS reformulado como evoluções futuras fora do escopo atual, evitando confundir melhoria opcional com requisito pendente;
- auditoria dos quatro projetos principais sem PRs abertas, `TODO` ou `FIXME` pendentes no código indexado;
- ordem de apresentação no README: CHS Recruta, LeadFlow, Indoor Grow Automation e Aurora Document RAG;
- PostgreSQL persistente do CHS provisionado separadamente para produção.

## Pendências administrativas confirmadas

- excluir o repositório vazio duplicado `berger33/berger33-chs-recruta`;
- aplicar descriptions, topics e pins abaixo;
- melhorar a description do repositório de perfil `berger33/berger33` (atualmente genérica);
- só definir Homepage do CHS depois de um backend público passar no healthcheck externo.

## Metadata recomendada

### CHS Recruta

Descrição:

> Recruiting system built with Python, FastAPI, PostgreSQL, RBAC, audit logs, tests and Docker.

Topics:

`python` · `fastapi` · `postgresql` · `sqlalchemy` · `recruitment` · `hr-tech` · `pytest` · `docker`

### Aurora Document RAG

Descrição:

> Document-grounded RAG backend with FastAPI, Ollama, vector retrieval, citations, evals and Docker.

Topics:

`python` · `fastapi` · `rag` · `ollama` · `information-retrieval` · `pytest` · `docker` · `artificial-intelligence`

### LeadFlow Local First

Descrição:

> Local-first AI automation with n8n, Ollama, Gmail, Calendar, WhatsApp, human approval and Docker smoke tests.

Topics:

`n8n` · `ollama` · `automation` · `docker` · `ai-agents` · `whatsapp` · `gmail` · `human-in-the-loop` · `local-first`

### Indoor Grow Automation

Descrição:

> Local-first IoT automation platform with FastAPI, PostgreSQL, MQTT, React and ESP32 firmware.

Topics:

`python` · `fastapi` · `postgresql` · `mqtt` · `react` · `esp32` · `iot` · `docker`

### Perfil (`berger33/berger33`)

Descrição sugerida:

> Developer portfolio focused on Python backend, FastAPI, PostgreSQL, Docker, applied AI and automation.

## Pins recomendados

1. `chs-recruta`
2. `leadflow-local-first`
3. `indoor-grow-automation`
4. `aurora-document-rag`

O repositório especial `berger33/berger33` continua servindo o README do perfil e não precisa ocupar um pin de projeto.

## Backend público do CHS

Só publicar uma URL como **Live App** quando os três critérios abaixo forem confirmados de fora da plataforma:

1. `/health` responde com sucesso;
2. `/docs` abre a documentação OpenAPI;
3. a aplicação consegue ler/escrever no PostgreSQL persistente.

A integração Vercel está autenticada no time correto, mas na auditoria de 26/08/2026 continuou retornando zero projetos. Portanto, não há deployment verificável por essa integração neste momento e nenhuma URL deve ser anunciada como produção.

Depois da validação, usar a URL pública como Homepage do repositório e adicionar links de **Live App** e **OpenAPI** ao README. Não apresentar deployment não validado ou demo estática como backend ativo.

## Critério para acabamento

Priorizar, nesta ordem:

1. aplicação online validada;
2. API/OpenAPI;
3. CI passando;
4. código e testes;
5. arquitetura e documentação;
6. metadata/topics/pins;
7. badges e gráficos apenas como informação secundária.
