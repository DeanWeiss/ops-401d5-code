#!/bin/env python3

log = logging.getLogger(__name__)

def do_something():
    log.debug("Do something.")
    log.warning("Watch out!")
    log.info("This will not print.")

do_something()