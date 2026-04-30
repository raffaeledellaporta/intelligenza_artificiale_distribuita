import json


class Message:
    def __init__(self, msg_type, data=None):
        """
        Costruttore della classe Message.
        Args:
            - msg_type (str): il tipo del messaggio (es. "TOKEN").
            - data (dict, opzionale): i dati associati al messaggio.
        """
        self.msg_type = msg_type
        self.data = data or {}

    def to_json(self):
        """
        Serializza il messaggio in formato JSON.
        Returns:
            (str): Rappresentazione JSON del messaggio.
        """
        return json.dumps({
            "type": self.msg_type,
            "data": self.data
        })

    @staticmethod
    def from_json(json_str):
        """
        Deserializza un messaggio JSON in un oggetto Message.
        Args:
            - json_str (str): Messaggio in formato JSON.
        Returns:
            (Message): Istanza della classe Message creata dal JSON fornito.
        """
        obj = json.loads(json_str)
        return Message(obj["type"], obj["data"])
