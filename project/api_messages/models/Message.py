from django.db import models


class Message(models.Model):
    vk_id = models.IntegerField(unique=True, blank=False, null=False)
    vk_name_author = models.CharField(max_length=100)
    vk_id_author = models.IntegerField(blank=False, null=False)
    text_question = models.TextField(max_length=1000)

    telegram_id_who_answered = models.IntegerField(null=True)
    telegram_name_author = models.CharField(max_length=100)
    telegram_id = models.IntegerField(unique=True, null=True)
    text_answer = models.TextField(max_length=1000)

    def to_json(self):
        return {
            "vk_id": self.vk_id,
            "vk_name_author": self.vk_name_author,
            "vk_id_author": self.vk_id_author,
            "text_question": self.text_question,
            "telegram_id_who_answered": self.telegram_id_who_answered,
            "telegram_name_author": self.telegram_name_author,
            "telegram_id": self.telegram_id,
            "text_answer": self.text_answer
        }
