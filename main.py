import pandas as pd
import streamlit as st
import plotly.express as px

###### titulo ######

############# configuração api #######################

############# configuração api #######################

st.set_page_config(page_title="Sistema Departamento pessoal",
                   page_icon="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.mwexicont.com.br%2Fdepartamento-pessoal&psig=AOvVaw15S6UQA9K-3M3OAOq9ScDz&ust=1684964996029000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCNi3qvK1jP8CFQAAAAAdAAAAABAF",
                   )
st.title("Sistema Departamento Pessoal")

##################### Menu ##################

menu = ["Colaboradores", "Cadastro", "Chat"]

menu_lateral = st.sidebar.selectbox("Navegação do Sistema", menu)

##### mostrar conteúdo da 1 página #######

if menu_lateral == "Colaboradores":
    st.markdown("Página desenvolvida para auxiliar em análises")

    ##### carregamento de dados ######
    Banco_Dados = pd.read_excel("Banco_Funcionario.xlsx")

    # coluna principal
    col1, col2 = st.columns(2)

    # Primeira Coluna
    with col1:
        grafico = px.pie(Banco_Dados,
                         title="Funcionários Cadastrados",
                         values="Idade",
                         names="Cargo")

        st.plotly_chart(grafico)


    # Métrica de número total de funcionários
    total_funcionarios = len(Banco_Dados)
    st.write("Número total de funcionários:", total_funcionarios)















