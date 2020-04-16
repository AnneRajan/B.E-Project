const bcrypt = require('bcrypt')

const User = require('../database/models/User')

module.exports=(request,response)=>{
    const {email,pass} = request.body;

    User.findOne({email}, (error,user)=>{
        if(user)
        {
            bcrypt.compare(pass, user.pass,
                (error, same)=>{
                    if(same)
                    {
                        request.session.userId = user._id
                        response.redirect('/jobprofile')
                    }
                    else{
                        
                        response.redirect('/signup')
                        console.log('Error');
                    }
                })
        }
        else
        {
            return response.redirect('/signup')
        }
    })
    
}