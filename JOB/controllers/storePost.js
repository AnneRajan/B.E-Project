const Post = require('../database/models/Post')

module.exports = (req, res) => {
    console.log(req.body);
    
    const os = req.body.os;
    const aoa = req.body.aoa;
    const pc = req.body.pc;
    const se = req.body.se;
    const cn = req.body.cn;
    const ma = req.body.ma;
    const cs = req.body.cs;
    const hac = req.body.hac;
    const select = req.body.select;
    const cert = req.body.cert;
    const personality = req.body.personality;
    const management = req.body.management;
    const leadership = req.body.leadership;
    const team = req.body.team;
    const selfability = req.body.selfability;
    const technical = req.body.technical;

  
    const post = new Post({
    os: os,
    aoa: aoa,
    pc: pc,
    se: se,
    cn: cn,
    ma: ma,
    cs: cs,
    hac: hac,
    select: select,
    cert: cert,
    personality: personality,
    management: management,
    leadership: leadership,
    team: team,
    selfability: selfability,
    technical: technical
    });
     post.save()
        .then(result => {
            console.log('Details Saved');
            res.setHeader("Set-Cookie", "postID="+result.id+"; Path=/");
            res.redirect('/');
        })
        .catch(err => {
            console.log(err);
        });
};