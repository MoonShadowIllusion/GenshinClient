# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GadgetPlayStartNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class GadgetPlayStartNotify(betterproto.Message):
    """
    CmdId: 873 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    start_time: int = betterproto.uint32_field(14)
    entity_id: int = betterproto.uint32_field(15)
    play_type: int = betterproto.uint32_field(8)
