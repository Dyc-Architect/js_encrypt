function J(t) {
            var data = t.split("").reverse().join("");
            !function(t) {
                o = new Array(t);
                for (var e = 0; e < o.length; e++)
                    o[e] = 0;
                d = new h,
                (n = new h).digits[0] = 1
            }(130);
            for (var e = new x("10001","","d741760e63aab01eecf8f2237468da2c9a1f3dfb7de74d8bed23de8eb734b0771aa88ab3acfe3d223f24c057a37f8976cd592a5061fba10cfa212ac7448ef4ce9710a3c5ecb176ed10f55612de976edda1a000faf74923efa80645d0654588c1bc314a28879aeda2ed08b0b83c3582ef3de1fe9125aa67130cdfcd3128732461"), r = data.length, l = "", c = 0, i = 0; r - c > 0; )
                l = L(e, r - c > 128 ? data.substr(c, 128) : data.substr(c, r - c)) + l,
                c = 128 * ++i;
            return l
        }
function h(t) {
    this.digits = "boolean" == typeof t && 1 == t ? null : o.slice(0),
    this.isNeg = !1
}


var o, n, d, l = [0, 32768, 49152, 57344, 61440, 63488, 64512, 65024, 65280, 65408, 65472, 65504, 65520, 65528, 65532, 65534, 65535], c = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535], f = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];
        function h(t) {
            this.digits = "boolean" == typeof t && 1 == t ? null : o.slice(0),
            this.isNeg = !1
        }
        function m(s) {
            for (var t, e = 0, r = Math.min(s.length, 4), i = 0; i < r; ++i)
                e <<= 4,
                e |= (t = s.charCodeAt(i)) >= 48 && t <= 57 ? t - 48 : t >= 65 && t <= 90 ? 10 + t - 65 : t >= 97 && t <= 122 ? 10 + t - 97 : 0;
            return e
        }
        function v(s) {
            for (var t = new h, i = s.length, e = 0; i > 0; i -= 4,
            ++e)
                t.digits[e] = m(s.substr(Math.max(i - 4, 0), Math.min(i, 4)));
            return t
        }
        function x(t, e, r) {
            this.e = v(t),
            this.d = v(e),
            this.m = v(r),
            this.chunkSize = 128,
            this.radix = 16,
            this.barrett = new w(this.m)
        }
        function w(t) {
            this.modulus = k(t),
            this.k = A(this.modulus) + 1;
            var e, r, o = new h;
            o.digits[2 * this.k] = 1,
            this.mu = (e = o,
            r = this.modulus,
            y(e, r)[0]),
            this.bkplus1 = new h,
            this.bkplus1.digits[this.k + 1] = 1,
            this.modulo = T,
            this.multiplyMod = U,
            this.powMod = I
        }
        function k(t) {
            var e = new h(!0);
            return e.digits = t.digits.slice(0),
            e.isNeg = t.isNeg,
            e
        }
        function A(t) {
            for (var e = t.digits.length - 1; e > 0 && 0 == t.digits[e]; )
                --e;
            return e
        }
        function y(t, e) {
            var q, r, o = j(t), d = j(e), l = e.isNeg;
            if (o < d)
                return t.isNeg ? ((q = k(n)).isNeg = !e.isNeg,
                t.isNeg = !1,
                e.isNeg = !1,
                r = O(e, t),
                t.isNeg = !0,
                e.isNeg = l) : (q = new h,
                r = k(t)),
                [q, r];
            q = new h,
            r = t;
            for (var c = Math.ceil(d / 16) - 1, f = 0; e.digits[c] < 32768; )
                e = _(e, 1),
                ++f,
                ++d,
                c = Math.ceil(d / 16) - 1;
            r = _(r, f),
            o += f;
            for (var m = Math.ceil(o / 16) - 1, b = z(e, m - c); -1 != N(r, b); )
                ++q.digits[m - c],
                r = O(r, b);
            for (var i = m; i > c; --i) {
                var v = i >= r.digits.length ? 0 : r.digits[i]
                  , x = i - 1 >= r.digits.length ? 0 : r.digits[i - 1]
                  , w = i - 2 >= r.digits.length ? 0 : r.digits[i - 2]
                  , y = c >= e.digits.length ? 0 : e.digits[c]
                  , C = c - 1 >= e.digits.length ? 0 : e.digits[c - 1];
                q.digits[i - c - 1] = v == y ? 65535 : Math.floor((65536 * v + x) / y);
                for (var T = q.digits[i - c - 1] * (65536 * y + C), U = 4294967296 * v + (65536 * x + w); T > U; )
                    --q.digits[i - c - 1],
                    T = q.digits[i - c - 1] * (65536 * y | C),
                    U = 65536 * v * 65536 + (65536 * x + w);
                (r = O(r, E(b = z(e, i - c - 1), q.digits[i - c - 1]))).isNeg && (r = Q(r, b),
                --q.digits[i - c - 1])
            }
            return r = S(r, f),
            q.isNeg = t.isNeg != l,
            t.isNeg && (q = l ? Q(q, n) : O(q, n),
            r = O(e = S(e, f), r)),
            0 == r.digits[0] && 0 == A(r) && (r.isNeg = !1),
            [q, r]
        }
        function j(t) {
            var e, r = A(t), o = t.digits[r], n = 16 * (r + 1);
            for (e = n; e > n - 16 && 0 == (32768 & o); --e)
                o <<= 1;
            return e
        }
        function _(t, e) {
            var r = Math.floor(e / 16)
              , o = new h;
            C(t.digits, 0, o.digits, r, o.digits.length - r);
            for (var n = e % 16, d = 16 - n, i = o.digits.length - 1, c = i - 1; i > 0; --i,
            --c)
                o.digits[i] = o.digits[i] << n & 65535 | (o.digits[c] & l[n]) >>> d;
            return o.digits[0] = o.digits[i] << n & 65535,
            o.isNeg = t.isNeg,
            o
        }
        function C(t, e, r, o, n) {
            for (var d = Math.min(e + n, t.length), i = e, l = o; i < d; ++i,
            ++l)
                r[l] = t[i]
        }
        function z(t, e) {
            var r = new h;
            return C(t.digits, 0, r.digits, e, r.digits.length - e),
            r
        }
        function N(t, e) {
            if (t.isNeg != e.isNeg)
                return 1 - 2 * Number(t.isNeg);
            for (var i = t.digits.length - 1; i >= 0; --i)
                if (t.digits[i] != e.digits[i])
                    return t.isNeg ? 1 - 2 * Number(t.digits[i] > e.digits[i]) : 1 - 2 * Number(t.digits[i] < e.digits[i]);
            return 0
        }
        function O(t, e) {
            var r;
            if (t.isNeg != e.isNeg)
                e.isNeg = !e.isNeg,
                r = Q(t, e),
                e.isNeg = !e.isNeg;
            else {
                var o, n;
                r = new h,
                n = 0;
                for (var i = 0; i < t.digits.length; ++i)
                    o = t.digits[i] - e.digits[i] + n,
                    r.digits[i] = o % 65536,
                    r.digits[i] < 0 && (r.digits[i] += 65536),
                    n = 0 - Number(o < 0);
                if (-1 == n) {
                    n = 0;
                    for (var d = 0; d < t.digits.length; ++d)
                        o = 0 - r.digits[d] + n,
                        r.digits[d] = o % 65536,
                        r.digits[d] < 0 && (r.digits[d] += 65536),
                        n = 0 - Number(o < 0);
                    r.isNeg = !t.isNeg
                } else
                    r.isNeg = t.isNeg
            }
            return r
        }
        function E(t, e) {
            var r, o, n, d = new h;
            r = A(t),
            o = 0;
            for (var l = 0; l <= r; ++l)
                n = d.digits[l] + t.digits[l] * e + o,
                d.digits[l] = 65535 & n,
                o = n >>> 16;
            return d.digits[1 + r] = o,
            d
        }
        function S(t, e) {
            var r = Math.floor(e / 16)
              , o = new h;
            C(t.digits, r, o.digits, 0, t.digits.length - r);
            for (var n = e % 16, d = 16 - n, i = 0, l = i + 1; i < o.digits.length - 1; ++i,
            ++l)
                o.digits[i] = o.digits[i] >>> n | (o.digits[l] & c[n]) << d;
            return o.digits[o.digits.length - 1] >>>= n,
            o.isNeg = t.isNeg,
            o
        }
        function T(t) {
            var e = R(t, this.k - 1)
              , r = R(B(e, this.mu), this.k + 1)
              , o = O(F(t, this.k + 1), F(B(r, this.modulus), this.k + 1));
            o.isNeg && (o = Q(o, this.bkplus1));
            for (var n = N(o, this.modulus) >= 0; n; )
                n = N(o = O(o, this.modulus), this.modulus) >= 0;
            return o
        }
        function U(t, e) {
            var r = B(t, e);
            return this.modulo(r)
        }
        function I(t, e) {
            var r = new h;
            r.digits[0] = 1;
            for (var a = t, o = e; 0 != (1 & o.digits[0]) && (r = this.multiplyMod(r, a)),
            0 != (o = S(o, 1)).digits[0] || 0 != A(o); )
                a = this.multiplyMod(a, a);
            return r
        }
        function L(t, s) {
            for (var a = [], e = s.length, i = 0; i < e; )
                a[i] = s.charCodeAt(i),
                i++;
            for (; a.length % t.chunkSize != 0; )
                a[i++] = 0;
            var r, o, n, d = a.length, l = "";
            for (i = 0; i < d; i += t.chunkSize) {
                for (n = new h,
                r = 0,
                o = i; o < i + t.chunkSize; ++r)
                    n.digits[r] = a[o++],
                    n.digits[r] += a[o++] << 8;
                var c = t.barrett.powMod(n, t.e);
                l += (16 == t.radix ? D(c) : H(c, t.radix)) + " "
            }
            return l.substring(0, l.length - 1)
        }
        function B(t, e) {
            for (var r, o, n, d = new h, l = A(t), c = A(e), i = 0; i <= c; ++i) {
                r = 0,
                n = i;
                for (var f = 0; f <= l; ++f,
                ++n)
                    o = d.digits[n] + t.digits[f] * e.digits[i] + r,
                    d.digits[n] = 65535 & o,
                    r = o >>> 16;
                d.digits[i + l + 1] = r
            }
            return d.isNeg = t.isNeg != e.isNeg,
            d
        }
        function R(t, e) {
            var r = new h;
            return C(t.digits, e, r.digits, 0, r.digits.length - e),
            r
        }
        function F(t, e) {
            var r = new h;
            return C(t.digits, 0, r.digits, 0, e),
            r
        }
        function D(t) {
            for (var e = "", i = A(t); i > -1; --i)
                e += P(t.digits[i]);
            return e
        }
        function P(t) {
            for (var e = "", i = 0; i < 4; ++i)
                e += f[15 & t],
                t >>>= 4;
            return M(e)
        }
        function M(s) {
            for (var t = "", i = s.length - 1; i > -1; --i)
                t += s.charAt(i);
            return t
        }
        function Q(t, e) {
            var r;
            if (t.isNeg != e.isNeg)
                e.isNeg = !e.isNeg,
                r = O(t, e),
                e.isNeg = !e.isNeg;
            else {
                r = new h;
                for (var o, n = 0, i = 0; i < t.digits.length; ++i)
                    o = t.digits[i] + e.digits[i] + n,
                    r.digits[i] = o % 65536,
                    n = Number(o >= 65536);
                r.isNeg = t.isNeg
            }
            return r
        }
        var V = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
        function H(t, e) {
            var b = new h;
            b.digits[0] = e;
            for (var r = y(t, b), o = V[r[1].digits[0]]; 1 == N(r[0], d); )
                r = y(r[0], b),
                o += V[r[1].digits[0]];
            return (t.isNeg ? "-" : "") + M(o)
        }


function test(custMobile, custLoginPsw, verifyCode){
        var e = {"terminal":"WEB","reqTime":(new Date).toUTCString(),"accessTerminal":"WEB","clientVersion":"4.1.0","version":"1.0","channelCode":"LD","appId":1002,"custMobile":custMobile,"custLoginPsw":custLoginPsw,"verifyCode":verifyCode}
    return "data=" + J(JSON.stringify(e))
        }


console.log(test('13269619917', '123456', '04091'))
