# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneGalleryInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .SceneGalleryInfo import *


@dataclass
class SceneGalleryInfoNotify(betterproto.Message):
    """
    CmdId: 5581 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    gallery_info: "SceneGalleryInfo" = betterproto.message_field(4)