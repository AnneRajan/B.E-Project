

const http = require('http')
const fs = require('fs')
const express = require('express');
const app = express();
const { config, engine } = require('express-edge');
const path = require('path')
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
const Post = require('./database/models/Post')


app.use(express.static('public'))
app.use(engine);
app.set('views', `${__dirname}/views`);


app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended:true}))

 mongoose.connect('mongodb://localhost/career')


app.get('/', (req, res) => {
    res.render('index')
});


app.get('/jobprofile', (req, res)=>{
    res.render('jobprofile')
})


app.get('/resume', (req, res)=>{
    res.render('resume')
})


app.get('/pages/frames.html', (req,res)=>{
    res.sendFile(path.resolve(__dirname, 'pages/frames.html'))
})

app.get('/pages/framesearch.html', (req,res)=>{
    res.sendFile(path.resolve(__dirname, 'pages/framesearch.html'))
})

app.get('/pages/frame_left.html', (req,res)=>{
    res.sendFile(path.resolve(__dirname, 'pages/frame_left.html'))
})

app.get('/pages/frame_right.html', (req,res)=>{
    res.sendFile(path.resolve(__dirname, 'pages/frame_right.html'))
})


app.post('/posts/store', (req,res)=>{
    res.redirect('/')
    console.log(req.body)
})

app.get('/create', (req, res)=>{
    res.render('create')
})


app.get('/signup', (req, res)=>{
    res.render('signup')
})


app.listen(4000, ()=>{
    console.log("App Listening on 4000")
})




