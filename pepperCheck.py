import os
import platform
import distro
import json
import networks
import socket
from pythonping import ping
#import processes

### Preciso fazer uma verificação básica onde identifico se :
# - O Servidor está up
# - Se o banco está up
# - Se o usuário do banco está up
# - Se o SO está com LOAD alto
# - Se foi reiniciado recentemente
### Para isso preciso
# - IP
# - Porta
# - Serviço
# - Credenciais de acesso
# - Saber o tipo de Banco
# - String de Conexão
# - Tipo do SO
# - Nome da Maquina

######### Variaveis
WHO=socket.gethostname()
WHOAMI=socket.gethostbyname(WHO)
SO=platform.system()
ARCH=platform.machine()
DISTRO=distro.info()
OSIFO=(f'SO : {SO}({DISTRO["id"].upper()}) -- Versão : {DISTRO["version"]}  -- Derivado : {DISTRO["like"].upper()}  -- CodeName : {DISTRO["codename"].upper()}')

print(OSIFO)
print(WHOAMI)


