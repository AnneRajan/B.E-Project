const mongoose = require('mongoose')

const PostSchema = new mongoose.Schema({

    os: Number,
    aoa: Number,
    pc: Number,
    se: Number,
    cn: Number,
    ma: Number,
    cs: Number,
    hac: Number,
    select: Array,
    cert: Array,
    personality: String,
    management: String,
    leadership:String,
    team: String,
    selfability: String,
    technical: String
})

const Post = mongoose.model('post', PostSchema)

module.exports =Post;

