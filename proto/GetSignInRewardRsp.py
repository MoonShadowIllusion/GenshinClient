# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetSignInRewardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .SignInInfo import *


@dataclass
class GetSignInRewardRsp(betterproto.Message):
    """
    CmdId: 2521 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(1)
    sign_in_info: "SignInInfo" = betterproto.message_field(14)
