# Mini Calculator DSL

A simple Domain Specific Language (DSL) for mathematical expressions with a complete lexer, parser, and evaluator implementation in Python.

## Features

- **Mathematical Operations**: Addition (+), subtraction (-), multiplication (*), division (/)
- **Parentheses Support**: Proper grouping with parentheses for complex expressions
- **Operator Precedence**: Follows standard mathematical precedence (multiplication/division before addition/subtraction)
- **Interactive REPL**: Command-line interface for interactive calculations
- **File Processing**: Execute mathematical expressions from files
- **Error Handling**: Comprehensive error reporting for invalid expressions

## Project Structure

```
mini_calculator_dsl/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── lexer.py             # Tokenization of input expressions
│   ├── parser.py            # Recursive descent parser for AST generation
│   ├── evaluator.py         # AST evaluation engine
│   └── main.py              # Main application entry point
├── tests/
│   ├── test_lexer.py        # Lexer unit tests
│   ├── test_parser.py       # Parser unit tests
│   └── test_evaluator.py    # Evaluator unit tests
├── requirements.txt         # Python dependencies
├── Dockerfile              # Container configuration
└── README.md               # This file
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pytest (for running tests)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/milindasandaru/mini_calculator_dsl.git
   cd mini_calculator_dsl
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Interactive Mode (REPL)

Run the calculator in interactive mode:

```bash
python src/main.py
```

Example session:
```
calc> 2 + 3
5
calc> 5 * (10 - 3)
35
calc> 15 / 3 + 2 * 4
13.0
calc> (2 + 3) * (4 - 1)
15
calc> exit
```

### File Mode

Execute expressions from a file:

```bash
python src/main.py input.txt
```

Create an input file with mathematical expressions:
```
2 + 3 * 4
(10 - 5) / 2
```

### Supported Expressions

The calculator supports the following mathematical expressions:

- **Basic arithmetic**: `2 + 3`, `5 - 2`, `4 * 6`, `8 / 2`
- **Operator precedence**: `2 + 3 * 4` evaluates to `14` (not `20`)
- **Parentheses**: `(2 + 3) * 4` evaluates to `20`
- **Complex expressions**: `((2 + 3) * 4) - (10 / 2)`
- **Decimal numbers**: `3.14 + 2.86`

## Architecture

### Lexer (`lexer.py`)
- Converts input strings into tokens
- Recognizes numbers, operators, and parentheses
- Handles whitespace and invalid characters

### Parser (`parser.py`)
- Implements recursive descent parsing
- Builds Abstract Syntax Tree (AST) from tokens
- Enforces proper operator precedence and associativity
- Grammar:
  ```
  expr   → term ((PLUS | MINUS) term)*
  term   → factor ((TIMES | DIVIDE) factor)*
  factor → NUMBER | LPAREN expr RPAREN
  ```

### Evaluator (`evaluator.py`)
- Recursively evaluates AST nodes
- Performs arithmetic operations
- Returns numerical results

## Development

### Running Tests

Execute all tests:
```bash
pytest
```

Run specific test modules:
```bash
pytest tests/test_lexer.py
pytest tests/test_parser.py
pytest tests/test_evaluator.py
```

Run tests with verbose output:
```bash
pytest -v
```

### Docker Support

Build the Docker image:
```bash
docker build -t mini-calculator .
```

Run in Docker:
```bash
docker run -it mini-calculator
```

### Code Quality

The project follows Python best practices:
- Clear separation of concerns (lexer, parser, evaluator)
- Comprehensive error handling
- Unit tests for all components
- Proper module structure

## Examples

### Basic Operations
```python
# Addition and subtraction
calc> 10 + 5
15
calc> 20 - 8
12

# Multiplication and division
calc> 6 * 7
42
calc> 24 / 6
4.0
```

### Operator Precedence
```python
# Multiplication before addition
calc> 2 + 3 * 4
14

# Division before subtraction
calc> 10 - 8 / 2
6.0
```

### Parentheses
```python
# Changing precedence with parentheses
calc> (2 + 3) * 4
20

# Nested parentheses
calc> ((2 + 3) * 4) - 5
15
```

### Complex Expressions
```python
calc> (10 + 5) / (3 * 1)
5.0

calc> 2 * (3 + 4) - (10 / 2)
9.0
```

## Error Handling

The calculator provides clear error messages for various scenarios:

- **Syntax errors**: Invalid expressions like `2 + + 3`
- **Unexpected tokens**: Malformed input like `2 3 +`
- **Missing operators**: Incomplete expressions like `2 +`
- **Invalid characters**: Non-mathematical symbols

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run the test suite (`pytest`)
6. Commit your changes (`git commit -am 'Add new feature'`)
7. Push to the branch (`git push origin feature/new-feature`)
8. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Technical Details

### Token Types
- `NUMBER`: Integer or decimal numbers
- `PLUS`: Addition operator (+)
- `MINUS`: Subtraction operator (-)
- `TIMES`: Multiplication operator (*)
- `DIVIDE`: Division operator (/)
- `LPAREN`: Left parenthesis (()
- `RPAREN`: Right parenthesis ())

### AST Node Types
- `NUM`: Numeric literal
- `PLUS`: Addition operation
- `MINUS`: Subtraction operation
- `MUL`: Multiplication operation
- `DIV`: Division operation

## Roadmap

Future enhancements may include:
- Support for variables and assignments
- Mathematical functions (sin, cos, sqrt, etc.)
- Exponentiation operator
- Modulo operation
- Improved error messages with position information
- Syntax highlighting for expressions
