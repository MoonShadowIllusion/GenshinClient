# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ProfilePictureChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ProfilePicture import *


@dataclass
class ProfilePictureChangeNotify(betterproto.Message):
    """
    CmdId: 4016 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    profile_picture: "ProfilePicture" = betterproto.message_field(12)
