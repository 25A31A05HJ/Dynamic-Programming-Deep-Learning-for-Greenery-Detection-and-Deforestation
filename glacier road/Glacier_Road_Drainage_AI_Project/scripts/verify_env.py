import importlib
mods=['numpy','pandas','rasterio','geopandas','shapely','sklearn','skimage','networkx','yaml']
missing=[]
for m in mods:
    try: importlib.import_module(m)
    except Exception as e: missing.append((m,str(e)))
print('Environment check')
if missing:
    print('Missing/unavailable:')
    for x in missing: print(' -',x[0],':',x[1])
    raise SystemExit(1)
print('All core modules imported successfully.')
