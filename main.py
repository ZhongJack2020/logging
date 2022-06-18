import jack_log as jlog

log = jlog.initLog("main")

def prints():
    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log.error("error")
    log.fatal("fatal")

if __name__ == '__main__':  
    prints()
    