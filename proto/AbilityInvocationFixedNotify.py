# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityInvocationFixedNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .AbilityInvokeEntry import *


@dataclass
class AbilityInvocationFixedNotify(betterproto.Message):
    """
    CmdId: 1172 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    invoke1_st: "AbilityInvokeEntry" = betterproto.message_field(10)
    invoke2_nd: "AbilityInvokeEntry" = betterproto.message_field(5)
    invoke3_rd: "AbilityInvokeEntry" = betterproto.message_field(12)
    invoke4_th: "AbilityInvokeEntry" = betterproto.message_field(1)
    invoke5_th: "AbilityInvokeEntry" = betterproto.message_field(8)
    invoke6_th: "AbilityInvokeEntry" = betterproto.message_field(14)
