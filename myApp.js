require('dotenv').config();
let mongoose=require('mongoose');

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true });

let personSchema = new mongoose.Schema({
  name: {
    type: String, 
    required: true
  },
  age: Number, 
  favoriteFoods: [String]
});

let Person = mongoose.model('Person', personSchema);

const createAndSavePerson = (done) => {
  let person = new Person({name: 'John Wick', age: 40, favoriteFoods: ['pizza', 'icecream']});
  person.save((error, data) => {
    if (error) return done(error);
    done(null, data);
  });
};

const createManyPeople = (arrayOfPeople, done) => {
  Person.create(arrayOfPeople, (err, data) => {
    if (err) return done(err);
    done(null, data);
  });
};

const findPeopleByName = (personName, done) => {
  Person.find({name: personName}, (err, data) => {
    if (err) return done(err);
    done(null, data);
  });
};

const findOneByFood = (food, done) => {
  Person.findOne({favoriteFoods: [food]}, (err, data) =>{
    if (err) return done(err);
    done(null, data);
  });
};

const findPersonById = (personId, done) => {
  Person.findById(personId, (error, data) =>{
    if (error) return done(error);
    done(null, data);
  });
};

const findEditThenSave = (personId, done) => {
  const foodToAdd = "hamburger";
  Person.findById(personId, (error, p) => {
    if (error) return done(error);
    p.favoriteFoods.push(foodToAdd);
    p.save((error, data) =>{
      if (error) return done(error);
      done(null, data);
    });
  });
};

const findAndUpdate = (personName, done) => {
  const ageToSet = 20;
  Person.findOneAndUpdate({name: personName}, {age: ageToSet}, {new: true}, (err, data) =>{
    if (err) return done(err);
    done(null, data);
  });
};

const removeById = (personId, done) => {
  Person.findByIdAndRemove(personId, (err, data)=>{
    if (err) return done(err);
    done(null, data);
  })
};

const removeManyPeople = (done) => {
  const nameToRemove = "Mary";
  Person.remove({name: nameToRemove}, (err, data)=>{
    if (err) return done(err);
    done(null, data);
  });
};

const queryChain = (done) => {
  const foodToSearch = "burrito";
  Person.find({'favoriteFoods': foodToSearch}).sort('name').limit(2).select('name favoriteFoods').exec((err, data)=>{
    if (err) return done(err);
    done(null, data);
  });
};

/** **Well Done !!**
/* You completed these challenges, let's go celebrate !
 */

//----- **DO NOT EDIT BELOW THIS LINE** ----------------------------------

exports.PersonModel = Person;
exports.createAndSavePerson = createAndSavePerson;
exports.findPeopleByName = findPeopleByName;
exports.findOneByFood = findOneByFood;
exports.findPersonById = findPersonById;
exports.findEditThenSave = findEditThenSave;
exports.findAndUpdate = findAndUpdate;
exports.createManyPeople = createManyPeople;
exports.removeById = removeById;
exports.removeManyPeople = removeManyPeople;
exports.queryChain = queryChain;
