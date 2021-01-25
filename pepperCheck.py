import os
import platform
import process

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