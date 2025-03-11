# <div align="center">RedditAnalytics</div>

<div align="center">
  <img src="/data/external/redditpost.png" alt="RedditAnalytics" width="600"/>
  <p><i>Análise e visualização avançada de dados do Reddit para identificar padrões de engajamento entre comunidades</i></p>
</div>

<p align="center">
  <a href="#-sobre">Sobre</a> •
  <a href="#-aplicabilidades">Aplicabilidades</a> •
  <a href="#-benefícios">Benefícios</a> •
  <a href="#-funcionalidades">Funcionalidades</a> •
  <a href="#-instalação">Instalação</a> •
  <a href="#-uso">Uso</a> •
  <a href="#-visualizações">Visualizações</a> •
  <a href="#-estrutura">Estrutura</a> •
  <a href="#-licença">Licença</a>
</p>

---

## 📖 Sobre

O RedditAnalytics é uma ferramenta de análise de dados que processa comentários do Reddit para identificar padrões de engajamento, mapear interseções entre comunidades e visualizar a distribuição de usuários ativos entre diferentes subreddits.

---

## 🌟 Aplicabilidades

O RedditAnalytics pode ser utilizado em diversos contextos:

### 📊 Pesquisa de Mercado
- **Análise de Audiência**: Identifique onde seu público-alvo está mais ativo
- **Tendências de Nicho**: Descubra conexões entre diferentes interesses e comunidades
- **Validação de Produto**: Encontre comunidades para testar ideias e obter feedback

### 🔬 Pesquisa Acadêmica
- **Estudos Sociológicos**: Analise padrões de comportamento online
- **Pesquisa de Redes Sociais**: Mapeie como comunidades se conectam e interagem
- **Análise de Discurso**: Identifique tópicos e termos comuns entre diferentes grupos

### 💼 Marketing e Estratégia
- **Direcionamento de Conteúdo**: Otimize sua estratégia para comunidades específicas
- **Identificação de Influenciadores**: Encontre usuários ativos em múltiplas comunidades
- **Análise Competitiva**: Compare engajamento entre nichos relacionados

### 🧠 Ciência de Dados
- **Visualização de Dados Complexos**: Transforme dados brutos em insights visuais
- **Treinamento de Modelos**: Gere datasets para análise de sentimento e classificação
- **Detecção de Padrões**: Identifique anomalias e tendências emergentes

---

## 💎 Benefícios

### Para Empresas e Marcas
- **Decisões Baseadas em Dados**: Fundamente estratégias em comportamentos reais
- **Otimização de ROI**: Direcione recursos para comunidades com maior potencial
- **Insights Competitivos**: Entenda onde concorrentes têm maior presença

### Para Pesquisadores
- **Dados Estruturados**: Acesso a informações organizadas e processadas
- **Visualizações Prontas**: Gráficos e representações visuais de alta qualidade
- **Análise Escalável**: Processamento eficiente de grandes volumes de dados

### Para Criadores de Conteúdo
- **Descoberta de Nichos**: Encontre comunidades receptivas ao seu conteúdo
- **Estratégia de Crescimento**: Identifique padrões de migração entre subreddits
- **Otimização de Engajamento**: Entenda quais tópicos geram mais interação

---

## 🚀 Funcionalidades

- **Análise de Comentários**: Processamento de arquivos de comentários do Reddit
- **Identificação de Usuários**: Mapeamento de usuários únicos por subreddit
- **Visualização Avançada**: Geração de gráficos interativos com Plotly
- **Processamento de Ícones**: Integração visual com ícones oficiais dos subreddits
- **Análise de Adjacência**: Mapeamento de conexões entre comunidades
- **Exportação de Dados**: Salvamento de resultados em formatos utilizáveis

---

## 📋 Pré-requisitos

- Python 3.x
- Bibliotecas Python:
  - lxml
  - requests
  - plotly
  - pandas
  - Pillow (PIL)

---

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Reddit_TopSort.git
cd Reddit_TopSort
```

2. Instale as dependências:
```bash
pip install lxml requests plotly pandas Pillow
```

---

## 💻 Uso

O projeto utiliza um orquestrador principal (`orchestrator.py`) que coordena todas as operações:

```bash
# Atualizar lista de subreddits
python orchestrator.py -u

# Processar arquivo de comentários
python orchestrator.py arquivo_comentarios.json

# Mesclar arquivos de saída
python orchestrator.py -m

# Analisar top subreddits (N é opcional, define o número de subreddits)
python orchestrator.py -t [N]

# Gerar gráficos
python orchestrator.py -g

# Atualizar ícones dos subreddits
python orchestrator.py -i
```

### Fluxo de Trabalho Recomendado

1. Atualize a lista de subreddits (`-u`)
2. Processe os arquivos de comentários
3. Mescle os resultados (`-m`)
4. Gere visualizações (`-g` ou `-t`)

---

## 📊 Visualizações

O RedditAnalytics gera visualizações interativas de alta qualidade:

- **Gráficos de Barras**: Ranking de subreddits por comentaristas únicos
- **Heatmaps**: Matrizes de adjacência mostrando sobreposição entre comunidades
- **Visualizações Enriquecidas**: Integração com ícones oficiais dos subreddits
- **Gráficos de Rede**: Mapeamento de conexões entre comunidades relacionadas

<div align="center">
  <p><i>Exemplo de visualização gerada pelo RedditAnalytics</i></p>
</div>

---

## 📁 Estrutura do Projeto

```
Reddit_TopSort/
├── src/                    # Código fonte principal
│   ├── analysis/          # Módulos de análise
│   │   ├── __init__.py
│   │   ├── top_subs.py    # Análise de subreddits mais ativos
│   │   └── metrics.py     # Cálculos de métricas e estatísticas
│   │
│   ├── data/              # Processamento de dados
│   │   ├── __init__.py
│   │   ├── parser.py      # Processamento de arquivos
│   │   └── cleaner.py     # Limpeza e normalização de dados
│   │
│   ├── visualization/     # Geração de visualizações
│   │   ├── __init__.py
│   │   ├── graphs.py      # Geração de gráficos
│   │   └── image_tools.py # Manipulação de imagens
│   │
│   └── utils/            # Utilitários gerais
│       ├── __init__.py
│       └── tools.py      # Funções auxiliares
│
├── tests/                # Testes unitários e de integração
│   ├── __init__.py
│   ├── test_analysis/
│   ├── test_data/
│   └── test_visualization/
│
├── data/                 # Dados e arquivos de entrada
│   ├── raw/             # Dados brutos
│   ├── processed/       # Dados processados
│   └── external/        # Dados externos (ex: ícones)
│
├── output/              # Resultados e visualizações
│   ├── graphs/         # Gráficos gerados
│   ├── reports/        # Relatórios e análises
│   └── exports/        # Dados exportados
│
├── docs/                # Documentação
│   ├── api/            # Documentação da API
│   ├── guides/         # Guias de uso
│   └── examples/       # Exemplos de uso
│
├── scripts/            # Scripts de automação e utilitários
│   ├── setup.py       # Script de configuração
│   └── update.py      # Script de atualização
│
├── requirements/       # Requisitos do projeto
│   ├── base.txt       # Dependências básicas
│   ├── dev.txt        # Dependências de desenvolvimento
│   └── test.txt       # Dependências de teste
│
├── .github/           # Configurações do GitHub
│   ├── workflows/     # GitHub Actions
│   └── ISSUE_TEMPLATE/
│
├── .gitignore         # Arquivos ignorados pelo git
├── README.md          # Documentação principal
├── LICENSE           # Licença do projeto
├── setup.py          # Configuração do pacote
├── requirements.txt   # Atalho para requirements/base.txt
└── orchestrator.py    # Script principal de execução
```

### 📦 Organização dos Módulos

#### 1. `src/` - Código Fonte
- **analysis/**: Módulos de análise de dados
- **data/**: Processamento e manipulação de dados
- **visualization/**: Geração de gráficos e visualizações
- **utils/**: Funções utilitárias compartilhadas

#### 2. `tests/` - Testes
- Estrutura espelhada do código fonte
- Testes unitários e de integração
- Fixtures e mocks

#### 3. `data/` - Dados
- **raw/**: Dados brutos do Reddit
- **processed/**: Dados após processamento
- **external/**: Recursos externos

#### 4. `output/` - Resultados
- **graphs/**: Visualizações geradas
- **reports/**: Relatórios analíticos
- **exports/**: Dados exportados

#### 5. `docs/` - Documentação
- **api/**: Documentação técnica
- **guides/**: Guias do usuário
- **examples/**: Exemplos práticos

### 🔧 Scripts e Configurações

- **requirements/**: Gerenciamento modular de dependências
- **scripts/**: Automação e utilitários
- **.github/**: Configurações de CI/CD e templates

### 📝 Arquivos Principais

- **orchestrator.py**: Ponto de entrada principal
- **setup.py**: Configuração do pacote Python
- **requirements.txt**: Dependências do projeto

---

## 📝 Licença

Este projeto está sob a licença incluída no arquivo LICENSE.

---

## 🔗 Referências

Inspirado por: [r/dataisbeautiful - Subreddits with the most unique commenters](https://www.reddit.com/r/dataisbeautiful/comments/i2ocob/oc_subreddits_with_the_most_unique_commenters/)