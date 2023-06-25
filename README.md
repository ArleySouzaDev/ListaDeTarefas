# Aplicativo de Lista de Tarefas

Um aplicativo simples em Python que permite aos usuários criar e gerenciar suas listas de tarefas. Os usuários podem adicionar, remover e marcar as tarefas como concluídas.

## Requisitos

- Python 3.x

## Bibliotecas Utilizadas

- `tkinter`: Biblioteca gráfica para criação da interface do usuário.
- `messagebox`: Módulo do `tkinter` para exibição de caixas de diálogo.
- `font`: Módulo do `tkinter` para configuração de estilos de fonte.

## Funcionalidades

### Classe Task

Representa uma tarefa da lista de tarefas.

#### Atributos

- `description`: `str` - A descrição da tarefa.
- `completed`: `bool` - Indica se a tarefa foi concluída.

#### Método `__init__(self, description)`

Inicializa uma nova instância da classe Task.

##### Parâmetros

- `description`: `str` - A descrição da tarefa.

### Classe TodoList

Representa a lista de tarefas.

#### Atributos

- `tasks`: `list` - A lista de objetos `Task`.

#### Método `__init__(self)`

Inicializa uma nova instância da classe TodoList.

#### Método `add_task(self, description)`

Adiciona uma nova tarefa à lista de tarefas.

##### Parâmetros

- `description`: `str` - A descrição da tarefa a ser adicionada.

#### Método `remove_task(self, index)`

Remove uma tarefa da lista de tarefas.

##### Parâmetros

- `index`: `int` - O índice da tarefa a ser removida.

#### Método `complete_task(self, index)`

Marca uma tarefa como concluída na lista de tarefas.

##### Parâmetros

- `index`: `int` - O índice da tarefa a ser marcada como concluída.

#### Método `display_tasks(self)`

Exibe todas as tarefas da lista de tarefas.

### Funções de Eventos dos Botões

#### Função `add_task_button_click()`

Função chamada quando o botão "Adicionar Tarefa" é clicado. Obtém a descrição da tarefa do campo de entrada, adiciona a tarefa à lista e limpa o campo de entrada.

#### Função `remove_task_button_click()`

Função chamada quando o botão "Remover Tarefa" é clicado. Obtém o índice da tarefa do campo de entrada, remove a tarefa da lista e limpa o campo de entrada.

#### Função `complete_task_button_click()`

Função chamada quando o botão "Marcar como Concluída" é clicado. Obtém o índice da tarefa do campo de entrada, marca a tarefa como concluída na lista e limpa o campo de entrada.

#### Função `display_tasks_button_click()`

Função chamada quando o botão "Exibir Tarefas" é clicado. Exibe todas as tarefas da lista de tarefas em uma caixa de diálogo.

## Execução

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Execute o programa com o seguinte comando:

python ListaDeTarefas.py


## Personalização

Para personalizar a aparência da interface gráfica, você pode modificar as seguintes configurações:

- Tamanho da janela: `window.geometry("largura x altura")`
- Cor de fundo da janela: `window.configure(bg="cor")`
- Estilo da fonte: `font_style = font.Font(family="fonte", size=tamanho)`
- Cor do texto: `fg="cor"`
- Cor de fundo do botão: `bg="cor"`

Sinta-se à vontade para ajustar essas configurações conforme suas preferências.

## Contribuição

Sinta-se à vontade para contribuir para o desenvolvimento deste projeto. Você pode enviar pull requests com melhorias, correções de bugs ou adição de novas funcionalidades.

## Licença

Este projeto é licenciado sob a licença [MIT](LICENSE).
