# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MailData.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .MailItem import *
from .MailTextContent import *
from .Unk2700_CBJEDMGOBPL import *


@dataclass
class MailData(betterproto.Message):
    mail_id: int = betterproto.uint32_field(1)
    mail_text_content: "MailTextContent" = betterproto.message_field(4)
    item_list: List["MailItem"] = betterproto.message_field(7)
    send_time: int = betterproto.uint32_field(8)
    expire_time: int = betterproto.uint32_field(9)
    importance: int = betterproto.uint32_field(10)
    is_read: bool = betterproto.bool_field(11)
    is_attachment_got: bool = betterproto.bool_field(12)
    config_id: int = betterproto.uint32_field(13)
    argument_list: List[str] = betterproto.string_field(14)
    unk2700__n_d_p_p_g_j_k_j_o_m_h: "Unk2700_CBJEDMGOBPL" = betterproto.enum_field(15)
