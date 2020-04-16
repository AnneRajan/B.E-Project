
const http = require('http')
const fs = require('fs')
const express = require('express');
const app = express();
const { config, engine } = require('express-edge');
const path = require('path')
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
const expressSession = require('express-session')
var amqp = require('amqplib/callback_api');

const storeUserController = require('./controllers/storeUser');
const loginUserController = require('./controllers/loginUser');
const storePostController = require('./controllers/storePost');

const spawn = require('child_process').spawn;
const process = spawn('Python',['./app.py']);
process.stdout.on('data', data =>{
    console.log(data.toString());
})


const auth = require("./middleware/auth")
app.use('/jobprofile/new',  auth)




mongoose.set('useCreateIndex', true);

app.use(express.static('public'))

app.use(express.static('skill'))



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
    res.render('create')
})


// app.get('/create', (req, res)=>{
//     if(req.session.userId)
//     {
//        return res.render("create");
//     }

//     res.redirect('/signup')
  
// })

app.post('/users/create', storeUserController)

app.get('/jobprofile', (req, res)=>{
    res.render('jobprofile')
})

app.post('/posts/jobprofile', (request,res)=>{
    var results;
    os          = request.body.os
    aoa         = request.body.aoa
    pc          = request.body.pc
    se          = request.body.se
    cn          = request.body.cn
    ma          = request.body.ma
    cs          = request.body.cs
    hac         = request.body.hac
    interest    = request.body.interest
    cert        = request.body.cert
    personality = request.body.personality
    mantech     = request.body.mantech
    leadership  = request.body.leadership
    team        = request.body.team
    selfab      = request.body.selfab
    var input = [os,aoa,pc,se,cn,ma,cs,hac,interest,cert,personality,mantech,leadership,team,selfab]
    amqp.connect('amqp://localhost', function (err, conn) {
    conn.createChannel(function (err, ch) {
      var simulations = 'simulations';
      ch.assertQueue(simulations, { durable: false });
      results = 'results';
      ch.assertQueue(results, { durable: false });
      ch.sendToQueue(simulations, new Buffer(JSON.stringify(input)));
      ch.consume(results, function (msg) {
        res.send(msg.content.toString())
      }, { noAck: true });
    });
    setTimeout(function () { conn.close(); }, 500); 
    });
    console.log(results)

})



app.get('/main', (req, res)=>{
    res.render('main')
})

 
 app.get('/pages/resume.html', (req,res)=>{
    res.sendFile(path.resolve(__dirname, 'pages/resume.html'))
})
 



app.listen(4000, ()=>{
    console.log("App Listening on 4000")
})




