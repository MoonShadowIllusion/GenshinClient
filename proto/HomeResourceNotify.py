# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeResourceNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .HomeResource import *


@dataclass
class HomeResourceNotify(betterproto.Message):
    """
    CmdId: 4892 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    home_coin: "HomeResource" = betterproto.message_field(9)
    fetter_exp: "HomeResource" = betterproto.message_field(8)
