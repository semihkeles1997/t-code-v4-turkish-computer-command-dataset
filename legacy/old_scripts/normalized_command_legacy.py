import json

input_file = 't_code_dataset_v1_1000.jsonl'
output_file = 't_code_dataset_v2_unique.jsonl'

seen_commands = set()
unique_data = []

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        # Komutu alıp boşluklarını temizleyerek eşsiz bir anahtar yapıyoruz
        cmd = data['normalized_command'].strip()
        
        if cmd not in seen_commands:
            seen_commands.add(cmd)
            unique_data.append(data)

# Benzersiz verileri yeni dosyaya yaz
with open(output_file, 'w', encoding='utf-8') as f:
    for item in unique_data:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

print(f"Orijinal Veri Sayısı: {len(seen_commands) + (len(data_list) - len(seen_commands) if 'data_list' in locals() else 0)}") # Kaba bir hesap
print(f"Benzersiz (Unique) Veri Sayısı: {len(unique_data)}")
print(f"Silinen Kopya Sayısı: {1000 - len(unique_data)}") # Eğer ilk dosyan tam 1000 ise