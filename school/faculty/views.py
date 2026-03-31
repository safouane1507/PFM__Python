# faculty/views.py
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from .models import Teacher
#from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('First test')  <- l'ancienne version
    #return render(request, 'Home/index.html')
    return render(request, 'authentification/login.html')
def dashboard(request):
    return render (request, 'students/student-dashboard.html')

def teacher_list(request):
    # 1. On récupère tous les enseignants de la base de données
    teachers = Teacher.objects.all()
    
    # 2. On les envoie (contexte) à un template HTML qu'on créera juste après
    return render(request, 'teachers/teachers.html', {'teachers': teachers})

def add_teacher(request):
    # Si le formulaire a été soumis (clic sur le bouton Enregistrer)
    if request.method == 'POST':
        # 1. On récupère toutes les données tapées dans les champs 'name' du HTML
        teacher_id = request.POST.get('teacher_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')
        experience = request.POST.get('experience')
        
        # ATTENTION : Pour les fichiers/images, on utilise request.FILES, pas request.POST
        image = request.FILES.get('image')

        # 2. On crée la nouvelle ligne dans la base de données
        Teacher.objects.create(
            teacher_id=teacher_id,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            joining_date=joining_date,
            mobile_number=mobile_number,
            address=address,
            experience=experience,
            image=image
        )

        # 3. On prépare un message de succès
        messages.success(request, 'L\'enseignant a été ajouté avec succès !')
        
        # 4. On redirige l'utilisateur vers la page qui liste les profs
        return redirect('teacher_list')
    
    # Si ce n'est pas un POST (ex: on vient juste d'ouvrir la page), on affiche le HTML
    return render(request, 'teachers/add-teacher.html')

def delete_teacher(request, teacher_id):
    # 1. On récupère le prof
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    
    # 2. On le supprime de la base de données
    teacher.delete()
    
    # 3. On affiche un message et on redirige
    messages.success(request, 'Enseignant supprimé avec succès !')
    return redirect('teacher_list')

# --- VUE : Modifier un enseignant ---
def edit_teacher(request, teacher_id):
    # 1. On récupère le prof spécifique grâce à son ID
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)

    if request.method == 'POST':
        # 2. On met à jour les champs avec les nouvelles données du formulaire
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.gender = request.POST.get('gender')
        teacher.date_of_birth = request.POST.get('date_of_birth')
        teacher.joining_date = request.POST.get('joining_date')
        teacher.mobile_number = request.POST.get('mobile_number')
        teacher.address = request.POST.get('address')
        teacher.experience = request.POST.get('experience')
        
        # On vérifie s'il a uploadé une nouvelle image, sinon on garde l'ancienne
        if request.FILES.get('image'):
            teacher.image = request.FILES.get('image')
        
        # 3. On sauvegarde les modifications
        teacher.save()
        messages.success(request, 'Enseignant mis à jour avec succès !')
        return redirect('teacher_list')

    # Si c'est un GET, on affiche la page en lui envoyant les données du prof
    return render(request, 'teachers/edit-teacher.html', {'teacher': teacher})


# --- VUE : Voir les détails d'un enseignant ---
def view_teacher(request, teacher_id):
    # 1. On récupère le prof grâce à son ID
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    
    # 2. On envoie les données à la page de profil
    return render(request, 'teachers/teacher-details.html', {'teacher': teacher})