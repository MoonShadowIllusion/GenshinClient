# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeChangeEditModeRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class HomeChangeEditModeRsp(betterproto.Message):
    """
    CmdId: 4559 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(10)
    is_enter_edit_mode: bool = betterproto.bool_field(5)
