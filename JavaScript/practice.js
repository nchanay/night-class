// Write a function to move all the elements of a list with value less than 10 to a new list and return it.
//
// function extract_less_than_ten(nums) {...}

const numList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

let newList = numList.filter(x => x < 10)

let newList2 = (nums) => numList.filter(x => x < 10)

function lessThanTen(nums) {
  let newList1 = []
  for (let i=0; i<nums.length; i++) {
    if (nums[i] < 10){
      newList1.push(nums[i])
    }
  }
  return newList1
}

function beep(nums) {
  let less_than_10 = []
  for (let num of nums) {
    if (num < 10) {
      less_than_10.push(num)
    }
  }
  return less_than_10
}

// Get a string from the user, print out another string, doubling every letter.
//
// function double_letters(x) {...}
//
// double_letters('hello')
// hheelllloo

function doubleLetters(phrase) {
  let double = ""
  for (let i=0; i<phrase.length; i++) {
    double += phrase[i] + phrase[i]
  }
  return double
}

function doubleLetters(phrase) {
  let double = []
  for (let letter of phrase) {
    double.push(letter + letter)
  }
  return double.join('')
}

function doubleLetters = (phrase) => phrase.split('').map(letter => letter + letter).join('')

doubleLetters("hello")

// Write a function to find all common elements between two lists.
//
// function common_elements(nums1, nums2) {...}

let nums1 = [1, 2, 3, 4, 5, 6, 7]
let nums2 = [4, 5, 6, 7, 8, 9, 10]

let common_elements = (nums1, nums2) => nums1.filter(x => nums2.includes(x));

const common_elements_using -sets = (nums1, nums2) => {
  const setA = new Set(nums1);
  const setB = new Set(nums2);
  const intersection = [...setA].filter(elem => setB.has(elem))
  return intersection
}

// Write a function that returns the maximum of 3 parameters.
//
// (Hint: use reduce)
//
// function maximum_of_three(a, b, c) {...}
//     ...
// maximum_of_three(5,6,2) → 6
// maximum_of_three(-4,3,10) → 10

const someList = [1, 2, 3]
const maximumOfThree = (accumulator, currentValue) => (accumulator > currentValue ? accumulator : currentValue)
someList.reduce(maximumOfThree)

let maximum_of_three = (a, b, c) = Math.max(a, b, c)
let maximum_of_three = (a, b, c) => {
  let running_max = -Infinity
  for(let num of [a, b, c]){
    if (num > running_max)
  }
}

// Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.
//
// fibonacci(8) → [1, 1, 2, 3, 5, 8, 13, 21]

const fibonacci = (n) => (n <= 1) ? n : (fibonacci(n-1) + fibonacci(n-2))

// Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.
//
// nums = [[5,2,3],[4,5,1],[7,6,3]]
// combine_all(nums) → [5,2,3,4,5,1,7,6,3]

const listOfLists = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
const combineAll = (lol) => {
  let test = lol.reduce((a,b) => a + b, [])
}

// Practice: write a dog class
// props: name, breed, (anything else you want)
// methods: bark (anything else you want)

class Dog {
  constructor(name, breed, color) {
    this.name = name
    this.breed = breed
    this.color = color
  }
  bark() {
    console.log(`${this.name}'s eye grow wide and she lets out a muffled woooof`)
  }
}

// Given a the two arrays, combine them into a dictionary.
//
// function lists_to_dict(keys, values) {
//     /*
//     returns dictionary of keys mapped to values
//     :keys: arr
//     :values: arr
//     */
//     lists_to_dict(['a', 'b', 'c'], ['aardvark', 'bear', 'coyote']) // {'a': 'aardvark', 'b': 'bear', 'c': 'coyote'}
// }

let dogs = ['Chihuahua', 'Mastif', 'Corgi']
let colors = ['brown', 'black', 'yellow']

function lists_to_dict(keys, values) {
  let combined = {}
  keys.map((elem, idx) => Object.assign(combined, {[elem]: values[idx]}))
  return combined
}

function lists_to_dict(keys, values) {
  return Object.assign({}, ...keys.map((n, i) => {[n]: values[i]}))
}

function  lists_to_dict(arry1, arry2) {
  return arry1.map((key, value) => [key, arry2[value]]).reduce((acc, cur) => {
    acc[cur[0]] = cur[1]
    return acc
  }, {})
}

// using old fashioned loop and logic
function lists_to_dict(keys, values) {
  let combined = {}
  for (let i=0; i<keys.length; i++) {
    combined[keys[i]] = values[i]
  }
  return combined
}

// Using the result from the previous problem, iterate through the dictionary and calculate the average price of an item.
//
// function average(d) { ... }
// combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}
// average(combined) // 2.2

let combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}

function average(dict) {
  let nums = []
  for (let key in dict) {
    nums.push(dict[key])
  }
  return nums.reduce((acc, cur) => acc + cur) / nums.length
}

// Average numbers whose keys start with the same letter. Output a dictionary containing those letters as keys and the averages.
//
// d = {'a1':4, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
// unify(d) -> {'a':3.0, 'b':4.0, 'c':5.0}

let d = {'a1':4, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}

function unify(d) {
  let runningSum = {}
  let val = d[key]
  for (let key in d) {
    if (runningSum.hasOwnProperty(key[0])) {
      currentSum, count = runningSum[key[0]]
      runningSum[key[0]] = [currentSum + val, count + 1]
    } else {
      runningSum[key[0]] = [val, 1]
    }
  }
return Object.assign({},...Object.entries(runningSum).map(([key, [rsum, count]]) => ({[key]: rsum/count})))
}

// Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
//
// fizzbuzz(15)
// // output
// 1
// 2
// fizz
// 4
// buzz
// fizz
// 7
// 8
// fizz
// buzz
// 11
// fizz
// 13
// 14
// fizzbuzz

// Now try this with multiples of 7 as 'fuzz' and multiples of 9 as 'baz' in addition to 'fizz' and 'buzz'.

function fizzbuzz(n) {
  for (let i=1; i<=n; i++) {
    let num = ''
    if (i % 3 === 0) num += 'fizz'
    if (i % 5 === 0) num += 'buzz'
    if (i % 7 === 0) num += 'fuzz'
    if (i % 9 === 0) num += 'baz'
    console.log(num ? num : i)
  }
}

function fizzBuzzFuzzBaz(n) {
  const translate = {3: 'Fizz', 5: 'Buzz', 7: 'Fuzz', 9: 'Baz'}
  for (let i=1; i<=n; i++) {
    let num = ''
    for (let k in translate) {
      if (i % k === 0) num += translate[k]
    }
    console.log(num ? num : i)
  }
}
