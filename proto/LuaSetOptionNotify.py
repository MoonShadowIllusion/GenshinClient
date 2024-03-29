# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: LuaSetOptionNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class LuaSetOptionNotifyLuaOptionType(betterproto.Enum):
    LUA_OPTION_TYPE_NONE = 0
    LUA_OPTION_TYPE_PLAYER_INPUT = 1


@dataclass
class LuaSetOptionNotify(betterproto.Message):
    """
    CmdId: 316 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    lua_set_param: str = betterproto.string_field(8)
    option_type: "LuaSetOptionNotifyLuaOptionType" = betterproto.enum_field(10)
