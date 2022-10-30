const staticPyPWA = "dev-pypwa-v4"
const assets = [
    // "",
    // "/",
    "./static/css/site.css",
    "./static/js/site.js",
    "./static/js/pwa-scaffold.js",

    "./static/python/client.py",
    "./static/python/subject_api.py",

    "./static/pyscript/pyscript.css",
    "./static/pyscript/pyscript.js",
    "./static/pyscript/pyscript.py",

    "./static/images/architects/bi.webp",
    "./static/images/architects/fg.webp",
    "./static/images/architects/imp.webp",
    "./static/images/architects/jn.webp",
    "./static/images/architects/offline.webp",
    "./static/images/architects/zh.webp",

    "./static/images/architecture/bi.webp",
    "./static/images/architecture/fg.webp",
    "./static/images/architecture/imp.webp",
    "./static/images/architecture/jn.webp",
    "./static/images/architecture/offline.webp",
    "./static/images/architecture/zh.webp",

    "./static/pyodide/pyodide.js",
    "./static/pyodide/packages.json",
    "./static/pyodide/pyodide_py.tar",
    "./static/pyodide/pyodide.asm.js",
    "./static/pyodide/pyodide.asm.data",
    "./static/pyodide/pyodide.asm.wasm",
    "./static/pyodide/micropip-0.1-py3-none-any.whl",
    "./static/pyodide/pyparsing-3.0.7-py3-none-any.whl",
    "./static/pyodide/packaging-21.3-py3-none-any.whl",
    "./static/pyodide/distutils.tar",

    "./static/images/icons/icon-144x144.png",
]

self.addEventListener("install", installEvent => {
    installEvent.waitUntil(
        caches.open(staticPyPWA).then(cache => {
            cache.addAll(assets).then(r => {
                console.log("Cache assets downloaded");
            }).catch(err => console.log("Error caching item", err))
            console.log(`Cache ${staticPyPWA} opened.`);
        }).catch(err => console.log("Error opening cache", err))
    )
})

self.addEventListener("fetch", fetchEvent => {
    fetchEvent.respondWith(
        caches.match(fetchEvent.request).then(res => {
            return res || fetch(fetchEvent.request)
        }).catch(err => console.log("Cache fetch error: ", err))
    )
})