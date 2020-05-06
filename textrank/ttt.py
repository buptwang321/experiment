# elif p1 == 'student_manage':
#       username = request.GET['usr']
#       password = request.GET['pwd']
#       user = User.objects.filter(username=username)
#       if user.count() == 0:
#         return HttpResponse('no user')
#       user = user[0]
#       if p2 == 'my_class':
#         ret = []
#         if user.type == 1:
#           i = 0
#           for uc in user.courses.all():
#             ret.append({
#               "id": uc.klass.id,
#               "class_name": uc.klass.name
#             })
#             i += 1
#           response = HttpResponse(json.dumps(ret))
#           return response
#         else:
#             i = 0
#             for uc in user.t_classes.all():
#                 ret.append({
#                     "id": uc.id,
#                     "class_name": uc.name
#                 })
#                 i += 1
#             response = HttpResponse(json.dumps(ret))
#             return response
