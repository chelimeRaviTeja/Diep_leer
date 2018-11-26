const mongoose = require('mongoose');

mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost:27017/Diep_leer', {useNewUrlParser:true});
mongoose.set('useCreateIndex', true);

module.exports = {mongoose};
