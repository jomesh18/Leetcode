'use strict';
const mongoose = require('mongoose');
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true });
let issueSchema = new mongoose.Schema({
  "issue_title": {type: String, required: true}, 
  "issue_text": {type: String, required: true}, 
  "created_by": {type: String, required: true}, 
  "assigned_to": String,
  "status_text": String,
  "created_on": {type: Date, default: mongoose.now()},
  "updated_on": {type: Date, default: mongoose.now()},
  "open": {type: Boolean, default: true},
});

let projectSchema = new mongoose.Schema({
  "project": {type: String, required: true},
  "issues": [issueSchema]
})

let Issue = mongoose.model('Issue', issueSchema);
let Project = mongoose.model('Project', projectSchema);

let findProject = (project, done) => {
  Project.findOne({'project': project}, (err, data) => {
    if (err) return done(err);
    return done(null, data);
  });
}

let createNewProject = (project, done) => {
  new Project({'project': project}).save((err, data) => {
    if (err) return done(err);
    return done(null, data);
  });
}

let addIssueToProject = (proj, data, done) => {
  proj["issues"].push(new Issue({
    "issue_title": data.issue_title, 
    "issue_text": data.issue_text, 
    "created_by": data.created_by, 
    "assigned_to": data.assigned_to,
    "status_text": data.status_text
  }));
  proj.save((err, dat) =>{
    if(err) return err;
    return done(null, dat);
  });
}

module.exports = function (app) {

  app.route('/api/issues/:project')
  
  .get(function (req, res){
    let project = req.params.project;
    findProject(project, (err, data) => {
      if (err) return err;
      res.send(data['issues']);
    });
  })
  
  .post(function (req, res){
    let project = req.params.project;
    if (!req.body.issue_title || !req.body.issue_text || !req.body.created_by){
      res.json({ error: 'required field(s) missing' });
    }
    else{
      let projData = {
        "issue_title": req.body.issue_title, 
        "issue_text": req.body.issue_text, 
        "created_by": req.body.created_by, 
        "assigned_to": req.body.assigned_to || "",
        "status_text": req.body.status_text || ""
      }
      findProject(project, (err, data) => {
        if (err) return err;
        if (!data){
          createNewProject(project, (e, d) => {
            // console.log('e and d are', e, d);
            if (e) return e;
            addIssueToProject(d, projData, (err1, data1) => {
              if (err1) return err1;
              // console.log("CREATED DATA IS", data1);
              return res.json({
                "_id": "5871dda29faedc3491ff93bb",
              "issue_title": data1.issues[data1.issues.length-1].issue_title,
              "issue_text": data1.issues[data1.issues.length-1].issue_text,
              "created_on": data1.issues[data1.issues.length-1].created_on,
              "updated_on": data1.issues[data1.issues.length-1].updated_on,
              "created_by": data1.issues[data1.issues.length-1].created_by,
              "assigned_to": data1.issues[data1.issues.length-1].assigned_to,
              "open": data1.issues[data1.issues.length-1].open,
              "status_text": data1.issues[data1.issues.length-1].status_text,
              });
            })
          });
        }
        else{
          addIssueToProject(data, projData, (err1, data1) => {
            if (err) return err;
            // console.log("DATA IS", data1);
            return res.json({
              "_id": "5871dda29faedc3491ff93bb",
              "issue_title": data1.issues[data1.issues.length-1].issue_title,
              "issue_text": data1.issues[data1.issues.length-1].issue_text,
              "created_on": data1.issues[data1.issues.length-1].created_on,
              "updated_on": data1.issues[data1.issues.length-1].updated_on,
              "created_by": data1.issues[data1.issues.length-1].created_by,
              "assigned_to": data1.issues[data1.issues.length-1].assigned_to,
              "open": data1.issues[data1.issues.length-1].open,
              "status_text": data1.issues[data1.issues.length-1].status_text,
            });
        })
        }
      });  
    }
  })
    
    .put(function (req, res){
      let project = req.params.project;
      console.log(req.body);
      if (!req.body._id){
        res.json({ error: 'missing _id' });
      }
      else{
        let to_update = {};
        if (req.body.issue_text){
          to_update['issue_text'] = req.body.issue_text
        }
        if (req.body.issue_title){
          to_update['issue_title'] = req.body.issue_title
        }
        if (req.body.created_by){
          to_update['created_by'] = req.body.created_by
        }
        if (req.body.assigned_to){
          to_update['assigned_to'] = req.body.assigned_to
        }
        if (req.body.status_text){
          to_update['status_text'] = req.body.status_text
        }
        if (req.body.open){
          to_update['open'] = false;
        }
        if (!to_update) {
          res.json({ error: 'could not update', '_id': _id });
        }
        findProject(project, (err, dat) => {
          if (err) return err
          dat.findOneAndUpdate({project: project, issues._id: req.body._id}, to_update, (err, data) => {
            if (err) return err;
            console.log(data);
          })
        })
      }
    })
    
    .delete(function (req, res){
      let project = req.params.project;
      
    });
    
};
