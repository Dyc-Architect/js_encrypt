const CryptoJS = require("crypto-js")

function rndString() {
    for (var e = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz", t = "", n = 0; n < 16; n++) {
        var a = Math.floor(Math.random() * e.length);
        t += e.substring(a, a + 1)
    }
    return t
}


var utils = {
    desEncrypt: function (e, t) {
        var n = CryptoJS.enc.Utf8.parse(t);
        return CryptoJS.DES.encrypt(e, n, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        }).toString()
    },
};


function RSAEncrypt(e, t) {
    return (setMaxDigits(130), encryptedString(new RSAKeyPair("10001", "", t), e))
}

function setMaxDigits(e) {
    ZERO_ARRAY = new Array(maxDigits = e);
    for (var t = 0; t < ZERO_ARRAY.length; t++)
        ZERO_ARRAY[t] = 0;
    bigZero = new BigInt,
        (bigOne = new BigInt).digits[0] = 1
}

function BigInt(e) {
    this.digits = "boolean" == typeof e && 1 == e ? null : ZERO_ARRAY.slice(0),
        this.isNeg = !1
}

function encryptedString(e, t) {
    for (var n = new Array, a = t.length, i = 0; i < a;)
        n[i] = t.charCodeAt(i),
            i++;
    for (; n.length % e.chunkSize != 0;)
        n[i++] = 0;
    var r, o, s, l = n.length, d = "";
    for (i = 0; i < l; i += e.chunkSize) {
        for (s = new BigInt,
                 r = 0,
                 o = i; o < i + e.chunkSize; ++r)
            s.digits[r] = n[o++],
                s.digits[r] += n[o++] << 8;
        var u = e.barrett.powMod(s, e.e);
        d += (16 == e.radix ? biToHex(u) : biToString(u, e.radix)) + " "
    }
    return d.substring(0, d.length - 1)
}

function RSAKeyPair(e, t, n) {
    this.e = biFromHex(e),
        this.d = biFromHex(t),
        this.m = biFromHex(n),
        this.chunkSize = 2 * biHighIndex(this.m),
        this.radix = 16,
        this.barrett = new BarrettMu(this.m)
}

function hexToDigit(e) {
    for (var t = 0, n = Math.min(e.length, 4), a = 0; a < n; ++a)
        t <<= 4,
            t |= charToHex(e.charCodeAt(a));
    return t
}

function biFromHex(e) {
    for (var t = new BigInt, n = e.length, a = 0; n > 0; n -= 4,
        ++a)
        t.digits[a] = hexToDigit(e.substr(Math.max(n - 4, 0), Math.min(n, 4)));
    return t
}

function charToHex(e) {
    return e >= 48 && e <= 57 ? e - 48 : e >= 65 && e <= 90 ? 10 + e - 65 : e >= 97 && e <= 122 ? 10 + e - 97 : 0
}

function biHighIndex(e) {
    for (var t = e.digits.length - 1; t > 0 && 0 == e.digits[t];)
        --t;
    return t
}

function BarrettMu(e) {
    this.modulus = biCopy(e),
        this.k = biHighIndex(this.modulus) + 1;
    var t = new BigInt;
    t.digits[2 * this.k] = 1,
        this.mu = biDivide(t, this.modulus),
        this.bkplus1 = new BigInt,
        this.bkplus1.digits[this.k + 1] = 1,
        this.modulo = BarrettMu_modulo,
        this.multiplyMod = BarrettMu_multiplyMod,
        this.powMod = BarrettMu_powMod
}

function biCopy(e) {
    var t = new BigInt(!0);
    return t.digits = e.digits.slice(0),
        t.isNeg = e.isNeg,
        t
}

function biDivideModulo(e, t) {
    var n, a, i = biNumBits(e), r = biNumBits(t), o = t.isNeg;
    if (i < r)
        return e.isNeg ? ((n = biCopy(bigOne)).isNeg = !t.isNeg,
            e.isNeg = !1,
            t.isNeg = !1,
            a = biSubtract(t, e),
            e.isNeg = !0,
            t.isNeg = o) : (n = new BigInt,
            a = biCopy(e)),
            new Array(n, a);
    n = new BigInt,
        a = e;
    for (var s = Math.ceil(r / bitsPerDigit) - 1, l = 0; t.digits[s] < biHalfRadix;)
        t = biShiftLeft(t, 1),
            ++l,
            ++r,
            s = Math.ceil(r / bitsPerDigit) - 1;
    a = biShiftLeft(a, l),
        i += l;
    for (var d = Math.ceil(i / bitsPerDigit) - 1, u = biMultiplyByRadixPower(t, d - s); -1 != biCompare(a, u);)
        ++n.digits[d - s],
            a = biSubtract(a, u);
    for (var c = d; c > s; --c) {
        var m = c >= a.digits.length ? 0 : a.digits[c]
            , p = c - 1 >= a.digits.length ? 0 : a.digits[c - 1]
            , f = c - 2 >= a.digits.length ? 0 : a.digits[c - 2]
            , h = s >= t.digits.length ? 0 : t.digits[s]
            , g = s - 1 >= t.digits.length ? 0 : t.digits[s - 1];
        n.digits[c - s - 1] = m == h ? maxDigitVal : Math.floor((m * biRadix + p) / h);
        for (var _ = n.digits[c - s - 1] * (h * biRadix + g), b = m * biRadixSquared + (p * biRadix + f); _ > b;)
            --n.digits[c - s - 1],
                _ = n.digits[c - s - 1] * (h * biRadix | g),
                b = m * biRadix * biRadix + (p * biRadix + f);
        (a = biSubtract(a, biMultiplyDigit(u = biMultiplyByRadixPower(t, c - s - 1), n.digits[c - s - 1]))).isNeg && (a = biAdd(a, u),
            --n.digits[c - s - 1])
    }
    return a = biShiftRight(a, l),
        n.isNeg = e.isNeg != o,
    e.isNeg && (n = o ? biAdd(n, bigOne) : biSubtract(n, bigOne),
        a = biSubtract(t = biShiftRight(t, l), a)),
    0 == a.digits[0] && 0 == biHighIndex(a) && (a.isNeg = !1),
        new Array(n, a)
}

function biDivide(e, t) {
    return biDivideModulo(e, t)[0]
}

function biNumBits(e) {
    var t, n = biHighIndex(e), a = e.digits[n], i = (n + 1) * bitsPerDigit;
    for (t = i; t > i - bitsPerDigit && 0 == (32768 & a); --t)
        a <<= 1;
    return t
}

var biRadixBase = 2, biRadixBits = 16, bitsPerDigit = biRadixBits, biRadix = 65536, biHalfRadix = biRadix >>> 1,
    biRadixSquared = biRadix * biRadix, maxDigitVal = biRadix - 1, maxInteger = 9999999999999998, maxDigits, ZERO_ARRAY,
    bigZero, bigOne;

function biShiftLeft(e, t) {
    var n = Math.floor(t / bitsPerDigit)
        , a = new BigInt;
    arrayCopy(e.digits, 0, a.digits, n, a.digits.length - n);
    for (var i = t % bitsPerDigit, r = bitsPerDigit - i, o = a.digits.length - 1, s = o - 1; o > 0; --o,
        --s)
        a.digits[o] = a.digits[o] << i & maxDigitVal | (a.digits[s] & highBitMasks[i]) >>> r;
    return a.digits[0] = a.digits[o] << i & maxDigitVal,
        a.isNeg = e.isNeg,
        a
}

function arrayCopy(e, t, n, a, i) {
    for (var r = Math.min(t + i, e.length), o = t, s = a; o < r; ++o,
        ++s)
        n[s] = e[o]
}

var highBitMasks = new Array(0, 32768, 49152, 57344, 61440, 63488, 64512, 65024, 65280, 65408, 65472, 65504, 65520, 65528, 65532, 65534, 65535);

function biMultiplyByRadixPower(e, t) {
    var n = new BigInt;
    return arrayCopy(e.digits, 0, n.digits, t, n.digits.length - t),
        n
}

function biCompare(e, t) {
    if (e.isNeg != t.isNeg)
        return 1 - 2 * Number(e.isNeg);
    for (var n = e.digits.length - 1; n >= 0; --n)
        if (e.digits[n] != t.digits[n])
            return e.isNeg ? 1 - 2 * Number(e.digits[n] > t.digits[n]) : 1 - 2 * Number(e.digits[n] < t.digits[n]);
    return 0
}

function biSubtract(e, t) {
    var n;
    if (e.isNeg != t.isNeg)
        t.isNeg = !t.isNeg,
            n = biAdd(e, t),
            t.isNeg = !t.isNeg;
    else {
        var a, i;
        n = new BigInt,
            i = 0;
        for (var r = 0; r < e.digits.length; ++r)
            a = e.digits[r] - t.digits[r] + i,
                n.digits[r] = a % biRadix,
            n.digits[r] < 0 && (n.digits[r] += biRadix),
                i = 0 - Number(a < 0);
        if (-1 == i) {
            i = 0;
            for (r = 0; r < e.digits.length; ++r)
                a = 0 - n.digits[r] + i,
                    n.digits[r] = a % biRadix,
                n.digits[r] < 0 && (n.digits[r] += biRadix),
                    i = 0 - Number(a < 0);
            n.isNeg = !e.isNeg
        } else
            n.isNeg = e.isNeg
    }
    return n
}

function biMultiplyDigit(e, t) {
    var n, a, i;
    result = new BigInt,
        n = biHighIndex(e),
        a = 0;
    for (var r = 0; r <= n; ++r)
        i = result.digits[r] + e.digits[r] * t + a,
            result.digits[r] = i & maxDigitVal,
            a = i >>> biRadixBits;
    return result.digits[1 + n] = a,
        result
}

function biShiftRight(e, t) {
    var n = Math.floor(t / bitsPerDigit)
        , a = new BigInt;
    arrayCopy(e.digits, n, a.digits, 0, e.digits.length - n);
    for (var i = t % bitsPerDigit, r = bitsPerDigit - i, o = 0, s = o + 1; o < a.digits.length - 1; ++o,
        ++s)
        a.digits[o] = a.digits[o] >>> i | (a.digits[s] & lowBitMasks[i]) << r;
    return a.digits[a.digits.length - 1] >>>= i,
        a.isNeg = e.isNeg,
        a
}

var lowBitMasks = new Array(0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535);

function BarrettMu_modulo(e) {
    var t = biDivideByRadixPower(e, this.k - 1)
        , n = biDivideByRadixPower(biMultiply(t, this.mu), this.k + 1)
        ,
        a = biSubtract(biModuloByRadixPower(e, this.k + 1), biModuloByRadixPower(biMultiply(n, this.modulus), this.k + 1));
    a.isNeg && (a = biAdd(a, this.bkplus1));
    for (var i = biCompare(a, this.modulus) >= 0; i;)
        i = biCompare(a = biSubtract(a, this.modulus), this.modulus) >= 0;
    return a
}

function BarrettMu_multiplyMod(e, t) {
    var n = biMultiply(e, t);
    return this.modulo(n)
}

function BarrettMu_powMod(e, t) {
    var n = new BigInt;
    n.digits[0] = 1;
    for (var a = e, i = t; 0 != (1 & i.digits[0]) && (n = this.multiplyMod(n, a)),
    0 != (i = biShiftRight(i, 1)).digits[0] || 0 != biHighIndex(i);)
        a = this.multiplyMod(a, a);
    return n
}

function biMultiply(e, t) {
    for (var n, a, i, r = new BigInt, o = biHighIndex(e), s = biHighIndex(t), l = 0; l <= s; ++l) {
        for (n = 0,
                 i = l,
                 j = 0; j <= o; ++j,
                 ++i)
            a = r.digits[i] + e.digits[j] * t.digits[l] + n,
                r.digits[i] = a & maxDigitVal,
                n = a >>> biRadixBits;
        r.digits[l + o + 1] = n
    }
    return r.isNeg = e.isNeg != t.isNeg,
        r
}

function biDivideByRadixPower(e, t) {
    var n = new BigInt;
    return arrayCopy(e.digits, t, n.digits, 0, n.digits.length - t),
        n
}

function biModuloByRadixPower(e, t) {
    var n = new BigInt;
    return arrayCopy(e.digits, 0, n.digits, 0, t),
        n
}

function biToHex(e) {
    for (var t = "", n = (biHighIndex(e),
        biHighIndex(e)); n > -1; --n)
        t += digitToHex(e.digits[n]);
    return t
}

function digitToHex(e) {
    var t = "";
    for (i = 0; i < 4; ++i)
        t += hexToChar[15 & e],
            e >>>= 4;
    return reverseStr(t)
}

var hexToChar = new Array("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f");

function reverseStr(e) {
    for (var t = "", n = e.length - 1; n > -1; --n)
        t += e.charAt(n);
    return t
}

function get_rndString() {
    i = rndString()
    return i
}
function get_encryption(t, i) {
    var aaa = RSAEncrypt(i.split("").reverse().join(""), t)
    return aaa
}


function get_data(i) {
    var aaa = utils.desEncrypt("{\"username\":\"abcd123456\",\"password\":\"1233456\",\"captcha\":\"\"}", i)
    return aaa
}

console.log(get_data(get_rndString()))
