from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # 删除浏览器中的refresh_token cookie
            response = Response({'result': 'success'})
            response.delete_cookie('refresh_token')
            return response
        except:
            return Response({'result': '系统异常，请稍后重试'})