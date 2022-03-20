import platform,socket,uuid,logging

from re import findall as re_findall



def getSystemInfo():

    try:

        info={}

        info['platform']=platform.system()

        info['platform-release']=platform.release()

        info['platform-version']=platform.version()

        info['architecture']=platform.machine()

        info['hostname']=socket.gethostname()

        info['ip-address']=socket.gethostbyname(socket.gethostname())

        info['mac-address']=':'.join(re_findall('..', '%012x' % uuid.getnode()))

        info['processor']=platform.processor()

        try:

            import psutil

            info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"

        except: pass

        return str(info)

    except Exception as e:

        logging.exception(e)

