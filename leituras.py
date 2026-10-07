from django.db import models
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
import json

class Leitura(models.Model):
    """
    Modelo simplificado que representa um livro, artigo ou link a ser lido.
    """
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=100, blank=True)
    lido = models.BooleanField(default=False)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "leituras"

    def __str__(self) -> str:
        return self.titulo

def listar_leituras(request: HttpRequest) -> JsonResponse:
    """
    Retorna todas as leituras cadastradas no banco de dados.
    """
    leituras = list(Leitura.objects.values("id", "titulo", "autor", "lido"))
    return JsonResponse(leituras, safe=False, json_dumps_params={"ensure_ascii": False})

@csrf_exempt
def criar_leitura(request: HttpRequest) -> JsonResponse:
    """
    Cria um novo item de leitura através de uma requisição POST com dados JSON.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            if not data.get("titulo"):
                return JsonResponse({"erro": "O título é obrigatório"}, status=400)
            
            leitura = Leitura.objects.create(
                titulo=data.get("titulo"),
                autor=data.get("autor", "")
            )
            return JsonResponse({"id": leitura.id, "status": "criado"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"erro": "JSON inválido"}, status=400)
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=500)
            
    return JsonResponse({"erro": "Método não permitido"}, status=405)