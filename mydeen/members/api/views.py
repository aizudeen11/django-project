from rest_framework.decorators import api_view
from rest_framework.response import Response
from members.models import Member
from .serializers import MemberSerializer
# user can only get data
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/members'
    ]
    return Response(routes)
# @ is a decoretor django rest framework
@api_view(['GET'])
def getMembers(request):
    mymembers = Member.objects.all()
    # many mean serialize many object
    serializer = MemberSerializer(mymembers, many=True)
    return Response(serializer.data)