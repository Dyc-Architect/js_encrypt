var JSEncrypt  = require('node-jsencrypt');
function encrypt(password) {
    var publicKey = "-----BEGIN PUBLIC KEY-----"
+"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqCvtrtBBeP/LIO6VtFAUItx9Dwi9lXRX"
+"sSHT8C9p/yQ9FaUjB8YQTI7FL/HxggTU+P61A3a17GK23Whm4VNkriIDJZVd7opqnGzGC0XAdeml"
+"LCxmutZIypbUEhQmd68pZ+74e6QH2lu/lcukFFSdeI6p5IaWAUgvOjzPGUCZLKuABfhw8LoOmcFW"
+"LgPMQy6BZheKBqiLvFTx5eX9VbzaPCfZsSCxPRXb4snL5QyIbtBppamPW5TkUcGPECMNdbpfbIoX"
+"LBGhcxqrYEGNtXEwu47eOUBLbPPrE0o5KZ7sw3b1LepoxH3MXKpDHcBg1n3jUreE5ZfcNLX1GWKs"
+"eyNQiQIDAQAB"
+"-----END PUBLIC KEY-----";
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(publicKey);
    password = encrypt.encrypt(password);
    return password
}

var password = '123456'
console.log(encrypt(password))
