# ES_6 - JavaScript basics

## General :clap:
- ES6, or ECMAScript 6, is the sixth edition of the ECMAScript standard, introducing significant enhancements and new features to JavaScript.
- Key features of ES6 include arrow functions, template literals, classes, destructuring assignment, default function parameters, rest parameters, and spread syntax.
- Constants (declared with const) cannot be reassigned after initialization, while variables (declared with let) can be reassigned.
- Block-scoped variables in ES6 are limited to the block of code in which they are defined, including nested blocks.
- Arrow functions provide a concise syntax for defining functions, with lexical this binding.
- Rest parameters allow functions to accept an indefinite number of arguments, while spread syntax expands arrays in function calls.
- Template literals use backticks for easier interpolation of variables and expressions within strings.
- Object creation in ES6 includes shorthand property names, computed property names, method definitions, and object destructuring.
- Iterators and for-of loops simplify iteration over arrays, strings, and objects, providing a standardized way to produce sequences of values.

## Requirements 🚔
- The code should use the js extension.
- The code will be tested using the `Jest Testing Framework`
- The code will be analyzed using the linter `ESLint` along with specific rules that we’ll provide.
- All of functions must be exported.

### Setup 💻
- Install NodeJS : `curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh`
                    `sudo bash nodesource_setup.sh`
                    `sudo apt install nodejs -y`
- Install Jest : `npm install --save-dev jest`
- Install Babel : `npm install --save-dev babel-jest @babel/core @babel/preset-env`
- Install ESLint : `npm install --save-dev eslint`
- run `npm install`

### Configuration files 📁
- Create this files : package.json / babel.config.js / .eslintrc.js

## Tasks 🌵
0. Const or let? : Modify those function `taskFirst` to instantiate variables using `const` and `taskNext` to instantiate variables using `let`
1. Block Scope : Given what you’ve read about var and hoisting, modify the variables inside the function `taskBlock` so that the variables aren’t overwritten inside the conditional block.
2. Arrow functions : Rewrite the following standard function to use ES6’s arrow syntax of the function `add` (it will be an anonymous function after).
3. Parameter defaults : Condense the internals of the following function to 1 line - without changing the name of each function/variable.
4. Rest parameter syntax for functions : Modify the function to return the number of arguments passed to it using the rest parameter syntax
5. The wonders of spread syntax : Using spread syntax, concatenate 2 arrays and each character of a string by modifying the function below. Your function body should be one line long.
6. Take advantage of template literals : Rewrite the return statement to use a template literal so you can the substitute the variables you’ve defined.
7. Object property value shorthand syntax : Modify the function’s `budget` object to simply use the object property value shorthand syntax instead.
8. No need to create empty objects before adding in properties : Rewrite the `getBudgetForCurrentYear` function to use ES6 computed property names on the `budget` object.
9. ES6 method properties: Rewrite `getFullBudgetObject` to use ES6 method properties in the `fullBudget` object.
10. For...of Loops : Rewrite the function `appendToEachArrayValue` to use ES6’s `for...of` operator. And don’t forget that `var` is not ES6-friendly.
11. Iterator : Write a function named create `EmployeesObject` that will receive two arguments: `departmentName` (String) `employees` (Array of Strings).
12. Let's create a report object : Write a function named `createReportObject` whose parameter, `employeesList`, is the return value of the previous function `createEmployeesObject`.

## Authors 🧞‍♀️
Sarah Boutier