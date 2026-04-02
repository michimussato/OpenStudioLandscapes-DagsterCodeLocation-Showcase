from dagster import (
    AssetSelection,
    define_asset_job,
    AssetKey,
)


from OpenStudioLandscapes.DagsterCodeLocation.Showcase.assets import ASSET_HEADER


# Asset Selections
asset_selection_create_file = AssetSelection.assets(
    AssetKey([*ASSET_HEADER["key_prefix"], "temp_dir"]),
    AssetKey([*ASSET_HEADER["key_prefix"], "create_file"]),
)
asset_selection_delete_file = AssetSelection.assets(
    AssetKey([*ASSET_HEADER["key_prefix"], "temp_dir"]),
    AssetKey([*ASSET_HEADER["key_prefix"], "delete_file"]),
)


job_create_file = define_asset_job(
    name="job_create_file",
    selection=asset_selection_create_file,
)


job_delete_file = define_asset_job(
    name="job_delete_file",
    selection=asset_selection_delete_file,
)
