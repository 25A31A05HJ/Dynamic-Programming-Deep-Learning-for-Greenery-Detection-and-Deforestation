import argparse, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','src'))
from geoai.utils.io import load_config, ensure_dirs

def main():
    p=argparse.ArgumentParser(description='Run project modules after data preparation.')
    p.add_argument('--module',choices=['lakes','roads','drainage','change','all'],required=True)
    a=p.parse_args(); cfg=load_config(); ensure_dirs()
    print(f"Selected module: {a.module}")
    print('Configuration loaded for',cfg['project']['name'])
    print('Next stage: connect prepared raster/label files to the corresponding module functions in src/geoai.')
    print('No results are fabricated when source data are absent.')
if __name__=='__main__': main()
