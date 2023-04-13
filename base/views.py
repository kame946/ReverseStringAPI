from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def rev_string(request):
    input_string = request.data.get('input_string', '')
    output_string = input_string[::-1]
    return Response({'output_string': output_string})