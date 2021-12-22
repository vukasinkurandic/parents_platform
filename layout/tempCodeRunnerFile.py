post_data = request.POST.copy()
email = post_data.get("exampleInputEmail1", None)
subscribedUsers = Newsletter()
subscribedUsers.email = email
subscribedUsers.save()