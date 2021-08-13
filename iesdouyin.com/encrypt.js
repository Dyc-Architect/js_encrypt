var aaa;
navigator = {
    userAgent : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41"
}
CanvasRenderingContext2D = {
    fillText : function (val) {
        return undefined
    },
    arc : function () {
        return undefined
    },
    stroke : function () {
        return undefined
    }
}
canvas = {
    getContext: function (val) {
        return CanvasRenderingContext2D
    },
    toDataURL : function () {
        return "data:image/png;base64,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"
    }
}
document = {
    createElement : function (val) {
        if (val === 'canvas') {
            return canvas
        }
    }
};
//
// document = new Proxy(document, {
//     get(target, key) {
//       console.log('document获取了' + key +'属性');
//       return target[key]
// }
// });
// canvas = new Proxy(canvas, {
//     get(target, key) {
//       console.log('canvas获取了' + key +'属性');
//       return target[key]
// }
// });
// CanvasRenderingContext2D = new Proxy(CanvasRenderingContext2D, {
//     get(target, key) {
//       console.log('CanvasRenderingContext2D获取了' + key +'属性');
//       return target[key]
// }
// });


!function (e) {
    function __webpack_require__(moduleId) {
        var installedModules = {};
        if (installedModules[moduleId]) {
            return installedModules[moduleId].exports;
        }
        var module = installedModules[moduleId] = {
            i: moduleId,
            l: false,
            exports: {}
        };

        e[moduleId].call(module.exports, module, module.exports, __webpack_require__);

        module.l = true;

        return module.exports;
    }

    aaa = __webpack_require__;
}(
    {
        "9bd2804c7e68ac461d65":
            (function (module, exports) {

                Function(function (t) {
                    return 'e(e,a,r){(b[e]||(b[e]=t("x,y","x "+e+" y")(r,a)}a(e,a,r){(k[r]||(k[r]=t("x,y","new x[y]("+Array(r+1).join(",x[y]")(1)+")")(e,a)}r(e,a,r){n,t,s={},b=s.d=r?r.d+1:0;for(s["$"+b]=s,t=0;t<b;t)s[n="$"+t]=r[n];for(t=0,b=s=a;t<b;t)s[t]=a[t];c(e,0,s)}c(t,b,k){u(e){v[x]=e}f{g=,ting(bg)}l{try{y=c(t,b,k)}catch(e){h=e,y=l}}for(h,y,d,g,v=[],x=0;;)switch(g=){case 1:u(!)4:f5:u((e){a=0,r=e;{c=a<r;c&&u(e[a]),c}}(6:y=,u((y8:if(g=,lg,g=,y===c)b+=g;else if(y!==l)y9:c10:u(s(11:y=,u(+y)12:for(y=f,d=[],g=0;g<y;g)d[g]=y.charCodeAt(g)^g+y;u(String.fromCharCode.apply(null,d13:y=,h=delete [y]14:59:u((g=)?(y=x,v.slice(x-=g,y:[])61:u([])62:g=,k[0]=65599*k[0]+k[1].charCodeAt(g)>>>065:h=,y=,[y]=h66:u(e(t[b],,67:y=,d=,u((g=).x===c?r(g.y,y,k):g.apply(d,y68:u(e((g=t[b])<"<"?(b--,f):g+g,,70:u(!1)71:n72:+f73:u(parseInt(f,3675:if(){bcase 74:g=<<16>>16g76:u(k[])77:y=,u([y])78:g=,u(a(v,x-=g+1,g79:g=,u(k["$"+g])81:h=,[f]=h82:u([f])83:h=,k[]=h84:!085:void 086:u(v[x-1])88:h=,y=,h,y89:u({e{r(e.y,arguments,k)}e.y=f,e.x=c,e})90:null91:h93:h=0:;default:u((g<<16>>16)-16)}}n=this,t=n.Function,s=Object.keys||(e){a={},r=0;for(c in e)a[r]=c;a=r,a},b={},k={};r'.replace(/[-]/g, function (m) {
                        return t[m.charCodeAt(0) & 15]
                    })
                }("v[x++]=v[--x]t.charCodeAt(b++)-32function return ))++.substrvar .length(),b+=;break;case ;break}".split("")))()('gr$Daten Иb/s!l y͒yĹg,(lfi~ah`{mv,-n|jqewVxp{rvmmx,&effkx[!cs"l".Pq%widthl"@q&heightl"vr*getContextx$"2d[!cs#l#,*;?|u.|uc{uq$fontl#vr(fillTextx$$龘ฑภ경2<[#c}l#2q*shadowBlurl#1q-shadowOffsetXl#$$limeq+shadowColorl#vr#arcx88802[%c}l#vr&strokex[ c}l"v,)}eOmyoZB]mx[ cs!0s$l$Pb<k7l l!r&lengthb%^l$1+s$jl  s#i$1ek1s$gr#tack4)zgr#tac$! +0o![#cj?o ]!l$b%s"o ]!l"l$b*b^0d#>>>s!0s%yA0s"l"l!r&lengthb<k+l"^l"1+s"jl  s&l&z0l!$ +["cs\'(0l#i\'1ps9wxb&s() &{s)/s(gr&Stringr,fromCharCodes)0s*yWl ._b&s o!])l l Jb<k$.aj;l .Tb<k$.gj/l .^b<k&i"-4j!+& s+yPo!]+s!l!l Hd>&l!l Bd>&+l!l <d>&+l!l 6d>&+l!l &+ s,y=o!o!]/q"13o!l q"10o!],l 2d>& s.{s-yMo!o!]0q"13o!]*Ld<l 4d#>>>b|s!o!l q"10o!],l!& s/yIo!o!].q"13o!],o!]*Jd<l 6d#>>>b|&o!]+l &+ s0l-l!&l-l!i\'1z141z4b/@d<l"b|&+l-l(l!b^&+l-l&zl\'g,)gk}ejo{cm,)|yn~Lij~em["cl$b%@d<l&zl\'l $ +["cl$b%b|&+l-l%8d<@b|l!b^&+ q$sign ', [Object.defineProperty(exports, '__esModule', {value: !0})]);

            }),
    }
)

function get_sign(id) {

    return aaa('9bd2804c7e68ac461d65').sign(id)
}
console.log(aaa('9bd2804c7e68ac461d65').sign("110567353301"))
