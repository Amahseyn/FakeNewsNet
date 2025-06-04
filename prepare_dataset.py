import os
import json
import pandas as pd

def extract_title_text_label(json_path, label):
    data = []
    filename = os.path.basename(json_path)
    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            content = json.load(f)
            title = content.get('title', '')
            text = content.get('text', '')
            if title or text:
                data.append({
                    'filename': filename,
                    'title': title,
                    'text': text,
                    'label': label
                })
        except Exception as e:
            print(f"Error reading {filename}: {e}")
    return data

def process_directory(base_path, source_name):
    fake_dir = os.path.join(base_path, source_name, 'FakeNewsContent')
    real_dir = os.path.join(base_path, source_name, 'RealNewsContent')

    all_data = []

    # Process fake news
    if os.path.exists(fake_dir):
        for file in os.listdir(fake_dir):
            if file.endswith('.json'):
                all_data.extend(extract_title_text_label(os.path.join(fake_dir, file), 'fake'))

    # Process real news
    if os.path.exists(real_dir):
        for file in os.listdir(real_dir):
            if file.endswith('.json'):
                all_data.extend(extract_title_text_label(os.path.join(real_dir, file), 'real'))

    df = pd.DataFrame(all_data)
    output_file = f"{source_name.lower()}_news_with_filenames.csv"
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Saved {len(df)} records to {output_file}")

# Run for both platforms
base_path = 'Data'
process_directory(base_path, 'BuzzFeed')
process_directory(base_path, 'PolitiFact')