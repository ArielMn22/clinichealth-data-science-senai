# Baixando as bibliotecas necessárias
!pip install matplotlib

# Importando as bibliotecas necessárias
import matplotlib.pyplot as plt

# Dados ficticios - Substitua pelos seus dados reais
procedimentos = ['Botox', 'Preenchimento', 'Peeling', 'Depilação a laser', 'Microagulhamento']
lucro = [25000, 18000, 12000, 10000, 8000]

# Crie o gráfico de barras
plt.bar(procedimentos, lucro, color='skyblue')
plt.xlabel('Procedimentos')
plt.ylabel('Lucro (R$)')
plt.title('Lucro por Procedimento')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor visualização
plt.tight_layout()  # Ajusta o layout para evitar sobreposição de elementos
plt.show()
