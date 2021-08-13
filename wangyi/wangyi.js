var CryptoJS = require("crypto-js");
var wo4s = function() {
        var IL8D = function(i) {
            return i % 32
        }
          , IM8E = function(i) {
            return 32 - 8 - i % 32
        };
        return function(cS4W, IN8F) {
            var VA2x = []
              , lZ8R = (1 << 8) - 1
              , mF8x = IN8F ? IL8D : IM8E;
            for (var i = 0, l = cS4W.length * 8; i < l; i += 8)
                VA2x[i >> 5] |= (cS4W.charCodeAt(i / 8) & lZ8R) << mF8x(i);
            return VA2x
        }
    }();
function bdr4v(hr6l, cs4w) {
        return hr6l << cs4w | hr6l >>> 32 - cs4w
    };
function mE8w(x, y) {
        var bZm2x = (x & 65535) + (y & 65535)
          , cEB7u = (x >> 16) + (y >> 16) + (bZm2x >> 16);
        return cEB7u << 16 | bZm2x & 65535
    };
function bdn4r(q, a, b, x, s, t) {
        return mE8w(bdr4v(mE8w(mE8w(a, q), mE8w(x, t)), s), b)
    };
function qa9R(a, b, c, d, x, s, t) {
        return bdn4r(b & c | ~b & d, a, b, x, s, t)
    };
function pX9O(a, b, c, d, x, s, t) {
        return bdn4r(b & d | c & ~d, a, b, x, s, t)
    };
function pH9y(a, b, c, d, x, s, t) {
        return bdn4r(b ^ c ^ d, a, b, x, s, t)
    };
function pA9r(a, b, c, d, x, s, t) {
        return bdn4r(c ^ (b | ~d), a, b, x, s, t)
    };
function LV9M(x, y) {
        x[y >> 5] |= 128 << y % 32;
        x[(y + 64 >>> 9 << 4) + 14] = y;
        var a = 1732584193
          , b = -271733879
          , c = -1732584194
          , d = 271733878;
        for (var i = 0, l = x.length, cac2x, cad2x, cag2x, cam2x; i < l; i += 16) {
            cac2x = a;
            cad2x = b;
            cag2x = c;
            cam2x = d;
            a = qa9R(a, b, c, d, x[i + 0], 7, -680876936);
            d = qa9R(d, a, b, c, x[i + 1], 12, -389564586);
            c = qa9R(c, d, a, b, x[i + 2], 17, 606105819);
            b = qa9R(b, c, d, a, x[i + 3], 22, -1044525330);
            a = qa9R(a, b, c, d, x[i + 4], 7, -176418897);
            d = qa9R(d, a, b, c, x[i + 5], 12, 1200080426);
            c = qa9R(c, d, a, b, x[i + 6], 17, -1473231341);
            b = qa9R(b, c, d, a, x[i + 7], 22, -45705983);
            a = qa9R(a, b, c, d, x[i + 8], 7, 1770035416);
            d = qa9R(d, a, b, c, x[i + 9], 12, -1958414417);
            c = qa9R(c, d, a, b, x[i + 10], 17, -42063);
            b = qa9R(b, c, d, a, x[i + 11], 22, -1990404162);
            a = qa9R(a, b, c, d, x[i + 12], 7, 1804603682);
            d = qa9R(d, a, b, c, x[i + 13], 12, -40341101);
            c = qa9R(c, d, a, b, x[i + 14], 17, -1502002290);
            b = qa9R(b, c, d, a, x[i + 15], 22, 1236535329);
            a = pX9O(a, b, c, d, x[i + 1], 5, -165796510);
            d = pX9O(d, a, b, c, x[i + 6], 9, -1069501632);
            c = pX9O(c, d, a, b, x[i + 11], 14, 643717713);
            b = pX9O(b, c, d, a, x[i + 0], 20, -373897302);
            a = pX9O(a, b, c, d, x[i + 5], 5, -701558691);
            d = pX9O(d, a, b, c, x[i + 10], 9, 38016083);
            c = pX9O(c, d, a, b, x[i + 15], 14, -660478335);
            b = pX9O(b, c, d, a, x[i + 4], 20, -405537848);
            a = pX9O(a, b, c, d, x[i + 9], 5, 568446438);
            d = pX9O(d, a, b, c, x[i + 14], 9, -1019803690);
            c = pX9O(c, d, a, b, x[i + 3], 14, -187363961);
            b = pX9O(b, c, d, a, x[i + 8], 20, 1163531501);
            a = pX9O(a, b, c, d, x[i + 13], 5, -1444681467);
            d = pX9O(d, a, b, c, x[i + 2], 9, -51403784);
            c = pX9O(c, d, a, b, x[i + 7], 14, 1735328473);
            b = pX9O(b, c, d, a, x[i + 12], 20, -1926607734);
            a = pH9y(a, b, c, d, x[i + 5], 4, -378558);
            d = pH9y(d, a, b, c, x[i + 8], 11, -2022574463);
            c = pH9y(c, d, a, b, x[i + 11], 16, 1839030562);
            b = pH9y(b, c, d, a, x[i + 14], 23, -35309556);
            a = pH9y(a, b, c, d, x[i + 1], 4, -1530992060);
            d = pH9y(d, a, b, c, x[i + 4], 11, 1272893353);
            c = pH9y(c, d, a, b, x[i + 7], 16, -155497632);
            b = pH9y(b, c, d, a, x[i + 10], 23, -1094730640);
            a = pH9y(a, b, c, d, x[i + 13], 4, 681279174);
            d = pH9y(d, a, b, c, x[i + 0], 11, -358537222);
            c = pH9y(c, d, a, b, x[i + 3], 16, -722521979);
            b = pH9y(b, c, d, a, x[i + 6], 23, 76029189);
            a = pH9y(a, b, c, d, x[i + 9], 4, -640364487);
            d = pH9y(d, a, b, c, x[i + 12], 11, -421815835);
            c = pH9y(c, d, a, b, x[i + 15], 16, 530742520);
            b = pH9y(b, c, d, a, x[i + 2], 23, -995338651);
            a = pA9r(a, b, c, d, x[i + 0], 6, -198630844);
            d = pA9r(d, a, b, c, x[i + 7], 10, 1126891415);
            c = pA9r(c, d, a, b, x[i + 14], 15, -1416354905);
            b = pA9r(b, c, d, a, x[i + 5], 21, -57434055);
            a = pA9r(a, b, c, d, x[i + 12], 6, 1700485571);
            d = pA9r(d, a, b, c, x[i + 3], 10, -1894986606);
            c = pA9r(c, d, a, b, x[i + 10], 15, -1051523);
            b = pA9r(b, c, d, a, x[i + 1], 21, -2054922799);
            a = pA9r(a, b, c, d, x[i + 8], 6, 1873313359);
            d = pA9r(d, a, b, c, x[i + 15], 10, -30611744);
            c = pA9r(c, d, a, b, x[i + 6], 15, -1560198380);
            b = pA9r(b, c, d, a, x[i + 13], 21, 1309151649);
            a = pA9r(a, b, c, d, x[i + 4], 6, -145523070);
            d = pA9r(d, a, b, c, x[i + 11], 10, -1120210379);
            c = pA9r(c, d, a, b, x[i + 2], 15, 718787259);
            b = pA9r(b, c, d, a, x[i + 9], 21, -343485551);
            a = mE8w(a, cac2x);
            b = mE8w(b, cad2x);
            c = mE8w(c, cag2x);
            d = mE8w(d, cam2x)
        }
        return [a, b, c, d]
    };
var VC2x = function() {
        var bZO2x = "0123456789abcdef"
          , IL8D = function(i) {
            return i % 4
        }
          , IM8E = function(i) {
            return 3 - i % 4
        };
        return function(iO7H, IN8F) {
            var bu4y = []
              , mF8x = IN8F ? IL8D : IM8E;
            for (var i = 0, l = iO7H.length * 4; i < l; i++) {
                bu4y.push(bZO2x.charAt(iO7H[i >> 2] >> mF8x(i) * 8 + 4 & 15) + bZO2x.charAt(iO7H[i >> 2] >> mF8x(i) * 8 & 15))
            }
            return bu4y.join("")
        }
    }()

var maxDigits, ZERO_ARRAY, bigZero, bigOne, dpl10, lr10, hexatrigesimalToChar, hexToChar, highBitMasks, lowBitMasks, biRadixBase = 2, biRadixBits = 16, bitsPerDigit = biRadixBits, biRadix = 65536, biHalfRadix = biRadix >>> 1, biRadixSquared = biRadix * biRadix, maxDigitVal = biRadix - 1, maxInteger = 9999999999999998;
setMaxDigits(20),
dpl10 = 15,
lr10 = biFromNumber(1e15),
hexatrigesimalToChar = new Array("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),
hexToChar = new Array("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"),
highBitMasks = new Array(0,32768,49152,57344,61440,63488,64512,65024,65280,65408,65472,65504,65520,65528,65532,65534,65535),
lowBitMasks = new Array(0,1,3,7,15,31,63,127,255,511,1023,2047,4095,8191,16383,32767,65535);
function biFromNumber(a) {
    var c, b = new BigInt;
    for (b.isNeg = 0 > a,
    a = Math.abs(a),
    c = 0; a > 0; )
        b.digits[c++] = a & maxDigitVal,
        a >>= biRadixBits;
    return b
}
function BigInt(a) {
    this.digits = "boolean" == typeof a && 1 == a ? null : ZERO_ARRAY.slice(0),
    this.isNeg = !1
}
function setMaxDigits(a) {
    maxDigits = a,
    ZERO_ARRAY = new Array(maxDigits);
    for (var b = 0; b < ZERO_ARRAY.length; b++)
        ZERO_ARRAY[b] = 0;
    bigZero = new BigInt,
    bigOne = new BigInt,
    bigOne.digits[0] = 1
}
function charToHex(a) {
    var h, b = 48, c = b + 9, d = 97, e = d + 25, f = 65, g = 90;
    return h = a >= b && c >= a ? a - b : a >= f && g >= a ? 10 + a - f : a >= d && e >= a ? 10 + a - d : 0
}
function hexToDigit(a) {
    var d, b = 0, c = Math.min(a.length, 4);
    for (d = 0; c > d; ++d)
        b <<= 4,
        b |= charToHex(a.charCodeAt(d));
    return b
}
function biFromHex(a) {
    var d, e, b = new BigInt, c = a.length;
    for (d = c,
    e = 0; d > 0; d -= 4,
    ++e)
        b.digits[e] = hexToDigit(a.substr(Math.max(d - 4, 0), Math.min(d, 4)));
    return b
}
function biHighIndex(a) {
    for (var b = a.digits.length - 1; b > 0 && 0 == a.digits[b]; )
        --b;
    return b
}
function biCopy(a) {
    var b = new BigInt(!0);
    return b.digits = a.digits.slice(0),
    b.isNeg = a.isNeg,
    b
}
function biNumBits(a) {
    var e, b = biHighIndex(a), c = a.digits[b], d = (b + 1) * bitsPerDigit;
    for (e = d; e > d - bitsPerDigit && 0 == (32768 & c); --e)
        c <<= 1;
    return e
}
function biSubtract(a, b) {
    var c, d, e, f;
    if (a.isNeg != b.isNeg)
        b.isNeg = !b.isNeg,
        c = biAdd(a, b),
        b.isNeg = !b.isNeg;
    else {
        for (c = new BigInt,
        e = 0,
        f = 0; f < a.digits.length; ++f)
            d = a.digits[f] - b.digits[f] + e,
            c.digits[f] = 65535 & d,
            c.digits[f] < 0 && (c.digits[f] += biRadix),
            e = 0 - Number(0 > d);
        if (-1 == e) {
            for (e = 0,
            f = 0; f < a.digits.length; ++f)
                d = 0 - c.digits[f] + e,
                c.digits[f] = 65535 & d,
                c.digits[f] < 0 && (c.digits[f] += biRadix),
                e = 0 - Number(0 > d);
            c.isNeg = !a.isNeg
        } else
            c.isNeg = a.isNeg
    }
    return c
}
function arrayCopy(a, b, c, d, e) {
    var g, h, f = Math.min(b + e, a.length);
    for (g = b,
    h = d; f > g; ++g,
    ++h)
        c[h] = a[g]
}
function biShiftLeft(a, b) {
    var e, f, g, h, c = Math.floor(b / bitsPerDigit), d = new BigInt;
    for (arrayCopy(a.digits, 0, d.digits, c, d.digits.length - c),
    e = b % bitsPerDigit,
    f = bitsPerDigit - e,
    g = d.digits.length - 1,
    h = g - 1; g > 0; --g,
    --h)
        d.digits[g] = d.digits[g] << e & maxDigitVal | (d.digits[h] & highBitMasks[e]) >>> f;
    return d.digits[0] = d.digits[g] << e & maxDigitVal,
    d.isNeg = a.isNeg,
    d
}
function biMultiplyByRadixPower(a, b) {
    var c = new BigInt;
    return arrayCopy(a.digits, 0, c.digits, b, c.digits.length - b),
    c
}
function biCompare(a, b) {
    if (a.isNeg != b.isNeg)
        return 1 - 2 * Number(a.isNeg);
    for (var c = a.digits.length - 1; c >= 0; --c)
        if (a.digits[c] != b.digits[c])
            return a.isNeg ? 1 - 2 * Number(a.digits[c] > b.digits[c]) : 1 - 2 * Number(a.digits[c] < b.digits[c]);
    return 0
}
function biMultiplyDigit(a, b) {
    var c, d, e, f;
    for (result = new BigInt,
    c = biHighIndex(a),
    d = 0,
    f = 0; c >= f; ++f)
        e = result.digits[f] + a.digits[f] * b + d,
        result.digits[f] = e & maxDigitVal,
        d = e >>> biRadixBits;
    return result.digits[1 + c] = d,
    result
}
function biAdd(a, b) {
    var c, d, e, f;
    if (a.isNeg != b.isNeg)
        b.isNeg = !b.isNeg,
        c = biSubtract(a, b),
        b.isNeg = !b.isNeg;
    else {
        for (c = new BigInt,
        d = 0,
        f = 0; f < a.digits.length; ++f)
            e = a.digits[f] + b.digits[f] + d,
            c.digits[f] = 65535 & e,
            d = Number(e >= biRadix);
        c.isNeg = a.isNeg
    }
    return c
}
function biShiftRight(a, b) {
    var e, f, g, h, c = Math.floor(b / bitsPerDigit), d = new BigInt;
    for (arrayCopy(a.digits, c, d.digits, 0, a.digits.length - c),
    e = b % bitsPerDigit,
    f = bitsPerDigit - e,
    g = 0,
    h = g + 1; g < d.digits.length - 1; ++g,
    ++h)
        d.digits[g] = d.digits[g] >>> e | (d.digits[h] & lowBitMasks[e]) << f;
    return d.digits[d.digits.length - 1] >>>= e,
    d.isNeg = a.isNeg,
    d
}
function biDivideModulo(a, b) {
    var f, g, h, i, j, k, l, m, n, o, p, q, r, s, c = biNumBits(a), d = biNumBits(b), e = b.isNeg;
    if (d > c)
        return a.isNeg ? (f = biCopy(bigOne),
        f.isNeg = !b.isNeg,
        a.isNeg = !1,
        b.isNeg = !1,
        g = biSubtract(b, a),
        a.isNeg = !0,
        b.isNeg = e) : (f = new BigInt,
        g = biCopy(a)),
        new Array(f,g);
    for (f = new BigInt,
    g = a,
    h = Math.ceil(d / bitsPerDigit) - 1,
    i = 0; b.digits[h] < biHalfRadix; )
        b = biShiftLeft(b, 1),
        ++i,
        ++d,
        h = Math.ceil(d / bitsPerDigit) - 1;
    for (g = biShiftLeft(g, i),
    c += i,
    j = Math.ceil(c / bitsPerDigit) - 1,
    k = biMultiplyByRadixPower(b, j - h); -1 != biCompare(g, k); )
        ++f.digits[j - h],
        g = biSubtract(g, k);
    for (l = j; l > h; --l) {
        for (m = l >= g.digits.length ? 0 : g.digits[l],
        n = l - 1 >= g.digits.length ? 0 : g.digits[l - 1],
        o = l - 2 >= g.digits.length ? 0 : g.digits[l - 2],
        p = h >= b.digits.length ? 0 : b.digits[h],
        q = h - 1 >= b.digits.length ? 0 : b.digits[h - 1],
        f.digits[l - h - 1] = m == p ? maxDigitVal : Math.floor((m * biRadix + n) / p),
        r = f.digits[l - h - 1] * (p * biRadix + q),
        s = m * biRadixSquared + (n * biRadix + o); r > s; )
            --f.digits[l - h - 1],
            r = f.digits[l - h - 1] * (p * biRadix | q),
            s = m * biRadix * biRadix + (n * biRadix + o);
        k = biMultiplyByRadixPower(b, l - h - 1),
        g = biSubtract(g, biMultiplyDigit(k, f.digits[l - h - 1])),
        g.isNeg && (g = biAdd(g, k),
        --f.digits[l - h - 1])
    }
    return g = biShiftRight(g, i),
    f.isNeg = a.isNeg != e,
    a.isNeg && (f = e ? biAdd(f, bigOne) : biSubtract(f, bigOne),
    b = biShiftRight(b, i),
    g = biSubtract(b, g)),
    0 == g.digits[0] && 0 == biHighIndex(g) && (g.isNeg = !1),
    new Array(f,g)
}
function biDivide(a, b) {
    return biDivideModulo(a, b)[0]
}
function biDivideByRadixPower(a, b) {
    var c = new BigInt;
    return arrayCopy(a.digits, b, c.digits, 0, c.digits.length - b),
    c
}
function biMultiply(a, b) {
    var d, h, i, k, c = new BigInt, e = biHighIndex(a), f = biHighIndex(b);
    for (k = 0; f >= k; ++k) {
        for (d = 0,
        i = k,
        j = 0; e >= j; ++j,
        ++i)
            h = c.digits[i] + a.digits[j] * b.digits[k] + d,
            c.digits[i] = h & maxDigitVal,
            d = h >>> biRadixBits;
        c.digits[k + e + 1] = d
    }
    return c.isNeg = a.isNeg != b.isNeg,
    c
}
function biModuloByRadixPower(a, b) {
    var c = new BigInt;
    return arrayCopy(a.digits, 0, c.digits, 0, b),
    c
}
function BarrettMu_multiplyMod(a, b) {
    var c = biMultiply(a, b);
    return this.modulo(c)
}
function BarrettMu_powMod(a, b) {
    var d, e, c = new BigInt;
    for (c.digits[0] = 1,
    d = a,
    e = b; ; ) {
        if (0 != (1 & e.digits[0]) && (c = this.multiplyMod(c, d)),
        e = biShiftRight(e, 1),
        0 == e.digits[0] && 0 == biHighIndex(e))
            break;
        d = this.multiplyMod(d, d)
    }
    return c
}
function BarrettMu_modulo(a) {
    var i, b = biDivideByRadixPower(a, this.k - 1), c = biMultiply(b, this.mu), d = biDivideByRadixPower(c, this.k + 1), e = biModuloByRadixPower(a, this.k + 1), f = biMultiply(d, this.modulus), g = biModuloByRadixPower(f, this.k + 1), h = biSubtract(e, g);
    for (h.isNeg && (h = biAdd(h, this.bkplus1)),
    i = biCompare(h, this.modulus) >= 0; i; )
        h = biSubtract(h, this.modulus),
        i = biCompare(h, this.modulus) >= 0;
    return h
}
function BarrettMu(a) {
    this.modulus = biCopy(a),
    this.k = biHighIndex(this.modulus) + 1;
    var b = new BigInt;
    b.digits[2 * this.k] = 1,
    this.mu = biDivide(b, this.modulus),
    this.bkplus1 = new BigInt,
    this.bkplus1.digits[this.k + 1] = 1,
    this.modulo = BarrettMu_modulo,
    this.multiplyMod = BarrettMu_multiplyMod,
    this.powMod = BarrettMu_powMod
}
function RSAKeyPair(a, b, c) {
    this.e = biFromHex(a),
    this.d = biFromHex(b),
    this.m = biFromHex(c),
    this.chunkSize = 2 * biHighIndex(this.m),
    this.radix = 16,
    this.barrett = new BarrettMu(this.m)
}
function reverseStr(a) {
    var c, b = "";
    for (c = a.length - 1; c > -1; --c)
        b += a.charAt(c);
    return b
}
function digitToHex(a) {
    var b = 15
      , c = "";
    for (i = 0; 4 > i; ++i)
        c += hexToChar[a & b],
        a >>>= 4;
    return reverseStr(c)
}
function biToHex(a) {
    var d, b = "";
    for (biHighIndex(a),
    d = biHighIndex(a); d > -1; --d)
        b += digitToHex(a.digits[d]);
    return b
}
function biToString(a, b) {
    var d, e, c = new BigInt;
    for (c.digits[0] = b,
    d = biDivideModulo(a, c),
    e = hexatrigesimalToChar[d[1].digits[0]]; 1 == biCompare(d[0], bigZero); )
        d = biDivideModulo(d[0], c),
        digit = d[1].digits[0],
        e += hexatrigesimalToChar[d[1].digits[0]];
    return (a.isNeg ? "-" : "") + reverseStr(e)
}
function encryptedString(a, b) {
    for (var f, g, h, i, j, k, l, c = new Array, d = b.length, e = 0; d > e; )
        c[e] = b.charCodeAt(e),
        e++;
    for (; 0 != c.length % a.chunkSize; )
        c[e++] = 0;
    for (f = c.length,
    g = "",
    e = 0; f > e; e += a.chunkSize) {
        for (j = new BigInt,
        h = 0,
        i = e; i < e + a.chunkSize; ++h)
            j.digits[h] = c[i++],
            j.digits[h] += c[i++] << 8;
        k = a.barrett.powMod(j, a.e),
        l = 16 == a.radix ? biToHex(k) : biToString(k, a.radix),
        g += l + " "
    }
    return g.substring(0, g.length - 1)
}
function c(a, b, c) {
    var d, e;
    return setMaxDigits(131),
    d = new RSAKeyPair(b,"",c),
    e = encryptedString(d, a)
}
function a(a) {
    var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
    for (d = 0; a > d; d += 1)
        e = Math.random() * b.length,
        e = Math.floor(e),
        c += b.charAt(e);
    return c
}
function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
function asrsea(d, e, f, g) {
    var h = {}
      , i = a(16);
    return h.encText = b(d, g),
    h.encText = b(h.encText, i),
    h.encSecKey = c(i, e, f),
    h
}
FL9C = function(i7b, v7o) {
        var bb8T = {}
        try {
            v7o = v7o.toLowerCase();
            if (i7b === null)
                return v7o == "null";
            if (i7b === undefined)
                return v7o == "undefined";
            return bb8T.toString.call(i7b).toLowerCase() == "[object " + v7o + "]"
        } catch (e) {
            return !1
        }
    };
gS0x = function(i7b) {
        return FL9C(i7b, "function")
    }
bf8X = function(k7d, cF8x, O8G) {
        if (!k7d || !k7d.length || !gS0x(cF8x))
            return this;
        if (!!k7d.forEach) {
            k7d.forEach(cF8x, O8G);
            return this
        }
        for (var i = 0, l = k7d.length; i < l; i++)
            cF8x.call(O8G, k7d[i], i, k7d);
        return this
    };
emj = {
    "色": "00e0b",
    "流感": "509f6",
    "这边": "259df",
    "弱": "8642d",
    "嘴唇": "bc356",
    "亲": "62901",
    "开心": "477df",
    "呲牙": "22677",
    "憨笑": "ec152",
    "猫": "b5ff6",
    "皱眉": "8ace6",
    "幽灵": "15bb7",
    "蛋糕": "b7251",
    "发怒": "52b3a",
    "大哭": "b17a8",
    "兔子": "76aea",
    "星星": "8a5aa",
    "钟情": "76d2e",
    "牵手": "41762",
    "公鸡": "9ec4e",
    "爱意": "e341f",
    "禁止": "56135",
    "狗": "fccf6",
    "亲亲": "95280",
    "叉": "104e0",
    "礼物": "312ec",
    "晕": "bda92",
    "呆": "557c9",
    "生病": "38701",
    "钻石": "14af6",
    "拜": "c9d05",
    "怒": "c4f7f",
    "示爱": "0c368",
    "汗": "5b7a4",
    "小鸡": "6bee2",
    "痛苦": "55932",
    "撇嘴": "575cc",
    "惶恐": "e10b4",
    "口罩": "24d81",
    "吐舌": "3cfe4",
    "心碎": "875d3",
    "生气": "e8204",
    "可爱": "7b97d",
    "鬼脸": "def52",
    "跳舞": "741d5",
    "男孩": "46b8e",
    "奸笑": "289dc",
    "猪": "6935b",
    "圈": "3ece0",
    "便便": "462db",
    "外星": "0a22b",
    "圣诞": "8e7",
    "流泪": "01000",
    "强": "1",
    "爱心": "0CoJU",
    "女孩": "m6Qyw",
    "惊恐": "8W8ju",
    "大笑": "d"
}
var brx1x = function(cJp3x) {
        var m7f = [];
        bf8X(cJp3x, function(cJo3x) {
            m7f.push(emj[cJo3x])
        });
        return m7f.join("")
    };
md = ["色", "流感", "这边", "弱", "嘴唇", "亲", "开心", "呲牙", "憨笑", "猫", "皱眉", "幽灵", "蛋糕", "发怒", "大哭", "兔子", "星星", "钟情", "牵手", "公鸡", "爱意", "禁止", "狗", "亲亲", "叉", "礼物", "晕", "呆", "生病", "钻石", "拜", "怒", "示爱", "汗", "小鸡", "痛苦", "撇嘴", "惶恐", "口罩", "吐舌", "心碎", "生气", "可爱", "鬼脸", "跳舞", "男孩", "奸笑", "猪", "圈", "便便", "外星", "圣诞"]

function get_params_encSecKey(phone,password) {
    var i7b = {
    "phone": phone,
    "password": VC2x(LV9M(wo4s(password, !0), password.length * 8), !0) ,
    "rememberLogin": "true",
    "checkToken": "9ca17ae2e6ffcda170e2e6eebbaa4ea38abfbbce5aa6e78aa3d54a838b9aaaae7dacaabaafeb3fbce8e1b1d42af0feaec3b92a86aa8fd9e64286ac988ee74f868a9fb2c84e8aaea89bc15f98a69ad4c421ad91ee9e",
    "csrf_token": ""
    }
    console.log(i7b)
    var bZe7X = asrsea(JSON.stringify(i7b), brx1x(["流泪", "强"]), brx1x(md), brx1x(["爱心", "女孩", "惊恐", "大笑"]));
    return {
        'params': bZe7X.encText,
        'encSecKey': bZe7X.encSecKey
    }

}
console.log(get_params_encSecKey('15202458535','123456'))
