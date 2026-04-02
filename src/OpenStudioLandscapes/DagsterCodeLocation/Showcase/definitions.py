from dagster import (
    Definitions,
    load_assets_from_modules,
)

import OpenStudioLandscapes.DagsterCodeLocation.Showcase.assets
from OpenStudioLandscapes.DagsterCodeLocation.Showcase.sensors import (
    sensor_create_file,
    sensor_delete_file,
)

all_assets = load_assets_from_modules(
    modules=[OpenStudioLandscapes.DagsterCodeLocation.Showcase.assets]
)

all_sensors = [sensor_create_file, sensor_delete_file]

defs = Definitions(
    assets=all_assets,
    sensors=all_sensors,
)
