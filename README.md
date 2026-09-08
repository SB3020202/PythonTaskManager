# CarFleetManager
Projeto próprio para dominar Python.

---

## Features

| FR | Descrição | Status |
|----|-----------|--------|
| 1 | Criar uma classe `Carro` com atributos: matrícula, modelo, combustível, estado e data de inspeção. | ⬜ |
| 2 | Criar uma classe `Garagem` que guarda uma lista de objetos `Carro`. | ⬜ |
| 3 | Implementar herança: `CarroEletrico` e `CarroCombustao` derivados de `Carro`. | ⬜ |
| 4 | Usar o decorator `@dataclass` para simplificar a definição da classe `Carro`. | ⬜ |
| 5 | Usar `enum.Enum` para `Combustivel` (GASOLINA, DIESEL, ELETRICO) e `Estado` (DISPONIVEL, EM_MANUTENCAO, VENDIDO). | ⬜ |
| 6 | Guardar todas as garagens num `dict[str, Garagem]` indexado por ID da garagem. | ⬜ |
| 7 | Implementar exceções personalizadas: `CarroNaoEncontradoException`, `CarroDuplicadoException`. | ⬜ |
| 8 | Gravar e ler dados de ficheiros JSON (`garagens.json`, `carros.json`) usando o módulo `json`. | ⬜ |
| 9 | Usar list comprehensions e `filter()` para procurar carros por combustível ou estado. | ⬜ |
| 10 | Usar `sorted()` com funções `lambda` para ordenar carros por data de inspeção ou modelo. | ⬜ |
| 11 | Usar `*args` e `**kwargs` numa função genérica `search()` para filtragem flexível. | ⬜ |
| 12 | Usar os decorators `@property` e `@setter` para validar atributos do carro na atribuição. | ⬜ |
| 13 | Separar o código em módulos: `models.py`, `storage.py`, `cli.py`, `exceptions.py`. | ⬜ |
| 14 | Usar `argparse` para construir uma CLI: adicionar, listar, atualizar, apagar e filtrar carros. | ⬜ |
| 15 | Escrever testes unitários com `unittest` ou `pytest` para todas as funções centrais. | ⬜ |
| 16 | Adicionar type hints (`int`, `str`, `list[Carro]`, `Optional`) a todas as funções e classes. | ⬜ |
| 17 | Documentar o código com docstrings (estilo Google) em todas as classes e métodos públicos. | ⬜ |
| 18 | Implementar relatórios: carros por garagem, inspeções vencidas, taxa de disponibilidade por combustível. | ⬜ |
| 19 | Exportar relatórios para `.csv` usando o módulo `csv`. | ⬜ |
| 20 | Usar um `requirements.txt` e um `README.md` com instruções de instalação e utilização. | ⬜ |

---

## Roadmap

- **Semana 1** — Classes + enums + exceções (FR 1–7)
- **Semana 2** — Ficheiros JSON + pesquisa + ordenação (FR 8–11)
- **Semana 3** — Módulos + CLI + type hints (FR 12–16)
- **Semana 4** — Testes + documentação + relatórios (FR 17–20)

---

## Correspondência com a versão anterior

| Antes | Agora |
|-------|-------|
| `Task` | `Carro` |
| `Project` | `Garagem` |
| `BugTask` / `FeatureTask` | `CarroEletrico` / `CarroCombustao` |
| `Priority` (LOW/MEDIUM/HIGH) | `Combustivel` (GASOLINA/DIESEL/ELETRICO) |
| `Status` (TODO/IN_PROGRESS/DONE) | `Estado` (DISPONIVEL/EM_MANUTENCAO/VENDIDO) |
| `due_date` | `data_inspecao` |
