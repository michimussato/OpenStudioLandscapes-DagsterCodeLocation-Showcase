import os
import pathlib
import tempfile
from pathlib import Path
from typing import Any, Generator

from dagster import (
    asset,
    AssetIn,
    AssetExecutionContext,
    AssetKey,
    Output,
    AssetMaterialization,
    MetadataValue
)


from OpenStudioLandscapes.DagsterCodeLocation.Showcase import dist

# Todo
#  - [ ] fix this naive replacement logic
GROUP = dist.name.replace("-", "_")
KEY = [GROUP]

ASSET_HEADER = {
    "group_name": GROUP,
    "key_prefix": KEY,
}


@asset(
    **ASSET_HEADER,
)
def temp_dir(
        context: AssetExecutionContext,
) -> Generator[Output[pathlib.Path] | AssetMaterialization | Any, Any, None]:

    temp_dir_ = pathlib.Path(tempfile.gettempdir())
    context.log.info(f"Temp dir: {temp_dir_.as_posix()}")

    yield Output(temp_dir_)

    yield AssetMaterialization(
        asset_key=context.asset_key,
        metadata={
            "__".join(context.asset_key.path): MetadataValue.path(temp_dir_),
        },
    )


@asset(
    **ASSET_HEADER,
    ins={
        "temp_dir": AssetIn(
            AssetKey([*ASSET_HEADER["key_prefix"], "temp_dir"]),
        ),
    }
)
def create_file(
        context: AssetExecutionContext,
        temp_dir: pathlib.Path,
) -> Generator[Output[Path] | AssetMaterialization | Any, Any, Path | None]:

    i_was_here = temp_dir.joinpath("i_was_here")

    if i_was_here.exists():
        context.log.critical(f"File {i_was_here.as_posix()} already exists")
    else:
        i_was_here.write_text("i_was_here", encoding="utf-8")
        context.log.info(f"File {i_was_here.as_posix()} created.")

    yield Output(i_was_here)

    yield AssetMaterialization(
        asset_key=context.asset_key,
        metadata={
            "__".join(context.asset_key.path): MetadataValue.path(i_was_here),
        },
    )


@asset(
    **ASSET_HEADER,
    ins={
        "temp_dir": AssetIn(
            AssetKey([*ASSET_HEADER["key_prefix"], "temp_dir"]),
        ),
    }
)
def delete_file(
        context: AssetExecutionContext,
        temp_dir: pathlib.Path,
) -> None:

    i_was_here = temp_dir.joinpath("i_was_here")

    try:
        os.remove(i_was_here)
        context.log.info(f"File {i_was_here.as_posix()} deleted.")
    except FileNotFoundError as e:
        context.log.exception(f"File {i_was_here.as_posix()} not found.")

    return None
