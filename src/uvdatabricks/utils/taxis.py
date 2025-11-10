from databricks.sdk.runtime import spark

from uvdatabricks.logger import log


def find_all_taxis():
    """Find all taxis.

    Returns:
        DataFrame: show all taxis.

    """
    df = spark.read.table("samples.nyctaxi.trips")
    df.show(5)
    log.info("show 5 rows of taxis")
    return df


if __name__ == "__main__": # pragma: no cover
    find_all_taxis()
