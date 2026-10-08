import geopandas as gpd
from shapely.geometry import shape
from rasterio.features import shapes

def mask_to_gdf(mask, transform, crs, year):
    rows=[]
    for geom, val in shapes(mask.astype('uint8'), mask=mask, transform=transform):
        if val:
            rows.append({'year': int(year), 'geometry': shape(geom)})
    if not rows:
        return gpd.GeoDataFrame({'year': [], 'geometry': []}, geometry='geometry', crs=crs)
    gdf=gpd.GeoDataFrame(rows, geometry='geometry', crs=crs)
    gdf['area_m2']=gdf.geometry.area
    gdf['perimeter_m']=gdf.geometry.length
    return gdf
