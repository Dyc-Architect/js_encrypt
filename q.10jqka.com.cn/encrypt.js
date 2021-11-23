
function L() {
    S[0] = Math.random() * parseInt('11111111111111111111111111111111', 2) >>> 0
}
function MM(TOKEN_SERVER_TIME) {
    S = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0,
    "11": 0,
    "12": 0,
    "13": 0,
    "14": 0,
    "15": 0,
    "16": 0,
    "17": 0,
    "base_fileds": [
        4,
        4,
        4,
        4,
        1,
        1,
        1,
        3,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        4,
        2,
        1
    ]
};
    S[1] = parseInt(TOKEN_SERVER_TIME);
    L();
    S[15] = 0;
    S[17] = 3;
    S[16] = 0;
    S[3] = 1250746509;
    S[13] = 3748;
    S[4] = 1;
    S[5] = 10;
    S[6] = 5;
}


function timeNow() {
    return time = Date.now(),
                    time / parseInt("3" + "e" + "8", 16) >>> 0
}
function toBuffer(S) {
    var base_fileds = S['base_fileds'];
                for (var r = base_fileds, e = [], o = -1, i = 0, s = 18; i < s; i++)
                    for (var v = S[i], f = r[i], l = o += f; e[l] = v & parseInt('255', 10),
                    --f != 0; )
                        --l,
                        v >>= 8;
                return e
            };
function M(o) {
    var y = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_";
    for (var i = "7", s = 0, v = o["length"], f = []; s < v; ) {
        var p = o[s++] << parseInt("16", 10) | o[s++] << parseInt("10", 8) | o[s++];
        f.push(y.charAt(p >> parseInt("10010", 2)), y.charAt(p >> parseInt("12", 10) & parseInt("3" + "f", 16)), y.charAt(p >> 6 & parseInt("77", 8)), y.charAt(p & parseInt("3f", 16)))
    }
    return f.join("")
};
function SS(n, e, a, o, i) {
    for (var c = n["length"]; e < c; )
        a[o++] = n[e++] ^ i & parseInt("255", 10),
        i = ~(i * parseInt("10000011", 2))
};
function x(t) {
    for (var r = "7", e = 0, o = 0, i = t["length"]; o < i; o++)
        e = (e << 5) - e + t[o];
    return e & parseInt("37" + r, 8)
};
function encode(n) {
    var t = x(n)
      , e = [3, t];
    return SS(n, +0, e, +2, t),
    M(e)
}
function cookie(TOKEN_SERVER_TIME) {
    var TOKEN_SERVER_TIME = TOKEN_SERVER_TIME;
    MM(TOKEN_SERVER_TIME)
    S[16]++,
    S[1] = parseInt(TOKEN_SERVER_TIME),
    S[2] = timeNow(),
    S[15] = 0,
    S[7] = 0,
    S[8] = 0,
    S[9] = 0,
    S[10] = 0,
    S[11] =0,
    S[12] = 0;
    var n = toBuffer(S);
    return encode(n)
}
cookie(1637636000.633)