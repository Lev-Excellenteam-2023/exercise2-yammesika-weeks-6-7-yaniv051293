class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_subject,message_body, urgent=False):
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.

        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.

            >>> po_box = PostOffice(['a', 'b'])
            >>> message_id = po_box.send_message('a', 'b', 'Hello!')
            >>> len(po_box.boxes['b'])
            1
            >>> message_id
            1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'subject': message_subject,
            'body': message_body,
            'sender': sender,
            'read': False
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user_name, N=None):
        """
        read messages that not read yet
        :param user_name:
        :param N: number of messages to read
        :return: the messages to read
        """
        user_box = self.boxes[user_name]
        massages_to_read=[]
        if N == None:
            N = self.boxes[user_name]
        for i in range(0, N):
            massage = user_box[i]
            if not massage['read']:
                massages_to_read.append(massage)
                self.boxes[user_name][i]['read'] = True
        return massages_to_read

    def search_inbox(self,user_name,text):
        """
        find message that contains this text
        :param user_name: the user name
        :param text: the text the user search
        :return: list of messages
        """
        user_box = self.boxes[user_name]
        messages = []
        for msg in user_box:
            if text in msg['body'] or text in msg['subject']:
                messages.append(msg)
        return messages

