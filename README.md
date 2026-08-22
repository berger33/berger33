# William de Melo Berger

**Inteligência Artificial aplicada | Desenvolvimento Python | Backend | Automação**

Sou estudante de Inteligência Artificial e desenvolvimento de software, com foco em transformar problemas reais em aplicações funcionais. Atualmente concentro meus estudos e projetos em **Python, APIs, agentes de IA, RAG, automação, Docker e boas práticas de engenharia de software**.

Busco oportunidades em **desenvolvimento júnior, Python/backend e aplicações de IA**, onde eu possa contribuir com projetos reais enquanto evoluo tecnicamente em um ambiente profissional.

[LinkedIn](https://www.linkedin.com/in/william-m-berger/) · [Repositórios](https://github.com/berger33?tab=repositories)

---

## Visão rápida

- **Foco atual:** Python, backend e Inteligência Artificial aplicada
- **IA aplicada:** LangChain, RAG, Ollama, agentes, Function Calling e validação multiagente
- **Backend:** FastAPI, APIs REST e organização de serviços
- **Dados:** Pandas, CSV, SQLite, PostgreSQL, processamento e recuperação de informação
- **Automação:** n8n, webhooks, Gmail, Google Calendar, WhatsApp/WAHA e Human-in-the-loop
- **Infraestrutura:** Docker, Docker Compose e fundamentos de deploy em nuvem
- **Qualidade:** Git, GitHub, testes automatizados, smoke tests, CI e documentação técnica
- **Produto / DX:** demos navegáveis, instaladores guiados e onboarding orientado ao usuário
- **Idiomas:** Inglês avançado (C1) e espanhol básico

---

## Formação em destaque

<div align="center">
  <img src="./assets/badge-one-ia-correta.png" width="160" alt="Badge Oracle Next Education - ONE - Inteligência Artificial, Agentes e RAG">
  <br><br>
  <strong>Oracle Next Education (ONE) · Inteligência Artificial · Agentes e RAG</strong>
</div>

A formação ONE complementa meus projetos práticos em IA aplicada, especialmente construção de agentes, recuperação de contexto e soluções baseadas em documentação.

---

## Projetos em destaque

### [Aurora Moda Online — Agente Inteligente - Projeto Oracle Next Education](https://github.com/berger33/Projeto)

**[▶ Abrir demo online](https://htmlpreview.github.io/?https://github.com/berger33/Projeto/blob/main/demo/index.html)** · **[⬇ Baixar projeto](https://github.com/berger33/Projeto/archive/refs/heads/main.zip)** · **[📂 Ver repositório](https://github.com/berger33/Projeto)**

Projeto autoral desenvolvido para resolver um problema real de atendimento em e-commerce. O agente responde perguntas sobre compras, pagamentos, entregas, privacidade e devoluções usando exclusivamente uma base documental em PDF e CSV. A demo pública permite testar o comportamento documental imediatamente no navegador, incluindo fontes e recusa de perguntas fora da base.

**Principais pontos técnicos:**

- Python + FastAPI
- LangChain para processamento documental
- Pandas para leitura de CSV
- PyPDF para leitura de documentos
- recuperação documental com TF-IDF
- respostas fundamentadas com indicação de fontes
- testes automatizados com Pytest
- GitHub Actions para CI
- Docker e Docker Compose
- configuração para OCI Compute e Render

> Este projeto demonstra o ciclo problema → arquitetura → implementação → testes → documentação → preparação para deploy.

### [Sistema Agêntico n8n WhatsApp+Email](https://github.com/berger33/leadflow-local-first)

**[▶ Abrir demo interativa](https://htmlpreview.github.io/?https://github.com/berger33/leadflow-local-first/blob/main/demo/index.html)** · **[⬇ Baixar projeto](https://github.com/berger33/leadflow-local-first/archive/refs/heads/main.zip)** · **[📂 Ver repositório](https://github.com/berger33/leadflow-local-first)**

**Sistema agêntico local-first em versão 2.2**, evoluído a partir do LeadFlow para uma arquitetura centrada em **n8n Advanced AI, Function Calling, LLM local e execução segura de ferramentas reais**. O sistema combina Ollama, n8n, WAHA/WhatsApp, Gmail, Google Calendar e PostgreSQL em um stack Docker reproduzível.

O **Agente Orquestrador** interpreta o pedido e escolhe ferramentas como `ler_email`, `resumir_email`, `apagar_email`, `enviar_whatsapp` e `criar_evento`. Ações críticas entram em **Human-in-the-loop**, pausam em um nó `Wait` e exigem aprovação humana antes do efeito externo.

Depois da execução, um segundo **Agente QA Validador**, sem acesso a ferramentas destrutivas, revisa aderência ao pedido, consistência com resultados observáveis e respeito aos controles de segurança antes da resposta final.

A versão 2.2 também trata instalação como parte do produto: um **assistente visual local e responsivo** coleta em uma única tela o acesso local do n8n, modelos, e-mail de aprovação e, opcionalmente, Google OAuth Client ID/Secret. O bootstrap gera os segredos internos, instala/verifica os serviços, baixa a LLM, cria o proprietário n8n, prepara a credencial Ollama, importa o workflow e configura referências automaticamente. Depois disso, ficam manuais somente os consentimentos que pertencem ao usuário: OAuth do Google e QR Code do WhatsApp.

**Principais pontos técnicos:**

- n8n Advanced AI como orquestrador central;
- Function Calling com cinco contratos de ferramentas;
- LLM local com Ollama/Qwen3;
- segundo agente independente para QA da resposta;
- Human-in-the-loop para ações destrutivas ou de comunicação externa;
- Gmail e Google Calendar via OAuth2;
- integração WhatsApp via WAHA e webhooks;
- PostgreSQL para estado e histórico do n8n;
- audit trail de inputs, tools, parâmetros, resultados e outputs observáveis;
- Docker Compose com interfaces administrativas limitadas a localhost;
- instalador visual profissional servido apenas localmente;
- criação assistida do proprietário n8n sem persistir a senha no instalador;
- configuração automática da credencial Ollama e preparação opcional de Gmail/Calendar;
- bootstrap autorreparável e idempotente;
- GitHub Actions com validação estrutural e smoke test Docker do caminho de primeira instalação.

> O objetivo de entrega é que outra pessoa possa baixar o projeto, abrir o Docker Desktop, executar `INSTALAR_WINDOWS.bat`, preencher uma tela e deixar para o sistema toda a configuração técnica reproduzível.

### [CHS Recruta Portátil — Sistema de recrutamento local-first](portfolio/chs-recruta/ACESSO.md)

**[▶ Abrir demo online](https://htmlpreview.github.io/?https://github.com/berger33/berger33/blob/main/portfolio/chs-recruta/app/CHS-Recruta-Demo.html)** · **[⬇ Baixar versão portátil](https://htmlpreview.github.io/?https://github.com/berger33/berger33/blob/main/portfolio/chs-recruta/app/download.html)** · **[📘 Ver case técnico](portfolio/chs-recruta/README.md)**

**Credenciais da demonstração:** usuário `demo` · senha `demo123` · perfil Administradora.

**Projeto de fim de semana criado para ajudar uma profissional de RH em uma necessidade real.** Transformei um fluxo espalhado entre contatos, vagas e acompanhamento manual em uma aplicação portátil que funciona sem instalação de servidor ou banco externo.

O sistema reúne **dashboard, banco de talentos, vagas, triagem, matching por profissão, funil de contratação, financeiro, relatórios CSV, histórico de auditoria, usuários e permissões, backup/restauração, busca global, perfil com foto e persistência local**.

Também desenvolvi uma camada de experiência de uso que inclui **modo dia/noite, cinco paletas de cor persistentes, layout responsivo, tooltips, feedback por toast, impressão otimizada e adaptação de menus por permissão**.

**Principais pontos técnicos:**

- HTML5 + CSS3 + JavaScript sem framework
- arquitetura local-first com `localStorage` e `sessionStorage`
- autenticação local, hash de senha e bloqueio temporário após tentativas repetidas
- controle de acesso por perfil
- busca com normalização, prefixos e tokens
- normalização de profissões para evitar indicadores fragmentados
- detecção de possíveis candidatos duplicados
- geração de CSV e backup JSON
- auditoria de operações com data, hora e responsável
- redimensionamento e compressão de foto via Canvas API
- responsividade e temas com CSS custom properties

> A demo pública usa dados fictícios. A base operacional original contém dados de terceiros e não foi publicada por privacidade.

---

## Como eu trabalho

Nos projetos que considero de portfólio, procuro demonstrar mais do que código isolado:

1. entendimento do problema;
2. definição de arquitetura simples e justificável;
3. organização clara do repositório;
4. implementação incremental com histórico Git;
5. testes e validação;
6. README que permita outra pessoa executar o projeto;
7. empacotamento, onboarding e preparação para deploy quando aplicável.

---

## Stack que aparece nos meus projetos

| Área | Tecnologias |
| --- | --- |
| Linguagem principal | Python |
| Backend / API | FastAPI, Uvicorn, REST, Webhooks |
| Inteligência Artificial | LangChain, RAG, Ollama, agentes, Function Calling, validação multiagente |
| Dados | Pandas, CSV, PyPDF, SQLite, PostgreSQL, JSON |
| Automação / integração | n8n, WAHA, Gmail, Google Calendar, HTTP APIs, Human-in-the-loop |
| Front-end / produto | HTML5, CSS3, JavaScript, responsive design, setup wizard |
| Persistência local | SQLite, localStorage, sessionStorage, PostgreSQL e volumes Docker |
| Infraestrutura | Docker, Docker Compose, PowerShell |
| Engenharia | Git, GitHub, Pytest, smoke tests, GitHub Actions |

---

## Linguagens utilizadas no GitHub

<p align="center">
  <img src="./assets/languages.svg" width="720" alt="Distribuição automática das linguagens utilizadas nos repositórios públicos autorais de William Berger">
</p>

> Este painel é gerado dentro do próprio repositório por **GitHub Actions**, usando os dados de linguagens detectados pelo GitHub. Ele é atualizado automaticamente, considera repositórios públicos autorais e exclui forks e repositórios arquivados para evitar distorções.

---

## Em desenvolvimento contínuo

Estou aprofundando conhecimentos em:

- arquitetura de software e APIs;
- testes e qualidade de código;
- bancos de dados e SQL;
- deploy e serviços em nuvem;
- aplicações de IA com recuperação de contexto;
- automações e integração entre sistemas.

Também mantenho repositórios de **estudo, exercícios e forks**. Para avaliação de trabalho autoral, recomendo começar pelos projetos destacados acima.

---

## Atividade no GitHub

<p align="center">
  <a href="https://github.com/berger33?tab=overview&from=2026-01-01&to=2026-12-31">
    <img src="https://github-readme-activity-graph.vercel.app/graph?username=berger33&theme=github-compact&hide_border=true&area=true" alt="Gráfico de atividade e commits de William Berger no GitHub">
  </a>
</p>

> O gráfico acima acompanha minha atividade pública no GitHub. O histórico detalhado de cada projeto pode ser consultado diretamente na aba **Commits** dos respectivos repositórios.

---

## Contato profissional

A melhor forma de conhecer minha trajetória, formação, experiência e certificações é pelo meu **[LinkedIn](https://www.linkedin.com/in/william-m-berger/)**.

Estou aberto a conexões, feedback técnico e oportunidades para iniciar ou consolidar minha carreira em desenvolvimento de software.
