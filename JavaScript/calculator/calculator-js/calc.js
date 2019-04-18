// calculator.js
const displayDiv = document.querySelector('#display')
const acDiv = document.querySelector('#AC')
const ceDiv = document.querySelector('#CE')
const eqDiv = document.querySelector('#eq')
const decimalDiv = document.querySelector('#dec')
const digits = document.querySelectorAll('.num')
const ops = document.querySelectorAll('.op')

const add = (a, b) => a + b
const subtract = (a, b) => a - b
const multiply = (a, b) => a * b
const divide = (a, b) => a / b
const updateDisplay = (value) => {
  displayDiv.innerText = value
}

let runningTotal = 0
let currentValue = ''
let decimal = false
let operator = null

updateDisplay(runningTotal)

const calculate = () => {
  if (currentValue) {
    let a = parseFloat(runningTotal)
    let b = parseFloat(currentValue)
    if (['add', '+'].includes(operator)) {
      runningTotal = add(a, b)
    } else if (['sub', '-'].includes(operator)) {
      runningTotal = subtract(a, b)
    } else if (['mult', '*'].includes(operator)) {
      runningTotal = multiply(a, b)
    } else if (['div', '/'].includes(operator)) {
      runningTotal = divide(a, b)
    }
    currentValue = ''
  }
  updateDisplay(runningTotal)
}

const addDigit = (digit) => {
  currentValue += digit
  updateDisplay(currentValue)
}

const addDecimal = () => {
  if (!decimal) {
    currentValue += '.'
    updateDisplay(currentValue)
    decimal = true
  }
}

const addOp = (op) => {
  if (operator === null) {
    runningTotal = (currentValue ? currentValue : 0)
  } else {
    calculate()
  }
  operator = op
  currentValue = ''
  decimal = false
  updateDisplay(operator)
}

const clearEntry = () => {
  currentValue = ''
  decimal = false
  updateDisplay(runningTotal)
}

acDiv.addEventListener('click', () => {
  runningTotal = 0
  currentValue = ''
  operator = null
  dacimal = false
  updateDisplay(runningTotal)
})

ceDiv.addEventListener('click', () => {
  clearEntry()
})

digits.forEach(elem => {
  let digit = elem.innerText
  elem.addEventListener('click', () => {
    addDigit(digit)
  })
})

decimalDiv.addEventListener('click', () => {
  addDecimal()
})

ops.forEach(elem => {
  let op = elem.id
  elem.addEventListener('click', () => {
    addOp(op)
  })
})

eqDiv.addEventListener('click', () => {
  calculate()
})

document.addEventListener('keydown', (evt) => {
  if (!isNaN(evt.key)) {
    addDigit(evt.key)
  } else if ('+-/*'.includes(evt.key)) {
    addOp(evt.key)
  } else if (evt.key === '.') {
    addDecimal()
  } else if (evt.key === 'Enter' || evt.key === '=') {
    calculate()
  } else if (evt.key === 'Backspace') {
    clearEntry()
  }
})
