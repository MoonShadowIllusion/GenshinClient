# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarFlycloakChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AvatarFlycloakChangeNotify(betterproto.Message):
    """
    CmdId: 1643 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    flycloak_id: int = betterproto.uint32_field(8)
    avatar_guid: int = betterproto.uint64_field(2)