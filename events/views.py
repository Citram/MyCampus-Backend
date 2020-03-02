from django.shortcuts import render, redirect
from .forms import EventForm, AddressForm, CommentForm
from .models import Event, Address
from users import models as user_models
from django.http import Http404, HttpResponse
from events.forms import DeleteEventForm, RegistrationForm
from django.core.exceptions import ObjectDoesNotExist
from . import services

# Create your views here.
def create_event(request):
    if request.method == "POST":
        form_event = EventForm(request.POST)
        form_address = AddressForm(request.POST)
        if form_event.is_valid() and form_address.is_valid():
            form_address = form_address.save()
            form_event = form_event.save(commit=False)
            form_event.address = form_address
            form_event.save()
            return redirect("create_event")
    else:
        form_event = EventForm()
        form_address = AddressForm()
    return render(
        request,
        "events/create.html",
        {"event_form": form_event, "address_form": form_address},
    )


def delete_event(request):
    if request.method == "POST":
        delete_form = DeleteEventForm(request.POST)
        if delete_form.is_valid():
            id_field = delete_form.data["id_field"]

            try:
                services.delete_event(id_field)
            except services.UnsuccessfulOperationError:
                return HttpResponse("Delete ID not valid.")

            return HttpResponse("Event deleted.")

        # try:
        #     id = request.POST.get('id', '')
        # except:
        #     return HttpResponse("Error: ID of event to delete must be specified."
    else:
        delete_form = DeleteEventForm()
        return render(request, "events/delete.html", {"delete_form": delete_form})


def get_all_events(request):

    data_dbs = Event.objects.all()
    data_out = {"data_dbs": data_dbs}
    return render(request, "home.html", data_out)


def register_for_event(request):
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            current_user = request.session["id"]  # TODO: check
            user_id = current_user.id
            event_id = registration_form.data["event_id"]
            try:
                services.join_event(user_id, event_id)
                return HttpResponse("Successfully joined the event.")
            except services.UnsuccessfulOperationError as e:
                return HttpResponse(e.message)
    else:
        registration_form = RegistrationForm()
        return render(
            request, "events/register.html", {"registration_form": registration_form}
        )


def leave_event(request):
    if request.method == "DELETE":
        try:
            current_user = request.session["id"]
            user_id = current_user.id
            event_id = request.session["event_id"]
            services.leave_event(user_id, event_id)
            return HttpResponse("Successful left the event.")
        except services.UnsuccessfulOperationError as e:
            return HttpResponse(e.message)
        return render(request, "home.html")


def create_comment(request):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            current_user = request.session["id"]
            user_id = current_user.id
            event_id = comment_form.data["event_id"]
            try:
                services.create_comment(event_id, user_id, comment_form.data["message"])
            except ObjectDoesNotExist as error:
                return HttpResponse(error)
    else:
        comment_form = CommentForm()
        return render(request, {"comment_form": comment_form})


def query_event_by_category(request):
    if request.method == "GET":
        pass
    else:
        pass


def edit_event(request):
    if request.method == "PUT":
        pass
    else:
        pass
