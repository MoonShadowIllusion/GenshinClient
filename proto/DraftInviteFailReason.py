# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DraftInviteFailReason.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class DraftInviteFailReason(betterproto.Enum):
    DRAFT_INVITE_FAIL_REASON_UNKNOWN = 0
    DRAFT_INVITE_FAIL_REASON_ACTIVITY_NOT_OPEN = 1
    DRAFT_INVITE_FAIL_REASON_ACTIVITY_PLAY_NOT_OPEN = 2
    DRAFT_INVITE_FAIL_REASON_SCENE_NOT_MEET = 3
    DRAFT_INVITE_FAIL_REASON_WORLD_NOT_MEET = 4
    DRAFT_INVITE_FAIL_REASON_PLAY_LIMIT_NOT_MEET = 5
