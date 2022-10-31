from .PacketHead import PacketHead
from .GetPlayerTokenReq import GetPlayerTokenReq
from .GetPlayerTokenRsp import GetPlayerTokenRsp
from .PlayerLoginReq import PlayerLoginReq
from .PlayerLoginRsp import PlayerLoginRsp
from .TrackingIOInfo import TrackingIOInfo
from .PlayerLoginReq import PlayerLoginReq
from .AchievementAllDataNotify import AchievementAllDataNotify
from .PingReq import PingReq
from .AdjustTrackingInfo import AdjustTrackingInfo
# 用到的协议都要加到这里，Pack.make 制作数据包时需要proto2id通过获取cmdid
id2proto = {
    7: PingReq,
    112: PlayerLoginReq,
    135: PlayerLoginRsp,
    172: GetPlayerTokenReq,
    198: GetPlayerTokenRsp,
    2676: AchievementAllDataNotify,
}

proto2id = {k: v for v, k in id2proto.items()}
