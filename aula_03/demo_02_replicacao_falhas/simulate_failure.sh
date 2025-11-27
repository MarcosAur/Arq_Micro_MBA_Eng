#!/bin/bash
action=$1

if [ "$action" == "kill" ]; then
    echo "Derrubando kafka-2..."
    docker compose -f ../../aula_01/docker-compose.yml stop kafka-2
elif [ "$action" == "start" ]; then
    echo "Iniciando kafka-2..."
    docker compose -f ../../aula_01/docker-compose.yml start kafka-2
else
    echo "Uso: bash simulate_failure.sh [kill|start]"
fi

