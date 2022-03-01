from django.shortcuts import render, redirect, get_object_or_404
from babysitter.models import Babysitter
from connection . models import Connection


def number_waiting_connections(request):
    number_waiting_connections_base = 0
    # Number of requested connections
    if request.user.is_anonymous:
        number_waiting_connections_base = 0
    else:
        if request.user.user_type == 2:
            profil = get_object_or_404(Babysitter, user_id=request.user.id)
            all_match_connections_queryset = Connection.objects.filter(
                babysitter_id=profil.id)
            all_match_connections_list = list(all_match_connections_queryset)

            for one_match in all_match_connections_list:
                if one_match.is_matched == None:
                    number_waiting_connections_base += 1

    return {'number_waiting_connections_base': number_waiting_connections_base}
