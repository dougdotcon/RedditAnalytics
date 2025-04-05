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

O **RedditAnalytics** é uma ferramenta avançada para análise e visualização de dados do Reddit. Ela processa grandes volumes de comentários para identificar padrões de engajamento, mapear conexões entre comunidades e gerar gráficos interativos, facilitando insights para pesquisadores, analistas e profissionais de marketing.

---

## 🌟 Aplicabilidades

### 📊 Pesquisa de Mercado
- **Análise de Audiência:** Descubra onde seu público está mais ativo.
- **Tendências de Nicho:** Encontre conexões entre interesses.
- **Validação de Produto:** Identifique comunidades para testar ideias.

### 🔬 Pesquisa Acadêmica
- **Estudos Sociológicos:** Analise comportamentos online.
- **Redes Sociais:** Mapeie conexões entre comunidades.
- **Análise de Discurso:** Explore tópicos comuns entre grupos.

### 💼 Marketing e Estratégia
- **Direcionamento de Conteúdo:** Otimize sua comunicação.
- **Influenciadores:** Encontre usuários ativos em múltiplas comunidades.
- **Análise Competitiva:** Compare engajamento entre nichos.

### 🧠 Ciência de Dados
- **Visualização:** Transforme dados brutos em gráficos claros.
- **Modelagem:** Gere datasets para análise de sentimentos.
- **Detecção de Padrões:** Identifique tendências emergentes.

---

## 💎 Benefícios

- **Automação Completa:** Da coleta à visualização.
- **Alta Escalabilidade:** Processa milhões de comentários.
- **Visualizações Ricas:** Gráficos com ícones oficiais dos subreddits.
- **Modularidade:** Componentes reutilizáveis e personalizáveis.
- **Código Aberto:** Fácil de adaptar e expandir.

---

## 🚀 Funcionalidades

- **Scraping de Subreddits:** Atualiza listas de comunidades populares.
- **Processamento de Comentários:** Organiza dados por subreddit.
- **Mesclagem de Dados:** Consolida múltiplos arquivos.
- **Análise Quantitativa:** Calcula métricas e matrizes de sobreposição.
- **Visualização Gráfica:** Gera gráficos interativos e redes.
- **Download de Ícones:** Baixa e integra ícones oficiais.
- **Exportação:** Salva resultados em formatos utilizáveis.

---

## 📋 Pré-requisitos

- Python 3.x
- Dependências listadas em `requirements.txt`

Instale com:
```bash
pip install -r requirements.txt
```

---

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/dougdotcon/RedditAnalytics.git
cd RedditAnalytics
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

---

## 💻 Uso

O script principal é `reddit_analytics.py`. Ele aceita múltiplas opções combináveis:

```bash
# Atualizar lista de subreddits populares
python reddit_analytics.py -u

# Processar arquivo de comentários compactado (.zst)
python reddit_analytics.py caminho/para/arquivo.zst

# Mesclar arquivos processados
python reddit_analytics.py -m

# Deletar arquivos já processados
python reddit_analytics.py -d

# Baixar ícones dos subreddits
python reddit_analytics.py -i

# Analisar sobreposição entre comunidades (opcional: limite N)
python reddit_analytics.py -a N

# Identificar subreddits mais influentes (opcional: limite N)
python reddit_analytics.py -t N

# Gerar grafo da rede de subreddits
python reddit_analytics.py -g
```

### Fluxo de trabalho recomendado:

1. Atualize a lista de subreddits (`-u`)
2. Processe os arquivos de comentários
3. Mescle os resultados (`-m`)
4. Baixe os ícones (`-i`)
5. Realize análises (`-a` ou `-t`)
6. Gere visualizações (`-g`)

---

## 📊 Visualizações

- **Gráficos de Barras:** Ranking de subreddits por comentaristas únicos.
- **Heatmaps:** Sobreposição entre comunidades.
- **Grafos:** Rede de conexões entre subreddits.
- **Ícones Integrados:** Visualizações enriquecidas com logos oficiais.

---

## 📁 Estrutura do Projeto

```
Reddit_TopSort/
├── reddit_analytics.py     # Script principal CLI
├── src/
│   ├── analysis/           # Análises e métricas
│   ├── data/               # Processamento e scraping
│   ├── visualization/      # Visualizações e gráficos
│   └── utils/              # Funções auxiliares
├── data/                   # Dados brutos e processados
├── output/                 # Resultados e gráficos gerados
├── docs/                   # Documentação adicional
├── scripts/                # Scripts utilitários
├── requirements/           # Dependências organizadas
├── requirements.txt        # Dependências principais
├── README.md               # Este arquivo
├── LICENSE                 # Licença
```

---

## 📝 Licença

Este projeto está sob a licença incluída no arquivo `LICENSE`.

---

## 🔗 Referências

Inspirado por: [r/dataisbeautiful - Subreddits with the most unique commenters](https://www.reddit.com/r/dataisbeautiful/comments/i2ocob/oc_subreddits_with_the_most_unique_commenters/)