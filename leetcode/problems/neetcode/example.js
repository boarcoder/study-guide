

/*



*/
const testCase = (expected, actual, message) => {

    console.log(`
    message: ${message}
    expected: ${expected}
    actual: ${actual}
    `)
}

let input = 'asdf'
testCase(
    'fdsa',
    reverseString(input)
    ,'should reverse a string'
)

input = 'asdfone'
testCase(
    'fdsa',
    reverseString(input)
    ,'should reverse a string'
)

input = 'asdf1234asd'
testCase(
    'dsaf4321dsa',
    reverseString(input)
    ,'should reverse a string'
)