# import logging
# #The background is set with 40 plus the number of the color, and the foreground with 30

# #These are the sequences need to get colored ouput
# RESET_SEQ = "\033[0m"
# COLOR_SEQ = "\033[1;%dm"
# BOLD_SEQ = "\033[1m"

# def formatter_message(message, use_color = True):
#     if use_color:
#         message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
#     else:
#         message = message.replace("$RESET", "").replace("$BOLD", "")
#     return message

# COLORS = {
#     'WARNING': YELLOW,
#     'INFO': WHITE,
#     'DEBUG': BLUE,
#     'CRITICAL': YELLOW,
#     'ERROR': RED
# }

# class ColoredFormatter(logging.Formatter):
#     def __init__(self, msg, use_color = True):
#         logging.Formatter.__init__(self, msg)
#         self.use_color = use_color

#     def format(self, record):
#         levelname = record.levelname
#         if self.use_color and levelname in COLORS:
#             levelname_color = COLOR_SEQ % (30 + COLORS[levelname]) + levelname + RESET_SEQ
#             record.levelname = levelname_color
#         return logging.Formatter.format(self, record)


# class ColoredLogger(logging.Logger):
#     FORMAT = "[$BOLD%(name)-20s$RESET][%(levelname)-18s]  %(message)s ($BOLD%(filename)s$RESET:%(lineno)d)"
#     COLOR_FORMAT = formatter_message(FORMAT, True)
#     def __init__(self, name):
#         logging.Logger.__init__(self, name, logging.DEBUG)                

#         color_formatter = ColoredFormatter(self.COLOR_FORMAT)

#         console = logging.StreamHandler()
#         console.setFormatter(color_formatter)

#         self.addHandler(console)
#         return
import logging

class CustomFormatter(logging.Formatter):

    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

    format = "(%(filename)s:%(lineno)d): %(message)s "

    # %(asctime)s#     ??????????????????????????????# 2018-07-01 19:08:41,050# ????????????????????????
    # %(levelname)s#   ????????????????????????
    # %(message)s#     ??????????????????
    # %(name)s#        ????????????????????????????????????roots???
    # %(lineno)d#      ???????????????????????????????????????
    # %(levelno)s#     ?????????????????????????????????
    # %(pathname)s#    ????????????????????????????????????# sys.argv[0]# 
    # %(filename)s#    ????????????????????????
    # %(funcName)s#    ????????????????????????
    # %(thread)d#      ??????????????????ID
    # %(threadName)s#  ????????????????????????
    # %(process)d#     ??????????????????ID
    # %(processName)s# ????????????????????????
    # %(module)s#      ????????????????????????
    # %(created)f#     ??????UNIX???????????????????????????

    FORMATS = {
        logging.DEBUG: GREEN + format + END,
        logging.INFO: LIGHT_CYAN + format + END,
        logging.WARNING: YELLOW + format + END,
        logging.ERROR: RED + format + END,
        logging.CRITICAL: RED + BOLD + format + END
    }
    # CRITICAL   50
    # FATAL      50
    # ERROR      40
    # WARNING    30
    # WARN       30
    # INFO       20
    # DEBUG      10
    # NOTSET      0

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def initLog(name:str)->logging.log:
    log_level = logging.DEBUG
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(CustomFormatter())
    log.addHandler(ch)
    return log