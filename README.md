# 🛒 E-commerce de Tênis (Em Desenvolvimento)

Este projeto consiste em uma aplicação web de e-commerce focada na exibição e gerenciamento de tênis, desenvolvido com foco em escalabilidade, organização e experiência do usuário.

## 📌 Sobre o Projeto

A ideia surgiu a partir do interesse de um colega após visualizar meu Trabalho de Conclusão de Curso (TCC). A partir disso, iniciei o desenvolvimento de uma solução que funciona como uma **vitrine digital**, permitindo a divulgação e gestão de produtos de forma prática e eficiente.

Atualmente, o sistema está em desenvolvimento e novas funcionalidades estão sendo planejadas.

---

## 🚀 Tecnologias Utilizadas

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Tailwind CSS
- **Banco de Dados:** PostgreSQL
- **Algumas bibliotecas**

---

## 👤 Funcionalidades

### 🔍 Para usuários
- Visualização do catálogo de tênis
- Acesso a imagens e preços dos produtos
- Contato direto com o vendedor

### 🛠️ Para o administrador
- Cadastro de novos tênis
- Gerenciamento dos produtos exibidos na vitrine

---

## 🔮 Funcionalidades Futuras

- 📦 Visualização de protocolos de compra para acompanhamento de pedidos
- 💳 Integração com sistemas de pagamento
- 🚚 Cálculo automático de frete
- 📊 Melhorias na gestão e controle de pedidos

---

## 📈 Status do Projeto

🚧 Em desenvolvimento

---

## 📎 Objetivo

Desenvolver uma plataforma eficiente que facilite a apresentação de produtos e a comunicação entre cliente e vendedor, com potencial evolução para um e-commerce completo.

---
---

## ⚙️ Como Executar o Projeto

### 📥 1. Clonar o repositório

```bash
git clone https://github.com/BrunoCamargoDev/loja-tenis.git
cd loja-tenis
```

### 🐍 2. Criar e ativar ambiente virtual

```bash
python -m venv venv
```

### Windows:
```bash
venv\Scripts\activate
```

### ▶️ Linux/Mac:
```
source venv/bin/activate
```

### 📦 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 🗄️4. Configurar banco de dados

```👉 Certifique-se de ter o PostgreSQL instalado e configurado corretamente no arquivo settings.py.```

--- 

### 🔄 5. Aplicar migrações
```python manage.py migrate```
### ▶️ 6. Rodar o servidor
```python manage.py runserver```

### 🌐 7. Acessar no navegador
```http://127.0.0.1:8000/```


---

### 🔐 Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto e configure:

```bash
SECRET_KEY=sua_chave_secreta
DEBUG=True
DB_NAME=nome_do_banco
DB_USER=usuario
DB_PASSWORD=senha
DB_HOST=localhost
DB_PORT=5432
```

---
---
## 📬 Contato

Em caso de dúvidas, fique à vontade para entrar em contato.

---

### Email: brunocamargo.dev@gmail.com
