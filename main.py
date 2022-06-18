import logging
import jack_log as jlog

log_level = logging.DEBUG
log = logging.getLogger("main")
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(log_level)
ch.setFormatter(jlog.CustomFormatter())
log.addHandler(ch)

if __name__ == '__main__':
    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log.error("error")
    log.fatal("fatal")
    