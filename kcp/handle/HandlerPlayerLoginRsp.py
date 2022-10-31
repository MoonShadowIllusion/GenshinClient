from .BaseHandle import BaseHandle
from proto import PlayerLoginRsp
from kcp.py_kcp import py_kcp


class HandlerPlayerLoginRsp(BaseHandle):
    @staticmethod
    def func1(kcp: py_kcp, _: PlayerLoginRsp):
        print("PlayerLoginRsp")
        print(_)

    @staticmethod
    def getHandles() -> tuple[type, tuple]:
        return PlayerLoginRsp, (HandlerPlayerLoginRsp.func1,)
