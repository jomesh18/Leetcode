const { init } = require("../server");

function ConvertHandler() {
  
  this.getNum = function(input) {
    let result;
    result = input.match(/[0-9.\/]+/g);
    console.log(result);
    if (!result) return 'not given';
    if (result.length > 1) return null;
    result = result[0];
    if (result.split('/').length > 2){
      return null;
    }
    else if (result.split('/').length == 2){
      let arr = result.split('/');
      return arr[0]/arr[1];
    }
    else {
      return result;
    }
  };
  
  this.getUnit = function(input) {
    let result;
    result = input.match(/[A-Za-z]+/g);
    if (!result || result.length > 1) return null;
    result = result[0].toLowerCase();
    let valid_units = ['gal', 'l', 'lbs', 'kg', 'mi', 'km'];
    if (!valid_units.includes(result)){
      return null;
    } else {
      if (result == 'l'){
        return 'L';
      } else {
        return result;
      }
    }
  };
  
  this.getReturnUnit = function(initUnit) {
    let result;
    switch(initUnit){
      case 'L':
        result = 'gal';
        break;
      case 'gal':
        result = 'L';
        break;
      case 'mi':
        result = 'km';
        break;
      case 'km':
        result = 'mi';
        break;
      case 'lbs':
        result = 'kg';
        break;
      case 'kg':
        result = 'lbs';
        break;
    }
    return result;
  };

  this.spellOutUnit = function(unit) {
    let res;
    switch (unit){
      case 'L':
        res = 'liters';
        break;
      case 'gal':
        res = 'gallons';
        break;
      case 'mi':
        res = 'miles';
        break;
      case 'km':
        res = 'kilometers';
        break;
      case 'lbs':
        res = 'pounds';
        break;
      case 'kg':
        res = 'kilograms';
        break;
    }
    return res;
  };
  
  this.convert = function(initNum, initUnit) {
    const galToL = 3.78541;
    const lbsToKg = 0.453592;
    const miToKm = 1.60934;
    let result;
    switch (initUnit){
      case 'gal':
        result = [parseFloat(initNum*galToL).toFixed(5), 'L'];
        break;
      case 'L':
        result = [parseFloat(initNum/galToL).toFixed(5), 'gal'];
        break;
      case 'lbs':
        result = [parseFloat(initNum*lbsToKg).toFixed(5), 'kg'];
        break;
      case 'kg':
        result = [parseFloat(initNum/lbsToKg).toFixed(5), 'lbs'];
        break;
      case 'mi':
        result = [parseFloat(initNum*miToKm).toFixed(5), 'km'];
        break;
      case 'km':
        result = [parseFloat(initNum/miToKm).toFixed(5), 'mi'];
        break;
    }
    return result;
  };
  
  this.getString = function(initNum, initUnit, returnNum, returnUnit) {
    let result;
    result = `${initNum} ${this.spellOutUnit(initUnit)} converts to ${returnNum} ${this.spellOutUnit(returnUnit)}`;
    return result;
  };
  
}

module.exports = ConvertHandler;
