
const http = require('http')
const fs = require('fs')
const express = require('express');
const app = express();
const { config, engine } = require('express-edge');
const path = require('path')
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
const expressSession = require('express-session')

const storeUserController = require('./controllers/storeUser');
const loginUserController = require('./controllers/loginUser');
const storePostController = require('./controllers/storePost');


const auth = require("./middleware/auth")
app.use('/jobprofile/new',  auth)


mongoose.set('useCreateIndex', true);

app.use(express.static('public'))
app.use(engine);
app.set('views', `${__dirname}/views`);

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended:true}))


mongoose.connect('mongodb://localhost:27017/career')
    .then(()=>{ console.log("Connected to mongoD") })
    .catch((err) =>{
        console.log(`Error Dude ${err}`)
    });

    
const connectMongo = require('connect-mongo')
const mongoStore = connectMongo(expressSession)

app.use(expressSession({
    secret: 'secret',
    store: new mongoStore({
    mongooseConnection: mongoose.connection
    })
}))


app.get('/', (req, res) => {
    res.render('index')
   
});



// app.get('/auth/create', createUserController)


app.get('/signup', (req, res)=>{
    res.render('signup')
})

app.post('/users/signup', loginUserController)


app.get('/create', (req, res)=>{
    if(req.session.userId)
    {
       return res.render("create");
    }

    res.redirect('/signup')
  
})

app.post('/users/create', storeUserController)

app.get('/jobprofile', (req, res)=>{
    res.render('jobprofile')
})

app.post('/posts/jobprofile', storePostController)


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

 
 app.get('/pages/resume.html', (req,res)=>{
    res.sendFile(path.resolve(__dirname, 'pages/resume.html'))
})
 



app.listen(4000, ()=>{
    console.log("App Listening on 4000")
})




