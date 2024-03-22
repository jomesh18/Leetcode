const chai = require('chai');
let assert = chai.assert;
const ConvertHandler = require('../controllers/convertHandler.js');

// console.log(`inside unit test ${typeof ConvertHandler}`);
// let convertHandler = new ConvertHandler();

// suite('Unit Tests', function(){
//     // 1 convertHandler should correctly read a whole number input.
//     test('inp in a whole number', () => {
//         assert.equal(convertHandler.getNum('10mi'), '10');
//     });
//     // 2 convertHandler should correctly read a decimal number input.
//     test('inp is a decimal', () => {
//         assert.equal(convertHandler.getNum('10.2mi'), '10.2');
//     });
//     // 3 convertHandler should correctly read a fractional input.
//     test('inp is fractional', () => {
//         assert.equal(convertHandler.getNum('5/3'), 5/3);
//     });
//     // 4 convertHandler should correctly read a fractional input with a decimal.
//     test('inp is fractional with decimal', () => {
//         assert.equal(convertHandler.getNum('5.3/3'), 5.3/3);
//     });
//     // 5 convertHandler should correctly return an error on a double-fraction (i.e. 3/2/3).
//     test('inp is double fraction', () => {
//         assert.equal(convertHandler.getNum('2/3/5'), null);
//     });
//     // 6 convertHandler should correctly default to a numerical input of 1 when no numerical input is provided.
//     test('no numerical input', () => {
//         assert.equal(convertHandler.getNum('mi'), 1);
//     });
// });