# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ShowClientGuideNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ShowClientGuideNotify(betterproto.Message):
    """
    CmdId: 3005 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    guide_name: str = betterproto.string_field(7)
