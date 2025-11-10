# Aula 01 — Ambiente Kafka e Produtores

Esta pasta contém o ambiente base (Docker Compose) para Kafka + ferramentas e exemplos simples de produtores.

## Estrutura

```
aula_01/
├── docker-compose.yml       # Stack: Kafka, Zookeeper, Schema Registry, Kafka UI, AKHQ
├── environment.yml          # Ambiente conda (aula01-kafka)
├── requirements.txt         # Alternativa via pip
├── producer_example.py      # Producer com Schema Registry (Avro)
└── simple_producer_json.py  # Producer simples JSON + registro de schema via REST
```

## Subindo o ambiente

Pré-requisitos: Docker e Docker Compose.

```bash
cd aula_01
docker compose up -d
```

Serviços úteis:
- Kafka UI: `http://localhost:8080`
- AKHQ: `http://localhost:8081`
- Schema Registry: `http://localhost:8082`

## Preparando o ambiente Python

Usando conda (recomendado):
```bash
conda env create -f environment.yml
conda activate aula01-kafka
```

Ou via pip:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Executando os produtores

Producer com Schema Registry (Avro):
```bash
python producer_example.py
```

Producer simples JSON (registra schema via REST):
```bash
python simple_producer_json.py
```

## Encerrando o ambiente

```bash
docker compose down -v
```

# Exemplo Kafka com Schema Registry

Este diretório contém um exemplo completo de uso do Kafka com Schema Registry.

## Serviços Disponíveis

- **Kafka**: `localhost:9092`
- **Schema Registry**: `http://localhost:8082`
- **Kafka UI**: `http://localhost:8080`
- **AKHQ**: `http://localhost:8081`

## Instalação

### Opção 1: Usando Conda (Recomendado)

1. Crie o ambiente conda a partir do arquivo `environment.yml`:

```bash
conda env create -f environment.yml
conda activate aula01-kafka
```

### Opção 2: Usando pip e venv

1. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

### Opção 1: Script Simples JSON (Recomendado)

Execute o script simples que faz tudo automaticamente:

```bash
python simple_producer_json.py
```

### Opção 2: Script Simples com Avro

Execute o script com suporte Avro completo:

```bash
python simple_producer.py
```

### Opção 3: Script Completo com Opções

Execute o script completo com opções interativas:

```bash
python producer_example.py
```

Os scripts irão:
1. Criar o tópico `user-events` (se não existir)
2. Registrar um schema Avro no Schema Registry
3. Produzir 5 mensagens de exemplo no tópico

## Visualizando os Dados

Após executar o script, acesse:

- **Kafka UI**: http://localhost:8080
  - Navegue até o tópico `user-events`
  - Veja as mensagens e o schema registrado

- **AKHQ**: http://localhost:8081
  - Explore os tópicos e schemas

## Schema Registrado

O exemplo registra um schema Avro para eventos de usuário com os seguintes campos:
- `user_id` (int)
- `username` (string)
- `email` (string)
- `action` (enum: LOGIN, LOGOUT, PURCHASE, VIEW)
- `timestamp` (long)
- `metadata` (map<string, string>)

