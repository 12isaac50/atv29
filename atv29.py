def verificar_presenca(alunos_presentes):
    # Conta o número de alunos presentes
    total_presentes = len(alunos_presentes)
    
    # Exibe o número de alunos presentes e a lista dos nomes
    print(f"Alunos presentes: {total_presentes}")
    print("Lista de alunos presentes:", ", ".join(alunos_presentes))
    
    # Se o total de alunos presentes for menor que 5, exibe uma mensagem de alerta
    if total_presentes < 5:
        print("Aviso: Poucos alunos presentes. Revisar lista de chamada.")

# Exemplo de entrada com mais de 5 alunos
alunos_presentes = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gustavo']

# Chama a função
verificar_presenca(alunos_presentes)
