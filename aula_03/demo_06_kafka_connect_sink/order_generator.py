from confluent_kafka import Producer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import SerializationContext, MessageField
from faker import Faker
import time
import random
from datetime import datetime

# Configuração Schema Registry
schema_registry_conf = {'url': 'http://localhost:8082'}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

# Carregar schema Avro
with open("schemas/order.avsc", "r") as f:
    schema_str = f.read()

avro_serializer = AvroSerializer(schema_registry_client, schema_str)

# Configuração Producer
producer_conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(producer_conf)
topic = 'demo-orders'

# Configuração Faker
fake = Faker('pt_BR')
statuses = ['pending', 'processing', 'shipped', 'delivered', 'cancelled']
products = [
    'Notebook Dell Inspiron', 'Mouse Logitech MX', 'Teclado Mecânico',
    'Monitor LG 27"', 'Webcam Full HD', 'Headset Gamer',
    'SSD Samsung 1TB', 'Memória RAM 16GB', 'Placa de Vídeo RTX'
]

def delivery_callback(err, msg):
    if err:
        print(f'❌ Erro: {err}')
    else:
        print(f'✅ Pedido enviado: {msg.value()[:50] if isinstance(msg.value(), bytes) else str(msg.value())[:50]}...')

print(f"🚀 Iniciando gerador de pedidos AVRO para o tópico '{topic}'...")
print("   Gerando 1 pedido a cada 2 segundos")
print("   Usando Schema Registry + Avro")
print("   Pressione Ctrl+C para parar\n")

order_counter = 1000

try:
    while True:
        # Gera pedido
        order_id = f"ORD-{order_counter}"
        order = {
            "order_id": order_id,
            "customer_name": fake.name(),
            "product": random.choice(products),
            "amount": round(random.uniform(50.0, 5000.0), 2),
            "status": random.choice(statuses),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        # Serializa com Avro e envia para Kafka
        try:
            serialized_value = avro_serializer(
                order,
                SerializationContext(topic, MessageField.VALUE)
            )
            
            producer.produce(
                topic,
                value=serialized_value,
                callback=delivery_callback
            )
            producer.poll(0)
            
            order_counter += 1
            time.sleep(2)
        except Exception as e:
            print(f"❌ Erro ao serializar/enviar: {e}")
            time.sleep(1)

except KeyboardInterrupt:
    print("\n\n🛑 Parando gerador...")
finally:
    producer.flush()
    print("✅ Todas as mensagens foram enviadas!")
