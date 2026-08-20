# William de Melo Berger

**Inteligência Artificial aplicada | Desenvolvimento Python | Backend | Automação**

Sou estudante de Inteligência Artificial e desenvolvimento de software, com foco em transformar problemas reais em aplicações funcionais. Atualmente concentro meus estudos e projetos em **Python, APIs, agentes de IA, RAG, automação, Docker e boas práticas de engenharia de software**.

Busco oportunidades em **desenvolvimento júnior, Python/backend e aplicações de IA**, onde eu possa contribuir com projetos reais enquanto evoluo tecnicamente em um ambiente profissional.

[LinkedIn](https://www.linkedin.com/in/william-m-berger/) · [Repositórios](https://github.com/berger33?tab=repositories)

---

## Visão rápida

- **Foco atual:** Python, backend e Inteligência Artificial aplicada
- **IA aplicada:** LangChain, RAG, agentes locais, Ollama e validação multiagente
- **Backend:** FastAPI, APIs REST e organização de serviços
- **Dados:** Pandas, CSV, SQLite, processamento e recuperação de informação
- **Automação:** n8n, webhooks, integrações e tarefas programadas
- **Infraestrutura:** Docker, Docker Compose e fundamentos de deploy em nuvem
- **Qualidade:** Git, GitHub, testes automatizados, CI e documentação técnica
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

Projeto autoral desenvolvido para resolver um problema real de atendimento em e-commerce. O agente responde perguntas sobre compras, pagamentos, entregas, privacidade e devoluções usando exclusivamente uma base documental em PDF e CSV.

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

### [LeadFlow Local-First — Assistente IA no WhatsApp](https://github.com/berger33/leadflow-local-first)

**Assistente pessoal local-first em versão 1.0**, projetado para rodar no computador do usuário e conversar pelo WhatsApp sem depender de API paga de LLM. O sistema combina **Ollama, FastAPI, WAHA, n8n, pesquisa web e Gmail** em uma arquitetura Docker reproduzível.

A resposta passa por **dois agentes independentes**: o primeiro interpreta e responde; o segundo recebe a pergunta original, a resposta preliminar e as fontes utilizadas para verificar se a intenção foi compreendida, se o conteúdo está aderente ao pedido e se afirmações atuais têm suporte. Quando encontra problemas, o validador devolve uma versão corrigida antes do envio ao WhatsApp.

**Principais pontos técnicos:**

- LLM executada localmente com Ollama;
- integração bidirecional com WhatsApp via WAHA e webhooks;
- FastAPI como camada de aplicação testável entre WhatsApp, n8n e LLM;
- pesquisa atual na internet via metabuscadores, com fontes anexadas ao contexto;
- arquitetura dual-agent para revisão antes da resposta final;
- memória curta e persistente por conversa com SQLite;
- n8n para agendamento de pesquisas e automações;
- workflow diário de **10 notícias quentes de tecnologia** com relatório HTML;
- envio automático de relatório por Gmail após autorização do usuário;
- resumo diário opcional também pelo WhatsApp;
- Docker Compose com Ollama, WAHA, n8n e API em um único stack;
- instalador/inicializador Windows, diagnóstico, documentação, testes e GitHub Actions.

> O projeto foi estruturado para que outra pessoa possa baixar, configurar seus próprios acessos e executar o stack localmente com Docker Desktop.

### [CHS Recruta Portátil — Sistema de recrutamento local-first](portfolio/chs-recruta/ACESSO.md)

**Projeto de fim de semana criado para ajudar uma profissional de RH em uma necessidade real.** Transformei um fluxo espalhado entre contatos, vagas e acompanhamento manual em uma aplicação portátil que funciona sem instalação de servidor ou banco externo.

**[▶ Abrir demo online](https://htmlpreview.github.io/?https://github.com/berger33/berger33/blob/main/portfolio/chs-recruta/app/CHS-Recruta-Demo.html)** · **[⬇ Baixar versão portátil](https://htmlpreview.github.io/?https://github.com/berger33/berger33/blob/main/portfolio/chs-recruta/app/download.html)** · **[📘 Ver case técnico](portfolio/chs-recruta/README.md)**

**Credenciais da demonstração:** usuário `demo` · senha `demo123` · perfil Administradora.

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
7. empacotamento e preparação para deploy quando aplicável.

---

## Stack que aparece nos meus projetos

| Área | Tecnologias |
| --- | --- |
| Linguagem principal | Python |
| Backend / API | FastAPI, Uvicorn, REST, Webhooks |
| Inteligência Artificial | LangChain, RAG, Ollama, agentes, validação multiagente |
| Dados | Pandas, CSV, PyPDF, SQLite, JSON |
| Automação / integração | n8n, WAHA, Gmail, HTTP APIs |
| Front-end / produto | HTML5, CSS3, JavaScript, responsive design |
| Persistência local | SQLite, localStorage, sessionStorage, volumes Docker |
| Infraestrutura | Docker, Docker Compose |
| Engenharia | Git, GitHub, Pytest, GitHub Actions |

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
