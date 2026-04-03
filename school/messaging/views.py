from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages as flash_messages
from django.db.models import Q
from .models import Message, Announcement
from home_auth.models import CustomUser


def is_staff_user(user):
    return getattr(user, 'is_admin', False) or getattr(user, 'is_teacher', False)


# ─── MESSAGERIE PRIVÉE ─────────────────────────────────────────────

@login_required
def inbox(request):
    """Boîte de réception : messages reçus"""
    received = Message.objects.filter(recipient=request.user).select_related('sender')
    unread_count = received.filter(is_read=False).count()
    return render(request, 'messaging/inbox.html', {
        'messages_list': received,
        'unread_count': unread_count,
        'active_tab': 'inbox',
    })


@login_required
def sent_messages(request):
    """Messages envoyés"""
    sent = Message.objects.filter(sender=request.user).select_related('recipient')
    return render(request, 'messaging/inbox.html', {
        'messages_list': sent,
        'unread_count': 0,
        'active_tab': 'sent',
    })


@login_required
def message_detail(request, pk):
    """Lire un message (marquer comme lu si destinataire)"""
    msg = get_object_or_404(Message, pk=pk)

    # Sécurité : seul l'expéditeur ou destinataire peut lire
    if msg.sender != request.user and msg.recipient != request.user:
        flash_messages.error(request, "Accès refusé.")
        return redirect('inbox')

    # Marquer comme lu si c'est le destinataire
    if msg.recipient == request.user and not msg.is_read:
        msg.is_read = True
        msg.save()

    return render(request, 'messaging/message_detail.html', {'msg': msg})


@login_required
def compose(request):
    """Composer et envoyer un message"""
    # Destinataires possibles : admins + profs si étudiant, tout le monde sinon
    if getattr(request.user, 'is_student', False):
        recipients = CustomUser.objects.filter(
            Q(is_admin=True) | Q(is_teacher=True)
        ).exclude(pk=request.user.pk)
    else:
        recipients = CustomUser.objects.exclude(pk=request.user.pk)

    if request.method == 'POST':
        recipient_id = request.POST.get('recipient')
        subject = request.POST.get('subject', '').strip()
        body = request.POST.get('body', '').strip()

        if not recipient_id or not subject or not body:
            flash_messages.error(request, "Tous les champs sont obligatoires.")
        else:
            try:
                recipient = CustomUser.objects.get(pk=recipient_id)
                Message.objects.create(
                    sender=request.user,
                    recipient=recipient,
                    subject=subject,
                    body=body,
                )
                flash_messages.success(request, f"Message envoyé à {recipient.first_name} {recipient.last_name} !")
                return redirect('inbox')
            except CustomUser.DoesNotExist:
                flash_messages.error(request, "Destinataire introuvable.")

    return render(request, 'messaging/compose.html', {'recipients': recipients})


# ─── ANNONCES ─────────────────────────────────────────────────────

@login_required
def announcements(request):
    """Liste de toutes les annonces (visible par tous)"""
    all_announcements = Announcement.objects.select_related('author').all()
    return render(request, 'messaging/announcements.html', {
        'announcements': all_announcements,
    })


@login_required
def create_announcement(request):
    """Créer une annonce (admin ou prof uniquement)"""
    if not is_staff_user(request.user):
        flash_messages.error(request, "Accès réservé aux administrateurs et professeurs.")
        return redirect('announcements')

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        is_important = request.POST.get('is_important') == 'on'

        if not title or not content:
            flash_messages.error(request, "Le titre et le contenu sont obligatoires.")
        else:
            Announcement.objects.create(
                author=request.user,
                title=title,
                content=content,
                is_important=is_important,
            )
            flash_messages.success(request, "Annonce publiée avec succès !")
            return redirect('announcements')

    return render(request, 'messaging/create_announcement.html')


@login_required
def delete_announcement(request, pk):
    """Supprimer une annonce (auteur ou admin)"""
    ann = get_object_or_404(Announcement, pk=pk)
    if request.user == ann.author or getattr(request.user, 'is_admin', False):
        ann.delete()
        flash_messages.success(request, "Annonce supprimée.")
    else:
        flash_messages.error(request, "Vous ne pouvez pas supprimer cette annonce.")
    return redirect('announcements')


@login_required
def delete_message(request, pk):
    """Supprimer un message (expéditeur ou destinataire)"""
    msg = get_object_or_404(Message, pk=pk)
    if request.user in [msg.sender, msg.recipient]:
        msg.delete()
        flash_messages.success(request, "Message supprimé.")
    return redirect('inbox')
