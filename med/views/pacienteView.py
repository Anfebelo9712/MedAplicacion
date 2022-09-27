from datetime import datetime
from med.models import Usuario,Paciente
from rest_framework import status, views
from med.serializers import UserSerializer, PacienteSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PacienteView(views.APIView):

    def post(self, request, *args, **kwargs):
        ##guardar el usuario
        data_usuario = request.data.pop('usuario_info')
        now = datetime.now()
        data_usuario['create_date'] = now.strftime("%Y-%m-%d")
        data_usuario['rol'] = Usuario.AplicationRol.AUX
        serializer_user = UserSerializer(data = data_usuario)
        serializer_user.is_valid(raise_exception=True)
        usuario = serializer_user.save()

        data_paciente = request.data.pop('paciente_info')
        data_paciente['id_usuario'] = usuario.id
        data_paciente['create_date'] = now.strftime("%Y-%m-%d")
        serializer_paciente = PacienteSerializer(data=data_paciente)
        serializer_paciente.is_valid(raise_exception=True)
        serializer_paciente.save()
        paciente = serializer_paciente.save()

        tokenData =  {"username":data_usuario['username'], "password":data_usuario['password']}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return_data = {'paciente': PacienteSerializer(paciente).data,
                        "token_data":tokenSerializer.validated_data}
        return Response(return_data, status = status.HTTP_201_CREATED) 

    

    def delete(self, request, *args, **kwargs):
        paciente = Paciente.objects.filter(id = kwargs['pk']).first()
        usuario = Usuario.objects.filter(id=paciente.usuario.id).first()

        paciente.delete()
        usuario.delete()

        stringResponse = {'detail': ' Registro eliminado exitosamente'}
        return Response(stringResponse, status = status.HTTP_200_OK)

    ##buscar por ID auxiliar
    def  get(self, request, *args, **kwargs):
        paciente = Paciente.objects.get(id=kwargs['pk'])
        serializer_pac = PacienteSerializer(paciente)

        return Response(serializer_pac.data, status= status.HTTP_20O_OK)
    
    ##Buscar todos los pacientes.
    def get(self,request, *args, **kwargs):
        paciente = Paciente.objects.all()
        paciente_serializer = PacienteSerializer(paciente,many=True)
        return Response(paciente_serializer.data)

    def put(self, request, *args, **kwargs):
        paciente = Paciente.objects.get(id=kwargs['pk']) ##busca por Pk
        usuario =  Usuario.objects.get(id=paciente.id_usuario.id)
        now = datetime.now() ##fecha de actualziacion

        data_usuario = request.data.pop('usuario_info')
        data_usuario['create_date'] = now.strftime("%Y-%m-%d")

        serializer_user = UserSerializer(usuario,data = data_usuario)
        serializer_user.is_valid(raise_exception=True)
        usuario = serializer_user.save()

        data_paciente = request.data.pop('paciente_info')
        data_paciente['create_date'] = now.strftime("%Y-%m-%d")
        data_paciente['usuario'] = usuario.id

        serializer_paciente = PacienteSerializer(paciente,data=data_paciente)
        serializer_paciente.is_valid(raise_exception=True)
        serializer_paciente.save()
        paciente = serializer_paciente.save()

        return_data = {'paciente':PacienteSerializer(paciente).data}
        return Response(return_data, status = status.HTTP_200_OK)