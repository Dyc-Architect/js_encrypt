var JSEncrypt  = require('node-jsencrypt');
function encrypt(password, privateKey) {
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey( privateKey );
    password = encrypt.encrypt( password );
    return password
}
var privateKey = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC2xXVwY4zjla1NpGwg6Z0KULKo\nWEvWdhilmXEf+lyIJ61Ygxo3SNK82G0Kz1OWSQnufGyZLIOB58O4/GIvCmc6Dxjn\ncRLDKgU6wyZ3GQpAqVUix8FN3H8eESt22vyL0v8ccOUOZoIX0+YDs2R5dYAS5Zky\nxCjygZ6s/gBJpmIh8QIDAQAB\n-----END PUBLIC KEY-----\n";
var password = '123456'
console.log(encrypt(password,privateKey))
