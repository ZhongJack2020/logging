from distutils.command.bdist import bdist
import jack_log as jlog

log = jlog.initLog("main")

def prints():
    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log.error("error")
    log.fatal("fatal")

    alist = [1,2,3]
    bdict = {"id":123456,"name":"jack"}
    log.fatal("alist:{} bdict:{}".format(alist,bdict))

if __name__ == '__main__':  
    prints()
    