# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SetPlayerBirthdayRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Birthday import *


@dataclass
class SetPlayerBirthdayRsp(betterproto.Message):
    """
    CmdId: 4097 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    birthday: "Birthday" = betterproto.message_field(2)
    retcode: int = betterproto.int32_field(5)
