from pathlib import Path
import yaml

def load_config(path='config/config.yaml'):
    with open(path,'r',encoding='utf-8') as f: return yaml.safe_load(f)

def ensure_dirs():
    for p in ['data/raw','data/interim','data/processed','data/external','models','mlruns','reports']:
        Path(p).mkdir(parents=True,exist_ok=True)
