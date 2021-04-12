// a.default {return"undefined"==typeof e?"undefined":l(e)}
var k = function(e){
	return"undefined"==typeof e?"undefined": typeof e
}
var genSignData = function(e) {
    var t = ""
      , n = [];
    for (var r in e)
        n.push(r);
    n = n.sort();
    for (var i = 0; i < n.length; i++) {
        var o = n[i]
          , s = e[o]
          , l = !1;
        if ("object" == ("undefined" == typeof s ? "undefined" : (0,
        k)(s))) {
            var c = "{";
            for (var u in s)
                c += u + "=" + s[u] + ", ",
                l = !0;
            l && (s = c.substring(0, c.length - 2) + "}")
        }
        "sign" != o && null !== s && void 0 !== s && "" !== s && ("object" != ("undefined" == typeof s ? "undefined" : (0,
        k)(s)) || l) && (t += (0 == i ? "" : "&") + o + "=" + s)
    }
    return null != t && "" != t && "&" == t.substr(0, 1) && (t = t.substr(1, t.length)),
    t
}
var liu94 = function (e, t) {
        var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
            , n = {
                rotl: function (e, t) {
                    return e << t | e >>> 32 - t
                },
                rotr: function (e, t) {
                    return e << 32 - t | e >>> t
                },
                endian: function (e) {
                    if (e.constructor == Number)
                        return 16711935 & n.rotl(e, 8) | 4278255360 & n.rotl(e, 24);
                    for (var t = 0; t < e.length; t++)
                        e[t] = n.endian(e[t]);
                    return e
                },
                randomBytes: function (e) {
                    for (var t = []; e > 0; e--)
                        t.push(Math.floor(256 * Math.random()));
                    return t
                },
                bytesToWords: function (e) {
                    for (var t = [], n = 0, r = 0; n < e.length; n++,
                        r += 8)
                        t[r >>> 5] |= e[n] << 24 - r % 32;
                    return t
                },
                wordsToBytes: function (e) {
                    for (var t = [], n = 0; n < 32 * e.length; n += 8)
                        t.push(e[n >>> 5] >>> 24 - n % 32 & 255);
                    return t
                },
                bytesToHex: function (e) {
                    for (var t = [], n = 0; n < e.length; n++)
                        t.push((e[n] >>> 4).toString(16)),
                            t.push((15 & e[n]).toString(16));
                    return t.join("")
                },
                hexToBytes: function (e) {
                    for (var t = [], n = 0; n < e.length; n += 2)
                        t.push(parseInt(e.substr(n, 2), 16));
                    return t
                },
                bytesToBase64: function (e) {
                    for (var n = [], r = 0; r < e.length; r += 3)
                        for (var i = e[r] << 16 | e[r + 1] << 8 | e[r + 2], a = 0; a < 4; a++)
                            8 * r + 6 * a <= 8 * e.length ? n.push(t.charAt(i >>> 6 * (3 - a) & 63)) : n.push("=");
                    return n.join("")
                },
                base64ToBytes: function (e) {
                    e = e.replace(/[^A-Z0-9+\/]/gi, "");
                    for (var n = [], r = 0, i = 0; r < e.length; i = ++r % 4)
                        0 != i && n.push((t.indexOf(e.charAt(r - 1)) & Math.pow(2, -2 * i + 8) - 1) << 2 * i | t.indexOf(e.charAt(r)) >>> 6 - 2 * i);
                    return n
                }
            };
        return n;
}

var er47 = {
    utf8: {
        stringToBytes: function (e) {
            return er47.bin.stringToBytes(unescape(encodeURIComponent(e)))
        },
        bytesToString: function (e) {
            return decodeURIComponent(escape(er47.bin.bytesToString(e)))
        }
    },
    bin: {
        stringToBytes: function (e) {
            for (var t = [], n = 0; n < e.length; n++)
                t.push(255 & e.charCodeAt(n));
            return t
        },
        bytesToString: function (e) {
            for (var t = [], n = 0; n < e.length; n++)
                t.push(String.fromCharCode(e[n]));
            return t.join("")
        }
    }
};

var jiu74 = function (e, t) {
    function n(e) {
        return !!e.constructor && "function" == typeof e.constructor.isBuffer && e.constructor.isBuffer(e)
    }
    function r(e) {
        return "function" == typeof e.readFloatLE && "function" == typeof e.slice && n(e.slice(0, 0))
    }
    return function (e) {
        return null != e && (n(e) || r(e) || !!e._isBuffer)
    }
}

var encrypt = function () {
    var t = liu94()
        , r = er47.utf8
        , i = jiu74()
        , a = er47.bin
        , o = function e(n, o) {
            n.constructor == String ? n = o && "binary" === o.encoding ? a.stringToBytes(n) : r.stringToBytes(n) : i(n) ? n = Array.prototype.slice.call(n, 0) : Array.isArray(n) || (n = n.toString());
            for (var s = t.bytesToWords(n), l = 8 * n.length, c = 1732584193, u = -271733879, f = -1732584194, d = 271733878, p = 0; p < s.length; p++)
                s[p] = 16711935 & (s[p] << 8 | s[p] >>> 24) | 4278255360 & (s[p] << 24 | s[p] >>> 8);
            s[l >>> 5] |= 128 << l % 32,
                s[(l + 64 >>> 9 << 4) + 14] = l;
            for (var h = e._ff, m = e._gg, v = e._hh, g = e._ii, p = 0; p < s.length; p += 16) {
                var y = c
                    , b = u
                    , w = f
                    , _ = d;
                c = h(c, u, f, d, s[p + 0], 7, -680876936),
                    d = h(d, c, u, f, s[p + 1], 12, -389564586),
                    f = h(f, d, c, u, s[p + 2], 17, 606105819),
                    u = h(u, f, d, c, s[p + 3], 22, -1044525330),
                    c = h(c, u, f, d, s[p + 4], 7, -176418897),
                    d = h(d, c, u, f, s[p + 5], 12, 1200080426),
                    f = h(f, d, c, u, s[p + 6], 17, -1473231341),
                    u = h(u, f, d, c, s[p + 7], 22, -45705983),
                    c = h(c, u, f, d, s[p + 8], 7, 1770035416),
                    d = h(d, c, u, f, s[p + 9], 12, -1958414417),
                    f = h(f, d, c, u, s[p + 10], 17, -42063),
                    u = h(u, f, d, c, s[p + 11], 22, -1990404162),
                    c = h(c, u, f, d, s[p + 12], 7, 1804603682),
                    d = h(d, c, u, f, s[p + 13], 12, -40341101),
                    f = h(f, d, c, u, s[p + 14], 17, -1502002290),
                    u = h(u, f, d, c, s[p + 15], 22, 1236535329),
                    c = m(c, u, f, d, s[p + 1], 5, -165796510),
                    d = m(d, c, u, f, s[p + 6], 9, -1069501632),
                    f = m(f, d, c, u, s[p + 11], 14, 643717713),
                    u = m(u, f, d, c, s[p + 0], 20, -373897302),
                    c = m(c, u, f, d, s[p + 5], 5, -701558691),
                    d = m(d, c, u, f, s[p + 10], 9, 38016083),
                    f = m(f, d, c, u, s[p + 15], 14, -660478335),
                    u = m(u, f, d, c, s[p + 4], 20, -405537848),
                    c = m(c, u, f, d, s[p + 9], 5, 568446438),
                    d = m(d, c, u, f, s[p + 14], 9, -1019803690),
                    f = m(f, d, c, u, s[p + 3], 14, -187363961),
                    u = m(u, f, d, c, s[p + 8], 20, 1163531501),
                    c = m(c, u, f, d, s[p + 13], 5, -1444681467),
                    d = m(d, c, u, f, s[p + 2], 9, -51403784),
                    f = m(f, d, c, u, s[p + 7], 14, 1735328473),
                    u = m(u, f, d, c, s[p + 12], 20, -1926607734),
                    c = v(c, u, f, d, s[p + 5], 4, -378558),
                    d = v(d, c, u, f, s[p + 8], 11, -2022574463),
                    f = v(f, d, c, u, s[p + 11], 16, 1839030562),
                    u = v(u, f, d, c, s[p + 14], 23, -35309556),
                    c = v(c, u, f, d, s[p + 1], 4, -1530992060),
                    d = v(d, c, u, f, s[p + 4], 11, 1272893353),
                    f = v(f, d, c, u, s[p + 7], 16, -155497632),
                    u = v(u, f, d, c, s[p + 10], 23, -1094730640),
                    c = v(c, u, f, d, s[p + 13], 4, 681279174),
                    d = v(d, c, u, f, s[p + 0], 11, -358537222),
                    f = v(f, d, c, u, s[p + 3], 16, -722521979),
                    u = v(u, f, d, c, s[p + 6], 23, 76029189),
                    c = v(c, u, f, d, s[p + 9], 4, -640364487),
                    d = v(d, c, u, f, s[p + 12], 11, -421815835),
                    f = v(f, d, c, u, s[p + 15], 16, 530742520),
                    u = v(u, f, d, c, s[p + 2], 23, -995338651),
                    c = g(c, u, f, d, s[p + 0], 6, -198630844),
                    d = g(d, c, u, f, s[p + 7], 10, 1126891415),
                    f = g(f, d, c, u, s[p + 14], 15, -1416354905),
                    u = g(u, f, d, c, s[p + 5], 21, -57434055),
                    c = g(c, u, f, d, s[p + 12], 6, 1700485571),
                    d = g(d, c, u, f, s[p + 3], 10, -1894986606),
                    f = g(f, d, c, u, s[p + 10], 15, -1051523),
                    u = g(u, f, d, c, s[p + 1], 21, -2054922799),
                    c = g(c, u, f, d, s[p + 8], 6, 1873313359),
                    d = g(d, c, u, f, s[p + 15], 10, -30611744),
                    f = g(f, d, c, u, s[p + 6], 15, -1560198380),
                    u = g(u, f, d, c, s[p + 13], 21, 1309151649),
                    c = g(c, u, f, d, s[p + 4], 6, -145523070),
                    d = g(d, c, u, f, s[p + 11], 10, -1120210379),
                    f = g(f, d, c, u, s[p + 2], 15, 718787259),
                    u = g(u, f, d, c, s[p + 9], 21, -343485551),
                    c = c + y >>> 0,
                    u = u + b >>> 0,
                    f = f + w >>> 0,
                    d = d + _ >>> 0
            }
            return t.endian([c, u, f, d])
        };
		o._ff = function (e, t, n, r, i, a, o) {
			var s = e + (t & n | ~t & r) + (i >>> 0) + o;
			return (s << a | s >>> 32 - a) + t
		}
        ,
        o._gg = function (e, t, n, r, i, a, o) {
            var s = e + (t & r | n & ~r) + (i >>> 0) + o;
            return (s << a | s >>> 32 - a) + t
        }
        ,
        o._hh = function (e, t, n, r, i, a, o) {
            var s = e + (t ^ n ^ r) + (i >>> 0) + o;
            return (s << a | s >>> 32 - a) + t
        }
        ,
        o._ii = function (e, t, n, r, i, a, o) {
            var s = e + (n ^ (t | ~r)) + (i >>> 0) + o;
            return (s << a | s >>> 32 - a) + t
        }
        ,
        o._blocksize = 16,
        o._digestsize = 16,
        res = function (e, n) {
			console.log(e)
			if (void 0 === e || null === e)
                throw new Error("Illegal argument " + e);
            var r = t.wordsToBytes(o(e, n));
            console.log(r)
            return n && n.asBytes ? r : n && n.asString ? a.bytesToString(r) : t.bytesToHex(r)
        }
        //res("password=123&userName=158062204096", undefined);
        //console.log('-------->',res(origin, undefined))
		return res;
}
var request = function (userName, password) {
    var UP = {
        userName: userName,
        password: password
    }
    return encrypt()("/account/login.json"+"&"+encrypt()(genSignData(UP))+"&"+"")
}
//encrypt()
//console.log(genSignData(UP))
//encrypt()
//encrypt()(genSignData(UP),undefined)
console.log(request("15806204096","123"));



