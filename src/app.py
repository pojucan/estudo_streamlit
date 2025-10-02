import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Visualizador CSV", page_icon="📊", layout="wide")

# Título do aplicativo
st.title("📊 Visualizador de Arquivos CSV")
st.markdown("Faça upload de um arquivo CSV e visualize os dados em um gráfico")

# Upload do arquivo
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    try:
        # Ler o arquivo CSV
        df = pd.read_csv(uploaded_file)
        
        # Mostrar informações básicas do dataset
        st.subheader("Pré-visualização dos Dados")
        st.write(f"**Formato do dataset:** {df.shape[0]} linhas × {df.shape[1]} colunas")
        
        # Mostrar as primeiras linhas
        st.dataframe(df.head())
        
        # Seleção de colunas para o gráfico
        st.subheader("Configuração do Gráfico")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Selecionar coluna para o eixo X
            x_column = st.selectbox(
                "Selecione a coluna para o eixo X:",
                options=df.columns,
                index=0
            )
        
        with col2:
            # Selecionar coluna para o eixo Y
            y_column = st.selectbox(
                "Selecione a coluna para o eixo Y:",
                options=df.columns,
                index=min(1, len(df.columns)-1)
            )
        
        # Tipo de gráfico
        chart_type = st.selectbox(
            "Selecione o tipo de gráfico:",
            options=["Linha", "Dispersão", "Barra", "Histograma"],
            index=0
        )
        
        # Criar o gráfico
        st.subheader("Gráfico")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        try:
            if chart_type == "Linha":
                ax.plot(df[x_column], df[y_column], marker='o', linewidth=2)
                ax.set_xlabel(x_column)
                ax.set_ylabel(y_column)
                ax.set_title(f"Gráfico de Linha: {y_column} vs {x_column}")
                ax.grid(True, alpha=0.3)
                
            elif chart_type == "Dispersão":
                ax.scatter(df[x_column], df[y_column], alpha=0.7)
                ax.set_xlabel(x_column)
                ax.set_ylabel(y_column)
                ax.set_title(f"Gráfico de Dispersão: {y_column} vs {x_column}")
                ax.grid(True, alpha=0.3)
                
            elif chart_type == "Barra":
                ax.bar(df[x_column], df[y_column], alpha=0.7)
                ax.set_xlabel(x_column)
                ax.set_ylabel(y_column)
                ax.set_title(f"Gráfico de Barras: {y_column} vs {x_column}")
                plt.xticks(rotation=45)
                
            elif chart_type == "Histograma":
                ax.hist(df[y_column], bins=20, alpha=0.7, edgecolor='black')
                ax.set_xlabel(y_column)
                ax.set_ylabel("Frequência")
                ax.set_title(f"Histograma de {y_column}")
                ax.grid(True, alpha=0.3)
            
            # Ajustar layout
            plt.tight_layout()
            st.pyplot(fig)
            
        except Exception as e:
            st.error(f"Erro ao criar o gráfico: {str(e)}")
            st.info("Verifique se as colunas selecionadas contêm dados numéricos apropriados.")
    
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {str(e)}")
        st.info("Verifique se o arquivo é um CSV válido.")

else:
    st.info("👆 Por favor, faça upload de um arquivo CSV para começar.")
    
    # Exemplo de como usar
    with st.expander("💡 Dica: Formato esperado do CSV"):
        st.markdown("""
        Seu arquivo CSV deve ter:
        - **Cabeçalho**: Nomes das colunas na primeira linha
        - **Dados**: Valores nas linhas seguintes
        - **Formato**: Separado por vírgulas
        
        Exemplo:
        ```
        Data, Vendas, Clientes
        2024-01-01, 100, 50
        2024-01-02, 150, 75
        2024-01-03, 120, 60
        ```
        """)

# Rodapé
st.markdown("---")
st.markdown("Feito com Streamlit 🎈")
