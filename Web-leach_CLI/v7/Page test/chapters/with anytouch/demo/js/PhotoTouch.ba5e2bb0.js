(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["PhotoTouch"], {
        "0876": function (t, e, n) {
            "use strict";
            n.r(e);
            var r = function () {
                    var t = this,
                        e = t.$createElement,
                        n = t._self._c || e;
                    return n("article", {
                        staticClass: "page-photo-touch"
                    }, [n("section", {
                        staticClass: "d-flex pos-r"
                    }, [n("canvas", {
                        ref: "canvas",
                        staticStyle: {
                            width: "100%"
                        }
                    }), t.loading ? n("p", [t._v("loading")]) : t._e(), null !== t.img ? n("div", {
                        staticClass: "pos-a",
                        staticStyle: {
                            width: "50px",
                            right: "-8px",
                            top: "16px"
                        }
                    }, [n("button", {
                        staticClass: "a-button a-button--dark ml-1",
                        staticStyle: {
                            background: "rgba(0, 0, 0, 0.6)",
                            color: "#fff"
                        },
                        on: {
                            click: function (e) {
                                return t.photoTouch.zoom(.9)
                            }
                        }
                    }, [n("i", {
                        staticClass: "ion-md-remove font-1"
                    })]), n("button", {
                        staticClass: "a-button a-button--dark mt-1",
                        staticStyle: {
                            background: "rgba(0, 0, 0, 0.6)",
                            color: "#fff"
                        },
                        on: {
                            click: function (e) {
                                return t.photoTouch.zoom(1.1)
                            }
                        }
                    }, [n("i", {
                        staticClass: "ion-md-add font-1"
                    })]), n("button", {
                        staticClass: "a-button a-button--dark mt-1",
                        staticStyle: {
                            background: "rgba(0, 0, 0, 0.6)",
                            color: "#fff"
                        },
                        on: {
                            click: function (e) {
                                return t.photoTouch.rotate(90)
                            }
                        }
                    }, [n("i", {
                        staticClass: "ion-md-refresh font-1"
                    })]), n("button", {
                        staticClass: "a-button a-button--danger mt-1",
                        staticStyle: {
                            background: "rgba(255, 0, 0, 0.6)",
                            color: "#fff"
                        },
                        on: {
                            click: t.togglePreview
                        }
                    }, [n("i", {
                        staticClass: "font-1",
                        class: ["ion-md-eye" + (t.isShowLine ? "" : "-off")]
                    })])]) : t._e()]), n("div", {
                        staticClass: "d-flex mt-1"
                    }, [n("ButtonLoadFile", {
                        staticClass: "a-button a-button--dark a-button--outline flex-1",
                        on: {
                            loaded: t.onImageLoaded
                        }
                    }, [n("i", {
                        staticClass: "ion-md-image font-1",
                        staticStyle: {
                            "vertical-align": "sub"
                        }
                    }), t._v(" Change")]), n("button", {
                        staticClass: "a-button a-button--primary flex-1",
                        on: {
                            click: t.toDataURL
                        }
                    }, [n("i", {
                        staticClass: "ion-md-checkmark font-1",
                        staticStyle: {
                            "vertical-align": "sub"
                        }
                    }), t._v(" Done ")])], 1), n("img", {
                        staticStyle: {
                            width: "100%"
                        },
                        attrs: {
                            src: t.dataURL
                        }
                    }), n("section", [n("hr", {
                        staticClass: "mt-2"
                    }), n("label", {
                        staticClass: "a-input"
                    }, [n("input", {
                        attrs: {
                            type: "range",
                            max: "400"
                        },
                        domProps: {
                            value: t.offset[0]
                        },
                        on: {
                            input: function (e) {
                                t.photoTouch.moveTo(Number(e.target.value), t.offset[1])
                            }
                        }
                    }), t._v(" OffsetX: " + t._s(t.offset[0]) + " ")]), n("label", {
                        staticClass: "a-input"
                    }, [n("input", {
                        attrs: {
                            type: "range",
                            max: "400"
                        },
                        domProps: {
                            value: t.offset[1]
                        },
                        on: {
                            input: function (e) {
                                t.photoTouch.moveTo(t.offset[0], Number(e.target.value))
                            }
                        }
                    }), t._v(" OffsetY: " + t._s(t.offset[1]) + " ")]), n("hr", {
                        staticClass: "mt-2"
                    }), n("label", {
                        staticClass: "a-input"
                    }, [n("input", {
                        attrs: {
                            type: "range",
                            max: "2000"
                        },
                        domProps: {
                            value: t.org[0]
                        },
                        on: {
                            input: function (e) {
                                t.photoTouch.changeOrg([t.org[0], Number(e.target.value)])
                            }
                        }
                    }), t._v(" OX:" + t._s(t.org[0]) + " ")]), n("label", {
                        staticClass: "a-input"
                    }, [n("input", {
                        attrs: {
                            type: "range",
                            max: "2000"
                        },
                        domProps: {
                            value: t.org[1]
                        },
                        on: {
                            input: function (e) {
                                t.photoTouch.changeOrg([Number(e.target.value), t.org[1]])
                            }
                        }
                    }), t._v(" OY:" + t._s(t.org[1]) + " ")]), n("label", {
                        staticClass: "a-input"
                    }, [n("input", {
                        attrs: {
                            min: "0.1",
                            max: "2",
                            step: "0.1",
                            type: "range"
                        },
                        domProps: {
                            value: t.scale
                        },
                        on: {
                            input: function (e) {
                                t.photoTouch.zoomTo(Number(e.target.value))
                            }
                        }
                    }), t._v(" Scale: " + t._s(t.scale) + " ")]), n("label", {
                        staticClass: "a-input"
                    }, [n("input", {
                        attrs: {
                            type: "range",
                            max: "360"
                        },
                        domProps: {
                            value: t.angle
                        },
                        on: {
                            input: function (e) {
                                t.photoTouch.rotateTo(Number(e.target.value))
                            }
                        }
                    }), t._v(" A:" + t._s(t.angle) + " ")])])])
                },
                i = [],
                o = (n("96cf"), n("1da1")),
                a = n("6b75");

            function s(t) {
                if (Array.isArray(t)) return Object(a["a"])(t)
            }
            n("a4d3"), n("e01a"), n("d28b"), n("a630"), n("d3b7"), n("3ca3"), n("ddb0");

            function c(t) {
                if ("undefined" !== typeof Symbol && Symbol.iterator in Object(t)) return Array.from(t)
            }
            var u = n("06c5");

            function h() {
                throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
            }

            function l(t) {
                return s(t) || c(t) || Object(u["a"])(t) || h()
            }
            var f = n("91b3"),
                p = n.n(f),
                d = n("a094"),
                v = {
                    name: "DIY",
                    components: {
                        ButtonLoadFile: d["a"]
                    },
                    data: function () {
                        return {
                            dataURL: "",
                            loading: !1,
                            img: null,
                            isShowLine: !1,
                            photoTouch: null,
                            overlayImgs: [],
                            activeOverlay: {},
                            org: [821, 1217],
                            angle: 0,
                            scale: 1,
                            offset: [0, 0],
                            width: 1642,
                            height: 2434,
                            background: "#fff",
                            lineOverlays: ["https://cdn.shopifycdn.net/s/files/1/0276/2922/4000/files/iPhone11_b44dc4e2-3e32-4b51-80de-675d8a273aed.png?v=1597476179"],
                            previewOverlays: ["https://cdn.shopifycdn.net/s/files/1/0276/2922/4000/files/iPhone11_0d08b826-a84d-4224-aca2-4f928c6fe6e5.png?v=1597476180", "https://cdn.shopifycdn.net/s/files/1/0276/2922/4000/files/iPhone11_9fa84a77-f492-424d-be4c-6241e4aa6bd7.png?v=1597476180"]
                        }
                    },
                    watch: {
                        isShowLine: function (t) {
                            var e, n;
                            this.img;
                            (this.loading = !0, t) ? (e = this.photoTouch).changeOverlay.apply(e, l(this.lineOverlays)): (this.photoTouch.changeBackground(this.background), (n = this.photoTouch).changeOverlay.apply(n, l(this.previewOverlays)));
                            this.loading = !1
                        }
                    },
                    mounted: function () {
                        var t = this;
                        return Object(o["a"])(regeneratorRuntime.mark((function e() {
                            return regeneratorRuntime.wrap((function (e) {
                                while (1) switch (e.prev = e.next) {
                                    case 0:
                                        t.photoTouch = new p.a(t.$refs.canvas, t.width, t.height), t.photoTouch.on("transform", (function (e) {
                                            var n = e.offset,
                                                r = e.scale,
                                                i = e.angle,
                                                o = e.org;
                                            t.offset = n, t.scale = r, t.angle = i, t.org = o
                                        })), t.photoTouch.on(["panstart", "pinchstart", "rotatestart", "tap"], (function () {
                                            t.isShowLine = !0
                                        })), t.photoTouch.on(["panend", "pinchend", "rotateend"], (function () {
                                            t.isShowLine = !1
                                        }));
                                    case 4:
                                    case "end":
                                        return e.stop()
                                }
                            }), e)
                        })))()
                    },
                    methods: {
                        toDataURL: function () {
                            var t = this;
                            this.isShowLine = !1, this.$nextTick((function () {
                                t.dataURL = t.photoTouch.canvas.toDataURL("image/jpeg", .7), console.log(t.img.src)
                            }))
                        },
                        togglePreview: function () {
                            var t = this;
                            return Object(o["a"])(regeneratorRuntime.mark((function e() {
                                return regeneratorRuntime.wrap((function (e) {
                                    while (1) switch (e.prev = e.next) {
                                        case 0:
                                            t.isShowLine = !t.isShowLine;
                                        case 1:
                                        case "end":
                                            return e.stop()
                                    }
                                }), e)
                            })))()
                        },
                        onImageLoaded: function (t) {
                            var e = this;
                            return Object(o["a"])(regeneratorRuntime.mark((function n() {
                                var r, i;
                                return regeneratorRuntime.wrap((function (n) {
                                    while (1) switch (n.prev = n.next) {
                                        case 0:
                                            e.loading = !0, i = t[0].source.img, e.img = i, e.photoTouch.changeBackground(e.background), e.photoTouch.changeImg(i), (r = e.photoTouch).changeOverlay.apply(r, l(e.previewOverlays)), e.loading = !1;
                                        case 7:
                                        case "end":
                                            return n.stop()
                                    }
                                }), n)
                            })))()
                        },
                        reset: function () {
                            this.photoTouch.reset()
                        }
                    }
                },
                g = v,
                m = (n("95e0"), n("2877")),
                y = Object(m["a"])(g, r, i, !1, null, null, null);
            e["default"] = y.exports
        },
        "13d5": function (t, e, n) {
            "use strict";
            var r = n("23e7"),
                i = n("d58f").left,
                o = n("a640"),
                a = n("ae40"),
                s = n("2d00"),
                c = n("605d"),
                u = o("reduce"),
                h = a("reduce", {
                    1: 0
                }),
                l = !c && s > 79 && s < 83;
            r({
                target: "Array",
                proto: !0,
                forced: !u || !h || l
            }, {
                reduce: function (t) {
                    return i(this, t, arguments.length, arguments.length > 1 ? arguments[1] : void 0)
                }
            })
        },
        "14c3": function (t, e, n) {
            var r = n("c6b6"),
                i = n("9263");
            t.exports = function (t, e) {
                var n = t.exec;
                if ("function" === typeof n) {
                    var o = n.call(t, e);
                    if ("object" !== typeof o) throw TypeError("RegExp exec method returned something other than an Object or null");
                    return o
                }
                if ("RegExp" !== r(t)) throw TypeError("RegExp#exec called on incompatible receiver");
                return i.call(t, e)
            }
        },
        "159b": function (t, e, n) {
            var r = n("da84"),
                i = n("fdbc"),
                o = n("17c2"),
                a = n("9112");
            for (var s in i) {
                var c = r[s],
                    u = c && c.prototype;
                if (u && u.forEach !== o) try {
                    a(u, "forEach", o)
                } catch (h) {
                    u.forEach = o
                }
            }
        },
        "17c2": function (t, e, n) {
            "use strict";
            var r = n("b727").forEach,
                i = n("a640"),
                o = n("ae40"),
                a = i("forEach"),
                s = o("forEach");
            t.exports = a && s ? [].forEach : function (t) {
                return r(this, t, arguments.length > 1 ? arguments[1] : void 0)
            }
        },
        4160: function (t, e, n) {
            "use strict";
            var r = n("23e7"),
                i = n("17c2");
            r({
                target: "Array",
                proto: !0,
                forced: [].forEach != i
            }, {
                forEach: i
            })
        },
        "46a8": function (t, e, n) {
            "use strict";
            n("98b7")
        },
        5319: function (t, e, n) {
            "use strict";
            var r = n("d784"),
                i = n("825a"),
                o = n("7b0b"),
                a = n("50c4"),
                s = n("a691"),
                c = n("1d80"),
                u = n("8aa5"),
                h = n("14c3"),
                l = Math.max,
                f = Math.min,
                p = Math.floor,
                d = /\$([$&'`]|\d\d?|<[^>]*>)/g,
                v = /\$([$&'`]|\d\d?)/g,
                g = function (t) {
                    return void 0 === t ? t : String(t)
                };
            r("replace", 2, (function (t, e, n, r) {
                var m = r.REGEXP_REPLACE_SUBSTITUTES_UNDEFINED_CAPTURE,
                    y = r.REPLACE_KEEPS_$0,
                    b = m ? "$" : "$0";
                return [function (n, r) {
                    var i = c(this),
                        o = void 0 == n ? void 0 : n[t];
                    return void 0 !== o ? o.call(n, i, r) : e.call(String(i), n, r)
                }, function (t, r) {
                    if (!m && y || "string" === typeof r && -1 === r.indexOf(b)) {
                        var o = n(e, t, this, r);
                        if (o.done) return o.value
                    }
                    var c = i(t),
                        p = String(this),
                        d = "function" === typeof r;
                    d || (r = String(r));
                    var v = c.global;
                    if (v) {
                        var w = c.unicode;
                        c.lastIndex = 0
                    }
                    var T = [];
                    while (1) {
                        var E = h(c, p);
                        if (null === E) break;
                        if (T.push(E), !v) break;
                        var O = String(E[0]);
                        "" === O && (c.lastIndex = u(p, a(c.lastIndex), w))
                    }
                    for (var I = "", S = 0, M = 0; M < T.length; M++) {
                        E = T[M];
                        for (var R = String(E[0]), P = l(f(s(E.index), p.length), 0), _ = [], A = 1; A < E.length; A++) _.push(g(E[A]));
                        var C = E.groups;
                        if (d) {
                            var L = [R].concat(_, P, p);
                            void 0 !== C && L.push(C);
                            var k = String(r.apply(void 0, L))
                        } else k = x(R, p, P, _, C, r);
                        P >= S && (I += p.slice(S, P) + k, S = P + R.length)
                    }
                    return I + p.slice(S)
                }];

                function x(t, n, r, i, a, s) {
                    var c = r + t.length,
                        u = i.length,
                        h = v;
                    return void 0 !== a && (a = o(a), h = d), e.call(s, h, (function (e, o) {
                        var s;
                        switch (o.charAt(0)) {
                            case "$":
                                return "$";
                            case "&":
                                return t;
                            case "`":
                                return n.slice(0, r);
                            case "'":
                                return n.slice(c);
                            case "<":
                                s = a[o.slice(1, -1)];
                                break;
                            default:
                                var h = +o;
                                if (0 === h) return e;
                                if (h > u) {
                                    var l = p(h / 10);
                                    return 0 === l ? e : l <= u ? void 0 === i[l - 1] ? o.charAt(1) : i[l - 1] + o.charAt(1) : e
                                }
                                s = i[h - 1]
                        }
                        return void 0 === s ? "" : s
                    }))
                }
            }))
        },
        "6c57": function (t, e, n) {
            var r = n("23e7"),
                i = n("da84");
            r({
                global: !0
            }, {
                globalThis: i
            })
        },
        7037: function (t, e, n) {
            function r(e) {
                return "function" === typeof Symbol && "symbol" === typeof Symbol.iterator ? t.exports = r = function (t) {
                    return typeof t
                } : t.exports = r = function (t) {
                    return t && "function" === typeof Symbol && t.constructor === Symbol && t !== Symbol.prototype ? "symbol" : typeof t
                }, r(e)
            }
            n("a4d3"), n("e01a"), n("d28b"), n("d3b7"), n("3ca3"), n("ddb0"), t.exports = r
        },
        "8aa5": function (t, e, n) {
            "use strict";
            var r = n("6547").charAt;
            t.exports = function (t, e, n) {
                return e + (n ? r(t, e).length : 1)
            }
        },
        "91b3": function (t, e, n) {
            var r, i;
            n("a4d3"), n("e01a"), n("d28b"), n("a623"), n("c740"), n("4160"), n("a630"), n("caad"), n("c975"), n("d81d"), n("13d5"), n("a434"), n("b0c0"), n("6c57"), n("a9e3"), n("aff5"), n("dca8"), n("d3b7"), n("ac1f"), n("25f0"), n("3ca3"), n("5319"), n("159b"), n("ddb0");
            var o = n("7037");
            ! function (a, s) {
                "object" == o(e) && "undefined" != typeof t ? t.exports = s() : (r = s, i = "function" === typeof r ? r.call(e, n, e, t) : r, void 0 === i || (t.exports = i))
            }(0, (function () {
                "use strict";
                var t = function (e, n) {
                    return (t = Object.setPrototypeOf || {
                            __proto__: []
                        }
                        instanceof Array && function (t, e) {
                            t.__proto__ = e
                        } || function (t, e) {
                            for (var n in e) e.hasOwnProperty(n) && (t[n] = e[n])
                        })(e, n)
                };

                function e(e, n) {
                    function r() {
                        this.constructor = e
                    }
                    t(e, n), e.prototype = null === n ? Object.create(n) : (r.prototype = n.prototype, new r)
                }
                var n = function () {
                    return (n = Object.assign || function (t) {
                        for (var e, n = 1, r = arguments.length; n < r; n++)
                            for (var i in e = arguments[n]) Object.prototype.hasOwnProperty.call(e, i) && (t[i] = e[i]);
                        return t
                    }).apply(this, arguments)
                };

                function r(t, e, n, r) {
                    return new(n || (n = Promise))((function (i, o) {
                        function a(t) {
                            try {
                                c(r.next(t))
                            } catch (t) {
                                o(t)
                            }
                        }

                        function s(t) {
                            try {
                                c(r.throw(t))
                            } catch (t) {
                                o(t)
                            }
                        }

                        function c(t) {
                            var e;
                            t.done ? i(t.value) : (e = t.value, e instanceof n ? e : new n((function (t) {
                                t(e)
                            }))).then(a, s)
                        }
                        c((r = r.apply(t, e || [])).next())
                    }))
                }

                function i(t, e) {
                    var n, r, i, o, a = {
                        label: 0,
                        sent: function () {
                            if (1 & i[0]) throw i[1];
                            return i[1]
                        },
                        trys: [],
                        ops: []
                    };
                    return o = {
                        next: s(0),
                        throw: s(1),
                        return: s(2)
                    }, "function" == typeof Symbol && (o[Symbol.iterator] = function () {
                        return this
                    }), o;

                    function s(o) {
                        return function (s) {
                            return function (o) {
                                if (n) throw new TypeError("Generator is already executing.");
                                for (; a;) try {
                                    if (n = 1, r && (i = 2 & o[0] ? r.return : o[0] ? r.throw || ((i = r.return) && i.call(r), 0) : r.next) && !(i = i.call(r, o[1])).done) return i;
                                    switch (r = 0, i && (o = [2 & o[0], i.value]), o[0]) {
                                        case 0:
                                        case 1:
                                            i = o;
                                            break;
                                        case 4:
                                            return a.label++, {
                                                value: o[1],
                                                done: !1
                                            };
                                        case 5:
                                            a.label++, r = o[1], o = [0];
                                            continue;
                                        case 7:
                                            o = a.ops.pop(), a.trys.pop();
                                            continue;
                                        default:
                                            if (i = a.trys, !((i = i.length > 0 && i[i.length - 1]) || 6 !== o[0] && 2 !== o[0])) {
                                                a = 0;
                                                continue
                                            }
                                            if (3 === o[0] && (!i || o[1] > i[0] && o[1] < i[3])) {
                                                a.label = o[1];
                                                break
                                            }
                                            if (6 === o[0] && a.label < i[1]) {
                                                a.label = i[1], i = o;
                                                break
                                            }
                                            if (i && a.label < i[2]) {
                                                a.label = i[2], a.ops.push(o);
                                                break
                                            }
                                            i[2] && a.ops.pop(), a.trys.pop();
                                            continue
                                    }
                                    o = e.call(t, a)
                                } catch (t) {
                                    o = [6, t], r = 0
                                } finally {
                                    n = i = 0
                                }
                                if (5 & o[0]) throw o[1];
                                return {
                                    value: o[0] ? o[1] : void 0,
                                    done: !0
                                }
                            }([o, s])
                        }
                    }
                }

                function o(t) {
                    var e = "function" == typeof Symbol && Symbol.iterator,
                        n = e && t[e],
                        r = 0;
                    if (n) return n.call(t);
                    if (t && "number" == typeof t.length) return {
                        next: function () {
                            return t && r >= t.length && (t = void 0), {
                                value: t && t[r++],
                                done: !t
                            }
                        }
                    };
                    throw new TypeError(e ? "Object is not iterable." : "Symbol.iterator is not defined.")
                }

                function a(t, e) {
                    var n = "function" == typeof Symbol && t[Symbol.iterator];
                    if (!n) return t;
                    var r, i, o = n.call(t),
                        a = [];
                    try {
                        for (;
                            (void 0 === e || e-- > 0) && !(r = o.next()).done;) a.push(r.value)
                    } catch (t) {
                        i = {
                            error: t
                        }
                    } finally {
                        try {
                            r && !r.done && (n = o.return) && n.call(o)
                        } finally {
                            if (i) throw i.error
                        }
                    }
                    return a
                }
                var s = function () {
                        function t() {
                            this.listenersMap = {}
                        }
                        return t.prototype.target = function (t) {
                            var e = this;
                            return {
                                on: function (n, r) {
                                    e.on(n, r, {
                                        target: t
                                    })
                                }
                            }
                        }, t.prototype.on = function (t, e, n) {
                            var r, i, a = (void 0 === n ? {} : n).target,
                                s = Array.isArray(t) ? t : [t];
                            try {
                                for (var c = o(s), u = c.next(); !u.done; u = c.next()) {
                                    var h = u.value;
                                    void 0 === this.listenersMap[h] && (this.listenersMap[h] = []), void 0 !== a && (e.target = a), this.listenersMap[h].push(e)
                                }
                            } catch (t) {
                                r = {
                                    error: t
                                }
                            } finally {
                                try {
                                    u && !u.done && (i = c.return) && i.call(c)
                                } finally {
                                    if (r) throw r.error
                                }
                            }
                        }, t.prototype.off = function (t, e) {
                            var n = this.listenersMap[t];
                            if (void 0 !== n)
                                if (void 0 === e) delete this.listenersMap[t];
                                else {
                                    var r = n.findIndex((function (t) {
                                        return t === e
                                    }));
                                    n.splice(r, 1)
                                }
                        }, t.prototype.emit = function (t, e, n) {
                            var r, i;
                            void 0 === n && (n = function () {
                                return !0
                            });
                            var a = this.listenersMap[t];
                            if (void 0 !== a && 0 < a.length) try {
                                for (var s = o(a), c = s.next(); !c.done; c = s.next()) {
                                    var u = c.value;
                                    n({
                                        target: u.target
                                    }) && u(e)
                                }
                            } catch (t) {
                                r = {
                                    error: t
                                }
                            } finally {
                                try {
                                    c && !c.done && (i = s.return) && i.call(s)
                                } finally {
                                    if (r) throw r.error
                                }
                            }
                        }, t.prototype.destroy = function () {
                            this.listenersMap = {}
                        }, t
                    }(),
                    c = Object.prototype.toString,
                    u = "cancel",
                    h = "end",
                    l = "touch" + h,
                    f = "touch" + u,
                    p = window.wx || "ontouchstart" in window,
                    d = "start",
                    v = "move",
                    g = h,
                    m = "r",
                    y = "f",
                    b = u;

                function x(t) {
                    return Math.round(100 * t) / 100
                }
                var w = function () {},
                    T = function (t) {
                        function n() {
                            return null !== t && t.apply(this, arguments) || this
                        }
                        return e(n, t), n.prototype.load = function (t, e) {
                            var n = [],
                                r = [];
                            Array.from(t.touches).forEach((function (t) {
                                var i = t.clientX,
                                    o = t.clientY,
                                    a = t.target;
                                (null == e ? void 0 : e.contains(a)) && (n.push(a), r.push({
                                    clientX: i,
                                    clientY: o,
                                    target: a
                                }))
                            }));
                            var i = Array.from(t.changedTouches).map((function (t) {
                                return {
                                    clientX: t.clientX,
                                    clientY: t.clientY,
                                    target: t.target
                                }
                            }));
                            return {
                                inputType: t.type.replace("touch", ""),
                                changedPoints: i,
                                points: r,
                                nativeEvent: t,
                                target: t.target,
                                targets: n
                            }
                        }, n
                    }(w),
                    E = function (t) {
                        function n() {
                            var e = t.call(this) || this;
                            return e.target = null, e.isPressed = !1, e
                        }
                        return e(n, t), n.prototype.load = function (t) {
                            var e, n = t.clientX,
                                r = t.clientY,
                                i = t.type,
                                o = t.button,
                                a = t.target,
                                s = [{
                                    clientX: n,
                                    clientY: r,
                                    target: a
                                }];
                            "mousedown" === i && 0 === o ? (this.target = a, this.isPressed = !0, e = "start") : this.isPressed && ("mousemove" === i ? e = "move" : "mouseup" === i && (s = [], e = h, this.isPressed = !1));
                            var c = this.prevPoints || [{
                                clientX: n,
                                clientY: r,
                                target: a
                            }];
                            if (this.prevPoints = [{
                                    clientX: n,
                                    clientY: r,
                                    target: a
                                }], void 0 !== e) return {
                                inputType: e,
                                changedPoints: c,
                                points: s,
                                target: this.target,
                                targets: [this.target],
                                nativeEvent: t
                            }
                        }, n
                    }(w),
                    O = function () {
                        function t(t) {
                            var e = p ? T : E;
                            this.adapter = new e, this.id = 0, this.el = t
                        }
                        return t.prototype.transform = function (t) {
                            this.prevInput = this.activeInput;
                            var e = this.adapter.load(t, this.el);
                            if (void 0 !== e) {
                                var r = Number.MAX_SAFE_INTEGER > this.id ? ++this.id : 1,
                                    i = function (t) {
                                        var e = t.inputType,
                                            r = t.points,
                                            i = t.changedPoints,
                                            o = t.nativeEvent,
                                            a = r.length,
                                            s = "start" === e,
                                            c = h === e && 0 === a || u === e,
                                            l = performance.now(),
                                            f = I(r) || I(i),
                                            p = f.x,
                                            d = f.y,
                                            v = o.currentTarget;
                                        return n(n({}, t), {
                                            x: p,
                                            y: d,
                                            timestamp: l,
                                            isStart: s,
                                            isEnd: c,
                                            pointLength: a,
                                            currentTarget: v,
                                            getOffset: function (t) {
                                                void 0 === t && (t = v);
                                                var e = t.getBoundingClientRect();
                                                return {
                                                    x: p - Math.round(e.left),
                                                    y: d - Math.round(e.top)
                                                }
                                            }
                                        })
                                    }(n(n({}, e), {
                                        id: r
                                    }));
                                this.activeInput = i;
                                var o = i.isStart,
                                    a = i.pointLength;
                                return o && (this.startInput = i, this.prevInput = void 0, this.startMultiInput = 1 < a ? i : void 0), n(n({}, i), {
                                    prevInput: this.prevInput,
                                    startMultiInput: this.startMultiInput,
                                    startInput: this.startInput
                                })
                            }
                        }, t
                    }();

                function I(t) {
                    var e = t.length;
                    if (0 < e) {
                        if (1 === e) {
                            var n = t[0],
                                r = n.clientX,
                                i = n.clientY;
                            return {
                                x: Math.round(r),
                                y: Math.round(i)
                            }
                        }
                        var o = t.reduce((function (t, e) {
                            return t.x += e.clientX, t.y += e.clientY, t
                        }), {
                            x: 0,
                            y: 0
                        });
                        return {
                            x: Math.round(o.x / e),
                            y: Math.round(o.y / e)
                        }
                    }
                }

                function S(t, e, n) {
                    e.target, e.currentTarget;
                    var r, i = e.type,
                        o = function (t, e) {
                            var n = {};
                            for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && e.indexOf(r) < 0 && (n[r] = t[r]);
                            if (null != t && "function" == typeof Object.getOwnPropertySymbols) {
                                var i = 0;
                                for (r = Object.getOwnPropertySymbols(t); i < r.length; i++) e.indexOf(r[i]) < 0 && Object.prototype.propertyIsEnumerable.call(t, r[i]) && (n[r[i]] = t[r[i]])
                            }
                            return n
                        }(e, ["target", "currentTarget", "type"]);
                    return document.createEvent ? (r = document.createEvent("HTMLEvents")).initEvent(i, null == n ? void 0 : n.bubbles, null == n ? void 0 : n.cancelable) : r = new Event(i, n), Object.assign(r, o, {
                        match: function () {
                            return e.targets.every((function (t) {
                                return r.currentTarget.contains(t)
                            }))
                        }
                    }), t.dispatchEvent(r)
                }

                function M(t, e) {
                    if (!e.isPreventDefault) return !1;
                    var n, r = !0;
                    if (null !== t.target) {
                        var i = e.preventDefaultExclude;
                        if (n = i, "[object RegExp]" === c.call(n)) {
                            if ("tagName" in t.target) {
                                var o = t.target.tagName;
                                r = !i.test(o)
                            }
                        } else(function (t) {
                            return "[object Function]" === c.call(t)
                        })(i) && (r = !i(t))
                    }
                    return r
                }
                var R = ["touchstart", "touchmove", l, f];

                function P(t, e, n) {
                    var r = null == n ? void 0 : n.name;
                    if (void 0 === r || void 0 === t.recognizerMap[r]) {
                        var i = new e(n);
                        t.recognizerMap[i.name] = i, i.recognizerMap = t.recognizerMap, t.recognizers.push(t.recognizerMap[i.name])
                    }
                }

                function _(t, e) {
                    var n, r;
                    if (void 0 === e) t.recognizers = [], t.recognizerMap = {};
                    else try {
                        for (var i = o(t.recognizers.entries()), s = i.next(); !s.done; s = i.next()) {
                            var c = a(s.value, 2),
                                u = c[0];
                            if (e === c[1].options.name) {
                                t.recognizers.splice(u, 1), delete t.recognizerMap[e];
                                break
                            }
                        }
                    } catch (t) {
                        n = {
                            error: t
                        }
                    } finally {
                        try {
                            s && !s.done && (r = i.return) && r.call(i)
                        } finally {
                            if (n) throw n.error
                        }
                    }
                }

                function A(t, e) {
                    var r = e.type,
                        i = e.target,
                        o = e.targets;
                    t.emit(r, e, (function (t) {
                        if (void 0 !== (null == t ? void 0 : t.target)) {
                            var e = t.target;
                            return o.every((function (t) {
                                return e.contains(t)
                            }))
                        }
                        return !0
                    })), t.emit("at:after", e), t.options.domEvents && void 0 !== t.el && null !== i && (S(i, e, t.options.domEvents), S(i, n(n({}, e), {
                        _type: e.type,
                        type: "at:after"
                    }), t.options.domEvents))
                }
                var C = {
                        domEvents: {
                            bubbles: !0,
                            cancelable: !0
                        },
                        isPreventDefault: !0,
                        preventDefaultExclude: /^(?:INPUT|TEXTAREA|BUTTON|SELECT)$/
                    },
                    L = function (t) {
                        function r(e, i) {
                            var o = t.call(this) || this;
                            if (o.recognizerMap = {}, o.recognizers = [], o.cacheComputedFunctionGroup = Object.create(null), o.el = e, o.input = new O(e), o.options = n(n({}, C), i), o.recognizerMap = r.recognizerMap, o.recognizers = r.recognizers, void 0 !== e) {
                                e.style.webkitTapHighlightColor = "rgba(0,0,0,0)";
                                var a = !1;
                                try {
                                    var s = {};
                                    Object.defineProperty(s, "passive", {
                                        get: function () {
                                            a = !0
                                        }
                                    }), window.addEventListener("_", (function () {}), s)
                                } catch (t) {}
                                o.on("unbind", function (t, e, n, r) {
                                    return p || "Touch" === r ? (R.forEach((function (r) {
                                        t.addEventListener(r, e, n)
                                    })), function () {
                                        R.forEach((function (n) {
                                            t.removeEventListener(n, e)
                                        }))
                                    }) : (t.addEventListener("mousedown", e, n), window.addEventListener("mousemove", e, n), window.addEventListener("mouseup", e, n), function () {
                                        t.removeEventListener("mousedown", e), window.removeEventListener("mousemove", e), window.removeEventListener("mouseup", e)
                                    })
                                }(e, o.catchEvent.bind(o), !(o.options.isPreventDefault || !a) && {
                                    passive: !0
                                }, o.options.device))
                            }
                            return o
                        }
                        return e(r, t), r.prototype.use = function (t, e) {
                            P(this, t, e)
                        }, r.prototype.removeUse = function (t) {
                            _(this, t)
                        }, r.prototype.catchEvent = function (t) {
                            var e, r, i = this;
                            M(t, this.options) && t.preventDefault();
                            var a = this.input.transform(t);
                            if (void 0 !== a) {
                                var s = "at:touch" + a.inputType;
                                this.emit("at:touch", a), this.emit(s, a);
                                var c = this.options.domEvents;
                                if (!1 !== c) {
                                    var u = t.target;
                                    null !== u && (S(u, n(n({}, a), {
                                        type: "at:touch"
                                    }), c), S(u, n(n({}, a), {
                                        type: s
                                    }), c))
                                }
                                var h = Object.create(null),
                                    l = function (t) {
                                        if (t.disabled) return "continue";
                                        t.computedGroup = h, t.computeFunctionMap = f.cacheComputedFunctionGroup, t.recognize(a, (function (e, r) {
                                            var o = n(n(n({}, a), r), {
                                                type: e,
                                                baseType: t.name
                                            });
                                            Object.freeze(o), void 0 === i.beforeEachHook ? A(i, o) : i.beforeEachHook(t, (function () {
                                                A(i, o)
                                            }))
                                        })), h = t.computedGroup, f.cacheComputedFunctionGroup = t.computeFunctionMap
                                    },
                                    f = this;
                                try {
                                    for (var p = o(this.recognizers), d = p.next(); !d.done; d = p.next()) l(d.value)
                                } catch (t) {
                                    e = {
                                        error: t
                                    }
                                } finally {
                                    try {
                                        d && !d.done && (r = p.return) && r.call(p)
                                    } finally {
                                        if (e) throw e.error
                                    }
                                }
                            }
                        }, r.prototype.beforeEach = function (t) {
                            this.beforeEachHook = t
                        }, r.prototype.get = function (t) {
                            return this.recognizerMap[t]
                        }, r.prototype.set = function (t) {
                            this.options = n(n({}, this.options), t)
                        }, r.prototype.destroy = function () {
                            this.emit("unbind"), this.listenersMap = {}
                        }, r.version = "0.7.7", r.recognizers = [], r.recognizerMap = {}, r.use = function (t, e) {
                            P(r, t, e)
                        }, r.removeUse = function (t) {
                            _(r, t)
                        }, r
                    }(s);

                function k(t) {
                    -1 !== [g, b, m, y].indexOf(t.status) && (t.status = "p")
                }

                function z(t, e, n) {
                    var r = t.test(e);
                    k(t);
                    var i = e.inputType;
                    t.status = function (t, e, n) {
                        var r, i, o, a, s, c, l, f = {
                            1: (r = {}, r.p = (i = {}, i.move = d, i), r[d] = (o = {}, o.move = v, o[h] = g, o[u] = b, o), r[v] = (a = {}, a.move = v, a[h] = g, a[u] = b, a), r),
                            0: (s = {}, s[d] = (c = {}, c.move = b, c[h] = g, c[u] = b, c), s[v] = (l = {}, l.start = y, l.move = b, l[h] = g, l[u] = b, l), s)
                        };
                        return void 0 !== f[Number(t)][e] && f[Number(t)][e][n] || e
                    }(r, t.status, i);
                    var o = t.computed;
                    t.isRecognized = [d, v].includes(t.status);
                    var a = t.name,
                        s = t.status,
                        c = t.isRecognized;
                    return c && n(a, o), (c || [g, b].includes(t.status)) && n(a + s, o), r
                }
                var D = function () {
                        function t(t) {
                            this.disabled = !1, this.status = "p", this.isRecognized = !1, this.recognizerMap = {}, this.computedGroup = {}, this.computed = {}, this.computeFunctionMap = {}, this.options = t, this.name = this.options.name
                        }
                        return t.prototype.set = function (t) {
                            return void 0 !== t && (this.options = n(n({}, this.options), t)), this
                        }, t.prototype.isValidPointLength = function (t) {
                            return 0 === this.options.pointLength || this.options.pointLength === t
                        }, t.prototype.compute = function (t, e) {
                            var n, r, i = Object.create(null);
                            try {
                                for (var a = o(t), s = a.next(); !s.done; s = a.next()) {
                                    var c = s.value,
                                        u = c._id,
                                        h = this.computedGroup,
                                        l = this.computeFunctionMap;
                                    for (var f in void 0 === l[u] && (l[u] = c()), h[u] = h[u] || l[u](e), h[u]) i[f] = h[u][f]
                                }
                            } catch (t) {
                                n = {
                                    error: t
                                }
                            } finally {
                                try {
                                    s && !s.done && (r = a.return) && r.call(a)
                                } finally {
                                    if (n) throw n.error
                                }
                            }
                            return i
                        }, t
                    }(),
                    j = function (t) {
                        return Math.sqrt(t.x * t.x + t.y * t.y)
                    },
                    F = function (t) {
                        return t / Math.PI * 180
                    },
                    U = function (t, e) {
                        var n = function (t, e) {
                            var n = j(t) * j(e);
                            if (0 === n) return 0;
                            var r = function (t, e) {
                                return t.x * e.x + t.y * e.y
                            }(t, e) / n;
                            return r > 1 && (r = 1), Math.acos(r)
                        }(t, e);
                        return function (t, e) {
                            return t.x * e.y - e.x * t.y
                        }(t, e) > 0 && (n *= -1), F(n)
                    },
                    N = function (t, e) {
                        return t === e ? "none" : Math.abs(t) > Math.abs(e) ? 0 < t ? "right" : "left" : 0 < e ? "down" : "up"
                    };

                function X() {
                    return function (t) {
                        var e = t.prevInput,
                            n = 0,
                            r = 0,
                            i = 0;
                        if (void 0 !== e && (n = t.x - e.x, r = t.y - e.y, 0 !== n || 0 !== r)) {
                            var o = Math.sqrt(Math.pow(n, 2) + Math.pow(r, 2));
                            i = Math.round(F(Math.acos(Math.abs(n) / o)))
                        }
                        return {
                            deltaX: n,
                            deltaY: r,
                            deltaXYAngle: i
                        }
                    }
                }

                function Y() {
                    var t = 0,
                        e = 0,
                        n = 0,
                        r = 0,
                        i = 0,
                        o = "none";
                    return function (a) {
                        var s = a.inputType,
                            c = a.startInput;
                        return "start" === s ? (t = 0, e = 0, n = 0, r = 0, i = 0, o = "none") : "move" === s && (t = Math.round(a.points[0].clientX - c.points[0].clientX), e = Math.round(a.points[0].clientY - c.points[0].clientY), n = Math.abs(t), r = Math.abs(e), i = Math.round(j({
                            x: n,
                            y: r
                        })), o = N(t, e)), {
                            displacementX: t,
                            displacementY: e,
                            distanceX: n,
                            distanceY: r,
                            distance: i,
                            overallDirection: o
                        }
                    }
                }

                function B() {
                    var t = 0;
                    return function (e) {
                        return "start" === e.inputType && (t = e.pointLength), {
                            maxPointLength: t
                        }
                    }
                }

                function V() {
                    var t, e, n = 0,
                        r = 0,
                        i = 0,
                        o = 0;
                    return function (a) {
                        if (void 0 !== a) {
                            var s = a.inputType;
                            e = e || a.startInput;
                            var c = a.timestamp - e.timestamp;
                            if ("move" === s && 16 < c) {
                                var u = a.x - e.x,
                                    h = a.y - e.y;
                                i = Math.round(u / c * 100) / 100, o = Math.round(h / c * 100) / 100, n = Math.abs(i), r = Math.abs(o), t = N(u, h) || t, e = a
                            }
                        }
                        return {
                            velocityX: n,
                            velocityY: r,
                            speedX: i,
                            speedY: o,
                            direction: t
                        }
                    }
                }

                function $(t) {
                    return {
                        x: t.points[1].clientX - t.points[0].clientX,
                        y: t.points[1].clientY - t.points[0].clientY
                    }
                }

                function H() {
                    return function (t) {
                        var e = t.prevInput,
                            n = t.startMultiInput;
                        if (void 0 !== n && void 0 !== e && t.id !== n.id && 1 < e.pointLength && 1 < t.pointLength) return {
                            startV: $(n),
                            prevV: $(e),
                            activeV: $(t)
                        }
                    }
                }
                X._id = "ComputeDeltaXY", Y._id = "computeDistance", B._id = "computeMaxLength", V._id = "ComputeVAndDir", H._id = "ComputeVectorForMutli";
                var W = {
                        name: "tap",
                        pointLength: 1,
                        tapTimes: 1,
                        waitNextTapTime: 300,
                        maxDistance: 2,
                        maxDistanceFromPrevTap: 9,
                        maxPressTime: 250
                    },
                    G = function (t) {
                        function r(e) {
                            var r = t.call(this, n(n({}, W), e)) || this;
                            return r.tapCount = 0, r
                        }
                        return e(r, t), r.prototype._isValidDistanceFromPrevTap = function (t) {
                            if (void 0 !== this.prevTapPoint) {
                                var e = j({
                                    x: t.x - this.prevTapPoint.x,
                                    y: t.y - this.prevTapPoint.y
                                });
                                return this.prevTapPoint = t, this.options.maxDistanceFromPrevTap >= e
                            }
                            return this.prevTapPoint = t, !0
                        }, r.prototype._isValidInterval = function () {
                            var t = performance.now();
                            if (void 0 === this.prevTapTime) return this.prevTapTime = t, !0;
                            var e = t - this.prevTapTime;
                            return this.prevTapTime = t, e < this.options.waitNextTapTime
                        }, r.prototype.recognize = function (t, e) {
                            var r = t.inputType,
                                i = t.x,
                                o = t.y;
                            this.computed = this.compute([B, Y], t), h === r && (this.status = "p", this.test(t) ? (this.cancelCountDownToFail(), this._isValidDistanceFromPrevTap({
                                x: i,
                                y: o
                            }) && this._isValidInterval() ? this.tapCount++ : this.tapCount = 1, 0 == this.tapCount % this.options.tapTimes ? (this.status = m, e(this.options.name, n(n({}, this.computed), {
                                tapCount: this.tapCount
                            })), this.reset()) : this.countDownToFail()) : (this.reset(), this.status = y))
                        }, r.prototype.countDownToFail = function () {
                            var t = this;
                            this._countDownToFailTimer = setTimeout((function () {
                                t.status = y, t.reset()
                            }), this.options.waitNextTapTime)
                        }, r.prototype.cancelCountDownToFail = function () {
                            clearTimeout(this._countDownToFailTimer)
                        }, r.prototype.reset = function () {
                            this.tapCount = 0, this.prevTapPoint = void 0, this.prevTapTime = void 0
                        }, r.prototype.test = function (t) {
                            var e = t.startInput,
                                n = t.pointLength,
                                r = t.timestamp - e.timestamp,
                                i = this.computed,
                                o = i.maxPointLength,
                                a = i.distance;
                            return o === this.options.pointLength && 0 === n && this.options.maxDistance >= a && this.options.maxPressTime > r
                        }, r
                    }(D),
                    K = {
                        name: "pan",
                        threshold: 10,
                        pointLength: 1
                    },
                    q = function (t) {
                        function r(e) {
                            return t.call(this, n(n({}, K), e)) || this
                        }
                        return e(r, t), r.prototype.test = function (t) {
                            var e = t.pointLength,
                                n = this.computed.distance;
                            return (this.isRecognized || this.options.threshold <= n) && this.isValidPointLength(e)
                        }, r.prototype.recognize = function (t, e) {
                            this.computed = this.compute([V, Y, X], t), void 0 !== this.computed.direction && z(this, t, e) && e(this.options.name + this.computed.direction, this.computed)
                        }, r
                    }(D),
                    J = {
                        name: "swipe",
                        threshold: 10,
                        velocity: .3,
                        pointLength: 1
                    },
                    Q = function (t) {
                        function r(e) {
                            return t.call(this, n(n({}, J), e)) || this
                        }
                        return e(r, t), r.prototype.test = function (t) {
                            var e = t.inputType;
                            if (h !== e) return !1;
                            var n = this.computed,
                                r = n.velocityX,
                                i = n.velocityY,
                                o = n.maxPointLength,
                                a = n.distance;
                            return this.options.pointLength === o && this.options.threshold < a && this.options.velocity < Math.max(r, i)
                        }, r.prototype.recognize = function (t, e) {
                            this.computed = this.compute([B, V, Y], t), this.test(t) && (e(this.options.name, this.computed), e(this.options.name + this.computed.direction, this.computed))
                        }, r
                    }(D),
                    Z = {
                        name: "press",
                        pointLength: 1,
                        maxDistance: 9,
                        minPressTime: 251
                    },
                    tt = function (t) {
                        function r(e) {
                            return t.call(this, n(n({}, Z), e)) || this
                        }
                        return e(r, t), r.prototype.recognize = function (t, e) {
                            var n = this,
                                r = t.inputType,
                                i = t.startInput,
                                o = t.pointLength;
                            if ("start" === r && this.isValidPointLength(o)) k(this), this.cancel(), this._timeoutId = setTimeout((function () {
                                n.status = m, e(n.options.name, t)
                            }), this.options.minPressTime);
                            else if (h === r && m === this.status) e(this.options.name + "up", this.computed);
                            else if (m !== this.status) {
                                var a = t.timestamp - i.timestamp;
                                (!this.test(t) || this.options.minPressTime > a && [h, u].includes(r)) && (this.cancel(), this.status = y)
                            }
                        }, r.prototype.test = function (t) {
                            this.computed = this.compute([Y], t);
                            var e = this.computed.distance;
                            return this.options.maxDistance > e
                        }, r.prototype.cancel = function () {
                            clearTimeout(this._timeoutId)
                        }, r
                    }(D),
                    et = {
                        name: "pinch",
                        threshold: 0,
                        pointLength: 2
                    },
                    nt = function (t) {
                        function r(e) {
                            return t.call(this, n(n({}, et), e)) || this
                        }
                        return e(r, t), r.prototype.test = function (t) {
                            var e = t.pointLength,
                                n = this.computed.scale;
                            return this.isValidPointLength(e) && void 0 !== n && (this.options.threshold < Math.abs(n - 1) || this.isRecognized)
                        }, r.prototype.recognize = function (t, e) {
                            var r, i, o, a, s, c = this.compute([H], t);
                            "activeV" in c && (this.computed = n(n({}, this.computed), (i = (r = c).startV, o = r.prevV, a = r.activeV, s = x(j(a) / j(o)), {
                                scale: x(j(a) / j(i)),
                                deltaScale: s
                            }))), z(this, t, e)
                        }, r
                    }(D),
                    rt = {
                        name: "rotate",
                        threshold: 0,
                        pointLength: 2
                    },
                    it = function (t) {
                        function r(e) {
                            return t.call(this, n(n({}, rt), e)) || this
                        }
                        return e(r, t), r.prototype.test = function (t) {
                            var e = t.pointLength,
                                n = this.computed.angle;
                            return this.isValidPointLength(e) && (this.options.threshold < Math.abs(n) || this.isRecognized)
                        }, r.prototype.recognize = function (t, e) {
                            var r, i, o, a, s, c = this.compute([H], t);
                            "activeV" in c && (this.computed = n(n({}, this.computed), (i = (r = c).startV, o = r.prevV, a = r.activeV, s = Math.round(U(a, o)), {
                                angle: Math.round(U(a, i)),
                                deltaAngle: s
                            }))), z(this, t, e)
                        }, r
                    }(D);
                L.use(G), L.use(q), L.use(Q), L.use(tt), L.use(nt), L.use(it), L.Tap = G, L.Pan = q, L.Swipe = Q, L.Press = tt, L.Pinch = nt, L.Rotate = it, L.STATUS_POSSIBLE = "p", L.STATUS_START = d, L.STATUS_MOVE = v, L.STATUS_END = g, L.STATUS_CANCELLED = b, L.STATUS_FAILED = y, L.STATUS_RECOGNIZED = m;
                var ot = {};

                function at(t) {
                    return new Promise((function (e, n) {
                        if (a = t, "[object HTMLImageElement]" === Object.prototype.toString.call(a)) e(t);
                        else if (/^#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$/.test(t)) {
                            var r = document.createElement("canvas");
                            r.width = 1, r.height = 1;
                            var i = r.getContext("2d");
                            i.fillStyle = t, i.fillRect(0, 0, 1, 1), at(r.toDataURL()).then(e)
                        } else {
                            if (ot[t]) return void e(ot[t]);
                            var o = new Image;
                            o.setAttribute("crossOrigin", "Anonymous"), o.onload = function () {
                                ot[t] = o, e(o)
                            }, o.onerror = n, o.src = t
                        }
                        var a
                    }))
                }
                return function (t) {
                    function n(e, n, r) {
                        void 0 === n && (n = 400), void 0 === r && (r = 300);
                        var i = t.call(this, e, n, r) || this;
                        i.moveRate = 1, i.moveRate = e.offsetWidth / n;
                        var o = new L(e);
                        return i.at = o, o.on(["tap", "pinchstart", "rotatestart"], (function (t) {
                            var e = t.x,
                                n = t.y,
                                r = i,
                                o = r.moveRate,
                                a = r.canvas.getBoundingClientRect(),
                                s = [(e - a.left) / o, (n - a.top) / o];
                            i.changeOrg(s), i.emit("change-org", s)
                        })), o.on("at:after", (function (t) {
                            i.emit(t.type, t)
                        })), o.on("panmove", (function (t) {
                            var e = t.deltaX,
                                n = t.deltaY;
                            i.move(e / i.moveRate, n / i.moveRate)
                        })), o.on("pinchmove", (function (t) {
                            var e = t.deltaScale;
                            i.zoom(e)
                        })), o.on("rotatemove", (function (t) {
                            var e = t.deltaAngle;
                            i.rotate(e, i.org)
                        })), i
                    }
                    return e(n, t), n.prototype.destroy = function () {
                        this.at.destroy()
                    }, n
                }(function (t) {
                    function n(e, n, r) {
                        void 0 === n && (n = 400), void 0 === r && (r = 300);
                        var i = t.call(this) || this;
                        return i.canvasWidth = 0, i.canvasHeight = 0, i.org = [0, 0], i.angle = 0, i.scale = 1, i.overlayImages = [], i.backgroundImages = [], i.imgWidth = 0, i.imgHeight = 0, i.offsetInOA = [0, 0], i.offsetInOB = [0, 0], i._timeout = -1, e.width = n, e.height = r, i.canvasWidth = n, i.canvasHeight = r, i.canvas = e, i.context = i.canvas.getContext("2d"), i
                    }
                    return e(n, t), Object.defineProperty(n.prototype, "rad", {
                        get: function () {
                            return this.angle * Math.PI / 180
                        },
                        enumerable: !1,
                        configurable: !0
                    }), n.prototype.render = function () {
                        var t = this;
                        clearTimeout(this._timeout), this._timeout = setTimeout((function () {
                            return r(t, void 0, void 0, (function () {
                                var t, e, n, r, a, s, c, u, h, l, f, p, d, v, g, m, y, b, x, w, T;
                                return i(this, (function (i) {
                                    if (null == this.context || !this.img || 0 === this.canvasWidth || 0 === this.canvasHeight) return [2];
                                    e = (t = this).context, n = t.canvasWidth, r = t.canvasHeight, a = t.org, s = t.rad, c = t.offsetInOB, u = t.scale, h = t.img, l = t.imgWidth, f = t.imgHeight, e.clearRect(0, 0, n, r), this.drawChessboard(e);
                                    try {
                                        for (p = o(this.backgroundImages), d = p.next(); !d.done; d = p.next()) v = d.value, e.drawImage(v, 0, 0, this.canvasWidth, this.canvasHeight)
                                    } catch (t) {
                                        b = {
                                            error: t
                                        }
                                    } finally {
                                        try {
                                            d && !d.done && (x = p.return) && x.call(p)
                                        } finally {
                                            if (b) throw b.error
                                        }
                                    }
                                    e.save(), e.translate(a[0], a[1]), e.scale(u, u), e.rotate(s), e.drawImage(h, 0, 0, h.width, h.height, c[0], c[1], l, f), e.restore();
                                    try {
                                        for (g = o(this.overlayImages), m = g.next(); !m.done; m = g.next()) y = m.value, e.drawImage(y, 0, 0, this.canvasWidth, this.canvasHeight)
                                    } catch (t) {
                                        w = {
                                            error: t
                                        }
                                    } finally {
                                        try {
                                            m && !m.done && (T = g.return) && T.call(g)
                                        } finally {
                                            if (w) throw w.error
                                        }
                                    }
                                    return this.emit("transform", {
                                        offset: this.offsetInOA,
                                        scale: this.scale,
                                        angle: this.angle,
                                        org: this.org
                                    }), [2]
                                }))
                            }))
                        }), 0)
                    }, n.prototype.changeOrg = function (t) {
                        this.org = t, this.offsetInOB = this.switchToOB(this.offsetInOA), this.render()
                    }, n.prototype.changeOverlay = function () {
                        for (var t = [], e = 0; e < arguments.length; e++) t[e] = arguments[e];
                        return r(this, void 0, void 0, (function () {
                            var e, n, r, a, s, c, u, h;
                            return i(this, (function (i) {
                                switch (i.label) {
                                    case 0:
                                        this.overlayImages = [], i.label = 1;
                                    case 1:
                                        i.trys.push([1, 6, 7, 8]), e = o(t), n = e.next(), i.label = 2;
                                    case 2:
                                        return n.done ? [3, 5] : (r = n.value, s = (a = this.overlayImages).push, [4, at(r)]);
                                    case 3:
                                        s.apply(a, [i.sent()]), i.label = 4;
                                    case 4:
                                        return n = e.next(), [3, 2];
                                    case 5:
                                        return [3, 8];
                                    case 6:
                                        return c = i.sent(), u = {
                                            error: c
                                        }, [3, 8];
                                    case 7:
                                        try {
                                            n && !n.done && (h = e.return) && h.call(e)
                                        } finally {
                                            if (u) throw u.error
                                        }
                                        return [7];
                                    case 8:
                                        return this.render(), [2]
                                }
                            }))
                        }))
                    }, n.prototype.changeBackground = function () {
                        for (var t = [], e = 0; e < arguments.length; e++) t[e] = arguments[e];
                        return r(this, void 0, void 0, (function () {
                            var e, n, r, a, s, c, u, h;
                            return i(this, (function (i) {
                                switch (i.label) {
                                    case 0:
                                        this.backgroundImages = [], i.label = 1;
                                    case 1:
                                        i.trys.push([1, 6, 7, 8]), e = o(t), n = e.next(), i.label = 2;
                                    case 2:
                                        return n.done ? [3, 5] : (r = n.value, s = (a = this.backgroundImages).push, [4, at(r)]);
                                    case 3:
                                        s.apply(a, [i.sent()]), i.label = 4;
                                    case 4:
                                        return n = e.next(), [3, 2];
                                    case 5:
                                        return [3, 8];
                                    case 6:
                                        return c = i.sent(), u = {
                                            error: c
                                        }, [3, 8];
                                    case 7:
                                        try {
                                            n && !n.done && (h = e.return) && h.call(e)
                                        } finally {
                                            if (u) throw u.error
                                        }
                                        return [7];
                                    case 8:
                                        return this.render(), [2]
                                }
                            }))
                        }))
                    }, n.prototype.changeImg = function (t) {
                        return r(this, void 0, void 0, (function () {
                            var e;
                            return i(this, (function (n) {
                                switch (n.label) {
                                    case 0:
                                        return e = this, [4, at(t)];
                                    case 1:
                                        return e.img = n.sent(), this.reset(), [2]
                                }
                            }))
                        }))
                    }, n.prototype.reset = function () {
                        if (this.img) {
                            this.changeOrg([this.canvasWidth / 2, this.canvasHeight / 2]);
                            var t = this.getCenterRectOffsetTopLeft(this.img.width, this.img.height, this.canvasWidth, this.canvasHeight),
                                e = t.top,
                                n = t.left,
                                r = t.width,
                                i = t.height;
                            this.offsetInOA = [n, e], this.scale = 1, this.angle = 0, this.offsetInOB = this.switchToOB(this.offsetInOA), this.imgWidth = r, this.imgHeight = i, this.render()
                        }
                    }, n.prototype.move = function (t, e) {
                        var n = a(this.offsetInOA, 2),
                            r = n[0],
                            i = n[1];
                        return this.moveTo(r + t, i + e), this.offsetInOA
                    }, n.prototype.moveTo = function (t, e) {
                        this.offsetInOA = [t, e], this.offsetInOB = this.switchToOB(this.offsetInOA), this.render()
                    }, n.prototype.changeOrgToImageCenter = function () {
                        var t = [this.offsetInOB[0] + this.imgWidth / 2, this.offsetInOB[1] + this.imgHeight / 2],
                            e = this.switchToOA(t);
                        this.changeOrg(e)
                    }, n.prototype.rotate = function (t, e) {
                        return this.rotateTo(this.angle + t, e), this.angle
                    }, n.prototype.rotateTo = function (t, e) {
                        void 0 === e && this.changeOrgToImageCenter(), this.angle = t, this.offsetInOA = this.switchToOA(this.offsetInOB), this.render()
                    }, n.prototype.zoom = function (t, e) {
                        return this.zoomTo(this.scale * t, e), this.scale
                    }, n.prototype.zoomTo = function (t, e) {
                        void 0 === e && this.changeOrgToImageCenter(), this.scale = t, this.offsetInOA = this.switchToOA(this.offsetInOB), this.render()
                    }, n.prototype.switchToOB = function (t) {
                        var e = a(t, 2),
                            n = e[0],
                            r = e[1],
                            i = this.rad,
                            o = this.scale,
                            s = this.org,
                            c = n - s[0],
                            u = r - s[1];
                        return [(Math.cos(i) * c + Math.sin(i) * u) / o, (-Math.sin(i) * c + Math.cos(i) * u) / o]
                    }, n.prototype.switchToOA = function (t) {
                        var e = a(t, 2),
                            n = e[0],
                            r = e[1],
                            i = this.rad,
                            o = this.scale,
                            s = this.org;
                        return [(Math.cos(i) * n - Math.sin(i) * r) * o + s[0], (Math.sin(i) * n + Math.cos(i) * r) * o + s[1]]
                    }, n.prototype.drawChessboard = function (t) {
                        var e = [24, Math.ceil(24 * this.canvasHeight / this.canvasWidth)],
                            n = this.canvasWidth / e[0];
                        t.save();
                        for (var r = "#ddd", i = 0; i <= e[0]; i++) {
                            for (var o = 0; o < e[1]; o++) {
                                t.fillStyle = r;
                                var a = 0 + n * i,
                                    s = 0 + n * o;
                                t.fillRect(a, s, n, n), r = "#ddd" === r ? "#fff" : "#ddd"
                            }
                            r = "#ddd" === r ? "#fff" : "#ddd"
                        }
                        t.stroke(), t.restore()
                    }, n.prototype.getCenterRectOffsetTopLeft = function (t, e, n, r) {
                        var i = [t / n, e / r];
                        if (i[0] > i[1]) {
                            var o = Math.floor(n * e / t);
                            return {
                                width: n,
                                height: o,
                                top: (r - o) / 2,
                                left: 0
                            }
                        }
                        var a = Math.floor(r * t / e);
                        return {
                            width: a,
                            height: r,
                            top: 0,
                            left: (n - a) / 2
                        }
                    }, n
                }(s))
            }))
        },
        9263: function (t, e, n) {
            "use strict";
            var r = n("ad6d"),
                i = n("9f7f"),
                o = RegExp.prototype.exec,
                a = String.prototype.replace,
                s = o,
                c = function () {
                    var t = /a/,
                        e = /b*/g;
                    return o.call(t, "a"), o.call(e, "a"), 0 !== t.lastIndex || 0 !== e.lastIndex
                }(),
                u = i.UNSUPPORTED_Y || i.BROKEN_CARET,
                h = void 0 !== /()??/.exec("")[1],
                l = c || h || u;
            l && (s = function (t) {
                var e, n, i, s, l = this,
                    f = u && l.sticky,
                    p = r.call(l),
                    d = l.source,
                    v = 0,
                    g = t;
                return f && (p = p.replace("y", ""), -1 === p.indexOf("g") && (p += "g"), g = String(t).slice(l.lastIndex), l.lastIndex > 0 && (!l.multiline || l.multiline && "\n" !== t[l.lastIndex - 1]) && (d = "(?: " + d + ")", g = " " + g, v++), n = new RegExp("^(?:" + d + ")", p)), h && (n = new RegExp("^" + d + "$(?!\\s)", p)), c && (e = l.lastIndex), i = o.call(f ? n : l, g), f ? i ? (i.input = i.input.slice(v), i[0] = i[0].slice(v), i.index = l.lastIndex, l.lastIndex += i[0].length) : l.lastIndex = 0 : c && i && (l.lastIndex = l.global ? i.index + i[0].length : e), h && i && i.length > 1 && a.call(i[0], n, (function () {
                    for (s = 1; s < arguments.length - 2; s++) void 0 === arguments[s] && (i[s] = void 0)
                })), i
            }), t.exports = s
        },
        "95e0": function (t, e, n) {
            "use strict";
            n("e911")
        },
        "98b7": function (t, e, n) {},
        "9f7f": function (t, e, n) {
            "use strict";
            var r = n("d039");

            function i(t, e) {
                return RegExp(t, e)
            }
            e.UNSUPPORTED_Y = r((function () {
                var t = i("a", "y");
                return t.lastIndex = 2, null != t.exec("abcd")
            })), e.BROKEN_CARET = r((function () {
                var t = i("^r", "gy");
                return t.lastIndex = 2, null != t.exec("str")
            }))
        },
        a094: function (t, e, n) {
            "use strict";
            var r = function () {
                    var t = this,
                        e = t.$createElement,
                        n = t._self._c || e;
                    return n("label", {
                        staticClass: "button-load-file"
                    }, [n("input", {
                        attrs: {
                            type: "file",
                            accept: "image/*",
                            multiple: ""
                        },
                        on: {
                            change: t.onChange
                        }
                    }), t._t("default", [t._v("Upload")])], 2)
                },
                i = [],
                o = (n("a630"), n("d81d"), n("b0c0"), n("d3b7"), n("3ca3"), n("ddb0"), n("96cf"), n("1da1")),
                a = {},
                s = function (t) {
                    return new Promise((function (e, n) {
                        if (a[t]) e(a[t]);
                        else {
                            var r = new Image;
                            r.onload = function () {
                                a[t] = r, e(r)
                            }, r.onerror = n, r.src = t
                        }
                    }))
                },
                c = {
                    name: "ButtonLoadFile",
                    props: {
                        cropSize: {
                            type: Array,
                            default: function () {
                                return [426, 269]
                            }
                        }
                    },
                    computed: {
                        cropRate: function () {
                            return this.cropSize[0] / this.cropSize[1]
                        }
                    },
                    data: function () {
                        return {
                            url: ""
                        }
                    },
                    methods: {
                        readFile: function (t) {
                            var e = this;
                            return new Promise((function (n, r) {
                                var i = new FileReader;
                                i.readAsDataURL(t), i.onload = function () {
                                    var r = Object(o["a"])(regeneratorRuntime.mark((function r(i) {
                                        var o, a, c, u;
                                        return regeneratorRuntime.wrap((function (r) {
                                            while (1) switch (r.prev = r.next) {
                                                case 0:
                                                    return r.next = 2, s(i.target.result);
                                                case 2:
                                                    o = r.sent, a = o.width, c = o.height, u = e.crop(o), n({
                                                        source: {
                                                            fileName: t.name,
                                                            url: i.target.result,
                                                            img: o,
                                                            width: a,
                                                            height: c
                                                        },
                                                        crop: u
                                                    });
                                                case 6:
                                                case "end":
                                                    return r.stop()
                                            }
                                        }), r)
                                    })));
                                    return function (t) {
                                        return r.apply(this, arguments)
                                    }
                                }(), i.onerror = r
                            }))
                        },
                        onChange: function (t) {
                            var e = this;
                            return Object(o["a"])(regeneratorRuntime.mark((function n() {
                                var r, i, a, s;
                                return regeneratorRuntime.wrap((function (n) {
                                    while (1) switch (n.prev = n.next) {
                                        case 0:
                                            if (r = t.target, i = r.files, a = Array.from(i), !(0 < a.length)) {
                                                n.next = 10;
                                                break
                                            }
                                            return n.next = 6, Promise.all(a.map(function () {
                                                var t = Object(o["a"])(regeneratorRuntime.mark((function t(n) {
                                                    return regeneratorRuntime.wrap((function (t) {
                                                        while (1) switch (t.prev = t.next) {
                                                            case 0:
                                                                return t.abrupt("return", e.readFile(n));
                                                            case 1:
                                                            case "end":
                                                                return t.stop()
                                                        }
                                                    }), t)
                                                })));
                                                return function (e) {
                                                    return t.apply(this, arguments)
                                                }
                                            }()));
                                        case 6:
                                            s = n.sent, e.$emit("loaded", s), n.next = 11;
                                            break;
                                        case 10:
                                            e.$emit("reset");
                                        case 11:
                                        case "end":
                                            return n.stop()
                                    }
                                }), n)
                            })))()
                        },
                        crop: function (t) {
                            var e = document.createElement("canvas"),
                                n = e.getContext("2d"),
                                r = t.width,
                                i = t.height,
                                o = r / i,
                                a = r,
                                s = i,
                                c = 0,
                                u = 0,
                                h = "x";
                            this.cropRate > o ? (h = "y", s = a / this.cropRate, c = (i - s) / 2) : (a = s * this.cropRate, u = (r - a) / 2), e.width = this.cropSize[0], e.height = this.cropSize[1];
                            var l = [t, u, c, a, s, 0, 0, this.cropSize[0], this.cropSize[1]];
                            n.drawImage.apply(n, l);
                            var f = e.toDataURL();
                            return {
                                url: f,
                                x: u,
                                y: c,
                                width: a,
                                height: s,
                                cropAxis: h,
                                cropRate: this.cropRate,
                                args: l
                            }
                        }
                    }
                },
                u = c,
                h = (n("46a8"), n("2877")),
                l = Object(h["a"])(u, r, i, !1, null, null, null);
            e["a"] = l.exports
        },
        a434: function (t, e, n) {
            "use strict";
            var r = n("23e7"),
                i = n("23cb"),
                o = n("a691"),
                a = n("50c4"),
                s = n("7b0b"),
                c = n("65f0"),
                u = n("8418"),
                h = n("1dde"),
                l = n("ae40"),
                f = h("splice"),
                p = l("splice", {
                    ACCESSORS: !0,
                    0: 0,
                    1: 2
                }),
                d = Math.max,
                v = Math.min,
                g = 9007199254740991,
                m = "Maximum allowed length exceeded";
            r({
                target: "Array",
                proto: !0,
                forced: !f || !p
            }, {
                splice: function (t, e) {
                    var n, r, h, l, f, p, y = s(this),
                        b = a(y.length),
                        x = i(t, b),
                        w = arguments.length;
                    if (0 === w ? n = r = 0 : 1 === w ? (n = 0, r = b - x) : (n = w - 2, r = v(d(o(e), 0), b - x)), b + n - r > g) throw TypeError(m);
                    for (h = c(y, r), l = 0; l < r; l++) f = x + l, f in y && u(h, l, y[f]);
                    if (h.length = r, n < r) {
                        for (l = x; l < b - r; l++) f = l + r, p = l + n, f in y ? y[p] = y[f] : delete y[p];
                        for (l = b; l > b - r + n; l--) delete y[l - 1]
                    } else if (n > r)
                        for (l = b - r; l > x; l--) f = l + r - 1, p = l + n - 1, f in y ? y[p] = y[f] : delete y[p];
                    for (l = 0; l < n; l++) y[l + x] = arguments[l + 2];
                    return y.length = b - r + n, h
                }
            })
        },
        a623: function (t, e, n) {
            "use strict";
            var r = n("23e7"),
                i = n("b727").every,
                o = n("a640"),
                a = n("ae40"),
                s = o("every"),
                c = a("every");
            r({
                target: "Array",
                proto: !0,
                forced: !s || !c
            }, {
                every: function (t) {
                    return i(this, t, arguments.length > 1 ? arguments[1] : void 0)
                }
            })
        },
        a640: function (t, e, n) {
            "use strict";
            var r = n("d039");
            t.exports = function (t, e) {
                var n = [][t];
                return !!n && r((function () {
                    n.call(null, e || function () {
                        throw 1
                    }, 1)
                }))
            }
        },
        ac1f: function (t, e, n) {
            "use strict";
            var r = n("23e7"),
                i = n("9263");
            r({
                target: "RegExp",
                proto: !0,
                forced: /./.exec !== i
            }, {
                exec: i
            })
        },
        aff5: function (t, e, n) {
            var r = n("23e7");
            r({
                target: "Number",
                stat: !0
            }, {
                MAX_SAFE_INTEGER: 9007199254740991
            })
        },
        bb2f: function (t, e, n) {
            var r = n("d039");
            t.exports = !r((function () {
                return Object.isExtensible(Object.preventExtensions({}))
            }))
        },
        c740: function (t, e, n) {
            "use strict";
            var r = n("23e7"),
                i = n("b727").findIndex,
                o = n("44d2"),
                a = n("ae40"),
                s = "findIndex",
                c = !0,
                u = a(s);
            s in [] && Array(1)[s]((function () {
                c = !1
            })), r({
                target: "Array",
                proto: !0,
                forced: c || !u
            }, {
                findIndex: function (t) {
                    return i(this, t, arguments.length > 1 ? arguments[1] : void 0)
                }
            }), o(s)
        },
        c975: function (t, e, n) {
            "use strict";
            var r = n("23e7"),
                i = n("4d64").indexOf,
                o = n("a640"),
                a = n("ae40"),
                s = [].indexOf,
                c = !!s && 1 / [1].indexOf(1, -0) < 0,
                u = o("indexOf"),
                h = a("indexOf", {
                    ACCESSORS: !0,
                    1: 0
                });
            r({
                target: "Array",
                proto: !0,
                forced: c || !u || !h
            }, {
                indexOf: function (t) {
                    return c ? s.apply(this, arguments) || 0 : i(this, t, arguments.length > 1 ? arguments[1] : void 0)
                }
            })
        },
        caad: function (t, e, n) {
            "use strict";
            var r = n("23e7"),
                i = n("4d64").includes,
                o = n("44d2"),
                a = n("ae40"),
                s = a("indexOf", {
                    ACCESSORS: !0,
                    1: 0
                });
            r({
                target: "Array",
                proto: !0,
                forced: !s
            }, {
                includes: function (t) {
                    return i(this, t, arguments.length > 1 ? arguments[1] : void 0)
                }
            }), o("includes")
        },
        d58f: function (t, e, n) {
            var r = n("1c0b"),
                i = n("7b0b"),
                o = n("44ad"),
                a = n("50c4"),
                s = function (t) {
                    return function (e, n, s, c) {
                        r(n);
                        var u = i(e),
                            h = o(u),
                            l = a(u.length),
                            f = t ? l - 1 : 0,
                            p = t ? -1 : 1;
                        if (s < 2)
                            while (1) {
                                if (f in h) {
                                    c = h[f], f += p;
                                    break
                                }
                                if (f += p, t ? f < 0 : l <= f) throw TypeError("Reduce of empty array with no initial value")
                            }
                        for (; t ? f >= 0 : l > f; f += p) f in h && (c = n(c, h[f], f, u));
                        return c
                    }
                };
            t.exports = {
                left: s(!1),
                right: s(!0)
            }
        },
        d784: function (t, e, n) {
            "use strict";
            n("ac1f");
            var r = n("6eeb"),
                i = n("d039"),
                o = n("b622"),
                a = n("9263"),
                s = n("9112"),
                c = o("species"),
                u = !i((function () {
                    var t = /./;
                    return t.exec = function () {
                        var t = [];
                        return t.groups = {
                            a: "7"
                        }, t
                    }, "7" !== "".replace(t, "$<a>")
                })),
                h = function () {
                    return "$0" === "a".replace(/./, "$0")
                }(),
                l = o("replace"),
                f = function () {
                    return !!/./ [l] && "" === /./ [l]("a", "$0")
                }(),
                p = !i((function () {
                    var t = /(?:)/,
                        e = t.exec;
                    t.exec = function () {
                        return e.apply(this, arguments)
                    };
                    var n = "ab".split(t);
                    return 2 !== n.length || "a" !== n[0] || "b" !== n[1]
                }));
            t.exports = function (t, e, n, l) {
                var d = o(t),
                    v = !i((function () {
                        var e = {};
                        return e[d] = function () {
                            return 7
                        }, 7 != "" [t](e)
                    })),
                    g = v && !i((function () {
                        var e = !1,
                            n = /a/;
                        return "split" === t && (n = {}, n.constructor = {}, n.constructor[c] = function () {
                            return n
                        }, n.flags = "", n[d] = /./ [d]), n.exec = function () {
                            return e = !0, null
                        }, n[d](""), !e
                    }));
                if (!v || !g || "replace" === t && (!u || !h || f) || "split" === t && !p) {
                    var m = /./ [d],
                        y = n(d, "" [t], (function (t, e, n, r, i) {
                            return e.exec === a ? v && !i ? {
                                done: !0,
                                value: m.call(e, n, r)
                            } : {
                                done: !0,
                                value: t.call(n, e, r)
                            } : {
                                done: !1
                            }
                        }), {
                            REPLACE_KEEPS_$0: h,
                            REGEXP_REPLACE_SUBSTITUTES_UNDEFINED_CAPTURE: f
                        }),
                        b = y[0],
                        x = y[1];
                    r(String.prototype, t, b), r(RegExp.prototype, d, 2 == e ? function (t, e) {
                        return x.call(t, this, e)
                    } : function (t) {
                        return x.call(t, this)
                    })
                }
                l && s(RegExp.prototype[d], "sham", !0)
            }
        },
        d81d: function (t, e, n) {
            "use strict";
            var r = n("23e7"),
                i = n("b727").map,
                o = n("1dde"),
                a = n("ae40"),
                s = o("map"),
                c = a("map");
            r({
                target: "Array",
                proto: !0,
                forced: !s || !c
            }, {
                map: function (t) {
                    return i(this, t, arguments.length > 1 ? arguments[1] : void 0)
                }
            })
        },
        dca8: function (t, e, n) {
            var r = n("23e7"),
                i = n("bb2f"),
                o = n("d039"),
                a = n("861d"),
                s = n("f183").onFreeze,
                c = Object.freeze,
                u = o((function () {
                    c(1)
                }));
            r({
                target: "Object",
                stat: !0,
                forced: u,
                sham: !i
            }, {
                freeze: function (t) {
                    return c && a(t) ? c(s(t)) : t
                }
            })
        },
        e911: function (t, e, n) {},
        f183: function (t, e, n) {
            var r = n("d012"),
                i = n("861d"),
                o = n("5135"),
                a = n("9bf2").f,
                s = n("90e3"),
                c = n("bb2f"),
                u = s("meta"),
                h = 0,
                l = Object.isExtensible || function () {
                    return !0
                },
                f = function (t) {
                    a(t, u, {
                        value: {
                            objectID: "O" + ++h,
                            weakData: {}
                        }
                    })
                },
                p = function (t, e) {
                    if (!i(t)) return "symbol" == typeof t ? t : ("string" == typeof t ? "S" : "P") + t;
                    if (!o(t, u)) {
                        if (!l(t)) return "F";
                        if (!e) return "E";
                        f(t)
                    }
                    return t[u].objectID
                },
                d = function (t, e) {
                    if (!o(t, u)) {
                        if (!l(t)) return !0;
                        if (!e) return !1;
                        f(t)
                    }
                    return t[u].weakData
                },
                v = function (t) {
                    return c && g.REQUIRED && l(t) && !o(t, u) && f(t), t
                },
                g = t.exports = {
                    REQUIRED: !1,
                    fastKey: p,
                    getWeakData: d,
                    onFreeze: v
                };
            r[u] = !0
        }
    }
]);
//# sourceMappingURL=PhotoTouch.ba5e2bb0.js.map