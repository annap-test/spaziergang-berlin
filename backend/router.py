"""Routing logic using OSMnx/NetworkX (stub).

This module will contain functionality to construct a pedestrian network
graph from OSM data and compute routes based on time budgets and user
preferences.
"""

from typing import List, Tuple, Optional


def find_route(
    start_latlon: Tuple[float, float],
    minutes: int,
    prefer_ice_at_end: bool = False,
) -> Optional[List[Tuple[float, float]]]:
    """Compute a demo route polyline (stub).

    Args:
        start_latlon: (lat, lon) tuple.
        minutes: Time budget in minutes.
        prefer_ice_at_end: If True, bias end near an ice cream POI.

    Returns:
        A list of (lat, lon) coordinates representing the route polyline,
        or None until implemented.
    """
    # TODO: Implement using OSMnx graph and NetworkX shortest paths.
    return None

