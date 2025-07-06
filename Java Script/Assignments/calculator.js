class Calculator {
    constructor() {
        this.display = document.querySelector('.display');
        this.buttons = document.querySelectorAll('button:not(.clear):not(.equals)');
        this.clearBtn = document.querySelector('.clear');
        this.equalsBtn = document.querySelector('.equals');
        this.currentInput = '0';
        this.previousInput = '';
        this.operation = undefined;
        this.resetScreen = false;

        this.init();
    }

    init() {
        // Number buttons
        this.buttons.forEach(button => {
            button.addEventListener('click', () => {
                if (button.classList.contains('operator')) {
                    this.handleOperator(button.textContent);
                } else {
                    this.appendNumber(button.textContent);
                }
                this.updateDisplay();
            });
        });

        // Clear button
        this.clearBtn.addEventListener('click', () => {
            this.clear();
            this.updateDisplay();
        });

        // Equals button
        this.equalsBtn.addEventListener('click', () => {
            this.compute();
            this.updateDisplay();
        });
    }

    appendNumber(number) {
        if (this.currentInput === '0' || this.resetScreen) {
            this.currentInput = '';
            this.resetScreen = false;
        }
        if (number === '.' && this.currentInput.includes('.')) return;
        this.currentInput += number;
    }

    handleOperator(operator) {
        if (this.currentInput === '') return;
        if (this.previousInput !== '') {
            this.compute();
        }
        this.operation = operator;
        this.previousInput = this.currentInput;
        this.currentInput = '';
    }

    compute() {
        let computation;
        const prev = parseFloat(this.previousInput);
        const current = parseFloat(this.currentInput);
        if (isNaN(prev) || isNaN(current)) return;

        switch (this.operation) {
            case '+':
                computation = prev + current;
                break;
            case '-':
                computation = prev - current;
                break;
            case '*':
                computation = prev * current;
                break;
            case '/':
                computation = prev / current;
                break;
            case '%':
                computation = prev % current;
                break;
            default:
                return;
        }

        this.currentInput = computation.toString();
        this.operation = undefined;
        this.previousInput = '';
        this.resetScreen = true;
    }

    clear() {
        this.currentInput = '0';
        this.previousInput = '';
        this.operation = undefined;
    }

    updateDisplay() {
        this.display.value = this.currentInput;
    }
}

// Initialize calculator
new Calculator();