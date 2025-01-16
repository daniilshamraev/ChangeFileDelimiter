# Change File Delimiter

**Change File Delimiter** is a Python-based CLI tool to easily change the delimiter of CSV or text files. It allows users to transform files with one delimiter (e.g., commas) to another (e.g., semicolons) with just a single command.

## Features

- Change delimiters for `.csv`, `.txt`, or other delimited text files.
- Supports empty row handling.
- Detects inconsistent column numbers.
- Handles errors gracefully.

## Installation

### Using Poetry

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/changefiledelimiter.git
   cd changefiledelimiter
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Build and install the package locally:

   ```bash
   poetry build
   pip install dist/changefiledelimiter-0.1.0-py3-none-any.whl
   ```

### From PyPI (Coming soon)

Once the package is published to PyPI, you can install it with:

```bash
pip install changefiledelimiter
```

## Usage

After installation, the CLI tool `changefiledelimiter` will be available globally. You can use it as follows:

### Basic Command

```bash
changefiledelimiter input.csv output.csv --old_delimiter "," --new_delimiter ";"
```

### Options

- `input_file` (required): Path to the input file.
- `output_file` (required): Path to the output file.
- `--old_delimiter` (optional): Current delimiter in the file (default: `,`).
- `--new_delimiter` (optional): Desired delimiter (default: `;`).

### Example

Transform a CSV file using tabs as the delimiter to use commas instead:

```bash
changefiledelimiter data.tsv data.csv --old_delimiter "\t" --new_delimiter ","
```

## Error Handling

- **Invalid Delimiters:** If you provide invalid delimiters (e.g., empty or multiple characters), the tool will raise an error.
- **Malformed CSV:** If rows in the file have an inconsistent number of columns, the tool will halt with an appropriate error message.
- **File Not Found:** If the input file does not exist, the tool will notify you.

## Development

To contribute to this project:

1. Fork the repository and clone it locally.
2. Install development dependencies:

   ```bash
   poetry install
   ```

3. Run tests to ensure everything works:

   ```bash
   poetry run pytest
   ```

## Tests

Run the unit tests using `pytest`:

```bash
poetry run pytest
```

## Установка и использование на русском

### Установка

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/changefiledelimiter.git
   cd changefiledelimiter
   ```

2. Установите зависимости с помощью Poetry:

   ```bash
   poetry install
   ```

3. Соберите пакет и установите его локально:

   ```bash
   poetry build
   pip install dist/changefiledelimiter-0.1.0-py3-none-any.whl
   ```

### Использование

После установки команда `changefiledelimiter` будет доступна из любого места. Пример использования:

```bash
changefiledelimiter input.csv output.csv --old_delimiter "," --new_delimiter ";"
```

### Опции

- `input_file` (обязательно): Путь к исходному файлу.
- `output_file` (обязательно): Путь к файлу для сохранения результата.
- `--old_delimiter` (опционально): Текущий разделитель в файле (по умолчанию: `,`).
- `--new_delimiter` (опционально): Желаемый разделитель (по умолчанию: `;`).

### Пример

Преобразование файла CSV с разделителями табуляции в файл с запятыми:

```bash
changefiledelimiter data.tsv data.csv --old_delimiter "\t" --new_delimiter ","
```

## Обработка ошибок

- **Неправильные разделители:** Если вы указали неверные разделители (например, пустые или содержащие несколько символов), инструмент выдаст ошибку.
- **Неправильный CSV:** Если строки в файле имеют разное количество колонок, инструмент остановится с соответствующим сообщением об ошибке.
- **Файл не найден:** Если указанный входной файл не существует, программа уведомит об этом.

## Лицензия

Этот проект распространяется под лицензией MIT.

## Автор

Daniil Shamraev