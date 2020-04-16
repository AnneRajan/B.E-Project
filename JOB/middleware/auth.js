const User =  require('../database/models/User')
module.exports = (req, res,next)=>{
    User.findById(req.Session.userId,(error,user)=>{
        if(error || !user)
        {
            return res.redirect('/')
        }
        next()
    })
}