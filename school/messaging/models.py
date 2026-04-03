from django.db import models
from django.conf import settings

CustomUser = settings.AUTH_USER_MODEL

class Message(models.Model):
    """Message privé entre utilisateurs (étudiant → admin/prof)"""
    sender    = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages', verbose_name="Expéditeur")
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages', verbose_name="Destinataire")
    subject   = models.CharField(max_length=200, verbose_name="Objet")
    body      = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read   = models.BooleanField(default=False, verbose_name="Lu")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"De {self.sender} → {self.recipient} : {self.subject}"


class Announcement(models.Model):
    """Annonce publiée par admin ou prof, visible par tous"""
    author      = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='announcements', verbose_name="Auteur")
    title       = models.CharField(max_length=200, verbose_name="Titre")
    content     = models.TextField(verbose_name="Contenu")
    is_important = models.BooleanField(default=False, verbose_name="Important")
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
