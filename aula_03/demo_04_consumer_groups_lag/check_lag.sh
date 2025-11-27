#!/bin/bash
echo "Verificando LAG do grupo 'demo-group'..."
docker exec kafka kafka-consumer-groups \
    --bootstrap-server kafka:29092 \
    --describe \
    --group demo-group

