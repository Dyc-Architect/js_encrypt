var JSEncrypt = require('node-jsencrypt')
function login_rsa_encrypt(pwd) {

    var PUBLIC_KEY = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCrLCvPQVj1dYDdtb34bUGrxAYHLDMQdsjbk7+pY/ugKdHKhxQo1E43gt4HMgjFuirvaGfh1NJ2FCX9thillLZlHhkNOUcEQSbpcJycQ9wq7FBtOk7lE0dBBA9t3Zk/qBx2A2xPVvVNf9lNdNDDp2vXhQ549H9hg1s1TPHFEags3QIDAQAB';
    PUBLIC_KEY = '-----BEGIN PUBLIC KEY-----' + PUBLIC_KEY + '-----END PUBLIC KEY-----';
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(PUBLIC_KEY);
    var encrypted = encrypt.encrypt(pwd);
    return encrypted;
}
console.log(login_rsa_encrypt('123456'))
