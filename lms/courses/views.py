from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
from .models import Note


@login_required
def upload_note(request):
    """Handle note upload for teachers."""
    if request.user.profile.role != 'teacher':
        return redirect('core:dashboard')

    if request.method == 'POST':
        Note.objects.create(
            title=request.POST.get('title', 'Untitled'),
            file=request.FILES.get('file'),
            uploaded_by=request.user
        )
        return redirect('core:dashboard')
    return render(request, 'courses/upload_note.html')


@login_required
def note_list(request):
    """List all notes."""
    notes = Note.objects.all()
    return render(request, 'courses/note_list.html', {'notes': notes})


@login_required
def download_note(request, note_id):
    """Download a note file."""
    note = get_object_or_404(Note, id=note_id)
    if note.file:
        return FileResponse(note.file.open('rb'), as_attachment=True, filename=note.file.name)
    return HttpResponse("File not found", status=404)

