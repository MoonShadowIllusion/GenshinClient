# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeResourceTakeFetterExpRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .HomeResource import *


@dataclass
class HomeResourceTakeFetterExpRsp(betterproto.Message):
    """
    CmdId: 4645 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    fetter_exp: "HomeResource" = betterproto.message_field(4)
    retcode: int = betterproto.int32_field(15)
