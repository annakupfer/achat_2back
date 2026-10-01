TEST_PHONE = "9859698002"
OTP_CODE = "00000"
TEST_PARTICIPANT_ID = 38
TEST_CHAT_ID = 145

WS_SEND_MESSAGE_TO_USER_PAYLOAD = {
  "action":"send_message",
  "participant_id": TEST_PARTICIPANT_ID,
  "message":"hi, user 3",
  "documents":[
   # {
    #  "name":"file2.png",
    #  "type":"image/png",
    #  "url":"uploads/d964c2be-89b0-4f9e-9da4-eec99ad094a4_file2.png"
    #}
  ]
}
WS_SEND_MESSAGE_TO_GROUP_PAYLOAD = {
  "action":"send_message",
  "chat_id": TEST_CHAT_ID,
  "message":"hi, user 3",
  "documents":[
   # {
    #  "name":"file2.png",
    #  "type":"image/png",
    #  "url":"uploads/d964c2be-89b0-4f9e-9da4-eec99ad094a4_file2.png"
    #}
  ]
}

EXPECTED_CHAT_MESSAGE_NO_ATTACHMENTS = {
  "type": "chat_message",
  "messages": {
    "id": 3202,
    "message": "Текст",
    "sender": 184,
    "created": "2025-07-09T21:55:47",
    "isMyMessage": True,
    "isRead": False,
    "isForwarded": False,
    "type": "OTHER",
    "attachments": [
    #  {
    #   "id": 343,
    #    "url": "uploads/d964c2be-89b0-4f9e-9da4-eec99ad094a4_Видосик.mp4",
    #    "name": "Видосик.mp4",
    #    "type": "video/mp4",
    #    "thumbnail": "https://api.jv.test.messenger.akatosphere.ru/s3/media-bucket/uploads/thumbnails/d508b23f...b9d5a",
    #    "duration": "2"
    #  }
    ],
    "parentId": None
  },
  "chat_id": 200,
  "original_sender": "19",
  "original_message_id": None,
  "is_reply": False
}
EXPECTED_CONFIRMATION = {
    "type": "confirmation",
    "message": "Message successfully",
    "created": True,
    "chat_id": 0
}

headers = {"Content-Type": "application/json",
           "Accept": "*/*",
           "User-Agent": "PostmanRuntime/7.48.0"}

def headers_with_token(token):
    return{
        "Content-Type": "application/json", 
        "Accept": "*/*",
        "Authorization": f"Bearer {token}"
    }
WS_REPLY_PAYLOAD_TEMPLATE = {
   "action":"reply_message",
   "chat_id": None,
   "original_message_id": None,
   "reply_text":"ответ",
   "attachments":[
      #{
      #  "name":"attachments.mp4",
      #  "type": "video/mp4",
      #  "url":"uploads/d964c2be-89b0-4f9e-9da4-eec99ad094a4_Видосик.mp4"
      #}
   ]
}
EXPECTED_REPLY_MESSAGE = {
   "type": "chat_message",
   "messages": {
      "id": 3291,
      "message": "ответ",
      "sender": 13,
      "created": "2025-07-21T12:54:52",
      "isMyMessage": False,
      "isRead": False,
      "isForwarded": False,
      "type": "TEXT",
      "attachments": [],
      "parentId": 3290
   },
   "chat_id": 219,
   "original_sender": None,
   "original_message_id": 3290,
   "is_reply": True
}
WS_GET_CHATS_PAYLOAD = {
  "action": "get_chats" 
}
EXPECTED_CHAT_LIST_STRUCTURE = {
  "type": "chat_list",
  "chats": [
    {
      "id": 200,
      "chatName": "",
      "is_public": True,
      "lastName": "lastName",
      "description": None,
      "chat_type": "ONE_ON_ONE",
      "created": "2025-07-09T17:07:40",
      "owner_id": 23,
      "consist": False,
      "avatar": None,
      "onlineStatus": "online",
      "unreadMessages": 0,
      "lastMessage": 
        {
          "id": 3207,
          "message": "Original message content",
          "sender": 184,
          "created": "2025-07-10T22:44:22",
          "isMyMessage": True,
          "isRead": False,
          "isForwarded": False,
          "type": "OTHER",
          "attachments": [
            {
              "id": 346,
              "url": "uploads/d964c2be-89b0-4f9e-9da4-eec99ad094a4_f91d12e2b7e31c497d8b25d44fd8724f.jpg",
              "name": "f91d12e2b7e31c497d8b25d44fd8724f.jpg",
              "type": "image/jpg",
              "thumbnail": "https://api.jv.test.messenger.akatosphere.ru/s3/media-bucket/uploads/thumbnails/d508b23f...b9d5a",
              "duration": None
            }
          ],
          "parentId": None
        },
      "participantId": [
        63
      ],
      "isPinned": False,
      "notificationsEnabled": True,
      "draft": None
    },
    {
      "id": 201,
      "chatName": "",
      "lastName": "lastName",
      "description": None,
      "chat_type": "ONE_ON_ONE",
      "created": "2025-07-09T22:10:23",
      "owner_id": 23,
      "consist": False,
      "avatar": None,
      "onlineStatus": "offline",
      "unreadMessages": 0,
      "lastMessage": None,
      "parentId": None,
      "participantId": [
        116
      ],
      "isPinned": False,
      "notificationsEnabled": True,
      "draft": {
        "message": "text",
        "documents": [
          {
            "id": 343,
            "url": "uploads/...",
            "name": "file.png",
            "type": "image/png",
            "thumbnail": "http://.../thumbnails/...",
            "duration": None
          }
        ],
        "modified": "2025-08-04T23:25:28.557902"
      }
    }
  ]
}
WS_GET_MESSAGES_TEMPLATE = {
  "action": "get_messages",
  "chat_id": None,
  "page_number": "0"
}
EXPECTED_MESSAGE_STRUCTURE = {
                    "id": 123,
                    "message": "text",
                    "created": "2025-10-12T07:13:34",
                    "isMyMessage": True,
          "isRead": False,
          "isForwarded": False,
          "type": "OTHER",
          "attachments": [
            #{
            # "id": 341,
            # "url": "uploads/d964c2be-89b0-4f9e-9da4-eec99ad094a4_капибара.jpg",
            # "name": "капибара.jpg",
            #  "type": "image/jpg",
            #  "thumbnail": "https://api.jv.test.messenger.akatosphere.ru/s3/media-bucket/uploads/thumbnails/d508b23f...b9d5a",
            #  "duration": None
            #}
          ],
          "parentId": None
    
                }
WS_CREATE_GROUP_PAYLOAD = {
  "action": "create_group_or_channel",
  "name_chat": "Капибарочка",
  "description": "Описание",
  "chat_type": "GROUP",
  "is_public": True,
  "participant_id": ["63"]
}
WS_GET_CHAT_INFO_TEMPLATE = {
  "action": "get_chat",
  "chat_id": None
}
WS_CALL_INITIATION_PAYLOAD = {
   "action": "start_call",
   "callee_phone_number": "9000000002",
   "sdp": "sdp-данные"   
}
EXPECTED_CALL_STARTED_RESPONSE = {
   "type": "call_started",
   "call_id": None,
   "user_phone": "9000000001",
   "callee_phone": "9000000002",
   "sdp": "sdp-данные"   
}
EXPECTED_CALL_TIMED_OUT_RESPONSE = {
    "type": "call_timed_out",
    "call_id": 15,
    "user_phone": "9000000003",
    "callee_phone": "9000000002"
}
WS_FORWARD_MESSAGE_TO_GROUP_TEMPLATE =  {
    "action": "forward_message",
    "chat_id": None,
    "message": "Original message content",
    "attachments_message": [
        # Пример вложения (если нужно, можно раскомментировать и заполнить)
        # {
        #     "name": "file2.png",
        #     "type": "image/png",
        #     "url": "uploads/d964c2be-89b0-4f9e-9da4-eec99ad094a4_file2.png"
        # }
    ],
    "original_message_id": None
}
WS_FORWARD_MESSAGE_TO_USER_TEMPLATE = {
  "action": "forward_message",
  "participant_id": 38,
  "message": "пересылаю тебе это",
  "attachments_message": [],
  "forwarded_message": "Сообщение для Антонио без вложений",
  "attachments_forwarded_message": [],
  "original_message_id": None

}
EXPECTED_CHAT_CREATED_STRUCTURE = {
  "type": "chat_created",
  "chat_id": 200,
  "message": "You have been added to a new chat",
  "sender": 184
}
EXPECTED_FORWARDED_MESSAGE_STRUCTURE = {
  "type": "chat_message",
  "messages": {
    "id": 3206,
    "message": "This is a forwarded message",
    "sender": 184,
    "created": "2025-07-10T22:44:15",
    "isMyMessage": True,
    "isRead": False,
    "isForwarded": True,
    "type": "OTHER",
    "attachments": [
      #{
       # "id": 345,
       #"url": "uploads/d964c2be-89b0-4f9e-9da4-eec99ad094a4_Видосик.mp4",
       # "name": "Видосик.mp4",
       #"type": "video/mp4",
       # thumbnail": "https://api.jv.test.messenger.akatosphere.ru/s3/media-bucket/uploads/thumbnails/d508b23f...b9d5a",
       # "duration": "2"
      #}
    ],
    "parentId": None
  },
  "chat_id": 200,
  "original_sender": "184",
  "original_message_id": 81,
  "is_reply": False
}
