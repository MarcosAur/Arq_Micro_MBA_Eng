#!/bin/bash
echo "Verificando estado das partições e ISR..."
docker exec kafka kafka-topics --describe \
    --topic demo-replicacao \
    --bootstrap-server kafka:29092

