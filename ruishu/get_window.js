function get_window(content) {
    var daobao = 'var section_1=require(\'./section_1\');window=section_1.window;'
    var data = ';var content = \'' + content +'\';var document = {\n' +
        '    \'createElement\': function (arg) {\n' +
        '        if ("i" === arg) {\n' +
        '            return undefined\n' +
        '        }\n' +
        '        if (\'div\' === arg) {\n' +
        '            var result = {\n' +
        '                "getElementsByTagName": function getElementsByTagName(arg) {\n' +
        '                    if ("i" === arg) {\n' +
        '                        return []\n' +
        '                    }\n' +
        '                }\n' +
        '            }\n' +
        '            return result\n' +
        '        }\n' +
        '        return undefined\n' +
        '                        },\n' +
        '    \'characterSet\': \'UTF-8\',\n' +
        '    \'charset\': \'UTF-8\',\n' +
        '    \'getElementsByTagName\': function (arg) {\n' +
        '        if ("meta" === arg) {\n' +
        '            return [\n' +
        '                {\n' +
        '                    "content": \'text/html; charset=utf-8\'\n' +
        '                },\n' +
        '                {\n' +
        '                    \'content\': content,\n' +
        '                    \'parentNode\': {\n' +
        '                        \'removeChild\': function (arg) {\n' +
        '                            return undefined\n' +
        '                        }\n' +
        '                    }\n' +
        '                },\n' +
        '            ]\n' +
        '        };\n' +
        '        if ("base" === arg) {\n' +
        '            return []\n' +
        '        };\n' +
        '        if ("script" === arg) {\n' +
        '            return [\n' +
        '                {\n' +
        '                    "getAttribute": function (arg) {\n' +
        '                            if (\'href\' === arg) {\n' +
        '                                return null\n' +
        '                            };\n' +
        '                            if (\'r\' === arg) {\n' +
        '                                return \'m\'\n' +
        '                            }\n' +
        '                    },\n' +
        '                    "parentElement": {\n' +
        '                            "removeChild": function removeChild(arg) {\n' +
        '\n' +
        '                            }\n' +
        '                    }\n' +
        '                },\n' +
        '                {\n' +
        '                    "getAttribute": function (arg) {\n' +
        '                            if (\'href\' === arg) {\n' +
        '                                return null\n' +
        '                            };\n' +
        '                            if (\'r\' === arg) {\n' +
        '                                return \'m\'\n' +
        '                            }\n' +
        '                    },\n' +
        '                    "parentElement": {\n' +
        '                            "removeChild": function removeChild(arg) {\n' +
        '\n' +
        '                            }\n' +
        '                    }\n' +
        '                }\n' +
        '            ]\n' +
        '        }\n' +
        '    },\n' +
        '    \'exitFullscreen\': function () {\n' +
        '\n' +
        '    },\n' +
        '    \'onautocomplete\': undefined,\n' +
        '    "addEventListener": function (arg1, arg2, arg3) {\n' +
        '        return undefined\n' +
        '    },\n' +
        '    "battery": undefined,\n' +
        '    "getBattery": undefined,\n' +
        '    "__webdriver_evaluate": undefined,\n' +
        '    "__webdriver_script_fn": undefined,\n' +
        '};\n' +
        'window.ActiveXObject = undefined;\n' +
        'window.addEventListener= function (arg1, arg2, arg3) {\n' +
        '        return undefined\n' +
        '    };\n' +
        'window.localStorage= {\n' +
        '        $_YWTU: "Jh3P2YKSyNGx_QEwhphSpSZo39RjjVlYhyGO5xxyrS7",\n' +
        '        $_cDro: "1",\n' +
        '        $_f0: "u3eVsy_Y8yMCJ9_Ck8dwdorC8Ea",\n' +
        '        $_f1: "aLgVWU1aQT0217YQ7mdhoUUDr7L",\n' +
        '        $_fb: "d7SAT3q4NajyVN8ibQfHAmQ66VJm0BH4aaX4dh8t25BewVjUgjqRo19YC0B1ojLJ",\n' +
        '        $_fh0: "t5vkmXwuUtqfnaX42LaFxHN6SJ9",\n' +
        '        $_nd: "66208",\n' +
        '        FSSBB2: "454716:PP0zyIlDN70_JnTIK9zwmG",\n' +
        '        FSSBB3: "454716:6hM5v6lriUUPG7nfOX9ujq",\n' +
        '        FSSBB17: "454716:3Vm70s24xdXcsSP6wql2MA",\n' +
        '        FSSBB18: "454716:0Mxv9qQ6O9fgeQbqHW3qLG",\n' +
        '        FSSBB22: "449168:3671",\n' +
        '        FSSBB26: "454716:{i.DO",\n' +
        '        FSSBB40: "454716:1",\n' +
        '        FSSBB46: "449168:2",\n' +
        '        FSSBB50: "454716:2",\n' +
        '        "__#classType": "localStorage",\n' +
        '    };\n' +
        'window.location = {\n' +
        '        hash: "",\n' +
        '        host: "www.customs.gov.cn",\n' +
        '        hostname: "www.customs.gov.cn",\n' +
        '        href: "http://www.customs.gov.cn/customs/302249/302274/302277/302276/1899449/index.html",\n' +
        '        origin: "http://www.customs.gov.cn",\n' +
        '        pathname: "/customs/302249/302274/302277/302276/1899449/index.html",\n' +
        '        port: "",\n' +
        '        protocol: "http:",\n' +
        '    };\n' +
        'window.document = document;\n' +
        'window.name =\'$_YWTU=Jh3P2YKSyNGx_QEwhphSpSZo39RjjVlYhyGO5xxyrS7&$_cDro=1&vdFm=\';\n' +
        'window.globalStorage=undefined;\n' +
        'window.sessionStorag={\n' +
        '        $_YWTU: "Jh3P2YKSyNGx_QEwhphSpSZo39RjjVlYhyGO5xxyrS7",\n' +
        '        $_cDro: "1",\n' +
        '        };\n' +
        'window.indexedDB={};\n' +
        'window.mozIndexedDB=undefined;\n' +
        'window.webkitIndexedDB=undefined;\n' +
        'window.msIndexedDB=undefined;\n' +
        'window.RegExp=RegExp;\n' +
        'window.unescape=unescape;\n' +
        'window.navigator={\n' +
        '        appCodeName: "Mozilla",\n' +
        '        appName: "Netscape",\n' +
        '        appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44",\n' +
        '        cookieEnabled: true,\n' +
        '        doNotTrack: null,\n' +
        '        hardwareConcurrency: 8,\n' +
        '        language: "zh-CN",\n' +
        '        languages: [\n' +
        '    "zh-CN",\n' +
        '    "en",\n' +
        '    "en-GB",\n' +
        '    "en-US",\n' +
        '    "zh"\n' +
        '],\n' +
        '        maxTouchPoints: 0,\n' +
        '        onLine: true,\n' +
        '        pdfViewerEnabled: true,\n' +
        '        platform: "Win32",\n' +
        '        product: "Gecko",\n' +
        '        productSub: "20030107",\n' +
        '        userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44",\n' +
        '        vendor: "Google Inc.",\n' +
        '        vendorSub: "",\n' +
        '        webdriver: false,\n' +
        '        webkitPersistentStorage: {},\n' +
        '    };\n' +
        'window.PointerEvent=function () {\n' +
        '\n' +
        '    };\n' +
        'window.MSPointerEvent=undefined;\n' +
        'window.msCredentials=undefined;\n' +
        'window.msCrypto=undefined;\n' +
        'window.FaveIconJavaInterface=undefined;\n' +
        'window.jesion=undefined;\n' +
        'window.chrome={\n' +
        '        "runtime": undefined,\n' +
        '        "webstore": undefined,\n' +
        '    };\n' +
        'window.onautocomplete=undefined;\n' +
        'window.PerformanceObserver=undefined;\n' +
        'window.PerformanceObserverEntryList=undefined;\n' +
        'window.Entity=undefined;\n' +
        'window.AnalyserNode=function () {\n' +
        '\n' +
        '    };\n' +
        'window.external={\n' +
        '        "AddSearchProvider": function () {\n' +
        '\n' +
        '        },\n' +
        '        "GetNextReqID": undefined,\n' +
        '        "GetOriginalUrl": undefined,\n' +
        '\n' +
        '    };\n' +
        'window.dumpAll=undefined;\n' +
        'window.callPhantom=undefined;\n' +
        'window._phantom=undefined;\n' +
        'window.$hook$=undefined;\n' +
        'window.$$logger=undefined;\n' +
        'window.$$lsp=undefined;\n' +
        'window.$$lsrb=undefined;\n' +
        'window.$hdx$=undefined;\n' +
        'window.$readyCodeAlreadyExecutedInThisFrame=undefined;\n' +
        'window.$sdx$=undefined;\n' +
        'window.$uie$=undefined;\n' +
        'window.netsparker=undefined;\n' +
        'window.__ns=undefined;\n' +
        'window.__nsAppendText=undefined;\n' +
        'window.eoWebBrowser=undefined;\n' +
        'window.hp_identifier=undefined;\n' +
        'window.appScanClick=undefined;\n' +
        'window.appScanFocusOut=undefined;\n' +
        'window.appScanKeyDown=undefined;\n' +
        'window.appScanKeyUp=undefined;\n' +
        'window.WebXMLogMsg_UNIQUE_=undefined;\n' +
        'window.webkitRequestFileSystem=function (arg1, arg2, arg3, arg4) {\n' +
        '\n' +
        '    };\n' +
        'window.TEMPORARY=0;\n' +
        'window.setInterval=function (arg1, arg2) {\n' +
        '\n' +
        '    };\n' +
        'window.openDatabase=function openDatabase(arg1, arg2, arg3, arg4) {\n' +
        '        var database = {\n' +
        '            version: "",\n' +
        '        }\n' +
        '        Database = {\n' +
        '            changeVersion: function changeVersion() {\n' +
        '\n' +
        '            },\n' +
        '            readTransaction: function readTransaction() {\n' +
        '\n' +
        '            },\n' +
        '            transaction: function transaction() {\n' +
        '\n' +
        '            },\n' +
        '            version: "",\n' +
        '            "get version": function () {\n' +
        '\n' +
        '            }\n' +
        '        }\n' +
        '        database.__proto__ = Database\n' +
        '        return database\n' +
        '    };\n' +
        'window.$b_callHandler=undefined;\n' +
        'window.$bmF0aXZlRmlVyUHJ=undefined;\n' +
        'window.JSON=JSON;\n' +
        'window.Math=Math;\n' +
        'window.isNaN=function isNaN(arg) {\n' +
        '        if (1 === arg) {\n' +
        '            return false\n' +
        '        }\n' +
        '    };\n' +
        'window.top = window;\n' +
        'window.self = window;\n' +
        'var XMLHttpRequest = function () {\n' +
        '\n' +
        '};\n' +
        '$_ts = window.$_ts;\n' +
        'var Storage = {\n' +
        '    removeItem: function (arg) {\n' +
        '        return undefined\n' +
        '    }\n' +
        '};'
    var get_cookie = 'function getcookie() {return document.cookie}'
    fs.writeFile('section_2.js', daobao + data + window._$Pp + get_cookie, function (err) {
        if (err) {console.log('error')};
        console.log('success')

    })
    return 'success'
}
exports.window = window;