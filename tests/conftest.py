"""This file configures automatically pytest."""

import os
import sys
from contextlib import contextmanager

try:
    import pytest
    from databricks.connect import DatabricksSession
    from databricks.sdk import WorkspaceClient
    from pyspark.sql import SparkSession
except ImportError as err:
    raise ImportError(
        "Test dependencies not found.\n\nRun tests using 'uv run pytest'."
    ) from err


def enable_fallback_compute():
    """Enable serverless compute if no compute is specified."""
    conf = WorkspaceClient().config
    if conf.serverless_compute_id or conf.cluster_id or os.environ.get("SPARK_REMOTE"):
        return

    url = "https://docs.databricks.com/dev-tools/databricks-connect/cluster-config"
    print("☁️ no compute specified, falling back to serverless compute", file=sys.stderr)
    print(f"  see {url} for manual configuration", file=sys.stderr)

    os.environ["DATABRICKS_SERVERLESS_COMPUTE_ID"] = "auto"


@contextmanager
def allow_stderr_output(config: pytest.Config):
    """
    Temporarily disable pytest output capture.

    This ensures that initialization logs or errors (e.g., from Spark or Databricks)
    are printed directly to the console instead of being captured by pytest,
    making it easier to debug setup or environment issues before tests start.
    """
    capman = config.pluginmanager.get_plugin("capturemanager")
    if capman:
        with capman.global_and_fixture_disabled():
            yield
    else:
        yield


def pytest_configure(config: pytest.Config):
    """Configure pytest session."""
    with allow_stderr_output(config):
        enable_fallback_compute()

        # Initialize Spark session eagerly, so it is available even when
        # SparkSession.builder.getOrCreate() is used. For DB Connect 15+,
        # we validate version compatibility with the remote cluster.
        if hasattr(DatabricksSession.builder, "validateSession"):
            DatabricksSession.builder.validateSession().getOrCreate()
        else:
            DatabricksSession.builder.getOrCreate()


@pytest.fixture(scope="session")
def spark() -> SparkSession:
    """Provide a SparkSession fixture for tests."""
    return DatabricksSession.builder.getOrCreate()
