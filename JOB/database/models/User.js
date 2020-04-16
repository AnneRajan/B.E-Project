const mongoose = require('mongoose')
const bcrypt = require('bcrypt')

const UserSchema = new mongoose.Schema({

    first_name: {
        type:String,
        required:true,
        
    },

    last_name: {
        type:String,
        required:true,
        
    },

    company: {
        type:String,
        required:true,
        
    },

    
    email: {
        type:String,
        required:true,
        unique:true
        
    },

    
    pass: {
        type:String,
        required:true,
        
    }
  
})

UserSchema.pre('save', function(next){
    const user = this

    bcrypt.hash(user.pass,10,function(error,encrypted){
        user.pass=encrypted
        next()
    })
})

module.exports = mongoose.model('User', UserSchema)