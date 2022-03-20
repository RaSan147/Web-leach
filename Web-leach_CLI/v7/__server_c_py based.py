import time, traceback, re

import inspect
import importlib
import main


Source_code_style = '''
<style>
code[class*=language-],pre[class*=language-]{color:#ccc;background:0 0;font-family:Consolas,Monaco,'Andale Mono','Ubuntu Mono',monospace;font-size:1em;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none}pre[class*=language-]{padding:1em;margin:.5em 0;overflow:auto}:not(pre)>code[class*=language-],pre[class*=language-]{background:#2d2d2d}:not(pre)>code[class*=language-]{padding:.1em;border-radius:.3em;white-space:normal}.token.block-comment,.token.cdata,.token.comment,.token.doctype,.token.prolog{color:#999}.token.punctuation{color:#ccc}.token.attr-name,.token.deleted,.token.namespace,.token.tag{color:#e2777a}.token.function-name{color:#6196cc}.token.boolean,.token.function,.token.number{color:#f08d49}.token.class-name,.token.constant,.token.property,.token.symbol{color:#f8c555}.token.atrule,.token.builtin,.token.important,.token.keyword,.token.selector{color:#cc99cd}.token.attr-value,.token.char,.token.regex,.token.string,.token.variable{color:#7ec699}.token.entity,.token.operator,.token.url{color:#67cdcc}.token.bold,.token.important{font-weight:700}.token.italic{font-style:italic}.token.entity{cursor:help}.token.inserted{color:green}
</style>
<script>
var _self="undefined"!=typeof window?window:"undefined"!=typeof WorkerGlobalScope&&self instanceof WorkerGlobalScope?self:{},Prism=function(u){var c=/\\blang(?:uage)?-([\\w-]+)\\b/i,n=0,e={},M={manual:u.Prism&&u.Prism.manual,disableWorkerMessageHandler:u.Prism&&u.Prism.disableWorkerMessageHandler,util:{encode:function e(n){return n instanceof W?new W(n.type,e(n.content),n.alias):Array.isArray(n)?n.map(e):n.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/\\u00a0/g," ")},type:function(e){return Object.prototype.toString.call(e).slice(8,-1)},objId:function(e){return e.__id||Object.defineProperty(e,"__id",{value:++n}),e.__id},clone:function t(e,r){var a,n;switch(r=r||{},M.util.type(e)){case"Object":if(n=M.util.objId(e),r[n])return r[n];for(var i in a={},r[n]=a,e)e.hasOwnProperty(i)&&(a[i]=t(e[i],r));return a;case"Array":return n=M.util.objId(e),r[n]?r[n]:(a=[],r[n]=a,e.forEach(function(e,n){a[n]=t(e,r)}),a);default:return e}},getLanguage:function(e){for(;e&&!c.test(e.className);)e=e.parentElement;return e?(e.className.match(c)||[,"none"])[1].toLowerCase():"none"},currentScript:function(){if("undefined"==typeof document)return null;if("currentScript"in document)return document.currentScript;try{throw new Error}catch(e){var n=(/at [^(\\r\\n]*\\((.*):[^:]+:[^:]+\\)$/i.exec(e.stack)||[])[1];if(n){var t=document.getElementsByTagName("script");for(var r in t)if(t[r].src==n)return t[r]}return null}},isActive:function(e,n,t){for(var r="no-"+n;e;){var a=e.classList;if(a.contains(n))return!0;if(a.contains(r))return!1;e=e.parentElement}return!!t}},languages:{plain:e,plaintext:e,text:e,txt:e,extend:function(e,n){var t=M.util.clone(M.languages[e]);for(var r in n)t[r]=n[r];return t},insertBefore:function(t,e,n,r){var a=(r=r||M.languages)[t],i={};for(var l in a)if(a.hasOwnProperty(l)){if(l==e)for(var o in n)n.hasOwnProperty(o)&&(i[o]=n[o]);n.hasOwnProperty(l)||(i[l]=a[l])}var s=r[t];return r[t]=i,M.languages.DFS(M.languages,function(e,n){n===s&&e!=t&&(this[e]=i)}),i},DFS:function e(n,t,r,a){a=a||{};var i=M.util.objId;for(var l in n)if(n.hasOwnProperty(l)){t.call(n,l,n[l],r||l);var o=n[l],s=M.util.type(o);"Object"!==s||a[i(o)]?"Array"!==s||a[i(o)]||(a[i(o)]=!0,e(o,t,l,a)):(a[i(o)]=!0,e(o,t,null,a))}}},plugins:{},highlightAll:function(e,n){M.highlightAllUnder(document,e,n)},highlightAllUnder:function(e,n,t){var r={callback:t,container:e,selector:'code[class*="language-"], [class*="language-"] code, code[class*="lang-"], [class*="lang-"] code'};M.hooks.run("before-highlightall",r),r.elements=Array.prototype.slice.apply(r.container.querySelectorAll(r.selector)),M.hooks.run("before-all-elements-highlight",r);for(var a,i=0;a=r.elements[i++];)M.highlightElement(a,!0===n,r.callback)},highlightElement:function(e,n,t){var r=M.util.getLanguage(e),a=M.languages[r];e.className=e.className.replace(c,"").replace(/\\s+/g," ")+" language-"+r;var i=e.parentElement;i&&"pre"===i.nodeName.toLowerCase()&&(i.className=i.className.replace(c,"").replace(/\\s+/g," ")+" language-"+r);var l={element:e,language:r,grammar:a,code:e.textContent};function o(e){l.highlightedCode=e,M.hooks.run("before-insert",l),l.element.innerHTML=l.highlightedCode,M.hooks.run("after-highlight",l),M.hooks.run("complete",l),t&&t.call(l.element)}if(M.hooks.run("before-sanity-check",l),(i=l.element.parentElement)&&"pre"===i.nodeName.toLowerCase()&&!i.hasAttribute("tabindex")&&i.setAttribute("tabindex","0"),!l.code)return M.hooks.run("complete",l),void(t&&t.call(l.element));if(M.hooks.run("before-highlight",l),l.grammar)if(n&&u.Worker){var s=new Worker(M.filename);s.onmessage=function(e){o(e.data)},s.postMessage(JSON.stringify({language:l.language,code:l.code,immediateClose:!0}))}else o(M.highlight(l.code,l.grammar,l.language));else o(M.util.encode(l.code))},highlight:function(e,n,t){var r={code:e,grammar:n,language:t};return M.hooks.run("before-tokenize",r),r.tokens=M.tokenize(r.code,r.grammar),M.hooks.run("after-tokenize",r),W.stringify(M.util.encode(r.tokens),r.language)},tokenize:function(e,n){var t=n.rest;if(t){for(var r in t)n[r]=t[r];delete n.rest}var a=new i;return I(a,a.head,e),function e(n,t,r,a,i,l){for(var o in r)if(r.hasOwnProperty(o)&&r[o]){var s=r[o];s=Array.isArray(s)?s:[s];for(var u=0;u<s.length;++u){if(l&&l.cause==o+","+u)return;var c=s[u],g=c.inside,f=!!c.lookbehind,h=!!c.greedy,d=c.alias;if(h&&!c.pattern.global){var p=c.pattern.toString().match(/[imsuy]*$/)[0];c.pattern=RegExp(c.pattern.source,p+"g")}for(var v=c.pattern||c,m=a.next,y=i;m!==t.tail&&!(l&&y>=l.reach);y+=m.value.length,m=m.next){var b=m.value;if(t.length>n.length)return;if(!(b instanceof W)){var k,x=1;if(h){if(!(k=z(v,y,n,f))||k.index>=n.length)break;var w=k.index,A=k.index+k[0].length,P=y;for(P+=m.value.length;P<=w;)m=m.next,P+=m.value.length;if(P-=m.value.length,y=P,m.value instanceof W)continue;for(var E=m;E!==t.tail&&(P<A||"string"==typeof E.value);E=E.next)x++,P+=E.value.length;x--,b=n.slice(y,P),k.index-=y}else if(!(k=z(v,0,b,f)))continue;var w=k.index,S=k[0],O=b.slice(0,w),L=b.slice(w+S.length),N=y+b.length;l&&N>l.reach&&(l.reach=N);var j=m.prev;O&&(j=I(t,j,O),y+=O.length),q(t,j,x);var C=new W(o,g?M.tokenize(S,g):S,d,S);if(m=I(t,j,C),L&&I(t,m,L),1<x){var _={cause:o+","+u,reach:N};e(n,t,r,m.prev,y,_),l&&_.reach>l.reach&&(l.reach=_.reach)}}}}}}(e,a,n,a.head,0),function(e){var n=[],t=e.head.next;for(;t!==e.tail;)n.push(t.value),t=t.next;return n}(a)},hooks:{all:{},add:function(e,n){var t=M.hooks.all;t[e]=t[e]||[],t[e].push(n)},run:function(e,n){var t=M.hooks.all[e];if(t&&t.length)for(var r,a=0;r=t[a++];)r(n)}},Token:W};function W(e,n,t,r){this.type=e,this.content=n,this.alias=t,this.length=0|(r||"").length}function z(e,n,t,r){e.lastIndex=n;var a=e.exec(t);if(a&&r&&a[1]){var i=a[1].length;a.index+=i,a[0]=a[0].slice(i)}return a}function i(){var e={value:null,prev:null,next:null},n={value:null,prev:e,next:null};e.next=n,this.head=e,this.tail=n,this.length=0}function I(e,n,t){var r=n.next,a={value:t,prev:n,next:r};return n.next=a,r.prev=a,e.length++,a}function q(e,n,t){for(var r=n.next,a=0;a<t&&r!==e.tail;a++)r=r.next;(n.next=r).prev=n,e.length-=a}if(u.Prism=M,W.stringify=function n(e,t){if("string"==typeof e)return e;if(Array.isArray(e)){var r="";return e.forEach(function(e){r+=n(e,t)}),r}var a={type:e.type,content:n(e.content,t),tag:"span",classes:["token",e.type],attributes:{},language:t},i=e.alias;i&&(Array.isArray(i)?Array.prototype.push.apply(a.classes,i):a.classes.push(i)),M.hooks.run("wrap",a);var l="";for(var o in a.attributes)l+=" "+o+'="'+(a.attributes[o]||"").replace(/"/g,"&quot;")+'"';return"<"+a.tag+' class="'+a.classes.join(" ")+'"'+l+">"+a.content+"</"+a.tag+">"},!u.document)return u.addEventListener&&(M.disableWorkerMessageHandler||u.addEventListener("message",function(e){var n=JSON.parse(e.data),t=n.language,r=n.code,a=n.immediateClose;u.postMessage(M.highlight(r,M.languages[t],t)),a&&u.close()},!1)),M;var t=M.util.currentScript();function r(){M.manual||M.highlightAll()}if(t&&(M.filename=t.src,t.hasAttribute("data-manual")&&(M.manual=!0)),!M.manual){var a=document.readyState;"loading"===a||"interactive"===a&&t&&t.defer?document.addEventListener("DOMContentLoaded",r):window.requestAnimationFrame?window.requestAnimationFrame(r):window.setTimeout(r,16)}return M}(_self);"undefined"!=typeof module&&module.exports&&(module.exports=Prism),"undefined"!=typeof global&&(global.Prism=Prism);
Prism.languages.markup={comment:{pattern:/<!--(?:(?!<!--)[\\s\\S])*?-->/,greedy:!0},prolog:{pattern:/<\\?[\\s\\S]+?\\?>/,greedy:!0},doctype:{pattern:/<!DOCTYPE(?:[^>"'[\\]]|"[^"]*"|'[^']*')+(?:\\[(?:[^<"'\\]]|"[^"]*"|'[^']*'|<(?!!--)|<!--(?:[^-]|-(?!->))*-->)*\\]\\s*)?>/i,greedy:!0,inside:{"internal-subset":{pattern:/(^[^\\[]*\\[)[\\s\\S]+(?=\\]>$)/,lookbehind:!0,greedy:!0,inside:null},string:{pattern:/"[^"]*"|'[^']*'/,greedy:!0},punctuation:/^<!|>$|[[\\]]/,"doctype-tag":/^DOCTYPE/i,name:/[^\\s<>'"]+/}},cdata:{pattern:/<!\\[CDATA\\[[\\s\\S]*?\\]\\]>/i,greedy:!0},tag:{pattern:/<\\/?(?!\\d)[^\\s>\\/=$<%]+(?:\\s(?:\\s*[^\\s>\\/=]+(?:\\s*=\\s*(?:"[^"]*"|'[^']*'|[^\\s'">=]+(?=[\\s>]))|(?=[\\s/>])))+)?\\s*\\/?>/,greedy:!0,inside:{tag:{pattern:/^<\\/?[^\\s>\\/]+/,inside:{punctuation:/^<\\/?/,namespace:/^[^\\s>\\/:]+:/}},"special-attr":[],"attr-value":{pattern:/=\\s*(?:"[^"]*"|'[^']*'|[^\\s'">=]+)/,inside:{punctuation:[{pattern:/^=/,alias:"attr-equals"},/"|'/]}},punctuation:/\\/?>/,"attr-name":{pattern:/[^\\s>\\/]+/,inside:{namespace:/^[^\\s>\\/:]+:/}}}},entity:[{pattern:/&[\\da-z]{1,8};/i,alias:"named-entity"},/&#x?[\\da-f]{1,8};/i]},Prism.languages.markup.tag.inside["attr-value"].inside.entity=Prism.languages.markup.entity,Prism.languages.markup.doctype.inside["internal-subset"].inside=Prism.languages.markup,Prism.hooks.add("wrap",function(a){"entity"===a.type&&(a.attributes.title=a.content.replace(/&amp;/,"&"))}),Object.defineProperty(Prism.languages.markup.tag,"addInlined",{value:function(a,e){var s={};s["language-"+e]={pattern:/(^<!\\[CDATA\\[)[\\s\\S]+?(?=\\]\\]>$)/i,lookbehind:!0,inside:Prism.languages[e]},s.cdata=/^<!\\[CDATA\\[|\\]\\]>$/i;var t={"included-cdata":{pattern:/<!\\[CDATA\\[[\\s\\S]*?\\]\\]>/i,inside:s}};t["language-"+e]={pattern:/[\\s\\S]+/,inside:Prism.languages[e]};var n={};n[a]={pattern:RegExp("(<__[^>]*>)(?:<!\\\\[CDATA\\\\[(?:[^\\\\]]|\\\\](?!\\\\]>))*\\\\]\\\\]>|(?!<!\\\\[CDATA\\\\[)[^])*?(?=</__>)".replace(/__/g,function(){return a}),"i"),lookbehind:!0,greedy:!0,inside:t},Prism.languages.insertBefore("markup","cdata",n)}}),Object.defineProperty(Prism.languages.markup.tag,"addAttribute",{value:function(a,e){Prism.languages.markup.tag.inside["special-attr"].push({pattern:RegExp("(^|[\\"'\\\\s])(?:"+a+")\\\\s*=\\\\s*(?:\\"[^\\"]*\\"|'[^']*'|[^\\\\s'\\">=]+(?=[\\\\s>]))","i"),lookbehind:!0,inside:{"attr-name":/^[^\\s=]+/,"attr-value":{pattern:/=[\\s\\S]+/,inside:{value:{pattern:/(^=\\s*(["']|(?!["'])))\\S[\\s\\S]*(?=\\2$)/,lookbehind:!0,alias:[e,"language-"+e],inside:Prism.languages[e]},punctuation:[{pattern:/^=/,alias:"attr-equals"},/"|'/]}}}})}}),Prism.languages.html=Prism.languages.markup,Prism.languages.mathml=Prism.languages.markup,Prism.languages.svg=Prism.languages.markup,Prism.languages.xml=Prism.languages.extend("markup",{}),Prism.languages.ssml=Prism.languages.xml,Prism.languages.atom=Prism.languages.xml,Prism.languages.rss=Prism.languages.xml;
!function(s){var e=/(?:"(?:\\\\(?:\\r\\n|[\\s\\S])|[^"\\\\\\r\\n])*"|'(?:\\\\(?:\\r\\n|[\\s\\S])|[^'\\\\\\r\\n])*')/;s.languages.css={comment:/\\/\\*[\\s\\S]*?\\*\\//,atrule:{pattern:/@[\\w-](?:[^;{\\s]|\\s+(?![\\s{]))*(?:;|(?=\\s*\\{))/,inside:{rule:/^@[\\w-]+/,"selector-function-argument":{pattern:/(\\bselector\\s*\\(\\s*(?![\\s)]))(?:[^()\\s]|\\s+(?![\\s)])|\\((?:[^()]|\\([^()]*\\))*\\))+(?=\\s*\\))/,lookbehind:!0,alias:"selector"},keyword:{pattern:/(^|[^\\w-])(?:and|not|only|or)(?![\\w-])/,lookbehind:!0}}},url:{pattern:RegExp("\\\\burl\\\\((?:"+e.source+"|(?:[^\\\\\\\\\\r\\n()\\"']|\\\\\\\\[^])*)\\\\)","i"),greedy:!0,inside:{function:/^url/i,punctuation:/^\\(|\\)$/,string:{pattern:RegExp("^"+e.source+"$"),alias:"url"}}},selector:{pattern:RegExp("(^|[{}\\\\s])[^{}\\\\s](?:[^{};\\"'\\\\s]|\\\\s+(?![\\\\s{])|"+e.source+")*(?=\\\\s*\\\\{)"),lookbehind:!0},string:{pattern:e,greedy:!0},property:{pattern:/(^|[^-\\w\\xA0-\\uFFFF])(?!\\s)[-_a-z\\xA0-\\uFFFF](?:(?!\\s)[-\\w\\xA0-\\uFFFF])*(?=\\s*:)/i,lookbehind:!0},important:/!important\\b/i,function:{pattern:/(^|[^-a-z0-9])[-a-z0-9]+(?=\\()/i,lookbehind:!0},punctuation:/[(){};:,]/},s.languages.css.atrule.inside.rest=s.languages.css;var t=s.languages.markup;t&&(t.tag.addInlined("style","css"),t.tag.addAttribute("style","css"))}(Prism);
Prism.languages.clike={comment:[{pattern:/(^|[^\\\\])\\/\\*[\\s\\S]*?(?:\\*\\/|$)/,lookbehind:!0,greedy:!0},{pattern:/(^|[^\\\\:])\\/\\/.*/,lookbehind:!0,greedy:!0}],string:{pattern:/(["'])(?:\\\\(?:\\r\\n|[\\s\\S])|(?!\\1)[^\\\\\\r\\n])*\\1/,greedy:!0},"class-name":{pattern:/(\\b(?:class|extends|implements|instanceof|interface|new|trait)\\s+|\\bcatch\\s+\\()[\\w.\\\\]+/i,lookbehind:!0,inside:{punctuation:/[.\\\\]/}},keyword:/\\b(?:break|catch|continue|do|else|finally|for|function|if|in|instanceof|new|null|return|throw|try|while)\\b/,boolean:/\\b(?:false|true)\\b/,function:/\\b\\w+(?=\\()/,number:/\\b0x[\\da-f]+\\b|(?:\\b\\d+(?:\\.\\d*)?|\\B\\.\\d+)(?:e[+-]?\\d+)?/i,operator:/[<>]=?|[!=]=?=?|--?|\\+\\+?|&&?|\\|\\|?|[?*/~^%]/,punctuation:/[{}[\\];(),.:]/};
Prism.languages.javascript=Prism.languages.extend("clike",{"class-name":[Prism.languages.clike["class-name"],{pattern:/(^|[^$\\w\\xA0-\\uFFFF])(?!\\s)[_$A-Z\\xA0-\\uFFFF](?:(?!\\s)[$\\w\\xA0-\\uFFFF])*(?=\\.(?:constructor|prototype))/,lookbehind:!0}],keyword:[{pattern:/((?:^|\\})\\s*)catch\\b/,lookbehind:!0},{pattern:/(^|[^.]|\\.\\.\\.\\s*)\\b(?:as|assert(?=\\s*\\{)|async(?=\\s*(?:function\\b|\\(|[$\\w\\xA0-\\uFFFF]|$))|await|break|case|class|const|continue|debugger|default|delete|do|else|enum|export|extends|finally(?=\\s*(?:\\{|$))|for|from(?=\\s*(?:['"]|$))|function|(?:get|set)(?=\\s*(?:[#\\[$\\w\\xA0-\\uFFFF]|$))|if|implements|import|in|instanceof|interface|let|new|null|of|package|private|protected|public|return|static|super|switch|this|throw|try|typeof|undefined|var|void|while|with|yield)\\b/,lookbehind:!0}],function:/#?(?!\\s)[_$a-zA-Z\\xA0-\\uFFFF](?:(?!\\s)[$\\w\\xA0-\\uFFFF])*(?=\\s*(?:\\.\\s*(?:apply|bind|call)\\s*)?\\()/,number:/\\b(?:(?:0[xX](?:[\\dA-Fa-f](?:_[\\dA-Fa-f])?)+|0[bB](?:[01](?:_[01])?)+|0[oO](?:[0-7](?:_[0-7])?)+)n?|(?:\\d(?:_\\d)?)+n|NaN|Infinity)\\b|(?:\\b(?:\\d(?:_\\d)?)+\\.?(?:\\d(?:_\\d)?)*|\\B\\.(?:\\d(?:_\\d)?)+)(?:[Ee][+-]?(?:\\d(?:_\\d)?)+)?/,operator:/--|\\+\\+|\\*\\*=?|=>|&&=?|\\|\\|=?|[!=]==|<<=?|>>>?=?|[-+*/%&|^!=<>]=?|\\.{3}|\\?\\?=?|\\?\\.?|[~:]/}),Prism.languages.javascript["class-name"][0].pattern=/(\\b(?:class|extends|implements|instanceof|interface|new)\\s+)[\\w.\\\\]+/,Prism.languages.insertBefore("javascript","keyword",{regex:{pattern:/((?:^|[^$\\w\\xA0-\\uFFFF."'\\])\\s]|\\b(?:return|yield))\\s*)\\/(?:\\[(?:[^\\]\\\\\\r\\n]|\\\\.)*\\]|\\\\.|[^/\\\\\\[\\r\\n])+\\/[dgimyus]{0,7}(?=(?:\\s|\\/\\*(?:[^*]|\\*(?!\\/))*\\*\\/)*(?:$|[\\r\\n,.;:})\\]]|\\/\\/))/,lookbehind:!0,greedy:!0,inside:{"regex-source":{pattern:/^(\\/)[\\s\\S]+(?=\\/[a-z]*$)/,lookbehind:!0,alias:"language-regex",inside:Prism.languages.regex},"regex-delimiter":/^\\/|\\/$/,"regex-flags":/^[a-z]+$/}},"function-variable":{pattern:/#?(?!\\s)[_$a-zA-Z\\xA0-\\uFFFF](?:(?!\\s)[$\\w\\xA0-\\uFFFF])*(?=\\s*[=:]\\s*(?:async\\s*)?(?:\\bfunction\\b|(?:\\((?:[^()]|\\([^()]*\\))*\\)|(?!\\s)[_$a-zA-Z\\xA0-\\uFFFF](?:(?!\\s)[$\\w\\xA0-\\uFFFF])*)\\s*=>))/,alias:"function"},parameter:[{pattern:/(function(?:\\s+(?!\\s)[_$a-zA-Z\\xA0-\\uFFFF](?:(?!\\s)[$\\w\\xA0-\\uFFFF])*)?\\s*\\(\\s*)(?!\\s)(?:[^()\\s]|\\s+(?![\\s)])|\\([^()]*\\))+(?=\\s*\\))/,lookbehind:!0,inside:Prism.languages.javascript},{pattern:/(^|[^$\\w\\xA0-\\uFFFF])(?!\\s)[_$a-z\\xA0-\\uFFFF](?:(?!\\s)[$\\w\\xA0-\\uFFFF])*(?=\\s*=>)/i,lookbehind:!0,inside:Prism.languages.javascript},{pattern:/(\\(\\s*)(?!\\s)(?:[^()\\s]|\\s+(?![\\s)])|\\([^()]*\\))+(?=\\s*\\)\\s*=>)/,lookbehind:!0,inside:Prism.languages.javascript},{pattern:/((?:\\b|\\s|^)(?!(?:as|async|await|break|case|catch|class|const|continue|debugger|default|delete|do|else|enum|export|extends|finally|for|from|function|get|if|implements|import|in|instanceof|interface|let|new|null|of|package|private|protected|public|return|set|static|super|switch|this|throw|try|typeof|undefined|var|void|while|with|yield)(?![$\\w\\xA0-\\uFFFF]))(?:(?!\\s)[_$a-zA-Z\\xA0-\\uFFFF](?:(?!\\s)[$\\w\\xA0-\\uFFFF])*\\s*)\\(\\s*|\\]\\s*\\(\\s*)(?!\\s)(?:[^()\\s]|\\s+(?![\\s)])|\\([^()]*\\))+(?=\\s*\\)\\s*\\{)/,lookbehind:!0,inside:Prism.languages.javascript}],constant:/\\b[A-Z](?:[A-Z_]|\\dx?)*\\b/}),Prism.languages.insertBefore("javascript","string",{hashbang:{pattern:/^#!.*/,greedy:!0,alias:"comment"},"template-string":{pattern:/`(?:\\\\[\\s\\S]|\\$\\{(?:[^{}]|\\{(?:[^{}]|\\{[^}]*\\})*\\})+\\}|(?!\\$\\{)[^\\\\`])*`/,greedy:!0,inside:{"template-punctuation":{pattern:/^`|`$/,alias:"string"},interpolation:{pattern:/((?:^|[^\\\\])(?:\\\\{2})*)\\$\\{(?:[^{}]|\\{(?:[^{}]|\\{[^}]*\\})*\\})+\\}/,lookbehind:!0,inside:{"interpolation-punctuation":{pattern:/^\\$\\{|\\}$/,alias:"punctuation"},rest:Prism.languages.javascript}},string:/[\\s\\S]+/}}}),Prism.languages.markup&&(Prism.languages.markup.tag.addInlined("script","javascript"),Prism.languages.markup.tag.addAttribute("on(?:abort|blur|change|click|composition(?:end|start|update)|dblclick|error|focus(?:in|out)?|key(?:down|up)|load|mouse(?:down|enter|leave|move|out|over|up)|reset|resize|scroll|select|slotchange|submit|unload|wheel)","javascript")),Prism.languages.js=Prism.languages.javascript;
!function(e){e.languages.pug={comment:{pattern:/(^([\\t ]*))\\/\\/.*(?:(?:\\r?\\n|\\r)\\2[\\t ].+)*/m,lookbehind:!0},"multiline-script":{pattern:/(^([\\t ]*)script\\b.*\\.[\\t ]*)(?:(?:\\r?\\n|\\r(?!\\n))(?:\\2[\\t ].+|\\s*?(?=\\r?\\n|\\r)))+/m,lookbehind:!0,inside:e.languages.javascript},filter:{pattern:/(^([\\t ]*)):.+(?:(?:\\r?\\n|\\r(?!\\n))(?:\\2[\\t ].+|\\s*?(?=\\r?\\n|\\r)))+/m,lookbehind:!0,inside:{"filter-name":{pattern:/^:[\\w-]+/,alias:"variable"}}},"multiline-plain-text":{pattern:/(^([\\t ]*)[\\w\\-#.]+\\.[\\t ]*)(?:(?:\\r?\\n|\\r(?!\\n))(?:\\2[\\t ].+|\\s*?(?=\\r?\\n|\\r)))+/m,lookbehind:!0},markup:{pattern:/(^[\\t ]*)<.+/m,lookbehind:!0,inside:e.languages.markup},doctype:{pattern:/((?:^|\\n)[\\t ]*)doctype(?: .+)?/,lookbehind:!0},"flow-control":{pattern:/(^[\\t ]*)(?:case|default|each|else|if|unless|when|while)\\b(?: .+)?/m,lookbehind:!0,inside:{each:{pattern:/^each .+? in\\b/,inside:{keyword:/\\b(?:each|in)\\b/,punctuation:/,/}},branch:{pattern:/^(?:case|default|else|if|unless|when|while)\\b/,alias:"keyword"},rest:e.languages.javascript}},keyword:{pattern:/(^[\\t ]*)(?:append|block|extends|include|prepend)\\b.+/m,lookbehind:!0},mixin:[{pattern:/(^[\\t ]*)mixin .+/m,lookbehind:!0,inside:{keyword:/^mixin/,function:/\\w+(?=\\s*\\(|\\s*$)/,punctuation:/[(),.]/}},{pattern:/(^[\\t ]*)\\+.+/m,lookbehind:!0,inside:{name:{pattern:/^\\+\\w+/,alias:"function"},rest:e.languages.javascript}}],script:{pattern:/(^[\\t ]*script(?:(?:&[^(]+)?\\([^)]+\\))*[\\t ]).+/m,lookbehind:!0,inside:e.languages.javascript},"plain-text":{pattern:/(^[\\t ]*(?!-)[\\w\\-#.]*[\\w\\-](?:(?:&[^(]+)?\\([^)]+\\))*\\/?[\\t ]).+/m,lookbehind:!0},tag:{pattern:/(^[\\t ]*)(?!-)[\\w\\-#.]*[\\w\\-](?:(?:&[^(]+)?\\([^)]+\\))*\\/?:?/m,lookbehind:!0,inside:{attributes:[{pattern:/&[^(]+\\([^)]+\\)/,inside:e.languages.javascript},{pattern:/\\([^)]+\\)/,inside:{"attr-value":{pattern:/(=\\s*(?!\\s))(?:\\{[^}]*\\}|[^,)\\r\\n]+)/,lookbehind:!0,inside:e.languages.javascript},"attr-name":/[\\w-]+(?=\\s*!?=|\\s*[,)])/,punctuation:/[!=(),]+/}}],punctuation:/:/,"attr-id":/#[\\w\\-]+/,"attr-class":/\\.[\\w\\-]+/}},code:[{pattern:/(^[\\t ]*(?:-|!?=)).+/m,lookbehind:!0,inside:e.languages.javascript}],punctuation:/[.\\-!=|]+/};for(var t=[{filter:"atpl",language:"twig"},{filter:"coffee",language:"coffeescript"},"ejs","handlebars","less","livescript","markdown",{filter:"sass",language:"scss"},"stylus"],n={},a=0,i=t.length;a<i;a++){var r=t[a];r="string"==typeof r?{filter:r,language:r}:r,e.languages[r.language]&&(n["filter-"+r.filter]={pattern:RegExp("(^([\\t ]*)):<filter_name>(?:(?:\\r?\\n|\\r(?!\\n))(?:\\\\2[\\t ].+|\\\\s*?(?=\\r?\\n|\\r)))+".replace("<filter_name>",function(){return r.filter}),"m"),lookbehind:!0,inside:{"filter-name":{pattern:/^:[\\w-]+/,alias:"variable"},rest:e.languages[r.language]}})}e.languages.insertBefore("pug","filter",n)}(Prism);
Prism.languages.python={comment:{pattern:/(^|[^\\\\])#.*/,lookbehind:!0},"string-interpolation":{pattern:/(?:f|fr|rf)(?:("""|\'\'\')[\\s\\S]*?\\1|("|')(?:\\\\.|(?!\\2)[^\\\\\\r\\n])*\\2)/i,greedy:!0,inside:{interpolation:{pattern:/((?:^|[^{])(?:\\{\\{)*)\\{(?!\\{)(?:[^{}]|\\{(?!\\{)(?:[^{}]|\\{(?!\\{)(?:[^{}])+\\})+\\})+\\}/,lookbehind:!0,inside:{"format-spec":{pattern:/(:)[^:(){}]+(?=\\}$)/,lookbehind:!0},"conversion-option":{pattern:/![sra](?=[:}]$)/,alias:"punctuation"},rest:null}},string:/[\\s\\S]+/}},"triple-quoted-string":{pattern:/(?:[rub]|br|rb)?("""|\'\'\')[\\s\\S]*?\\1/i,greedy:!0,alias:"string"},string:{pattern:/(?:[rub]|br|rb)?("|')(?:\\\\.|(?!\\1)[^\\\\\\r\\n])*\\1/i,greedy:!0},function:{pattern:/((?:^|\\s)def[ \\t]+)[a-zA-Z_]\\w*(?=\\s*\\()/g,lookbehind:!0},"class-name":{pattern:/(\\bclass\\s+)\\w+/i,lookbehind:!0},decorator:{pattern:/(^[\\t ]*)@\\w+(?:\\.\\w+)*/im,lookbehind:!0,alias:["annotation","punctuation"],inside:{punctuation:/\\./}},keyword:/\\b(?:and|as|assert|async|await|break|class|continue|def|del|elif|else|except|exec|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|print|raise|return|try|while|with|yield)\\b/,builtin:/\\b(?:__import__|abs|all|any|apply|ascii|basestring|bin|bool|buffer|bytearray|bytes|callable|chr|classmethod|cmp|coerce|compile|complex|delattr|dict|dir|divmod|enumerate|eval|execfile|file|filter|float|format|frozenset|getattr|globals|hasattr|hash|help|hex|id|input|int|intern|isinstance|issubclass|iter|len|list|locals|long|map|max|memoryview|min|next|object|oct|open|ord|pow|property|range|raw_input|reduce|reload|repr|reversed|round|set|setattr|slice|sorted|staticmethod|str|sum|super|tuple|type|unichr|unicode|vars|xrange|zip)\\b/,boolean:/\\b(?:False|None|True)\\b/,number:/\\b0(?:b(?:_?[01])+|o(?:_?[0-7])+|x(?:_?[a-f0-9])+)\\b|(?:\\b\\d+(?:_\\d+)*(?:\\.(?:\\d+(?:_\\d+)*)?)?|\\B\\.\\d+(?:_\\d+)*)(?:e[+-]?\\d+(?:_\\d+)*)?j?(?!\\w)/i,operator:/[-+%=]=?|!=|:=|\\*\\*?=?|\\/\\/?=?|<[<=>]?|>[=>]?|[&|^~]/,punctuation:/[{}[\\];(),.:]/},Prism.languages.python["string-interpolation"].inside.interpolation.inside.rest=Prism.languages.python,Prism.languages.py=Prism.languages.python;
</script>
'''

# print(Source_code_style)

def read_wltxt(f_code):

	try:
		main_py_file = open('Output codes v6.wltxt', 'r').readlines()
	except Exception as e:
		print("NO 'Output codes v6.wltxt' file found, try Recheck if the file Exists\n\n")
		raise e

	text_ = []
	read = False
	vars = dict()
	return_box = []
	
	for i in main_py_file:
		if i.startswith('py:'):
			exec(i[3:].strip(), globals(), vars)
			# files_dict = locals()['files_dict']
			continue
		if read== False:
			if i.startswith(f_code):
				text_.append(i)
				read = True
		
		else:
			# print(i)
			if i.startswith(' ') or i.startswith('\n'):
				text_.append(i)
			else:
				read = False

	files_dict = vars['files_dict']

	_f_code, _f_name = (i.strip() for i in text_[0].split('>>>'))
	print('=================================\n\n', f_code, _f_code, _f_name)
	return_box= []

	return_box.append(Source_code_style)

	return_box.append("<h3><u>File</u>: " + files_dict[_f_code[0]]+'</h3>')

	if '>' in _f_name:
		return_box.append("<h3><u>Class</u>: " + _f_name.split('>')[0][1:]+'</h3>')
		return_box.append("<h2><u>Method</u>: " + _f_name.split('>')[1].split(']')[0]+'</h3>')

		where = _f_name.split('>')[0][1:] + '.' + _f_name.split('>')[1].split(']')[0]
	else:
		return_box.append("<h2><u>Function</u>: " + _f_name[1:-1]+'</h3>')

		where = _f_name[1:-1]

	return_box.append("<h2><u>Description</u>: </h2> <br><pre><code class='language-pug'><noscript>" + "\n".join(text_) + "</noscript></code></pre>")

	try:
		# import the file
		file_name = re.search(r'\[(.*?)\]', files_dict[_f_code[0]]).group(1)
		if file_name == 'main.py':
			func_ = main
		else:
			func_ = importlib.import_module(file_name.split('.py')[0])
		return_box.append('<br><br><h2><u>Source Code</u>:</h2> <br><pre><code class="language-py"><noscript>' + inspect.getsource(eval('func_.' + where)) + "</noscript></code></pre>")
	except:
		traceback.print_exc()
		# print(re.search(r'\[(.*?)\]', files_dict[_f_code[0]]))
		

	return return_box

#from bs4 import BeautifulSoup

"""HTTP server classes.

Note: BaseHTTPRequestHandler doesn't implement any HTTP request; see
SimpleHTTPRequestHandler for simple implementations of GET, HEAD and POST,
and CGIHTTPRequestHandler for CGI scripts.

It does, however, optionally implement HTTP/1.1 persistent connections,
as of version 0.3.

Notes on CGIHTTPRequestHandler
------------------------------

This class implements GET and POST requests to cgi-bin scripts.

If the os.fork() function is not present (e.g. on Windows),
subprocess.Popen() is used as a fallback, with slightly altered semantics.

In all cases, the implementation is intentionally naive -- all
requests are executed synchronously.

SECURITY WARNING: DON'T USE THIS CODE UNLESS YOU ARE INSIDE A FIREWALL
-- it may execute arbitrary Python code or external programs.

Note that status code 200 is sent prior to execution of a CGI script, so
scripts cannot send other status codes such as 302 (redirect).

XXX To do:

- log requests even later (to capture byte count)
- log user-agent header and other interesting goodies
- send error log to separate file
"""


# See also:
#
# HTTP Working Group                                        T. Berners-Lee
# INTERNET-DRAFT                                            R. T. Fielding
# <draft-ietf-http-v10-spec-00.txt>                     H. Frystyk Nielsen
# Expires September 8, 1995                                  March 8, 1995
#
# URL: http://www.ics.uci.edu/pub/ietf/http/draft-ietf-http-v10-spec-00.txt
#
# and
#
# Network Working Group                                      R. Fielding
# Request for Comments: 2616                                       et al
# Obsoletes: 2068                                              June 1999
# Category: Standards Track
#
# URL: http://www.faqs.org/rfcs/rfc2616.html

# Log files
# ---------
#
# Here's a quote from the NCSA httpd docs about log file format.
#
# | The logfile format is as follows. Each line consists of:
# |
# | host rfc931 authuser [DD/Mon/YYYY:hh:mm:ss] "request" ddd bbbb
# |
# |        host: Either the DNS name or the IP number of the remote client
# |        rfc931: Any information returned by identd for this person,
# |                - otherwise.
# |        authuser: If user sent a userid for authentication, the user name,
# |                  - otherwise.
# |        DD: Day
# |        Mon: Month (calendar name)
# |        YYYY: Year
# |        hh: hour (24-hour format, the machine's timezone)
# |        mm: minutes
# |        ss: seconds
# |        request: The first line of the HTTP request as sent by the client.
# |        ddd: the status code returned by the server, - if not available.
# |        bbbb: the total number of bytes sent,
# |              *not including the HTTP/1.0 header*, - if not available
# |
# | You can determine the name of the file accessed through request.
#
# (Actually, the latter is only true if you know the server configuration
# at the time the request was made!)

__version__ = "0.6"

__all__ = [
	"HTTPServer", "ThreadingHTTPServer", "BaseHTTPRequestHandler",
	"SimpleHTTPRequestHandler", "CGIHTTPRequestHandler",
]

import copy
import datetime
import email.utils
import html
import http.client
import io
import mimetypes
import os
import posixpath
import select
import shutil
import socket # For gethostbyaddr()
import socketserver
import sys
import time
import urllib.parse
import contextlib
import urllib
import natsort
from functools import partial

from http import HTTPStatus
import webbrowser

import RcryptxAsuna2_1_c_py_lines as RxAsuna
import Number_sys_conv as Nsys
import re


enc = sys.getfilesystemencoding()


try:
	from bs4 import BeautifulSoup as bs
except:
	print('BeautifulSoup is not available, please Download it')
	input()
	exit(0)


try:
	print("Testing lxml program availability")
	_parser = 'lxml'
	bs("<p>test</p>", _parser).text

except:
	_parser= 'html.parser'
	print("Failed!\nSwitching to html.parser mode")

# _parser= 'html.parser'

print("Testing C program availability")
decryptor_lang=None
try:
	RxAsuna.Cdecrypt('hello', "world")
	decryptor_lang= 'C'
except FileNotFoundError:
	if RxAsuna.Cy_available:
		decryptor_lang= 'Cy'
	else:
		decryptor_lang= 'Py'
	print("Failed!\nSwitching to %sthon mode"%decryptor_lang)



# Default error message template
DEFAULT_ERROR_MESSAGE = """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
		"http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
		<title>Error response</title>
	</head>
	<body>
		<h1>Error response</h1>
		<p>Error code: %(code)d</p>
		<p>Message: %(message)s.</p>
		<p>Error code explanation: %(code)s - %(explain)s.</p>
	</body>
</html>
"""

DEFAULT_ERROR_CONTENT_TYPE = "text/html;charset=utf-8"

class HTTPServer(socketserver.TCPServer):

	allow_reuse_address = 1    # Seems to make sense in testing environment

	def server_bind(self):
		"""Override server_bind to store the server name."""
		socketserver.TCPServer.server_bind(self)
		host, port = self.server_address[: 2]
		self.server_name = socket.getfqdn(host)
		self.server_port = port


class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
	daemon_threads = True


class BaseHTTPRequestHandler(socketserver.StreamRequestHandler):

	"""HTTP request handler base class.

	The following explanation of HTTP serves to guide you through the
	code as well as to expose any misunderstandings I may have about
	HTTP (so you don't need to read the code to figure out I'm wrong
	:-).

	HTTP (HyperText Transfer Protocol) is an extensible protocol on
	top of a reliable stream transport (e.g. TCP/IP).  The protocol
	recognizes three parts to a request:

	1. One line identifying the request type and path
	2. An optional set of RFC-822-style headers
	3. An optional data part

	The headers and data are separated by a blank line.

	The first line of the request has the form

	<command> <path> <version>

	where <command> is a (case-sensitive) keyword such as GET or POST,
	<path> is a string containing path information for the request,
	and <version> should be the string "HTTP/1.0" or "HTTP/1.1".
	<path> is encoded using the URL encoding scheme (using %xx to signify
	the ASCII character with hex code xx).

	The specification specifies that lines are separated by CRLF but
	for compatibility with the widest range of clients recommends
	servers also handle LF.  Similarly, whitespace in the request line
	is treated sensibly (allowing multiple spaces between components
	and allowing trailing whitespace).

	Similarly, for output, lines ought to be separated by CRLF pairs
	but most clients grok LF characters just fine.

	If the first line of the request has the form

	<command> <path>

	(i.e. <version> is left out) then this is assumed to be an HTTP
	0.9 request; this form has no optional headers and data part and
	the reply consists of just the data.

	The reply form of the HTTP 1.x protocol again has three parts:

	1. One line giving the response code
	2. An optional set of RFC-822-style headers
	3. The data

	Again, the headers and data are separated by a blank line.

	The response code line has the form

	<version> <responsecode> <responsestring>

	where <version> is the protocol version ("HTTP/1.0" or "HTTP/1.1"),
	<responsecode> is a 3-digit response code indicating success or
	failure of the request, and <responsestring> is an optional
	human-readable string explaining what the response code means.

	This server parses the request and the headers, and then calls a
	function specific to the request type (<command>).  Specifically,
	a request SPAM will be handled by a method do_SPAM().  If no
	such method exists the server sends an error response to the
	client.  If it exists, it is called with no arguments:

	do_SPAM()

	Note that the request name is case sensitive (i.e. SPAM and spam
	are different requests).

	The various request details are stored in instance variables:

	- client_address is the client IP address in the form (host,
	port);

	- command, path and version are the broken-down request line;

	- headers is an instance of email.message.Message (or a derived
	class) containing the header information;

	- rfile is a file object open for reading positioned at the
	start of the optional input data part;

	- wfile is a file object open for writing.

	IT IS IMPORTANT TO ADHERE TO THE PROTOCOL FOR WRITING!

	The first thing to be written must be the response line.  Then
	follow 0 or more header lines, then a blank line, and then the
	actual data (if any).  The meaning of the header lines depends on
	the command executed by the server; in most cases, when data is
	returned, there should be at least one header line of the form

	Content-type: <type>/<subtype>

	where <type> and <subtype> should be registered MIME types,
	e.g. "text/html" or "text/plain".

	"""

	# The Python system version, truncated to its first component.
	sys_version = "Python/" + sys.version.split()[0]

	# The server software version.  You may want to override this.
	# The format is multiple whitespace-separated strings,
	# where each string is of the form name[/version].
	server_version = "BaseHTTP/" + __version__

	error_message_format = DEFAULT_ERROR_MESSAGE
	error_content_type = DEFAULT_ERROR_CONTENT_TYPE

	# The default request version.  This only affects responses up until
	# the point where the request line is parsed, so it mainly decides what
	# the client gets back when sending a malformed request line.
	# Most web servers default to HTTP 0.9, i.e. don't send a status line.
	default_request_version = "HTTP/0.9"

	def parse_request(self):
		"""Parse a request (internal).

		The request should be stored in self.raw_requestline; the results
		are in self.command, self.path, self.request_version and
		self.headers.

		Return True for success, False for failure; on failure, any relevant
		error response has already been sent back.

		"""
		self.command = None  # set in case of error on the first line
		self.request_version = version = self.default_request_version
		self.close_connection = True
		requestline = str(self.raw_requestline, 'iso-8859-1')
		requestline = requestline.rstrip('\r\n')
		self.requestline = requestline
		words = requestline.split()
		if len(words) == 0:
			return False

		if len(words) >= 3:  # Enough to determine protocol version
			version = words[-1]
			try:
				if not version.startswith('HTTP/'):
					raise ValueError
				base_version_number = version.split('/', 1)[1]
				version_number = base_version_number.split(".")
				# RFC 2145 section 3.1 says there can be only one "." and
				#   - major and minor numbers MUST be treated as
				#      separate integers;
				#   - HTTP/2.4 is a lower version than HTTP/2.13, which in
				#      turn is lower than HTTP/12.3;
				#   - Leading zeros MUST be ignored by recipients.
				if len(version_number) != 2:
					raise ValueError
				version_number = int(version_number[0]), int(version_number[1])
			except (ValueError, IndexError):
				self.send_error(
					HTTPStatus.BAD_REQUEST,
					"Bad request version (%r)" % version)
				return False
			if version_number >= (1, 1) and self.protocol_version >= "HTTP/1.1":
				self.close_connection = False
			if version_number >= (2, 0):
				self.send_error(
					HTTPStatus.HTTP_VERSION_NOT_SUPPORTED,
					"Invalid HTTP version (%s)" % base_version_number)
				return False
			self.request_version = version

		if not 2 <= len(words) <= 3:
			self.send_error(
				HTTPStatus.BAD_REQUEST,
				"Bad request syntax (%r)" % requestline)
			return False
		command, path = words[:2]
		if len(words) == 2:
			self.close_connection = True
			if command != 'GET':
				self.send_error(
					HTTPStatus.BAD_REQUEST,
					"Bad HTTP/0.9 request type (%r)" % command)
				return False
		self.command, self.path = command, path

		# Examine the headers and look for a Connection directive.
		try:
			self.headers = http.client.parse_headers(self.rfile,
													 _class=self.MessageClass)
			print(self.headers)
		except http.client.LineTooLong as err:
			self.send_error(
				HTTPStatus.REQUEST_HEADER_FIELDS_TOO_LARGE,
				"Line too long",
				str(err))
			return False
		except http.client.HTTPException as err:
			self.send_error(
				HTTPStatus.REQUEST_HEADER_FIELDS_TOO_LARGE,
				"Too many headers",
				str(err)
			)
			return False

		conntype = self.headers.get('Connection', "")
		if conntype.lower() == 'close':
			self.close_connection = True
		elif (conntype.lower() == 'keep-alive' and
			  self.protocol_version >= "HTTP/1.1"):
			self.close_connection = False
		# Examine the headers and look for an Expect directive
		expect = self.headers.get('Expect', "")
		if (expect.lower() == "100-continue" and
				self.protocol_version >= "HTTP/1.1" and
				self.request_version >= "HTTP/1.1"):
			if not self.handle_expect_100():
				return False
		return True

	def handle_expect_100(self):
		"""Decide what to do with an "Expect: 100-continue" header.

		If the client is expecting a 100 Continue response, we must
		respond with either a 100 Continue or a final response before
		waiting for the request body. The default is to always respond
		with a 100 Continue. You can behave differently (for example,
		reject unauthorized requests) by overriding this method.

		This method should either return True (possibly after sending
		a 100 Continue response) or send an error response and return
		False.

		"""
		self.send_response_only(HTTPStatus.CONTINUE)
		self.end_headers()
		return True

	def handle_one_request(self):
		"""Handle a single HTTP request.

		You normally don't need to override this method; see the class
		__doc__ string for information on how to handle specific HTTP
		commands such as GET and POST.

		"""
		try:
			self.raw_requestline = self.rfile.readline(65537)
			if len(self.raw_requestline) > 65536:
				self.requestline = ''
				self.request_version = ''
				self.command = ''
				self.send_error(HTTPStatus.REQUEST_URI_TOO_LONG)
				return
			if not self.raw_requestline:
				self.close_connection = True
				return
			if not self.parse_request():
				# An error code has been sent, just exit
				return
			mname = 'do_' + self.command
			if not hasattr(self, mname):
				self.send_error(
					HTTPStatus.NOT_IMPLEMENTED,
					"Unsupported method (%r)" % self.command)
				return
			method = getattr(self, mname)
			method()
			self.wfile.flush() #actually send the response if not already done.
		except TimeoutError as e:
			#a read or a write timed out.  Discard this connection
			self.log_error("Request timed out: %r", e)
			self.close_connection = True
			return

	def handle(self):
		"""Handle multiple requests if necessary."""
		self.close_connection = True

		self.handle_one_request()
		while not self.close_connection:
			self.handle_one_request()

	def send_error(self, code, message=None, explain=None):
		"""Send and log an error reply.

		Arguments are
		* code:    an HTTP error code
				   3 digits
		* message: a simple optional 1 line reason phrase.
				   *( HTAB / SP / VCHAR / %x80-FF )
				   defaults to short entry matching the response code
		* explain: a detailed message defaults to the long entry
				   matching the response code.

		This sends an error response (so it must be called before any
		output has been generated), logs the error, and finally sends
		a piece of HTML explaining the error to the user.

		"""

		try:
			shortmsg, longmsg = self.responses[code]
		except KeyError:
			shortmsg, longmsg = '???', '???'
		if message is None:
			message = shortmsg
		if explain is None:
			explain = longmsg
		self.log_error("code %d, message %s", code, message)
		self.send_response(code, message)
		self.send_header('Connection', 'close')

		# Message body is omitted for cases described in:
		#  - RFC7230: 3.3. 1xx, 204(No Content), 304(Not Modified)
		#  - RFC7231: 6.3.6. 205(Reset Content)
		body = None
		if (code >= 200 and
			code not in (HTTPStatus.NO_CONTENT,
						 HTTPStatus.RESET_CONTENT,
						 HTTPStatus.NOT_MODIFIED)):
			# HTML encode to prevent Cross Site Scripting attacks
			# (see bug #1100201)
			content = (self.error_message_format % {
				'code': code,
				'message': html.escape(message, quote=False),
				'explain': html.escape(explain, quote=False)
			})
			body = content.encode('UTF-8', 'replace')
			self.send_header("Content-Type", self.error_content_type)
			self.send_header('Content-Length', str(len(body)))
		self.end_headers()

		if self.command != 'HEAD' and body:
			self.wfile.write(body)

	def send_response(self, code, message=None):
		"""Add the response header to the headers buffer and log the
		response code.

		Also send two standard headers with the server software
		version and the current date.

		"""
		self.log_request(code)
		self.send_response_only(code, message)
		self.send_header('Server', self.version_string())
		self.send_header('Date', self.date_time_string())

	def send_response_only(self, code, message=None):
		"""Send the response header only."""
		if self.request_version != 'HTTP/0.9':
			if message is None:
				if code in self.responses:
					message = self.responses[code][0]
				else:
					message = ''
			if not hasattr(self, '_headers_buffer'):
				self._headers_buffer = []
			self._headers_buffer.append(("%s %d %s\r\n" %
					(self.protocol_version, code, message)).encode(
						'latin-1', 'strict'))

	def send_header(self, keyword, value):
		"""Send a MIME header to the headers buffer."""
		if self.request_version != 'HTTP/0.9':
			if not hasattr(self, '_headers_buffer'):
				self._headers_buffer = []
			self._headers_buffer.append(
				("%s: %s\r\n" % (keyword, value)).encode('latin-1', 'strict'))

		if keyword.lower() == 'connection':
			if value.lower() == 'close':
				self.close_connection = True
			elif value.lower() == 'keep-alive':
				self.close_connection = False

	def end_headers(self):
		"""Send the blank line ending the MIME headers."""
		if self.request_version != 'HTTP/0.9':
			self._headers_buffer.append(b"\r\n")
			self.flush_headers()

	def flush_headers(self):
		if hasattr(self, '_headers_buffer'):
			self.wfile.write(b"".join(self._headers_buffer))
			self._headers_buffer = []

	def log_request(self, code='-', size='-'):
		"""Log an accepted request.

		This is called by send_response().

		"""
		if isinstance(code, HTTPStatus):
			code = code.value
		self.log_message('"%s" %s %s',
						 self.requestline, str(code), str(size))

	def log_error(self, format, *args):
		"""Log an error.

		This is called when a request cannot be fulfilled.  By
		default it passes the message on to log_message().

		Arguments are the same as for log_message().

		XXX This should go to the separate error log.

		"""

		self.log_message(format, *args)

	def log_message(self, format, *args):
		"""Log an arbitrary message.

		This is used by all other logging functions.  Override
		it if you have specific logging wishes.

		The first argument, FORMAT, is a format string for the
		message to be logged.  If the format string contains
		any % escapes requiring parameters, they should be
		specified as subsequent arguments (it's just like
		printf!).

		The client ip and current date/time are prefixed to
		every message.

		"""

		sys.stderr.write("%s - - [%s] %s\n" %
						 (self.address_string(),
						  self.log_date_time_string(),
						  format%args))

	def version_string(self):
		"""Return the server software version string."""
		return self.server_version + ' ' + self.sys_version

	def date_time_string(self, timestamp=None):
		"""Return the current date and time formatted for a message header."""
		if timestamp is None:
			timestamp = time.time()
		return email.utils.formatdate(timestamp, usegmt=True)

	def log_date_time_string(self):
		"""Return the current time formatted for logging."""
		now = time.time()
		year, month, day, hh, mm, ss, x, y, z = time.localtime(now)
		s = "%02d/%3s/%04d %02d:%02d:%02d" % (
				day, self.monthname[month], year, hh, mm, ss)
		return s

	weekdayname = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

	monthname = [None,
				 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
				 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

	def address_string(self):
		"""Return the client address."""

		return self.client_address[0]

	# Essentially static class variables

	# The version of the HTTP protocol we support.
	# Set this to HTTP/1.1 to enable automatic keepalive
	protocol_version = "HTTP/1.0"

	# MessageClass used to parse headers
	MessageClass = http.client.HTTPMessage

	# hack to maintain backwards compatibility
	responses = {
		v: (v.phrase, v.description)
		for v in HTTPStatus.__members__.values()
	}


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

	"""Simple HTTP request handler with GET and HEAD commands.

	This serves files from the current directory and any of its
	subdirectories.  The MIME type for files is determined by
	calling the .guess_type() method.

	The GET and HEAD requests are identical except that the HEAD
	request omits the actual contents of the file.

	"""

	server_version = "SimpleHTTP/" + __version__
	extensions_map = _encodings_map_default = {
		'.gz': 'application/gzip',
		'.Z': 'application/octet-stream',
		'.bz2': 'application/x-bzip2',
		'.xz': 'application/x-xz',
	}

	def __init__(self, *args, directory=None, **kwargs):
		if directory is None:
			directory = os.getcwd()
		self.directory = os.fspath(directory)
		super().__init__(*args, **kwargs)

	def do_GET(self):
		"""Serve a GET request."""
		self.response_get = time.time()
		self.is_get_req = True
		f = self.send_head()
		if f:
			try:
				self.copyfile(f, self.wfile)
			finally:
				f.close()

	def do_HEAD(self):
		"""Serve a HEAD request."""
		self.response_get = time.time()
		self.is_get_req = False
		f = self.send_head()
		if f:
			f.close()

	def do_POST(self):
		"""Serve a POST request."""
		import logging
		self.response_get = time.time()
		self.is_get_req = False
		content_length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(content_length) # <--- Gets the data itself
		print("POST request,\nPath: %s\nHeaders: \n%s\n\nBody: \n%s\n"%(
				str(self.path), str(self.headers), post_data.decode('utf-8')))

		f = self.send_head()
		if f:
			f.close()

	def send_head(self, spid='', scode='', scodepart='', skeyword=''):
		"""Common code for GET and HEAD commands.

		This sends the response code and MIME headers.

		Return value is either a file object (which has to be copied
		to the outputfile by the caller unless the command was HEAD,
		and must be closed by the caller under all circumstances), or
		None, in which case the caller has nothing further to do.

		"""

		global decryptor_lang, enc
		path = self.translate_path(self.path)
		print(self.path)
		
		enc = sys.getfilesystemencoding()

		decrypto_header = open('_server001_decrypto.html').read()
		if self.path.startswith('/search='):
			spid, scode, scodepart, skeyword = (urllib.parse.unquote(part) for part in self.path[8: ].split('+'))


		f = None
		r=[]
		if self.path.startswith('/fcode='):
			_f_code = self.path[7:]
			try:
				func_docs = read_wltxt(_f_code)
			except Exception as e:
				traceback.print_exc()
				r.append('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" '
		'"http: //www.w3.org/TR/html4/strict.dtd">')
				r.append('<meta http-equiv="Content-Type" '
		'content="text/html; charset=%s">' % enc)
				r.append("""<h1>503 Error Occred</h1>
				<h2>Failed to execute decryption program (%s occured)</h2>
				<h1>Failed to load Documentation file. PLease recheck the file</h1>
				<p><b>Error message: </b> %s</p>"""%(str(e.__class__.__name__), str(e)))
				encoded = '\n'.join(r).encode(enc, 'surrogateescape')

				f = io.BytesIO()
				f.write(encoded)
				f.seek(0)
				self.send_response (HTTPStatus.SERVICE_UNAVAILABLE)
				self.send_header ("Content-type", "text/html; charset=%s" % enc)
				self.send_header ("Content-Length", str(len(encoded)))
				self.end_headers()
				return f
			

			encoded = '\n'.join(func_docs)

			
			# encoded += '<pre>'+ '\n'.join(text_)+'</pre>'
			encoded = encoded.encode(enc, 'surrogateescape')

			f = io.BytesIO()
			f.write(encoded)
			f.seek(0)
			self.send_response(HTTPStatus.OK)
			self.send_header("Content-type", "text/html; charset=%s" % enc)
			self.send_header("Content-Length", str(len(encoded)))
			self.end_headers()
			return f


					

		elif self.path=='/' or self.path.startswith('/search='):
			if self.is_get_req:
				request_time= time.time()
				decrypto_key = "Asuna" #input("Enter password: ")
				self.decrypto_dat= []
				self.PIDs=[]
				try:
					with open('data/userlog.leach') as f:
						read_dec = time.time()
						dec_raw = f.read()
				except FileNotFoundError as e:
					print("NO userlog.leach file found, try Recheck if the file Exists\n\n")
					enc = sys.getfilesystemencoding()
					r.append('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" '
			'"http: //www.w3.org/TR/html4/strict.dtd">')
					r.append('<meta http-equiv="Content-Type" '
			'content="text/html; charset=%s">' % enc)
					r.append("""<h1>503 Error Occred</h1>
					<h2>Failed to execute decryption program (%s occured)</h2>
					<h1>Failed to load Log file. PLease recheck the file</h1>
					<p><b>Error message: </b> %s</p>"""%(str(e.__class__.__name__), str(e)))
					encoded = '\n'.join(r).encode(enc, 'surrogateescape')

					f = io.BytesIO()
					f.write(encoded)
					f.seek(0)
					self.send_response (HTTPStatus.SERVICE_UNAVAILABLE)
					self.send_header ("Content-type", "text/html; charset=%s" % enc)
					self.send_header ("Content-Length", str(len(encoded)))
					self.end_headers()
					return f
				if decryptor_lang =='C':
					try:
						self.decrypto_dat = RxAsuna.Cdecrypt(dec_raw , decrypto_key).replace('\r\n', '\n').split('\n')
					except UnicodeDecodeError:
						print("Failed!\nEncoding Issue\nSwitching to Python mode")
						decryptor_lang =None
					except FileNotFoundError:
						print("Failed!\nExecutable file not found\nSwitching to Python mode")
						decryptor_lang =None

					#decryptor_lang = 'C'

				if decryptor_lang ==None or decryptor_lang in ['Py', 'Cy']:
					if decryptor_lang is None:
						if RxAsuna.Cy_available:
							decryptor_lang = 'Cy'
						else:
							decryptor_lang = 'Py'
					try:
						if decryptor_lang == 'Cy':
							self.decrypto_dat= RxAsuna.CYdecrypt(dec_raw, decrypto_key, 'list')
						else:
							self.decrypto_dat= RxAsuna.PYdecrypt(dec_raw, decrypto_key, 'list')
					except Exception as e:
						traceback.print_exc()
						print("can't execute the Decryption program, try Recheck if the file Exists\n\n")
						enc = sys.getfilesystemencoding()
						r.append('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" '
				'"http: //www.w3.org/TR/html4/strict.dtd">')
						r.append('<meta http-equiv="Content-Type" '
				'content="text/html; charset=%s">' % enc)
						r.append("""<h1>503 Error Occred</h1>
						<h2>Failed to execute decryption program (%s occured)</h2>
						<h1>Failed to decypt Log file. PLease recheck the file</h1>
						<p><b>Error message: </b> %s</p>"""%(str(e.__class__.__name__), str(e)))
						encoded = '\n'.join(r).encode(enc, 'surrogateescape')

						f = io.BytesIO()
						f.write(encoded)
						f.seek(0)
						self.send_response (HTTPStatus.SERVICE_UNAVAILABLE)
						self.send_header ("Content-type", "text/html; charset=%s" % enc)
						self.send_header ("Content-Length", str(len(encoded)))
						self.end_headers()
						return f



				read_dec = time.time()-read_dec

				self.current_sort= 'date_new2old'

				tables=[]
				td_t = '<td>%s</td>\n'
				table_made = time.time()
				table_len= len(self.decrypto_dat)
				line_index = 0

				
				Extractor = dict()
				exec(open('log_extractor.py').read(), Extractor)
				# print(self.decrypto_dat)

				# exit()


				while self.decrypto_dat!=[]:
					column = [[] for i in range(100)]
					line_index+=1
					try:
						_decrypto_dat_=self.decrypto_dat.pop()
					except:
						# print(self.decrypto_dat)
						traceback.print_exc()
						exit()
						continue

					if _decrypto_dat_=='':
						table_len-=1
						continue
					_Vcode = _decrypto_dat_[34:40]

					_decrypto_dat = _decrypto_dat_[40: ].split('||')[: -1]

					if spid!='' and spid!= _decrypto_dat[1]: continue
					if scode!='' and scode!= _decrypto_dat[2]: continue
					if scodepart!='' and scodepart not in _decrypto_dat[2]: continue

					try:
						column[0]= "%s/%s/%s &nbsp;&nbsp;&nbsp; %s: %s: %s" %Nsys.dec_dt(_decrypto_dat[0])
					except KeyError: pass
					except IndexError as e:
						try:
							if re.search(r'\d+/\d+/\d+ &nbsp;&nbsp;&nbsp; \d: \d: \d.?\d*', _decrypto_dat[0]):
								pass
							else:
								raise e
						except: continue
					except Exception as e:
						print([_decrypto_dat_], e)
						continue

					column[1]=_decrypto_dat[1]
					column[2]=_decrypto_dat[2]

					if _decrypto_dat[1] not in self.PIDs: self.PIDs.append(_decrypto_dat[1])

					column = Extractor['extractor'](_Vcode, _decrypto_dat, column, _decrypto_dat_, line_index)

					# print("converted")
					# print(column)
					if not column: continue


					_decrypto_dat = _decrypto_dat[: 5] #uncomment when done
					tr='<tr class = "p%s">'%_decrypto_dat[1]

					for j in range(5):
						try:
							# print(column[j])
							tr+=td_t%column[j]
						except:
							traceback.print_exc()
							# print([_decrypto_dat,column])
							continue
					tr+='</tr>'
					# print(bs(tr, "html.parser").text)

					if skeyword!='':
						
						if skeyword.lower() not in bs(tr, features= _parser).text.lower(): 
							continue
						else:
							#ignore case in regex
							# print(re.findall(r"(%s)"%re.escape(skeyword), tr, re.IGNORECASE))

							tr = re.sub(r"(%s)"%re.escape(skeyword), r'<span style="background-color:red">\1</span>', tr, flags=re.IGNORECASE)

							# print(tr)
							



					tables.append(tr)

				table_made= time.time()- table_made

				#self.PIDs= [i for i in self.PIDs]

				pink= self.PIDs[0: : 4]
				Lblue= self.PIDs[1: : 4]
				blue= self.PIDs[2: : 4]
				purple= self.PIDs[3: : 4]


			r.append('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" '
				'"http: //www.w3.org/TR/html4/strict.dtd">')
			r.append('<meta http-equiv="Content-Type" '
				'content="text/html; charset=%s">' % enc)

			if self.is_get_req:
				__x=f'''\n<div id='stats'><p style="color: darkgray;">Made by Ratul Hasan with Web leach</p><br>\n<p>[Server] {table_len} Results Arranged in {time.time()-request_time}s</p>\n<p>[Server] Decrypted in {read_dec}s ({decryptor_lang} powered)</p>\n<p>[Server] Table made in {table_made}s ({_parser} parser)</p>\n<p id="render"></p>\n<p id="response"></p>\n</div>'''
				r.append(decrypto_header%(str(pink), str(Lblue), str(blue), str(purple), __x, '\n'.join(tables)))
				r.append("""\n<hr>\n</body>\n<footer id="footer"><br><br><br><br><hr><hr></footer> <script>var response_get = %s; var response_send = %s;

				document.getElementById('response').innerHTML="[Browser] Sent and rendered in " + ((Date.now()/1000)- response_get)+'s';
				document.getElementById('render').innerHTML="[Browser] Rendered in "+((Date.now()/1000)- response_send)+'s';</script></html> \n"""%(str(self.response_get), str(time.time())))



			# print(self.PIDs)
			encoded = '\n'.join(r).encode(enc, 'surrogateescape')

			f = io.BytesIO()
			f.write(encoded)
			f.seek(0)
			self.send_response(HTTPStatus.OK)
			self.send_header("Content-type", "text/html; charset=%s" % enc)
			self.send_header("Content-Length", str(len(encoded)))
			self.end_headers()
			return f



		elif self.path.startswith('/sPID='):
			web_args= self.path[1: ].split('&')

		elif os.path.isdir(path):
			parts = urllib.parse.urlsplit(self.path)
			if not parts.path.endswith('/'):
				# redirect browser - doing basically what apache does
				self.send_response(HTTPStatus.MOVED_PERMANENTLY)
				new_parts = (parts[0], parts[1], parts[2] + '/',
							 parts[3], parts[4])
				new_url = urllib.parse.urlunsplit(new_parts)
				self.send_header("Location", new_url)
				self.send_header("Content-Length", "0")
				self.end_headers()
				return None
			for index in "index.html", "index.htm":
				index = os.path.join(path, index)
				if os.path.exists(index):
					path = index
					break
			else:
				return self.list_directory(path)
		ctype = self.guess_type(path)
		# check for trailing "/" which should return 404. See Issue17324
		# The test for this was added in test_httpserver.py
		# However, some OS platforms accept a trailingSlash as a filename
		# See discussion on python-dev and Issue34711 regarding
		# parseing and rejection of filenames with a trailing slash
		if path.endswith("/"):
			self.send_error(HTTPStatus.NOT_FOUND, "File not found")
			return None
		try:
			f = open(path, 'rb')
		except OSError:
			self.send_error(HTTPStatus.NOT_FOUND, "File not found")
			return None

		try:
			fs = os.fstat(f.fileno())
			# Use browser cache if possible
			if ("If-Modified-Since" in self.headers
					and "If-None-Match" not in self.headers):
				# compare If-Modified-Since and time of last file modification
				try:
					ims = email.utils.parsedate_to_datetime(
						self.headers["If-Modified-Since"])
				except (TypeError, IndexError, OverflowError, ValueError):
					# ignore ill-formed values
					pass
				else:
					if ims.tzinfo is None:
						# obsolete format with no timezone, cf.
						# https://tools.ietf.org/html/rfc7231#section-7.1.1.1
						ims = ims.replace(tzinfo=datetime.timezone.utc)
					if ims.tzinfo is datetime.timezone.utc:
						# compare to UTC datetime of last modification
						last_modif = datetime.datetime.fromtimestamp(
							fs.st_mtime, datetime.timezone.utc)
						# remove microseconds, like in If-Modified-Since
						last_modif = last_modif.replace(microsecond=0)

						if last_modif <= ims:
							self.send_response(HTTPStatus.NOT_MODIFIED)
							self.end_headers()
							f.close()
							return None

			self.send_response(HTTPStatus.OK)
			self.send_header("Content-type", ctype)
			self.send_header("Content-Length", str(fs[6]))
			self.send_header("Last-Modified",
				self.date_time_string(fs.st_mtime))
			self.end_headers()
			return f
		except:
			f.close()
			raise

	def list_directory(self, path):
		"""Helper to produce a directory listing (absent index.html).

		Return value is either a file object, or None (indicating an
		error).  In either case, the headers are sent, making the
		interface the same as for send_head().

		"""
		try:
			_list = os.listdir(path)
		except OSError:
			self.send_error(
				HTTPStatus.NOT_FOUND,
				"No permission to list directory")
			return None
		_list= natsort.realsorted(_list, reverse=True)
		r = []
		try:
			displaypath = urllib.parse.unquote(self.path,
											   errors='surrogatepass')
		except UnicodeDecodeError:
			displaypath = urllib.parse.unquote(path)
		displaypath = html.escape(displaypath, quote=False)
		enc = sys.getfilesystemencoding()
		title = 'Inside %s' % displaypath
		r.append('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
				 '"http://www.w3.org/TR/html4/strict.dtd">')
		r.append('<meta http-equiv="Content-Type" '
				 'content="text/html; charset=%s">' % enc)
		# r.append(directory_explorer_header)
		r.append('<title>%s</title>\n</head>' % title)
		r.append('<body>\n<h1>All files and folders in %s</h1>' % displaypath)
		r.append('<hr>\n<ul>')
		for name in _list:
			fullname = os.path.join(path, name)
			displayname = linkname = name
			_is_dir_= True
			# Append / for directories or @ for symbolic links
			if os.path.isdir(fullname):
				displayname = name + "/"
				linkname = name + "/"
			elif os.path.islink(fullname):
				displayname = name + "@"
				# Note: a link to a directory displays with @ and links with /
			else:
				_is_dir_ =False
				__, ext = posixpath.splitext(fullname)
				if ext=='.html':
					r.append('<li><a class= "%s" href="%s">%s</a></li>'
					% ("link", urllib.parse.quote(linkname,
										  errors='surrogatepass'),
					   html.escape(displayname, quote=False)))
				else:
					r.append('<li><a class= "%s" href="%s">%s</a></li>'
					% ("file", urllib.parse.quote(linkname,
										  errors='surrogatepass'),
					   html.escape(displayname, quote=False)))
			if _is_dir_:
				r.append('<li><a href="%s">%s</a></li>'
					% (urllib.parse.quote(linkname,
										  errors='surrogatepass'),
					   html.escape(displayname, quote=False)))

		r.append('</ul>\n<hr>\n</body>\n<footer id="footer><br><br><br><br><hr><hr>\n<p style="color: darkgray;">Made by Ratul Hasan with Web leach</p>\n<br><br>\n</footer></html> \n')
		encoded = '\n'.join(r).encode(enc, 'surrogateescape')
		f = io.BytesIO()
		f.write(encoded)
		f.seek(0)
		self.send_response(HTTPStatus.OK)
		self.send_header("Content-type", "text/html; charset=%s" % enc)
		self.send_header("Content-Length", str(len(encoded)))
		self.end_headers()
		return f

	def translate_path(self, path):
		"""Translate a /-separated PATH to the local filename syntax.

		Components that mean special things to the local file system
		(e.g. drive or directory names) are ignored.  (XXX They should
		probably be diagnosed.)

		"""
		# abandon query parameters
		path = path.split('?',1)[0]
		path = path.split('#',1)[0]
		# Don't forget explicit trailing slash when normalizing. Issue17324
		trailing_slash = path.rstrip().endswith('/')
		try:
			path = urllib.parse.unquote(path, errors='surrogatepass')
		except UnicodeDecodeError:
			path = urllib.parse.unquote(path)
		path = posixpath.normpath(path)
		words = path.split('/')
		words = filter(None, words)
		path = self.directory
		for word in words:
			if os.path.dirname(word) or word in (os.curdir, os.pardir):
				# Ignore components that are not a simple file/directory name
				continue
			path = os.path.join(path, word)
		if trailing_slash:
			path += '/'
		return path

	def copyfile(self, source, outputfile):
		"""Copy all data between two file objects.

		The SOURCE argument is a file object open for reading
		(or anything with a read() method) and the DESTINATION
		argument is a file object open for writing (or
		anything with a write() method).

		The only reason for overriding this would be to change
		the block size or perhaps to replace newlines by CRLF
		-- note however that this the default server uses this
		to copy binary data as well.

		"""
		shutil.copyfileobj(source, outputfile)

	def guess_type(self, path):
		"""Guess the type of a file.

		Argument is a PATH (a filename).

		Return value is a string of the form type/subtype,
		usable for a MIME Content-type header.

		The default implementation looks the file's extension
		up in the table self.extensions_map, using application/octet-stream
		as a default; however it would be permissible (if
		slow) to look inside the data to make a better guess.

		"""

		base, ext = posixpath.splitext(path)
		if ext in self.extensions_map:
			return self.extensions_map[ext]
		ext = ext.lower()
		if ext in self.extensions_map:
			return self.extensions_map[ext]
		guess, _ = mimetypes.guess_type(path)
		if guess:
			return guess
		return 'application/octet-stream'


# Utilities for CGIHTTPRequestHandler

def _url_collapse_path(path):
	"""
	Given a URL path, remove extra '/'s and '.' path elements and collapse
	any '..' references and returns a collapsed path.

	Implements something akin to RFC-2396 5.2 step 6 to parse relative paths.
	The utility of this function is limited to is_cgi method and helps
	preventing some security attacks.

	Returns: The reconstituted URL, which will always start with a '/'.

	Raises: IndexError if too many '..' occur within the path.

	"""
	# Query component should not be involved.
	path, _, query = path.partition('?')
	path = urllib.parse.unquote(path)

	# Similar to os.path.split(os.path.normpath(path)) but specific to URL
	# path semantics rather than local operating system semantics.
	path_parts = path.split('/')
	head_parts = []
	for part in path_parts[:-1]:
		if part == '..':
			head_parts.pop() # IndexError if more '..' than prior parts
		elif part and part != '.':
			head_parts.append( part )
	if path_parts:
		tail_part = path_parts.pop()
		if tail_part:
			if tail_part == '..':
				head_parts.pop()
				tail_part = ''
			elif tail_part == '.':
				tail_part = ''
	else:
		tail_part = ''

	if query:
		tail_part = '?'.join((tail_part, query))

	splitpath = ('/' + '/'.join(head_parts), tail_part)
	collapsed_path = "/".join(splitpath)

	return collapsed_path



nobody = None

def nobody_uid():
	"""Internal routine to get nobody's uid"""
	global nobody
	if nobody:
		return nobody
	try:
		import pwd
	except ImportError:
		return -1
	try:
		nobody = pwd.getpwnam('nobody')[2]
	except KeyError:
		nobody = 1 + max(x[2] for x in pwd.getpwall())
	return nobody


def executable(path):
	"""Test for executable file."""
	return os.access(path, os.X_OK)


class CGIHTTPRequestHandler(SimpleHTTPRequestHandler):

	"""Complete HTTP server with GET, HEAD and POST commands.

	GET and HEAD also support running CGI scripts.

	The POST command is *only* implemented for CGI scripts.

	"""

	# Determine platform specifics
	have_fork = hasattr(os, 'fork')

	# Make rfile unbuffered -- we need to read one line and then pass
	# the rest to a subprocess, so we can't use buffered input.
	rbufsize = 0

	def do_POST(self):
		"""Serve a POST request.

		This is only implemented for CGI scripts.

		"""

		if self.is_cgi():
			self.run_cgi()
		else:
			self.send_error(
				HTTPStatus.NOT_IMPLEMENTED,
				"Can only POST to CGI scripts")

	def send_head(self):
		"""Version of send_head that support CGI scripts"""
		if self.is_cgi():
			return self.run_cgi()
		else:
			return SimpleHTTPRequestHandler.send_head(self)

	def is_cgi(self):
		"""Test whether self.path corresponds to a CGI script.

		Returns True and updates the cgi_info attribute to the tuple
		(dir, rest) if self.path requires running a CGI script.
		Returns False otherwise.

		If any exception is raised, the caller should assume that
		self.path was rejected as invalid and act accordingly.

		The default implementation tests whether the normalized url
		path begins with one of the strings in self.cgi_directories
		(and the next character is a '/' or the end of the string).

		"""
		collapsed_path = _url_collapse_path(self.path)
		dir_sep = collapsed_path.find('/', 1)
		while dir_sep > 0 and not collapsed_path[:dir_sep] in self.cgi_directories:
			dir_sep = collapsed_path.find('/', dir_sep+1)
		if dir_sep > 0:
			head, tail = collapsed_path[:dir_sep], collapsed_path[dir_sep+1:]
			self.cgi_info = head, tail
			return True
		return False


	cgi_directories = ['/cgi-bin', '/htbin']

	def is_executable(self, path):
		"""Test whether argument path is an executable file."""
		return executable(path)

	def is_python(self, path):
		"""Test whether argument path is a Python script."""
		head, tail = os.path.splitext(path)
		return tail.lower() in (".py", ".pyw")

	def run_cgi(self):
		"""Execute a CGI script."""
		dir, rest = self.cgi_info
		path = dir + '/' + rest
		i = path.find('/', len(dir)+1)
		while i >= 0:
			nextdir = path[:i]
			nextrest = path[i+1:]

			scriptdir = self.translate_path(nextdir)
			if os.path.isdir(scriptdir):
				dir, rest = nextdir, nextrest
				i = path.find('/', len(dir)+1)
			else:
				break

		# find an explicit query string, if present.
		rest, _, query = rest.partition('?')

		# dissect the part after the directory name into a script name &
		# a possible additional path, to be stored in PATH_INFO.
		i = rest.find('/')
		if i >= 0:
			script, rest = rest[:i], rest[i:]
		else:
			script, rest = rest, ''

		scriptname = dir + '/' + script
		scriptfile = self.translate_path(scriptname)
		if not os.path.exists(scriptfile):
			self.send_error(
				HTTPStatus.NOT_FOUND,
				"No such CGI script (%r)" % scriptname)
			return
		if not os.path.isfile(scriptfile):
			self.send_error(
				HTTPStatus.FORBIDDEN,
				"CGI script is not a plain file (%r)" % scriptname)
			return
		ispy = self.is_python(scriptname)
		if self.have_fork or not ispy:
			if not self.is_executable(scriptfile):
				self.send_error(
					HTTPStatus.FORBIDDEN,
					"CGI script is not executable (%r)" % scriptname)
				return

		# Reference: http://hoohoo.ncsa.uiuc.edu/cgi/env.html
		# XXX Much of the following could be prepared ahead of time!
		env = copy.deepcopy(os.environ)
		env['SERVER_SOFTWARE'] = self.version_string()
		env['SERVER_NAME'] = self.server.server_name
		env['GATEWAY_INTERFACE'] = 'CGI/1.1'
		env['SERVER_PROTOCOL'] = self.protocol_version
		env['SERVER_PORT'] = str(self.server.server_port)
		env['REQUEST_METHOD'] = self.command
		uqrest = urllib.parse.unquote(rest)
		env['PATH_INFO'] = uqrest
		env['PATH_TRANSLATED'] = self.translate_path(uqrest)
		env['SCRIPT_NAME'] = scriptname
		if query:
			env['QUERY_STRING'] = query
		env['REMOTE_ADDR'] = self.client_address[0]
		authorization = self.headers.get("authorization")
		if authorization:
			authorization = authorization.split()
			if len(authorization) == 2:
				import base64, binascii
				env['AUTH_TYPE'] = authorization[0]
				if authorization[0].lower() == "basic":
					try:
						authorization = authorization[1].encode('ascii')
						authorization = base64.decodebytes(authorization).\
										decode('ascii')
					except (binascii.Error, UnicodeError):
						pass
					else:
						authorization = authorization.split(':')
						if len(authorization) == 2:
							env['REMOTE_USER'] = authorization[0]
		# XXX REMOTE_IDENT
		if self.headers.get('content-type') is None:
			env['CONTENT_TYPE'] = self.headers.get_content_type()
		else:
			env['CONTENT_TYPE'] = self.headers['content-type']
		length = self.headers.get('content-length')
		if length:
			env['CONTENT_LENGTH'] = length
		referer = self.headers.get('referer')
		if referer:
			env['HTTP_REFERER'] = referer
		accept = []
		for line in self.headers.getallmatchingheaders('accept'):
			if line[:1] in "\t\n\r ":
				accept.append(line.strip())
			else:
				accept = accept + line[7:].split(',')
		env['HTTP_ACCEPT'] = ','.join(accept)
		ua = self.headers.get('user-agent')
		if ua:
			env['HTTP_USER_AGENT'] = ua
		co = filter(None, self.headers.get_all('cookie', []))
		cookie_str = ', '.join(co)
		if cookie_str:
			env['HTTP_COOKIE'] = cookie_str
		# XXX Other HTTP_* headers
		# Since we're setting the env in the parent, provide empty
		# values to override previously set values
		for k in ('QUERY_STRING', 'REMOTE_HOST', 'CONTENT_LENGTH',
				  'HTTP_USER_AGENT', 'HTTP_COOKIE', 'HTTP_REFERER'):
			env.setdefault(k, "")

		self.send_response(HTTPStatus.OK, "Script output follows")
		self.flush_headers()

		decoded_query = query.replace('+', ' ')

		if self.have_fork:
			# Unix -- fork as we should
			args = [script]
			if '=' not in decoded_query:
				args.append(decoded_query)
			nobody = nobody_uid()
			self.wfile.flush() # Always flush before forking
			pid = os.fork()
			if pid != 0:
				# Parent
				pid, sts = os.waitpid(pid, 0)
				# throw away additional data [see bug #427345]
				while select.select([self.rfile], [], [], 0)[0]:
					if not self.rfile.read(1):
						break
				if sts:
					self.log_error("CGI script exit status %#x", sts)
				return
			# Child
			try:
				try:
					os.setuid(nobody)
				except OSError:
					pass
				os.dup2(self.rfile.fileno(), 0)
				os.dup2(self.wfile.fileno(), 1)
				os.execve(scriptfile, args, env)
			except:
				self.server.handle_error(self.request, self.client_address)
				os._exit(127)

		else:
			# Non-Unix -- use subprocess
			import subprocess
			cmdline = [scriptfile]
			if self.is_python(scriptfile):
				interp = sys.executable
				if interp.lower().endswith("w.exe"):
					# On Windows, use python.exe, not pythonw.exe
					interp = interp[:-5] + interp[-4:]
				cmdline = [interp, '-u'] + cmdline
			if '=' not in query:
				cmdline.append(query)
			self.log_message("command: %s", subprocess.list2cmdline(cmdline))
			try:
				nbytes = int(length)
			except (TypeError, ValueError):
				nbytes = 0
			p = subprocess.Popen(cmdline,
								 stdin=subprocess.PIPE,
								 stdout=subprocess.PIPE,
								 stderr=subprocess.PIPE,
								 env = env
								 )
			if self.command.lower() == "post" and nbytes > 0:
				data = self.rfile.read(nbytes)
			else:
				data = None
			# throw away additional data [see bug #427345]
			while select.select([self.rfile._sock], [], [], 0)[0]:
				if not self.rfile._sock.recv(1):
					break
			stdout, stderr = p.communicate(data)
			self.wfile.write(stdout)
			if stderr:
				self.log_error('%s', stderr)
			p.stderr.close()
			p.stdout.close()
			status = p.returncode
			if status:
				self.log_error("CGI script exit status %#x", status)
			else:
				self.log_message("CGI script exited OK")


def test(HandlerClass=BaseHTTPRequestHandler,
		 ServerClass=ThreadingHTTPServer,
		 protocol="HTTP/1.0", port=8000, bind=""):
	"""Test the HTTP request handler class.

	This runs an HTTP server on port 8000 (or the port argument).

	"""
	server_address = (bind, port)

	HandlerClass.protocol_version = protocol
	with ServerClass(server_address, HandlerClass) as httpd:
		sa = httpd.socket.getsockname()
		serve_message = "Serving HTTP on {host} port {port} (http://{host}:{port}/) ..."
		print(serve_message.format(host=sa[0], port=sa[1]))
		try:
			httpd.serve_forever()
		except KeyboardInterrupt:
			print("\nKeyboard interrupt received, exiting.")
			sys.exit(0)

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('--cgi', action='store_true',
					   help='Run as CGI Server')
	parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
						help='Specify alternate bind address '
							 '[default: all interfaces]')
	parser.add_argument('--directory', '-d', default=os.getcwd(),
						help='Specify alternative directory '
						'[default: current directory]')
	parser.add_argument('port', action='store',
						default=8090, type=int,
						nargs='?',
						help='Specify alternate port [default: 8000]')
	args = parser.parse_args()
	# webbrowser.open('http://localhost:%i'%args.port)
	if args.cgi:
		handler_class = CGIHTTPRequestHandler
	else:
		handler_class = partial(SimpleHTTPRequestHandler,
					directory=args.directory)

	test(HandlerClass=handler_class, port=args.port, bind=args.bind)
