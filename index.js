const express = require('express')
const app = express()
const cors = require('cors')
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
require('dotenv').config()

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true });
app.use(bodyParser.urlencoded({extended: false}));

app.use(cors())
app.use(express.static('public'))
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/views/index.html')
});


const listener = app.listen(process.env.PORT || 3000, () => {
  console.log('Your app is listening on port ' + listener.address().port)
})

let exerciseSchema = new mongoose.Schema({
  "description": String,
  "duration": Number,
  "date": String
});

let userSchema = new mongoose.Schema({
  "username": String, 
  "log": [exerciseSchema],
});

let User = mongoose.model('User', userSchema);
let Exercise = mongoose.model('Exercise', exerciseSchema);

getUserByName = (user, done) => {
  User.findOne({"username": user}, (err, data) => {
    if (err) return done(err);
    return done(null, data);
  });
}

getAllUsers = (done) => {
  User.find({}, 'username',(err, data) => {
    if (err) return done(err);
    return done(null, data);
  });
}

getUserById = (id, done) => {
  User.findOne({"_id": id}, (err, data) => {
    if (err) return done(err);
    return done(null, data);
  });
}

searchUser = (user, done) => {
  User.findOne({"username": user}, (err, data) => {
    if (err) return done(err);
    return done(null, data);
  })
}

createUser = (user, done) => {
  new User({"username": user}).save((err, data) => {
    if (err) return done(err);
    return done(null, data);
  });
};

app.post('/api/users', (req, res) => {
  let user = req.body.username;
  searchUser(user, (err, data) => {
    if (err) return err;
    if (!data){
      createUser(user, (er, dat) => {
        if (er) return er;
        console.log('created user ', dat);
        res.json({
          username: user,
          _id: dat['_id']
        });
      });
    }
    else{
      console.log('already added user ', data);
      res.json({
        username: user,
        _id: data['_id']
      });
    }
  });
});

app.get('/api/users/:user', (req, res) => {
  let user = req.params["user"];
  getUserByName(user, (err, data) => {
    if (err) return err;
    if (data) {
      res.json({
        'username': data['user'],
        '_id': data['_id']
      });
    }
  });
});

app.get('/api/users', (req, res) => {
  getAllUsers((err, data) =>{
    if (err) return err;
    res.send(data);
  })
});

app.post('/api/users/:_id/exercises', (req, res) => {
  let _id = req.params._id;
  getUserById(_id, (err1, data1) => {
    if (err1) return err1;
    let date;
    if (req.body.date) {
      let got_date = new Date(req.body.date);
      if (got_date){
        date = new Date(req.body.date).toDateString();
      }
      else{
        date = new Date().toDateString(); 
      }
    }
    else{
      date = new Date().toDateString();
    }
    data1['log'].push(new Exercise({"description": req.body.description, "duration": req.body.duration, "date": date}));
    data1.save((err2, data2) =>{
      if (err2) return err2;
      console.log("inside post/exercies, dat is ", data2);
      res.json({
        username: data1['username'],
        description: req.body.description, 
        duration: Number(req.body.duration), 
        date: date,
        _id: _id
      });
    });
  });
});

app.get('/api/users/:_id/logs', (req, res) => {
  let _id = req.params._id;
  getUserById(_id, (err, data) => {
    if (!err){
      console.log('type of data is ', typeof data);
      console.log('data is ', data);
      if (req.query.from){
        data['log'] = data['log'].filter((d) => new Date(d['date']) >= new Date(req.query.from));
        console.log("from data is ", data);
      }
      if (req.query.to){
        data['log'] = data['log'].filter((d) => new Date(d['date']) <= new Date(req.query.to));
        console.log('to date is ', req.query.to);
        console.log("to data is ", data);
      }
      data['log'] = data['log'].sort((a, b) => b['date'] - a['date']);
      console.log("sorted data is ", data);
      if (req.query.limit){
        data['log'] = data['log'].slice(0, req.query.limit);
        console.log("limited data is ", data);
      }
      res.json({
        username: data['username'],
        count: data['log'].length,
        _id: _id,
        log: data['log']
      });
    }
  });
});
