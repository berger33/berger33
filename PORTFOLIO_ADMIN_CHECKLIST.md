# Portfolio — ajustes administrativos pendentes

As mudanças abaixo dependem de operações administrativas do GitHub que não estão disponíveis na integração usada para esta refatoração. O código, READMEs e configurações correspondentes já foram preparados em branches separadas.

## 1. Criar repositório do CHS

Criar:

`berger33/chs-recruta`

Descrição sugerida:

> Recruiting system built with Python, FastAPI, PostgreSQL, RBAC, audit logs, tests and Docker.

Topics:

`python` · `fastapi` · `postgresql` · `sqlalchemy` · `recruitment` · `hr-tech` · `pytest` · `docker`

Depois, mover o conteúdo de `portfolio/chs-recruta-python/` para a raiz do novo repositório, preservando histórico por uma migração/commit claramente documentado.

## 2. Renomear Aurora

Renomear:

`berger33/Projeto` → `berger33/aurora-document-rag`

Descrição sugerida:

> Document-grounded RAG backend with FastAPI, Ollama, vector retrieval, citations, evals and Docker.

Topics:

`python` · `fastapi` · `rag` · `ollama` · `information-retrieval` · `pytest` · `docker` · `artificial-intelligence`

## 3. LeadFlow metadata

Descrição sugerida:

> Local-first AI automation with n8n, Ollama, Gmail, Calendar, WhatsApp, human approval and Docker smoke tests.

Topics:

`n8n` · `ollama` · `automation` · `docker` · `ai-agents` · `whatsapp` · `gmail` · `human-in-the-loop` · `local-first`

## 4. Indoor Grow metadata

Descrição sugerida:

> Local-first IoT automation platform with FastAPI, PostgreSQL, MQTT, React and ESP32 firmware.

Topics:

`python` · `fastapi` · `postgresql` · `mqtt` · `react` · `esp32` · `iot` · `docker`

## 5. Projetos fixados no perfil

Ordem recomendada:

1. `chs-recruta`
2. `leadflow-local-first`
3. `indoor-grow-automation`
4. `aurora-document-rag`

O repositório especial `berger33/berger33` continua servindo o README do perfil, mas não precisa competir como projeto de portfólio.

## 6. Backend público

A prioridade para deploy é o `chs-recruta`, porque ele demonstra diretamente FastAPI + banco relacional. O staging já contém `Dockerfile`, `docker-compose.yml`, `/health` e `render.yaml`.

Depois do deploy real:

- adicionar a URL pública como Homepage do repositório;
- incluir links separados para **Live App** e **OpenAPI `/docs`**;
- confirmar health check e banco antes de anunciar o deploy no README;
- nunca usar uma demo estática como evidência de backend ativo.

## 7. Critério para badges e gráficos

Não adicionar novos badges decorativos. Priorizar, nesta ordem:

1. aplicação online;
2. API/OpenAPI;
3. CI passando;
4. código e testes;
5. arquitetura;
6. formação/certificações;
7. gráficos de atividade/linguagens apenas como informação secundária.
