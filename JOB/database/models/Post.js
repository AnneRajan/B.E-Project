const mongoose = require('mongoose')

const PostSchema = new mongoose.Schema({
    os: Number,
    aoa: Number,
    pc:Number,
    se:Number,
    cn:Number,
    ma:Number,
    cs:Number,
    hac:Number,
    Select:String
})

const Post = mongoose.model('Post', PostSchema)

module.exports = Post