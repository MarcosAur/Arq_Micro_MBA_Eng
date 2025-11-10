# Aula 02 — Demonstrações Kafka

Esta pasta contém scripts e demos práticos para entender conceitos fundamentais do Kafka.

## Estrutura

```
aula_02/
└── DEMO_1/              # Demonstrações de Kafka
    ├── generate_1m_events.py    # Comparação JSON vs Avro
    ├── simple_producer.py       # Produtor simples (JSON)
    ├── simple_producer_json.py  # Produtor simples (JSON + schema via REST)
    ├── schema.avsc             # Schema Avro
    ├── environment.yml         # Ambiente conda
    └── README.md               # Documentação detalhada
```

## Pré-requisitos

Antes de executar os scripts, certifique-se de que:

1. **Kafka está rodando** (via `aula_01`):
   ```bash
   cd ../aula_01
   docker compose up -d
   ```

2. **Ambiente conda está criado**:
   ```bash
   cd DEMO_1
   conda env create -f environment.yml
   conda activate demo1-kafka
   ```

## Demos Disponíveis

### 1. Comparação JSON vs Avro
**Arquivo**: `DEMO_1/generate_1m_events.py`

Gera 1 milhão de eventos e compara o tamanho de armazenamento entre JSON e Avro.

### 2. Produtores simples
**Arquivos**: `DEMO_1/simple_producer.py`, `DEMO_1/simple_producer_json.py`

## Documentação Detalhada

Para instruções completas de cada demo, consulte:
- [`DEMO_1/README.md`](DEMO_1/README.md)

