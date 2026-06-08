from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class RefreshTokenView(APIView):
    def post(self, request):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return Response({'result': '未找到刷新令牌，请重新登录'}, status=401)

            refresh = RefreshToken(refresh_token)
            if sttings.SIMPLE_JWT['ROTATE_REFRESH_TOKENS']:
                refresh.set_jti()
                response = Response({
                    'result': 'success',
                    'access': str(refresh.access_token),
                })

                response.set_cookie(
                    key='refresh_token',
                    value=str(refresh),
                    httponly=True,
                    samesite='Lax',
                    secure=True,
                    max_age=86400 * 7,
                )

                return response
            return Response({
                'result': 'success',
                'access': str(refresh.access_token),
            })
        except Exception as e:
            return Response({'result': 'refresh token过期了'}, status=401)