import random
import tempfile

from dagster import (
    RunRequest,
    SensorResult,
    sensor,
    SensorEvaluationContext,
    AssetSelection,
    AutomationConditionSensorDefinition,
    DefaultSensorStatus,
)

import pathlib

from OpenStudioLandscapes.DagsterCodeLocation.Showcase.jobs import (
    job_create_file,
    job_delete_file
)


TEMPFILE = pathlib.Path(tempfile.gettempdir(), "i_was_here")


@sensor(
    job=job_create_file,
    default_status=DefaultSensorStatus.STOPPED,
    minimum_interval_seconds=random.randrange(15, 45),
)
def sensor_create_file(
        context: SensorEvaluationContext,
):

    runs_to_request = []

    context.log.info("Running sensor_create_file...")

    if not TEMPFILE.exists():
        context.log.info(f"TEMPFILE does not exist. Creating...")

        runs_to_request.append(
            RunRequest()
        )

    else:
        context.log.info(f"No request.")

    return SensorResult(
        run_requests=runs_to_request,
    )


@sensor(
    job=job_delete_file,
    default_status=DefaultSensorStatus.STOPPED,
    minimum_interval_seconds=random.randrange(15, 45),
)
def sensor_delete_file(
        context: SensorEvaluationContext,
):

    runs_to_request = []

    context.log.info("Running sensor_delete_file...")

    if TEMPFILE.exists():
        context.log.info(f"TEMPFILE exists. Deleting...")

        runs_to_request.append(
            RunRequest()
        )

    else:
        context.log.info(f"No request.")

    return SensorResult(
        run_requests=runs_to_request,
    )


# Custom AutoMaterialize Sensor
# https://docs.dagster.io/concepts/assets/asset-auto-execution#auto-materialize-sensors
my_custom_auto_materialize_sensor = AutomationConditionSensorDefinition(
    "my_custom_auto_materialize_sensor",
    target=AssetSelection.all(include_sources=True),
    minimum_interval_seconds=15,
    default_status=DefaultSensorStatus.RUNNING,
)
