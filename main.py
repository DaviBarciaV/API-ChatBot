import tkinter as tk
from tkinter import scrolledtext
import requests
import json
from senha import API_KEY  # Certifique-se de ter um arquivo senha.py com API_KEY

#Função para criar o prompt para a IA
def enviar_mensagem():
    conteudo = entrada_mensagem.get("1.0", tk.END).strip()
    if not conteudo:
        return
    
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-4o-mini"
    
    body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": conteudo}]
    }
    
    resposta_api = requests.post(link, headers=headers, data=json.dumps(body_mensagem))
    resposta_texto = resposta_api.json().get("choices", [{}])[0].get("message", {}).get("content", "Erro na resposta")
    
    saida_mensagem.config(state=tk.NORMAL)
    saida_mensagem.insert(tk.END, "Você: " + conteudo + "\n")
    saida_mensagem.insert(tk.END, "ChatGPT: " + resposta_texto + "\n\n")
    saida_mensagem.config(state=tk.DISABLED)
    entrada_mensagem.delete("1.0", tk.END)

def encerrar_chat():
    janela.destroy()

# Criando a interface gráfica
janela = tk.Tk()
janela.title("IA Hub")

saida_mensagem = scrolledtext.ScrolledText(janela, width=50, height=15, state=tk.DISABLED)
saida_mensagem.pack(pady=10)

entrada_mensagem = tk.Text(janela, width=50, height=3)
entrada_mensagem.pack(pady=5)

botao_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem)
botao_enviar.pack()

botao_encerrar = tk.Button(janela,text='Encerrar',command=encerrar_chat)
botao_encerrar.pack()

janela.mainloop()

