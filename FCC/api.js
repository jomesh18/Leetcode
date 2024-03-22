'use strict';

const expect = require('chai').expect;
const ConvertHandler = require('../controllers/convertHandler.js');
console.log(`inside api ${typeof ConvertHandler}`);
module.exports = function (app) {
  
  let convertHandler = new ConvertHandler();

  app.get('/api/convert/', (req, res) => {
    const inp = req.query.input;
    console.log(`Input is ${inp}`);
    let val = convertHandler.getNum(inp);
    console.log(`Value is ${val}`);
    let unit = convertHandler.getUnit(inp);
    console.log(`Unit is ${unit}`);
    if (!val & !unit){
      res.send('invalid number and unit');
    } else if (!val){
      res.send('invalid number');
    } else if (!unit){
      res.send('invalid unit');
    }
    else{
      if (val == 'not given') val = 1;
      let returnUnit = convertHandler.getReturnUnit(unit);
      console.log(`Return unit is ${returnUnit}`);
      let arr = convertHandler.convert(val, unit);
      let convertedValue = arr[0];
      let convertedUnit = arr[1];
      console.log(`Return value and unit is ${convertedValue} and ${convertedUnit}`);
      let returnString = convertHandler.getString(val, unit, convertedValue, convertedUnit);
      console.log(`Return string is ${returnString}`);
      res.json({
        initNum: val, initUnit: unit, returnNum: convertedValue, returnUnit: convertedUnit, string: returnString
      });
    }
  });
}