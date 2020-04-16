const User = require('../database/models/User')

module.exports = (req, res) => {
    console.log(req.body);
    const first_name = req.body.first_name;
    const last_name = req.body.last_name;
    const company = req.body.company;
    const email = req.body.email;
    const pass = req.body.pass;
    
    
    const user = new User({
        first_name: first_name,
        last_name: last_name,
        company: company,
        email:email,
        pass: pass
    });
    user
        .save()
        .then(result => {
            console.log('Details Saved');
            res.setHeader("Set-Cookie", "userID="+result.id+"; Path=/");
            res.redirect('/signup');
        })
        .catch(err => {
            console.log(err);
        });
};