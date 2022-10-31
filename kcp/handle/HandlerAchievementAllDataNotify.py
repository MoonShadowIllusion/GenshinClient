from proto import AchievementAllDataNotify
from .BaseHandle import BaseHandle
from kcp.py_kcp import py_kcp


class HandlerAchievementAllDataNotify(BaseHandle):
    @staticmethod
    def func1(kcp: py_kcp, _: AchievementAllDataNotify):
        print('HandlerAchievementAllDataNotify')
        open(r'C:\Users\xuke\Desktop\ys\成就.bin', 'wb').write(_.SerializeToString())

    @staticmethod
    def getHandles() -> tuple[type, tuple]:
        return AchievementAllDataNotify, (
            HandlerAchievementAllDataNotify.func1,
        )
