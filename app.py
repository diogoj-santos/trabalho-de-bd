import streamlit as st
import pandas as pd
import sqlite3

# import sqlite3

# # Conectar ao banco SQLite
# conn = sqlite3.connect("trabbd.db")

# cursor = conn.cursor()

# # Criar tabelas
# cursor.execute("""
# CREATE TABLE Especie (
#    id_especie INTEGER PRIMARY KEY,
#    tx_absorcao DECIMAL(10, 2),
#    tipo TEXT,
#    nome_cientifico TEXT,
#    nome_popular TEXT
# );
# """)

# cursor.execute("""
# CREATE TABLE Estado (
#    id_estado INTEGER PRIMARY KEY,
#    nome TEXT,
#    sigla TEXT(2),
#    populacao INTEGER
# );
# """)

# cursor.execute("""
# CREATE TABLE Cidade (
#    id_cidade INTEGER PRIMARY KEY,
#    id_estado INTEGER,
#    nome TEXT,
#    populacao INTEGER,
#    FOREIGN KEY (id_estado) REFERENCES Estado(id_estado)
# );
# """)

# cursor.execute("""
# CREATE TABLE Localizacao (
#    id_local INTEGER PRIMARY KEY,
#    latitude DECIMAL(10, 6),
#    longitude DECIMAL(10, 6),
#    descricao TEXT,
#    id_cidade INTEGER,
#    FOREIGN KEY (id_cidade) REFERENCES Cidade(id_cidade)
# );
# """)

# cursor.execute("""
# CREATE TABLE Tipo_Emissor (
#    id_tipo INTEGER PRIMARY KEY,
#    nome_tipo TEXT
# );
# """)

# cursor.execute("""
# CREATE TABLE Emissor (
#    id_emissor INTEGER PRIMARY KEY,
#    nome TEXT,
#    emissao_anual INTEGER,
#    id_tipo INTEGER,
#    FOREIGN KEY (id_tipo) REFERENCES Tipo_Emissor(id_tipo)
# );
# """)

# cursor.execute("""
# CREATE TABLE Organizacao (
#    id_organizacao INTEGER PRIMARY KEY,
#    nome TEXT,
#    data_criacao DATE,
#    tipo TEXT,
#    endereco TEXT
# );
# """)

# cursor.execute("""
# CREATE TABLE Funcionario (
#    id_funcionario INTEGER PRIMARY KEY,
#    nome TEXT,
#    cpf TEXT
# );
# """)

# cursor.execute("""
# CREATE TABLE Func_Voluntario (
#    id_voluntario INTEGER PRIMARY KEY,
#    id_funcionario INTEGER,
#    horas_semanais INTEGER,
#    FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
# );
# """)

# cursor.execute("""
# CREATE TABLE Func_Assalariado (
#    id_assalariado INTEGER PRIMARY KEY,
#    id_funcionario INTEGER,
#    salario DECIMAL(10, 2),
#    FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
# );
# """)

# cursor.execute("""
# CREATE TABLE Organizacao_Estado (
#    id_org_estado INTEGER PRIMARY KEY,
#    id_organizacao INTEGER,
#    id_estado INTEGER,
#    FOREIGN KEY (id_organizacao) REFERENCES Organizacao(id_organizacao),
#    FOREIGN KEY (id_estado) REFERENCES Estado(id_estado)
# );
# """)

# cursor.execute("""
# CREATE TABLE Organizacao_Emissor (
#    id_org_emissor INTEGER PRIMARY KEY,
#    id_organizacao INTEGER,
#    id_emissor INTEGER,
#    FOREIGN KEY (id_organizacao) REFERENCES Organizacao(id_organizacao),
#    FOREIGN KEY (id_emissor) REFERENCES Emissor(id_emissor)
# );
# """)

# cursor.execute("""
# CREATE TABLE Emissor_Cidade (
#    id_emissor_cidade INTEGER PRIMARY KEY,
#    id_emissor INTEGER,
#    id_cidade INTEGER,
#    FOREIGN KEY (id_emissor) REFERENCES Emissor(id_emissor),
#    FOREIGN KEY (id_cidade) REFERENCES Cidade(id_cidade)
# );
# """)

# cursor.execute("""
# CREATE TABLE Veg_Local (
#    id_vegetacao INTEGER PRIMARY KEY,
#    id_especie INTEGER,
#    id_local INTEGER,
#    FOREIGN KEY (id_especie) REFERENCES Especie(id_especie),
#    FOREIGN KEY (id_local) REFERENCES Localizacao(id_local)
# );
# """)

# cursor.execute("""
# CREATE TABLE Veg_Emissor (
#    id_veg_emissor INTEGER PRIMARY KEY,
#    id_vegetacao INTEGER,
#    id_emissor INTEGER,
#    FOREIGN KEY (id_vegetacao) REFERENCES Veg_Local(id_vegetacao),
#    FOREIGN KEY (id_emissor) REFERENCES Emissor(id_emissor)
# );
# """)

# # Inserir dados fictícios
# cursor.executemany("""
#     INSERT INTO Especie (id_especie, tx_absorcao, tipo, nome_cientifico, nome_popular) 
#     VALUES (?, ?, ?, ?, ?)
# """, [
#     (1, 12.5, 'Árvore', 'Quercus robur', 'Carvalho'),
#     (2, 10.2, 'Árvore', 'Pinus sylvestris', 'Pinheiro'),
#     (3, 15.3, 'Árvore', 'Eucalyptus globulus', 'Eucalipto'),
#     (4, 8.7, 'Arbusto', 'Rosa canina', 'Rosa-selvagem'),
#     (5, 11.8, 'Árvore', 'Fagus sylvatica', 'Faia'),
#     (6, 13.2, 'Árvore', 'Acer pseudoplatanus', 'Bordo'),
#     (7, 9.9, 'Arbusto', 'Rubus fruticosus', 'Amora'),
#     (8, 14.0, 'Árvore', 'Cedrus libani', 'Cedro-do-líbano'),
#     (9, 10.5, 'Árvore', 'Betula pendula', 'Bétula'),
#     (10, 12.0, 'Árvore', 'Populus alba', 'Choupo-branco')
# ])
# cursor.executemany("""
#     INSERT INTO Estado (id_estado, nome, sigla, populacao) 
#     VALUES (?, ?, ?, ?)
# """, [
#     (1, 'São Paulo', 'SP', 45919049),
#     (2, 'Minas Gerais', 'MG', 21292666),
#     (3, 'Rio de Janeiro', 'RJ', 17366189),
#     (4, 'Bahia', 'BA', 14873064),
#     (5, 'Paraná', 'PR', 11516840),
#     (6, 'Rio Grande do Sul', 'RS', 11329605),
#     (7, 'Pernambuco', 'PE', 9616621),
#     (8, 'Ceará', 'CE', 9240580),
#     (9, 'Pará', 'PA', 8602865),
#     (10, 'Santa Catarina', 'SC', 7338473)
# ])
# cursor.executemany("""
#     INSERT INTO Cidade (id_cidade, id_estado, nome, populacao) 
#     VALUES (?, ?, ?, ?)
# """, [
#     (1, 1, 'São Paulo', 12300000),
#     (2, 1, 'Campinas', 1210000),
#     (3, 2, 'Belo Horizonte', 2520000),
#     (4, 3, 'Rio de Janeiro', 6748000),
#     (5, 4, 'Salvador', 2885000),
#     (6, 5, 'Curitiba', 1940000),
#     (7, 6, 'Porto Alegre', 1485000),
#     (8, 7, 'Recife', 1650000),
#     (9, 8, 'Fortaleza', 2687000),
#     (10, 9, 'Belém', 1497000)
# ])
# cursor.executemany("""
#     INSERT INTO Localizacao (id_local, latitude, longitude, descricao, id_cidade) 
#     VALUES (?, ?, ?, ?, ?)
# """, [
#     (1, -23.55052, -46.633308, 'Centro de SP', 1),
#     (2, -22.908333, -47.062778, 'Parque Taquaral', 2),
#     (3, -19.916667, -43.934444, 'Praça da Liberdade', 3),
#     (4, -22.906847, -43.172897, 'Copacabana', 4),
#     (5, -12.977749, -38.50163, 'Pelourinho', 5),
#     (6, -25.429594, -49.271927, 'Centro Cívico', 6),
#     (7, -30.034647, -51.217659, 'Mercado Público', 7),
#     (8, -8.047562, -34.877, 'Marco Zero', 8),
#     (9, -3.71722, -38.54306, 'Beira-Mar', 9),
#     (10, -1.455833, -48.50389, 'Ver-o-Peso', 10)
# ])
# cursor.executemany("""
#     INSERT INTO Tipo_Emissor (id_tipo, nome_tipo) 
#     VALUES (?, ?)
# """, [
#     (1, 'Industrial'),
#     (2, 'Veicular'),
#     (3, 'Agrícola'),
#     (4, 'Comercial'),
#     (5, 'Residencial'),
#     (6, 'Energia'),
#     (7, 'Transporte'),
#     (8, 'Hospitalar'),
#     (9, 'Construção'),
#     (10, 'Siderúrgico')
# ])
# cursor.executemany("""
#    INSERT INTO Emissor (id_emissor, nome, emissao_anual, id_tipo) 
#     VALUES (?, ?, ?, ?)
# """, [
#     (1, 'Fábrica de Aço', 50000, 1),
#     (2, 'Usina Termelétrica', 75000, 6),
#     (3, 'Caminhões Logística', 30000, 2),
#     (4, 'Indústria Química', 45000, 1),
#     (5, 'Aeroporto Internacional', 65000, 7),
#     (6, 'Fábrica de Celulose', 40000, 1),
#     (7, 'Frota de Táxis', 20000, 2),
#     (8, 'Obra de Construção Civil', 35000, 9),
#     (9, 'Hospital Geral', 15000, 8),
#     (10, 'Queimada Agrícola', 70000, 3)
# ])
# cursor.executemany("""
#    INSERT INTO Organizacao (id_organizacao, nome, data_criacao, tipo, endereco)
#     VALUES (?, ?, ?, ?, ?)
# """, [
#     (1, 'ONG Verde', '2001-05-12', 'Ambiental', 'Rua das Árvores, 123'),
#     (2, 'Fundação Terra', '1998-09-15', 'Social', 'Av. Sustentável, 456'),
#     (3, 'EcoVida', '2010-03-22', 'Ecológica', 'Rua Verde, 789'),
#     (4, 'Clima Seguro', '2015-07-30', 'Climática', 'Alameda Natural, 101'),
#     (5, 'Planeta Limpo', '2000-12-01', 'Sustentável', 'Estrada Verde, 202'),
#     (6, 'Recicla Mais', '2012-06-18', 'Reciclagem', 'Rua Eco, 303'),
#     (7, 'Resíduo Zero', '2018-04-05', 'Resíduos', 'Av. Ambiental, 404'),
#     (8, 'Energia Renovável', '2005-11-20', 'Energia', 'Rua Solar, 505'),
#     (9, 'Água Pura', '1995-08-25', 'Hídrica', 'Av. das Águas, 606'),
#     (10, 'Floresta Viva', '2008-09-12', 'Reflorestamento', 'Estrada Natural, 707')
# ])
# cursor.executemany("""
#    INSERT INTO Funcionario (id_funcionario, nome, cpf)
#     VALUES (?, ?, ?)
# """, [
#     (1, 'João Silva', '123.456.789-01'),
#     (2, 'Maria Oliveira', '234.567.890-12'),
#     (3, 'Carlos Souza', '345.678.901-23'),
#     (4, 'Ana Costa', '456.789.012-34'),
#     (5, 'Pedro Santos', '567.890.123-45'),
#     (6, 'Lucia Pereira', '678.901.234-56'),
#     (7, 'Fernando Lima', '789.012.345-67'),
#     (8, 'Juliana Rocha', '890.123.456-78'),
#     (9, 'Ricardo Alves', '901.234.567-89'),
#     (10, 'Camila Martins', '012.345.678-90')
# ])
# cursor.executemany("""
#   INSERT INTO Func_Voluntario (id_voluntario, id_funcionario, horas_semanais)
#     VALUES (?, ?, ?)
# """, [
#     (1, 6, 10),
#     (2, 7, 15),
#     (3, 8, 20),
#     (4, 9, 12),
#     (5, 10, 8)
# ])
# cursor.executemany("""
#   INSERT INTO Func_Assalariado (id_assalariado, id_funcionario, salario)
#     VALUES (?, ?, ?)
# """, [
#     (1, 1, 3000.00),
#     (2, 2, 3500.00),
#     (3, 3, 4000.00),
#     (4, 4, 3200.00),
#     (5, 5, 2800.00)
# ])
# cursor.executemany("""
#   INSERT INTO Organizacao_Estado (id_organizacao, id_estado) 
#     VALUES (?, ?)
# """, [
#     (2, 7),
#     (1, 2),
#     (3, 2),
#     (9, 4),
#     (5, 7),
#     (10, 4)
# ])
# cursor.executemany("""
#   INSERT INTO Organizacao_Emissor (id_organizacao, id_emissor) 
#     VALUES (?, ?)
# """, [
#     (4, 10),
#     (7, 1),
#     (7, 4),
#     (7, 8),
#     (1, 6),
#     (6, 4),
#     (6, 9),
#     (8, 2),
#     (8, 4)
# ])
# cursor.executemany("""
#   INSERT INTO Veg_Emissor (id_vegetacao, id_emissor)  
#     VALUES (?, ?)
# """, [
#     (1, 1),
#     (1, 8),
#     (2, 3),
#     (3, 3), 
#     (3, 7), 
#     (3, 8),
#     (4, 10),
#     (5, 9),
#     (6, 5)
# ])
# cursor.executemany("""
#   INSERT INTO Veg_Local(id_vegetacao, id_especie,  id_local)  
#     VALUES (?, ?, ?)
# """, [
#     (1, 1, 5),
#     (2,  1, 3),
#     (3, 3, 7),
#     (4, 5, 2),
#     (5, 4, 6),
#     (6, 7, 8)
# ])
# cursor.executemany("""
#   INSERT INTO Emissor_Cidade (id_emissor, id_cidade)  
#     VALUES (?, ?)
# """, [
#     (1, 1),
#     (1, 3),
#     (2, 1),
#     (3, 6),
#     (4, 2),
#     (9, 5),
#     (10, 3),
# ])

# # Salvar e fechar conexão
# conn.commit()
# conn.close()


def executar_sql(query):
    try:
        conn = sqlite3.connect("trabbd.db")
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        return f"Erro: {str(e)}"

# Interface Gráfica com Streamlit
st.title("TRABALHO DE BD: CONSULTAS E VIZ DAS TABELAS")

# Visualizar tabelas disponíveis
st.subheader("🔍 Visualizar Tabelas")
tabelas = ["Especie", "Estado", "Cidade", "Localizacao", "Tipo_Emissor", "Emissor", "Organizacao", 
           "Funcionario", "Func_Voluntario", "Func_Assalariado", "Organizacao_Estado", 
           "Organizacao_Emissor", "Veg_Emissor", "Emissor_Cidade", "Veg_Local"]
tabela_escolhida = st.selectbox("Escolha uma tabela:", tabelas)

if st.button("Mostrar Dados"):
    dados = executar_sql(f"SELECT * FROM {tabela_escolhida}")
    if isinstance(dados, pd.DataFrame):
        st.dataframe(dados)
    else:
        st.error(dados)

# Consultas SQL personalizadas
st.subheader("💻 Digite sua consulta SQL")
query = st.text_area("Escreva sua consulta SQL abaixo:")

if st.button("Executar Consulta"):
    resultado = executar_sql(query)
    if isinstance(resultado, pd.DataFrame):
        st.dataframe(resultado)
    else:
        st.error(resultado)

