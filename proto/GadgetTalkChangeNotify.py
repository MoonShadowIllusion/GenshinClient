# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GadgetTalkChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class GadgetTalkChangeNotify(betterproto.Message):
    """
    CmdId: 839 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    gadget_entity_id: int = betterproto.uint32_field(5)
    cur_gadget_talk_state: int = betterproto.uint32_field(15)
