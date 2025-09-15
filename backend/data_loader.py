"""Data loading via Overpass API (stub).

This module will later provide functionality to query the Overpass API
for Points of Interest (POIs) within a given bounding box and category,
optionally caching results in a local database.
"""

from typing import Tuple
import geopandas as gpd


def fetch_pois(category: str, bbox: Tuple[float, float, float, float]) -> gpd.GeoDataFrame:
    """Prepare and (later) execute an Overpass query for POIs.

    Args:
        category: Overpass/OSM key/value category, e.g. "amenity=cafe".
        bbox: Bounding box as (south, west, north, east) in WGS84 degrees.

    Returns:
        A GeoDataFrame of POIs with geometry in EPSG:4326.

    Notes:
        - This is a stub. It currently raises NotImplementedError.
        - Future implementation will construct an Overpass QL statement,
          perform the HTTP request, convert results to GeoDataFrame,
          and apply optional local caching (DuckDB or SQLite).
    """
    raise NotImplementedError("fetch_pois is a stub; Overpass implementation pending")

