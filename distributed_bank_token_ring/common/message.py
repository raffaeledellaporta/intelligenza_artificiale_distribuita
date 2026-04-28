import json

class Message:
    def __init__(self, msg_type, data=None):
        self.msg_type = msg_type
        self.data = data or {}

    def to_json(self):
        return json.dumps({
            "type": self.msg_type,
            "data": self.data
        })

    @staticmethod
    def from_json(json_str):
        obj = json.loads(json_str)
        return Message(obj["type"], obj["data"])