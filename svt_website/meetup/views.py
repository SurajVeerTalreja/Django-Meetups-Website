from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Meetup, Participant
from .forms import RegistrationForm

# Create your views here.
class HomeTemplateView(ListView):
    template_name = 'meetup/index.html'

    model = Meetup

    queryset = Meetup.objects.all().order_by('-date')

    context_object_name = 'meetups'



def MeetupDetail(request, slug):
    # selected_meetup = Meetup.objects.get(slug=slug)
    selected_meetup = get_object_or_404(Meetup, slug=slug)

    if request.method == 'GET':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data
            user_fname = key['first_name']
            user_lname = key['last_name']
            user_email = key['email']
            participant, _ = Participant.objects.get_or_create(
                first_name=user_fname,
                last_name=user_lname,
                email=user_email)
            selected_meetup.participants.add(participant)

            return redirect('thanks', slug=selected_meetup.slug)


    return render(request, 'meetup/meetup-detail.html', {
        'meetup': selected_meetup,
        'form': form,
    })

def ThankYouPage(request, slug):
    selected_meetup = get_object_or_404(Meetup, slug=slug)
    return render(request, 'meetup/thanks.html', {
        'email': selected_meetup.organizer_email,
    })



# class MeetupDetailView(DetailView):
#     template_name = 'meetup/meetup-detail.html'

#     model = Meetup

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         form = RegistrationForm()
#         context["form"] = form
#         return context
    
# class FormHandlingView(View):
#     def post(self, request, slug):
#         form = RegistrationForm(request.POST)
#         meetup = Meetup.objects.get(slug=slug)
#         if form.is_valid():
#             participant = form.save()
#             meetup.participants.add(participant)

#             return redirect(reverse('home-page'))


# def MeetupList(request):
#     all_meetups = Meetup.objects.all()
#     return render(request, 'meetup/index.html', {
#         'meetups': all_meetups
#     })




# class MeetupDetailView(View):
#     def get(self, request, slug):
#         for meetup in meetups:
#             if meetup['slug'] == slug:
#                 selected_meetup = meetup
        
#         context = {
#             'meetup': selected_meetup
#         }
#         return render(request, 'meetup/meetup-detail.html', context=context)