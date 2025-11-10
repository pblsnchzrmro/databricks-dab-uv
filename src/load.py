# pragma: no cover
from uvdatabricks.logger import log
from uvdatabricks.utils.taxis import find_all_taxis

find_all_taxis()
log.info("show 5 rows of taxis from load")
