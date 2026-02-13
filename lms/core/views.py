from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import Profile


def home(request):
    """Render the home page."""
    return render(request, 'core/home.html')


@login_required
def dashboard(request):
    """Route users to their respective dashboards based on role."""
    try:
        profile = request.user.profile
        if profile.role == 'Teacher':
            return render(request, 'core/teacher_dashboard.html')
        else:
            return render(request, 'core/student_dashboard.html')
    except Profile.DoesNotExist:
        return render(request, 'core/home.html')