const mongoose = require('mongoose')

const Post = require('./database/models/Post')

mongoose.connect('mongodb://localhost/career')


Post.create({
    os:89,
    aoa:85,
    pc:80,
    se:75,
    cn:89,
    ma:89,
    cs:89,
    hac:5,
    Select:'Analyst',
    cert: 'Python',
    personality:'yes',
    management: 'yes',
    leadership: 'yes',
    team: 'yes',
    selfability:'yes',
    technical:'yes'
},(error,post)=>{
    console.log(error,post)
})


Post.find({})
