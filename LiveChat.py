import flet as ft
import datetime as dt


def main(pagina):
    
    titulo = ft.Text('LiveChat')
    
    nome_usuario = ft.TextField(label='Usuario')
    
    chat = ft.Column()

    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()


    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_campo_mensagem = f'{nome_usuario.value}: {campo_mensagem.value}'
        
        pagina.pubsub.send_all(texto_campo_mensagem)

        #limpando o campo de mensagem
        campo_mensagem.value = ''
        pagina.update()


    campo_mensagem = ft.TextField(label='Mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

    
    def entrar_chat(evento):
    
        popup.open = False
        
        pagina.remove(botao_iniciar)

        pagina.add(chat)
      
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(linha_mensagem)

        entrou_chat = f'{nome_usuario.value} entrou no chat'
        pagina.pubsub.send_all(entrou_chat)
        
        pagina.update()

    
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text('LiveChat'),
        content=nome_usuario,
        actions=[ft.ElevatedButton('Entrar', on_click=entrar_chat)]
        )
    
    def iniciar_chat(evento):
        
        pagina.dialog = popup
        
        popup.open = True
        
        pagina.update()


    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_iniciar)

ft.app(main, view=ft.WEB_BROWSER)